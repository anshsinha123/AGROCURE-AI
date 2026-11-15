from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

team_dir = Path(__file__).resolve().parent / "static" / "team"
team_dir.mkdir(parents=True, exist_ok=True)

devs = [
    {
        "filename": "dev1.png",
        "name": "Abhishek Sharma",
        "initials": "AS",
        "bg_top": (16, 185, 129),     # Emerald
        "bg_bottom": (13, 148, 136),  # Teal
        "accent": (52, 211, 153),
        "icon_label": "</> FULLSTACK"
    },
    {
        "filename": "dev2.png",
        "name": "Priya Patel",
        "initials": "PP",
        "bg_top": (124, 58, 237),    # Violet
        "bg_bottom": (79, 70, 229),   # Indigo
        "accent": (167, 139, 250),
        "icon_label": "AI / ML"
    },
    {
        "filename": "dev3.png",
        "name": "Rohan Verma",
        "initials": "RV",
        "bg_top": (37, 99, 235),     # Blue
        "bg_bottom": (2, 132, 199),   # Sky
        "accent": (96, 165, 250),
        "icon_label": "BACKEND"
    },
]

size = (400, 400)

for dev in devs:
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Draw smooth vertical gradient in a rounded square or circle
    # For a circular avatar:
    cx, cy, r = 200, 200, 180
    
    # Base circle with gradient
    for y in range(size[1]):
        t = y / size[1]
        r_col = int(dev["bg_top"][0] * (1 - t) + dev["bg_bottom"][0] * t)
        g_col = int(dev["bg_top"][1] * (1 - t) + dev["bg_bottom"][1] * t)
        b_col = int(dev["bg_top"][2] * (1 - t) + dev["bg_bottom"][2] * t)
        draw.line([(0, y), (size[0], y)], fill=(r_col, g_col, b_col, 255))
        
    # Mask to circle
    mask = Image.new("L", size, 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.ellipse((20, 20, 380, 380), fill=255)
    img.putalpha(mask)
    
    # Draw inner glowing border
    draw = ImageDraw.Draw(img)
    draw.ellipse((22, 22, 378, 378), outline=(255, 255, 255, 90), width=6)
    draw.ellipse((28, 28, 372, 372), outline=dev["accent"] + (180,), width=3)
    
    # Draw silhouette head & shoulders
    # Head
    draw.ellipse((140, 90, 260, 210), fill=(255, 255, 255, 240))
    # Shoulders
    draw.chord((80, 230, 320, 420), start=0, end=360, fill=(255, 255, 255, 240))
    
    # Initials overlay
    try:
        font_large = ImageFont.truetype("arial.ttf", 64)
        font_small = ImageFont.truetype("arial.ttf", 20)
    except:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()
        
    # Draw badge box on top of chest
    draw.rounded_rectangle((120, 290, 280, 335), radius=12, fill=(15, 23, 42, 230), outline=dev["accent"], width=2)
    
    # Text in badge box
    draw.text((200, 312), dev["icon_label"], fill=(255, 255, 255, 255), font=font_small, anchor="mm")
    
    # Monogram on head or top right
    draw.rounded_rectangle((280, 50, 350, 95), radius=10, fill=(15, 23, 42, 230), outline=(255, 255, 255, 200), width=2)
    draw.text((315, 72), dev["initials"], fill=dev["accent"], font=font_small, anchor="mm")
    
    out_path = team_dir / dev["filename"]
    img.save(out_path, "PNG")
    print(f"Created: {out_path}")
