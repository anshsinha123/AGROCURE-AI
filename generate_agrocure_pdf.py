"""
Generates the publication-grade PDF Handbook: 'AgroCure_AI_Handbook.pdf'
Covers AgroCure AI technical architecture, Pepper, Grapes, Wheat, Corn pathology,
multilingual (EN, HI, KN) guides, MobileNetV2 / CNN, and OpenCV leaf detection.
"""

import os
import subprocess
from pathlib import Path
from ai_engine.disease_catalog import DISEASE_CATALOG

PROJECT_DIR = Path(__file__).resolve().parent
HTML_PATH = PROJECT_DIR / "agrocure_report.html"
PDF_PATH = PROJECT_DIR / "AgroCure_AI_Handbook.pdf"
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

def build_pdf_html():
    disease_html = ""
    for ckey, d in DISEASE_CATALOG.items():
        loc_en = d["translations"]["en"]
        loc_hi = d["translations"]["hi"]
        loc_kn = d["translations"]["kn"]

        sev_col = "#10b981" if d["severity"] == "Healthy" else ("#f59e0b" if d["severity"] in ["Low", "Moderate"] else "#ef4444")
        sev_bg = "#ecfdf5" if d["severity"] == "Healthy" else ("#fffbeb" if d["severity"] in ["Low", "Moderate"] else "#fef2f2")

        disease_html += f"""
        <div class="disease-entry">
            <div class="disease-header">
                <div>
                    <span class="crop-tag">{d['crop']}</span>
                    <h3 class="disease-title">{loc_en['disease_name']}</h3>
                    <div class="lang-titles">
                        <span class="hi-text"><strong>हिंदी:</strong> {loc_hi['disease_name']}</span> &bull; 
                        <span class="kn-text"><strong>ಕನ್ನಡ:</strong> {loc_kn['disease_name']}</span>
                    </div>
                    <div class="pathogen-text">Pathogen: {d['pathogen']}</div>
                </div>
                <div class="severity-badge" style="color: {sev_col}; background-color: {sev_bg}; border: 1px solid {sev_col}40;">
                    {d['severity']}
                </div>
            </div>

            <div class="symptoms-box">
                <p><strong>English Symptoms:</strong> {loc_en['symptoms']}</p>
                <p class="hi-text" style="margin-top: 3px;"><strong>हिंदी लक्षण:</strong> {loc_hi['symptoms']}</p>
                <p class="kn-text" style="margin-top: 3px;"><strong>ಕನ್ನಡ ಲಕ್ಷಣಗಳು:</strong> {loc_kn['symptoms']}</p>
            </div>

            <div class="treat-grid">
                <div class="treat-card">
                    <div class="treat-subhead org-head"><span class="dot g-dot"></span>Organic & Bio-Control Remedies</div>
                    <ul class="treat-list">
                        {"".join([f"<li>{item}</li>" for item in loc_en['organic_treatment']])}
                    </ul>
                    <div class="hi-text" style="font-size: 7.5pt; margin-top: 4px; color: #065f46;">
                        <strong>जैविक उपाय:</strong> {loc_hi['organic_treatment'][0]}
                    </div>
                    <div class="kn-text" style="font-size: 7.5pt; margin-top: 2px; color: #065f46;">
                        <strong>ಸಾವಯವ ಪರಿಹಾರ:</strong> {loc_kn['organic_treatment'][0]}
                    </div>
                </div>

                <div class="treat-card">
                    <div class="treat-subhead chem-head"><span class="dot b-dot"></span>Chemical / Fungicide Sprays</div>
                    <ul class="treat-list">
                        {"".join([f"<li>{item}</li>" for item in loc_en['chemical_treatment']])}
                    </ul>
                    <div class="hi-text" style="font-size: 7.5pt; margin-top: 4px; color: #1e40af;">
                        <strong>रासायनिक उपाय:</strong> {loc_hi['chemical_treatment'][0]}
                    </div>
                    <div class="kn-text" style="font-size: 7.5pt; margin-top: 2px; color: #1e40af;">
                        <strong>ರಾಸಾಯನಿಕ ಸಿಂಪರಣೆ:</strong> {loc_kn['chemical_treatment'][0]}
                    </div>
                </div>
            </div>
        </div>
        """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>AgroCure AI Technical Handbook</title>
    <style>
        @page {{
            size: A4;
            margin: 16mm 14mm 16mm 14mm;
            @bottom-right {{
                content: counter(page);
                font-size: 8.5pt;
                color: #64748b;
            }}
        }}

        *, *::before, *::after {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Noto Sans Devanagari", "Noto Sans Kannada", sans-serif;
            color: #1e293b;
            background: #ffffff;
            line-height: 1.45;
            font-size: 9pt;
        }}

        .page-break {{
            page-break-before: always;
        }}

        .cover-page {{
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding: 24mm 10mm 15mm 10mm;
            border-bottom: 3px solid #10b981;
        }}

        .cover-top {{
            border-left: 6px solid #059669;
            padding-left: 18px;
        }}

        .cover-badge {{
            display: inline-block;
            background: #ecfdf5;
            color: #047857;
            font-size: 8.5pt;
            font-weight: 700;
            padding: 4px 10px;
            border-radius: 9999px;
            border: 1px solid #a7f3d0;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 12px;
        }}

        .cover-title {{
            font-size: 26pt;
            font-weight: 800;
            color: #0f172a;
            line-height: 1.15;
            letter-spacing: -0.02em;
        }}

        .cover-subtitle {{
            font-size: 13pt;
            color: #059669;
            font-weight: 600;
            margin-top: 8px;
        }}

        .cover-desc {{
            font-size: 10pt;
            color: #475569;
            margin-top: 14px;
            max-width: 620px;
            line-height: 1.5;
        }}

        .crops-grid {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 10px;
            margin: 25px 0;
        }}

        .crop-box {{
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 10px;
            text-align: center;
        }}

        .crop-title {{
            font-weight: 700;
            font-size: 10.5pt;
            color: #0f172a;
        }}

        .crop-sci {{
            font-size: 8pt;
            color: #059669;
            font-style: italic;
        }}

        .cover-meta {{
            background: #f1f5f9;
            border-radius: 8px;
            padding: 14px 18px;
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 12px;
            font-size: 8.5pt;
            border-left: 4px solid #0f172a;
        }}

        .meta-lbl {{
            color: #64748b;
            text-transform: uppercase;
            font-size: 7pt;
            font-weight: 700;
        }}

        .meta-val {{
            color: #0f172a;
            font-weight: 600;
            margin-top: 2px;
        }}

        h2.sec-heading {{
            font-size: 13pt;
            font-weight: 800;
            color: #0f172a;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 5px;
            margin-top: 18px;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
        }}

        h2.sec-heading .sec-num {{
            background: #059669;
            color: #ffffff;
            font-size: 8.5pt;
            font-weight: 800;
            width: 20px;
            height: 20px;
            border-radius: 4px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            margin-right: 8px;
        }}

        table.tbl {{
            width: 100%;
            border-collapse: collapse;
            margin: 8px 0 14px 0;
            font-size: 8pt;
        }}

        table.tbl th {{
            background: #0f172a;
            color: #ffffff;
            font-weight: 700;
            text-align: left;
            padding: 6px 8px;
            border: 1px solid #0f172a;
        }}

        table.tbl td {{
            padding: 5px 8px;
            border: 1px solid #cbd5e1;
            color: #1e293b;
        }}

        table.tbl tr:nth-child(even) {{
            background: #f8fafc;
        }}

        .callout {{
            background: #f0fdf4;
            border-left: 4px solid #10b981;
            padding: 8px 12px;
            border-radius: 0 6px 6px 0;
            margin: 10px 0;
            font-size: 8pt;
        }}

        .disease-entry {{
            background: #ffffff;
            border: 1px solid #cbd5e1;
            border-radius: 8px;
            padding: 10px 12px;
            margin-bottom: 10px;
            page-break-inside: avoid;
        }}

        .disease-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 4px;
        }}

        .crop-tag {{
            font-size: 7pt;
            font-weight: 700;
            text-transform: uppercase;
            color: #059669;
            background: #ecfdf5;
            padding: 2px 6px;
            border-radius: 4px;
            border: 1px solid #a7f3d0;
        }}

        .disease-title {{
            font-size: 10.5pt;
            font-weight: 800;
            color: #0f172a;
            margin-top: 2px;
        }}

        .lang-titles {{
            font-size: 7.5pt;
            color: #475569;
            margin: 2px 0;
        }}

        .pathogen-text {{
            font-size: 7.5pt;
            font-style: italic;
            color: #64748b;
        }}

        .severity-badge {{
            font-size: 7pt;
            font-weight: 700;
            padding: 2px 8px;
            border-radius: 9999px;
            text-transform: uppercase;
        }}

        .symptoms-box {{
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-left: 3px solid #cbd5e1;
            padding: 6px 8px;
            border-radius: 4px;
            margin: 6px 0;
            font-size: 8pt;
        }}

        .treat-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 8px;
        }}

        .treat-card {{
            background: #fafafa;
            border: 1px solid #e2e8f0;
            border-radius: 6px;
            padding: 6px 8px;
        }}

        .treat-subhead {{
            font-size: 7.5pt;
            font-weight: 700;
            margin-bottom: 3px;
        }}
        .org-head {{ color: #047857; }}
        .chem-head {{ color: #1d4ed8; }}

        .dot {{ width: 5px; height: 5px; border-radius: 50%; display: inline-block; margin-right: 4px; }}
        .g-dot {{ background: #10b981; }}
        .b-dot {{ background: #3b82f6; }}

        .treat-list {{
            list-style: square;
            padding-left: 12px;
            font-size: 7.5pt;
            color: #334155;
            line-height: 1.35;
        }}

        pre.code {{
            background: #0f172a;
            color: #34d399;
            padding: 8px 10px;
            border-radius: 6px;
            font-family: Consolas, Monaco, monospace;
            font-size: 7.5pt;
            line-height: 1.35;
            margin: 6px 0 10px 0;
        }}
    </style>
</head>
<body>

    <!-- COVER PAGE -->
    <div class="cover-page">
        <div class="cover-top">
            <span class="cover-badge">AgroCure AI Technical Specification</span>
            <h1 class="cover-title">AgroCure AI</h1>
            <div class="cover-subtitle">AI-Powered Agricultural Assistant for Inclusive Plant Disease Detection</div>
            <p class="cover-desc">
                An intelligent multi-platform agricultural web application using Deep Learning (CNN / MobileNetV2) and
                Computer Vision (OpenCV) to detect crop diseases from leaf images. Engineered for rural inclusivity with
                native trilingual support in English, Hindi (हिंदी), and Kannada (ಕನ್ನಡ).
            </p>
        </div>

        <div>
            <div style="font-weight: 700; font-size: 8.5pt; text-transform: uppercase; color: #475569; letter-spacing: 0.05em; margin-bottom: 6px;">Supported Agronomic Crops</div>
            <div class="crops-grid">
                <div class="crop-box">
                    <div class="crop-title">Pepper</div>
                    <div class="crop-sci">Capsicum annuum</div>
                </div>
                <div class="crop-box">
                    <div class="crop-title">Grapes</div>
                    <div class="crop-sci">Vitis vinifera</div>
                </div>
                <div class="crop-box">
                    <div class="crop-title">Wheat</div>
                    <div class="crop-sci">Triticum aestivum</div>
                </div>
                <div class="crop-box">
                    <div class="crop-title">Corn (Maize)</div>
                    <div class="crop-sci">Zea mays</div>
                </div>
            </div>
        </div>

        <div class="cover-meta">
            <div>
                <div class="meta-lbl">Core Stack</div>
                <div class="meta-val">React.js &bull; Node.js &bull; Express.js</div>
            </div>
            <div>
                <div class="meta-lbl">AI & CV Frameworks</div>
                <div class="meta-val">TensorFlow / MobileNetV2 &bull; OpenCV</div>
            </div>
            <div>
                <div class="meta-lbl">Supported Languages</div>
                <div class="meta-val">English &bull; हिंदी &bull; ಕನ್ನಡ</div>
            </div>
        </div>
    </div>

    <!-- PAGE 2: ARCHITECTURE & CV ENGINE -->
    <div class="page-break"></div>

    <h2 class="sec-heading"><span class="sec-num">1</span>System Architecture & Inclusivity Paradigm</h2>
    <p>
        AgroCure AI bridges advanced Deep Learning computer vision and practical agricultural extension services for smallholder
        farmers across diverse linguistic backgrounds. The full-stack architecture consists of:
    </p>

    <table class="tbl">
        <thead>
            <tr>
                <th>Tier</th>
                <th>Technology</th>
                <th>Responsibilities</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Frontend UI</strong></td>
                <td>React.js &bull; Tailwind CSS</td>
                <td>Reactive camera upload, live lesion heatmap toggle, audio speech synthesis (Voice Assistant), dynamic language switching.</td>
            </tr>
            <tr>
                <td><strong>Backend Gateway</strong></td>
                <td>Node.js &bull; Express.js</td>
                <td>Multer image upload processing, RESTful routing, MongoDB Mongoose schema persistence, and Python microservice orchestration.</td>
            </tr>
            <tr>
                <td><strong>AI Engine</strong></td>
                <td>Python &bull; TensorFlow / Keras &bull; OpenCV</td>
                <td>MobileNetV2 deep neural classification, Excess Green Index (ExG/GLI) leaf detection, lesion bounding box extraction.</td>
            </tr>
            <tr>
                <td><strong>Database Layer</strong></td>
                <td>MongoDB &bull; JSON Storage</td>
                <td>Permanent farmer scan records, foliar bounding boxes, timestamps, and language-specific audit logs.</td>
            </tr>
        </tbody>
    </table>

    <div class="callout">
        <strong>Trilingual Speech Synthesis for Rural Accessibility:</strong>
        AgroCure AI features built-in text-to-speech audio guidance in <strong>English</strong>, <strong>Hindi (हिंदी)</strong>, and <strong>Kannada (ಕನ್ನಡ)</strong>,
        enabling illiterate and semi-literate farmers to listen to disease symptoms and organic remedies directly from their smartphone speakers.
    </div>

    <h2 class="sec-heading"><span class="sec-num">2</span>Computer Vision Leaf Detection (OpenCV)</h2>
    <p>
        Before neural classification, the OpenCV preprocessing module segments the leaf blade and calculates quantitative metrics:
    </p>
    <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 6px 10px; border-radius: 6px; font-family: Consolas, monospace; font-size: 7.5pt; margin-bottom: 8px;">
        ExG = 2 &times; G - R - B<br>
        GLI = (2 &times; G - R - B) / (2 &times; G + R + B)
    </div>
    <pre class="code">
# HSV Color Space Foliage Extraction
plant_mask = ((hue >= 25) & (hue <= 165) & (sat > 0.12) & (val > 0.15))
lesion_mask = leaf_mask & (~healthy_green) & (
    ((hue < 48) & (sat > 0.15)) |   # Chlorotic / Rust pustules
    ((val < 0.35) & (sat > 0.10)) | # Dark necrotic lesions
    (exg < -5)
)
lesion_percentage = (lesion_pixel_count / leaf_pixel_count) * 100.0
    </pre>

    <h2 class="sec-heading"><span class="sec-num">3</span>MobileNetV2 Neural Network Backbone</h2>
    <p>
        MobileNetV2 uses Inverted Residual Blocks with Linear Bottlenecks to drastically reduce model size (only ~3.5M parameters)
        and achieve sub-25 millisecond inference latency on mobile CPU devices:
    </p>
    <pre class="code">
# MobileNetV2 Transfer Learning Architecture in TensorFlow / Keras
base_model = tf.keras.applications.MobileNetV2(input_shape=(224, 224, 3), include_top=False, weights='imagenet')
base_model.trainable = False
x = tf.keras.layers.GlobalAveragePooling2D()(base_model.output)
x = tf.keras.layers.Dropout(0.3)(x)
x = tf.keras.layers.Dense(128, activation='relu')(x)
outputs = tf.keras.layers.Dense(13, activation='softmax')(x)
    </pre>

    <!-- PAGE 3: DISEASE PROFILES -->
    <div class="page-break"></div>

    <h2 class="sec-heading"><span class="sec-num">4</span>Trilingual Pathology Encyclopedia (Pepper, Grapes, Wheat, Corn)</h2>

    {disease_html}

</body>
</html>
"""
    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"AgroCure HTML written to {HTML_PATH}")

def convert_to_pdf():
    cmd = [
        CHROME_PATH,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--no-pdf-header-footer",
        f"--print-to-pdf={PDF_PATH}",
        str(HTML_PATH)
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if PDF_PATH.exists():
        size_kb = round(PDF_PATH.stat().st_size / 1024, 1)
        print(f"[SUCCESS] AgroCure AI Handbook generated: {PDF_PATH} ({size_kb} KB)")
        return True
    return False

if __name__ == "__main__":
    build_pdf_html()
    convert_to_pdf()
