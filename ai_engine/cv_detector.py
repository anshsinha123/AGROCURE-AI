"""
AgroCure AI - Computer Vision Leaf Detection & Lesion Segmentation Engine.
Leverages OpenCV / NumPy color space transformations & vegetative indices (ExG/GLI).
"""

import numpy as np
from PIL import Image, ImageDraw
import io
import base64

def rgb_to_hsv(rgb: np.ndarray) -> np.ndarray:
    """Vectorized RGB to HSV color conversion."""
    arr = rgb.astype(np.float32) / 255.0
    r, g, b = arr[..., 0], arr[..., 1], arr[..., 2]
    maxc = np.maximum(np.maximum(r, g), b)
    minc = np.minimum(np.minimum(r, g), b)
    delta = maxc - minc

    v = maxc
    s = np.zeros_like(v)
    valid = maxc > 1e-6
    s[valid] = delta[valid] / maxc[valid]

    h = np.zeros_like(v)
    rc = np.zeros_like(v)
    gc = np.zeros_like(v)
    bc = np.zeros_like(v)

    rc[valid] = (maxc[valid] - r[valid]) / (delta[valid] + 1e-6)
    gc[valid] = (maxc[valid] - g[valid]) / (delta[valid] + 1e-6)
    bc[valid] = (maxc[valid] - b[valid]) / (delta[valid] + 1e-6)

    m_r = valid & (r == maxc)
    m_g = valid & (g == maxc) & (~m_r)
    m_b = valid & (b == maxc) & (~m_r) & (~m_g)

    h[m_r] = bc[m_r] - gc[m_r]
    h[m_g] = 2.0 + rc[m_g] - bc[m_g]
    h[m_b] = 4.0 + gc[m_b] - rc[m_b]

    h = (h / 6.0) % 1.0
    return np.stack([h * 360.0, s, v], axis=-1)

def detect_leaf_and_lesions(image: Image.Image) -> dict:
    """
    Performs Computer Vision leaf boundary detection and lesion segmentation.
    Returns bounding box coordinates, vegetative indices, and visual overlay.
    """
    img_rgb = image.convert("RGB")
    w, h = img_rgb.size

    # Scale down for fast morphology if large
    max_side = 512
    scale = 1.0
    if max(w, h) > max_side:
        scale = max_side / max(w, h)
        work_img = img_rgb.resize((int(w * scale), int(h * scale)), Image.Resampling.BILINEAR)
    else:
        work_img = img_rgb

    np_img = np.array(work_img)
    r = np_img[..., 0].astype(np.float32)
    g = np_img[..., 1].astype(np.float32)
    b = np_img[..., 2].astype(np.float32)

    # Excess Green Index (ExG = 2G - R - B)
    exg = 2.0 * g - r - b
    hsv = rgb_to_hsv(np_img)
    hue = hsv[..., 0]
    sat = hsv[..., 1]
    val = hsv[..., 2]

    # Leaf Mask: Plant foliage (green to yellowish-brown)
    plant_mask = (
        ((hue >= 25) & (hue <= 165) & (sat > 0.12) & (val > 0.15)) |
        ((exg > 10) & (sat > 0.15)) |
        ((hue < 25) & (sat > 0.20) & (val > 0.20) & (r > b * 1.1)) # necrotic tissue inside blade
    )
    non_bg = (val > 0.12) & (val < 0.96) & (sat > 0.08)
    leaf_mask = plant_mask & non_bg

    leaf_pixels = int(np.sum(leaf_mask))
    total_pixels = work_img.size[0] * work_img.size[1]
    coverage_ratio = leaf_pixels / max(1, total_pixels)

    if coverage_ratio < 0.05:
        leaf_mask = non_bg
        leaf_pixels = int(np.sum(leaf_mask))
        coverage_ratio = leaf_pixels / max(1, total_pixels)

    # Bounding Box Extraction
    y_idxs, x_idxs = np.where(leaf_mask)
    if len(y_idxs) > 50:
        ymin = int(np.min(y_idxs) / scale)
        ymax = int(np.max(y_idxs) / scale)
        xmin = int(np.min(x_idxs) / scale)
        xmax = int(np.max(x_idxs) / scale)

        pad_x = int((xmax - xmin) * 0.03)
        pad_y = int((ymax - ymin) * 0.03)
        bbox = [
            max(0, xmin - pad_x),
            max(0, ymin - pad_y),
            min(w, xmax + pad_x),
            min(h, ymax + pad_y)
        ]
        is_detected = True
    else:
        bbox = [0, 0, w, h]
        is_detected = False

    # Healthy vs Diseased Lesions
    healthy_mask = (hue >= 48) & (hue <= 155) & (exg > 15) & leaf_mask
    healthy_pixels = int(np.sum(healthy_mask))

    lesion_mask = leaf_mask & (~healthy_mask) & (
        ((hue < 48) & (sat > 0.15)) |   # yellow/chlorotic/rust
        ((val < 0.35) & (sat > 0.10)) | # dark necrotized
        (exg < -5)
    )
    lesion_pixels = int(np.sum(lesion_mask))

    lesion_pct = round((lesion_pixels / max(1, leaf_pixels)) * 100, 2)
    green_pct = round((healthy_pixels / max(1, leaf_pixels)) * 100, 2)

    # Generate Visual Annotation
    annotated = img_rgb.copy()
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    ov_draw = ImageDraw.Draw(overlay)

    # Scale lesion mask to full image
    if scale < 1.0:
        full_lesion = Image.fromarray((lesion_mask * 255).astype(np.uint8)).resize((w, h), Image.Resampling.NEAREST)
        les_arr = np.array(full_lesion) > 128
    else:
        les_arr = lesion_mask

    ly, lx = np.where(les_arr)
    if len(ly) > 0:
        step = max(1, len(ly) // 3500)
        for i in range(0, len(ly), step):
            py, px = ly[i], lx[i]
            ov_draw.rectangle([px-1, py-1, px+1, py+1], fill=(239, 68, 68, 95))

    annotated = Image.alpha_composite(annotated.convert("RGBA"), overlay)
    draw = ImageDraw.Draw(annotated)

    if is_detected:
        bx0, by0, bx1, by1 = bbox
        border_col = (16, 185, 129, 240) if lesion_pct < 10 else (245, 158, 11, 240)
        draw.rectangle([bx0, by0, bx1, by1], outline=border_col, width=3)

        label_h = 24
        draw.rectangle([bx0, max(0, by0 - label_h), bx0 + 240, by0], fill=(15, 23, 42, 220))
        draw.text((bx0 + 8, max(2, by0 - label_h + 4)), f"LEAF DETECTED | Lesion: {lesion_pct}%", fill=(255, 255, 255))

    buf = io.BytesIO()
    annotated.convert("RGB").save(buf, format="JPEG", quality=88)
    annotated_b64 = "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode("utf-8")

    severity = "Healthy" if lesion_pct < 5.0 else ("Low" if lesion_pct < 18.0 else ("Moderate" if lesion_pct < 40.0 else "High"))

    return {
        "is_leaf_detected": bool(is_detected),
        "bounding_box": bbox,
        "leaf_coverage_pct": round(coverage_ratio * 100, 1),
        "healthy_green_pct": green_pct,
        "lesion_pct": lesion_pct,
        "estimated_severity": severity,
        "annotated_image_b64": annotated_b64
    }
