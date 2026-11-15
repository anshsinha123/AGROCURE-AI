"""
AgroCure AI - Sample Leaf Generator
Generates realistic synthetic leaf test samples for the 4 target crops:
1. Tomato - Early Blight (Alternaria solani)
2. Potato - Late Blight (Phytophthora infestans)
3. Capsicum - Bacterial Spot (Xanthomonas vesicatoria)
4. Grapes - Black Rot (Guignardia bidwellii)
"""

from PIL import Image, ImageDraw, ImageFilter
from pathlib import Path
import numpy as np

SAMPLE_DIR = Path(__file__).resolve().parent.parent / "static" / "samples"
SAMPLE_DIR.mkdir(parents=True, exist_ok=True)

def create_tomato_early_blight():
    w, h = 420, 420
    img = Image.new("RGBA", (w, h), (248, 250, 252, 255))
    draw = ImageDraw.Draw(img)

    # Tomato compound serrated leaflet
    pts = [
        (210, 30), (230, 60), (255, 90), (240, 110), (275, 145),
        (255, 175), (285, 215), (255, 250), (270, 290), (235, 335),
        (210, 385), (185, 335), (150, 290), (165, 250), (135, 215),
        (165, 175), (145, 145), (180, 110), (165, 90), (190, 60)
    ]
    draw.polygon(pts, fill=(58, 140, 46, 255), outline=(38, 105, 30, 255))

    # Central midrib and lateral veins
    draw.line([(210, 385), (210, 35)], fill=(85, 175, 70, 255), width=3)
    for y, off in [(100, 45), (160, 55), (220, 60), (280, 50)]:
        draw.line([(210, y), (210 + off, y - 25)], fill=(75, 160, 62, 220), width=2)
        draw.line([(210, y), (210 - off, y - 25)], fill=(75, 160, 62, 220), width=2)

    # Early blight lesions: Concentric dark brown rings (target-board appearance) with chlorotic yellow halo
    lesions = [
        (240, 150, 24),
        (170, 210, 20),
        (235, 270, 22),
        (185, 120, 15),
        (225, 210, 18)
    ]
    for lx, ly, r in lesions:
        # Yellow chlorotic halo
        draw.ellipse([lx - r - 6, ly - r - 6, lx + r + 6, ly + r + 6], fill=(195, 190, 45, 200))
        # Concentric rings
        draw.ellipse([lx - r, ly - r, lx + r, ly + r], fill=(95, 55, 25, 255), outline=(50, 28, 12, 255))
        draw.ellipse([lx - int(r*0.65), ly - int(r*0.65), lx + int(r*0.65), ly + int(r*0.65)], outline=(125, 75, 35, 255), width=2)
        draw.ellipse([lx - int(r*0.35), ly - int(r*0.35), lx + int(r*0.35), ly + int(r*0.35)], fill=(45, 22, 10, 255))

    img = img.filter(ImageFilter.GaussianBlur(0.6))
    img.convert("RGB").save(SAMPLE_DIR / "sample_tomato_early_blight.jpg", quality=92)
    print("Created sample_tomato_early_blight.jpg")

def create_potato_late_blight():
    w, h = 420, 420
    img = Image.new("RGBA", (w, h), (248, 250, 252, 255))
    draw = ImageDraw.Draw(img)

    # Potato ovate leaflet with wavy margins
    pts = [
        (210, 35), (245, 75), (280, 140), (295, 210), (280, 280),
        (250, 340), (210, 385), (170, 340), (140, 280), (125, 210),
        (140, 140), (175, 75)
    ]
    draw.polygon(pts, fill=(52, 130, 48, 255), outline=(32, 95, 30, 255))

    # Midrib and lateral veins
    draw.line([(210, 385), (210, 40)], fill=(80, 165, 72, 255), width=4)
    for y in [95, 150, 205, 260, 315]:
        draw.line([(210, y), (275, y - 20)], fill=(70, 150, 65, 200), width=2)
        draw.line([(210, y), (145, y - 20)], fill=(70, 150, 65, 200), width=2)

    # Late blight lesions: Large, irregular, water-soaked dark brown to purplish-black necrotic blotches
    # often starting at margins, with pale chlorotic border and grayish-white downy mildew ring
    blotches = [
        # Margin lesion top right
        [(250, 110), (290, 130), (285, 185), (245, 160), (230, 130)],
        # Margin lesion bottom left
        [(130, 250), (170, 265), (165, 315), (140, 310)],
        # Central irregular necrosis
        [(185, 160), (225, 170), (220, 215), (180, 210), (175, 180)]
    ]
    for b in blotches:
        # Draw soft pale mildew halo
        draw.polygon(b, fill=(45, 35, 30, 240), outline=(180, 195, 160, 220))
        # Inner dark necrotic tissue
        for pt in b:
            draw.ellipse([pt[0]-10, pt[1]-10, pt[0]+10, pt[1]+10], fill=(30, 22, 18, 255))

    img = img.filter(ImageFilter.GaussianBlur(0.7))
    img.convert("RGB").save(SAMPLE_DIR / "sample_potato_late_blight.jpg", quality=92)
    print("Created sample_potato_late_blight.jpg")

