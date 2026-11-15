from __future__ import annotations

import base64
import hashlib
from io import BytesIO
from pathlib import Path
from threading import Lock

import streamlit as st
from PIL import Image, UnidentifiedImageError


BASE_DIR = Path(__file__).resolve().parent
MAX_IMAGE_BYTES = 10 * 1024 * 1024
MAX_IMAGE_PIXELS = 20_000_000
SAMPLE_IMAGES = {
    "Tomato - Early blight": "sample_tomato_early_blight.jpg",
    "Potato - Late blight": "sample_potato_late_blight.jpg",
    "Capsicum - Bacterial spot": "sample_capsicum_bacterial_spot.jpg",
}
LANGUAGES = {
    "English": "en",
    "हिन्दी (Hindi)": "hi",
    "ಕನ್ನಡ (Kannada)": "kn",
    "मराठी (Marathi)": "mr",
    "தமிழ் (Tamil)": "ta",
}


def decode_image(image_bytes: bytes) -> Image.Image:
    if not image_bytes:
        raise ValueError("Choose or capture an image before analyzing.")
    if len(image_bytes) > MAX_IMAGE_BYTES:
        raise ValueError("Image is too large. Please use an image smaller than 10 MB.")

    try:
        with Image.open(BytesIO(image_bytes)) as source:
            if source.width * source.height > MAX_IMAGE_PIXELS:
                raise ValueError("Image dimensions are too large. Please use an image under 20 megapixels.")
            source.load()
            return source.convert("RGB")
    except (UnidentifiedImageError, OSError, Image.DecompressionBombError) as error:
        raise ValueError("The selected file is not a valid, readable image.") from error


@st.cache_resource
def load_colab_model():
    from ai_engine.colab_engine import colab_ai_engine

    return colab_ai_engine


@st.cache_resource
def load_prediction_lock():
    return Lock()


def render_diagnosis(result: dict, image: Image.Image) -> None:
    prediction = result["prediction"]
    detection = result["detection"]

    st.divider()
    st.subheader("Diagnosis")

    image_column, result_column = st.columns([1, 1], gap="large")
    with image_column:
        st.image(
            image,
            caption="Submitted leaf image",
            width="stretch",
            alt="Submitted plant leaf",
        )
        annotated = detection.get("annotated_image")
        if annotated and "," in annotated:
            encoded_image = annotated.split(",", 1)[1]
            annotated_image = Image.open(BytesIO(base64.b64decode(encoded_image)))
            annotated_image.load()
            st.image(
                annotated_image,
                caption="Leaf and lesion visualization",
                width="stretch",
                alt="Leaf boundary and estimated lesion visualization",
            )

    with result_column:
        st.markdown(f"### {prediction['localized_disease']}")
        st.write(f"**Crop:** {prediction['localized_crop']}")
        st.write(f"**Severity:** {prediction['severity']}")
        st.metric("Model confidence", f"{prediction['confidence']:.1f}%")
        st.write(f"**Pathogen:** {prediction['pathogen']}")

        if not detection["is_leaf_detected"]:
            st.warning("A clear leaf boundary was not detected. Treat this result as less reliable.")

        metric_columns = st.columns(2)
        metric_columns[0].metric("Estimated lesion area", f"{detection['lesion_pct']:.1f}%")
        metric_columns[1].metric("Green leaf area", f"{detection['healthy_green_pct']:.1f}%")

    st.subheader("Other possibilities")
    st.dataframe(
        [
            {
                "Crop": item["crop"],
                "Condition": item["disease"],
                "Confidence": f"{item['confidence']:.1f}%",
            }
            for item in result["top_3"]
        ],
        hide_index=True,
        width="stretch",
        alt="Three highest-scoring disease predictions",
    )

    treatment = result["treatment"]
    symptoms_tab, organic_tab, chemical_tab, prevention_tab = st.tabs(
        ["Symptoms", "Organic care", "Chemical treatments", "Prevention"]
    )
    with symptoms_tab:
        st.write(treatment["symptoms"])
    with organic_tab:
        for item in treatment["organic"]:
            st.markdown(f"- {item}")
    with chemical_tab:
        for item in treatment["chemical"]:
            st.markdown(f"- {item}")
    with prevention_tab:
        for item in treatment["prevention"]:
            st.markdown(f"- {item}")

    st.caption(
        "This AI result is a screening aid, not a confirmed diagnosis. "
        "Verify treatment choices with a local agricultural expert and follow product labels."
    )


def main() -> None:
    st.set_page_config(
        page_title="AgroCure AI — Plant Disease Check",
        layout="wide",
    )
    st.title("AgroCure AI")
    st.subheader("Check a plant leaf for common diseases")
    st.write(
        "Upload a photo, take one with your camera, or try a sample. "
        "The trained Model 2 supports tomato, potato, and capsicum."
    )

    with st.sidebar:
        st.header("Diagnosis settings")
        crop = st.selectbox("Crop (optional)", ["Auto-detect", "Tomato", "Potato", "Capsicum"])
        language = st.selectbox("Result language", list(LANGUAGES))
        st.info("Uploaded images are analyzed in memory and are not saved by this app.")

    image_source = st.segmented_control(
        "Choose an image source",
        ["Upload", "Camera", "Sample"],
        default="Upload",
        required=True,
    )

    image_bytes = None
    image_label = ""
    if image_source == "Upload":
        uploaded = st.file_uploader(
            "Choose a leaf image",
            type=["jpg", "jpeg", "png"],
            max_upload_size=10,
        )
        if uploaded is not None:
            image_bytes = uploaded.getvalue()
            image_label = uploaded.name
    elif image_source == "Camera":
        captured = st.camera_input("Take a picture of a leaf", resolution="720p")
        if captured is not None:
            image_bytes = captured.getvalue()
            image_label = "Camera photo"
    elif image_source == "Sample":
        sample_label = st.selectbox("Choose a sample", list(SAMPLE_IMAGES))
        image_path = BASE_DIR / "static" / "samples" / SAMPLE_IMAGES[sample_label]
        image_bytes = image_path.read_bytes()
        image_label = sample_label

    selected_image = None
    image_key = None
    if image_bytes is not None:
        try:
            selected_image = decode_image(image_bytes)
        except ValueError as error:
            st.error(str(error))
        else:
            image_key = hashlib.sha256(image_bytes).hexdigest()
            st.image(
                selected_image,
                caption=image_label,
                width=400,
                alt="Selected plant leaf image",
            )

    result_key = (image_key, crop, LANGUAGES[language])
    if st.session_state.get("diagnosis_key") != result_key:
        st.session_state.pop("diagnosis", None)
        st.session_state["diagnosis_key"] = result_key

    if st.button("Analyze leaf", type="primary", disabled=selected_image is None):
        if selected_image is None:
            st.error("Choose or capture an image before analyzing.")
        else:
            st.session_state.pop("diagnosis", None)
            with st.spinner("Loading Model 2 and analyzing the leaf image…"):
                model = load_colab_model()
                if not model.is_loaded:
                    st.error(model.load_error or "The trained Model 2 checkpoint is unavailable.")
                else:
                    with load_prediction_lock():
                        result = model.predict(
                            selected_image,
                            crop_hint=None if crop == "Auto-detect" else crop,
                            lang=LANGUAGES[language],
                        )
                    st.session_state["diagnosis"] = result

    result = st.session_state.get("diagnosis")
    if result is not None and selected_image is not None:
        render_diagnosis(result, selected_image)


if __name__ == "__main__":
    main()
