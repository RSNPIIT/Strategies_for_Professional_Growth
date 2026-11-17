import os
import sys
from PIL import Image, ImageOps

# Source photo uploaded by user
SRC_PHOTO = "/Users/ramrupsatpati/.gemini/antigravity/brain/58faa843-d2fc-401a-a000-1fd5f6e320d5/.user_uploaded/media_1792068420954_edad5d39.png"
PROCESSED_PHOTO = "profile_photo_framed.png"

# Process photo: crop/fit and add background if needed
def prepare_photo():
    img = Image.open(SRC_PHOTO).convert("RGBA")
    # Create dark background matching slide
    bg = Image.new("RGBA", img.size, (20, 24, 30, 255))
    bg.paste(img, (0, 0), img)
    final_img = bg.convert("RGB")
    final_img.save(PROCESSED_PHOTO, "PNG", quality=95)
    print(f"[*] Processed photo saved to {PROCESSED_PHOTO}")

prepare_photo()
