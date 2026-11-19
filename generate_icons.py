from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs("assets", exist_ok=True)

def create_icon(size, path):
    img = Image.new('RGB', (size, size), color='#1e3a8a')
    draw = ImageDraw.Draw(img)
    # Draw simple yellow Python snake shape or letter 'P'
    margin = size // 6
    draw.ellipse([margin, margin, size - margin, size - margin], outline='#f59e0b', width=size//25)
    # Text P
    try:
        font = ImageFont.load_default()
    except Exception:
        font = None
    draw.text((size // 2 - size//10, size // 2 - size//8), "Py", fill="#ffffff")
    img.save(path)
    print(f"Created {path}")

create_icon(192, "assets/icon-192.png")
create_icon(512, "assets/icon-512.png")