def create_capsicum_bacterial_spot():
    w, h = 420, 420
    img = Image.new("RGBA", (w, h), (248, 250, 252, 255))
    draw = ImageDraw.Draw(img)

    # Capsicum / Bell pepper smooth ovate leaf
    pts = [
        (210, 25), (245, 70), (280, 140), (290, 210), (265, 280),
        (230, 340), (210, 375), (190, 340), (155, 280), (130, 210),
        (140, 140), (175, 70)
    ]
    draw.polygon(pts, fill=(46, 138, 50, 255), outline=(32, 102, 36, 255))

    # Midrib and side veins
    draw.line([(210, 375), (210, 30)], fill=(78, 172, 82, 255), width=4)
    for y in [90, 140, 190, 240, 290]:
        draw.line([(210, y), (268, y - 25)], fill=(68, 158, 72, 200), width=2)
        draw.line([(210, y), (152, y - 25)], fill=(68, 158, 72, 200), width=2)

    # Bacterial spots: small water-soaked dark spots with distinctive yellow halo
    spots = [
        (240, 150, 13), (170, 180, 11), (230, 230, 15),
        (180, 250, 12), (215, 110, 9), (160, 130, 10),
        (255, 200, 12), (185, 290, 11)
    ]
    for sx, sy, r in spots:
        draw.ellipse([sx - r - 5, sy - r - 5, sx + r + 5, sy + r + 5], fill=(190, 180, 42, 210))
        draw.ellipse([sx - r, sy - r, sx + r, sy + r], fill=(38, 30, 22, 255))

    img = img.filter(ImageFilter.GaussianBlur(0.6))
    img.convert("RGB").save(SAMPLE_DIR / "sample_capsicum_bacterial_spot.jpg", quality=92)
    # Also save as pepper for backwards compatibility
    img.convert("RGB").save(SAMPLE_DIR / "sample_pepper_bacterial_spot.jpg", quality=92)
    print("Created sample_capsicum_bacterial_spot.jpg")

def create_grapes_black_rot():
    w, h = 420, 420
    img = Image.new("RGBA", (w, h), (248, 250, 252, 255))
    draw = ImageDraw.Draw(img)

    # Grape palmate lobed leaf
    pts = [
        (210, 40), (250, 60), (320, 80), (340, 140), (350, 200),
        (310, 270), (270, 320), (220, 350), (200, 350), (150, 320),
        (110, 270), (70, 200), (80, 140), (100, 80), (170, 60)
    ]
    draw.polygon(pts, fill=(52, 124, 48, 255), outline=(36, 94, 34, 255))

    base = (210, 340)
    draw.line([base, (210, 50)], fill=(88, 158, 78, 255), width=4)
    draw.line([base, (325, 90)], fill=(82, 148, 72, 240), width=3)
    draw.line([base, (95, 90)], fill=(82, 148, 72, 240), width=3)
    draw.line([base, (340, 195)], fill=(78, 138, 68, 220), width=2)
    draw.line([base, (80, 195)], fill=(78, 138, 68, 220), width=2)

    # Black rot circular spots with tiny dark pycnidia
    spots = [
        (250, 130, 20), (160, 150, 23), (280, 210, 18),
        (170, 250, 19), (210, 180, 15), (230, 280, 16)
    ]
    for sx, sy, r in spots:
        draw.ellipse([sx - r, sy - r, sx + r, sy + r], fill=(132, 50, 34, 255), outline=(42, 22, 16, 255))
        for dx, dy in [(-4, -2), (3, 3), (0, 0), (5, -1), (-3, 4), (2, -3)]:
            draw.point((sx + dx, sy + dy), fill=(16, 12, 12, 255))

    img = img.filter(ImageFilter.GaussianBlur(0.7))
    img.convert("RGB").save(SAMPLE_DIR / "sample_grapes_black_rot.jpg", quality=92)
    print("Created sample_grapes_black_rot.jpg")

if __name__ == "__main__":
    create_tomato_early_blight()
    create_potato_late_blight()
    create_capsicum_bacterial_spot()
    create_grapes_black_rot()
    print("All 4 Target Crop leaf samples generated successfully!")
