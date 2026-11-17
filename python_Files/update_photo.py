from PIL import Image, ImageOps

SRC_PHOTO = "/Users/ramrupsatpati/.gemini/antigravity/brain/58faa843-d2fc-401a-a000-1fd5f6e320d5/.user_uploaded/media_1792071160385_ebc7d8be.jpg"
PROCESSED_PHOTO = "profile_photo_framed.png"

img = Image.open(SRC_PHOTO).convert("RGB")
# Aspect ratio of the photo slot: 320 x 425 = 0.753
target_w = 700
target_h = int(target_w * (425 / 320))  # approx 930

# Using ImageOps.fit to center crop cleanly
fitted = ImageOps.fit(img, (target_w, target_h), centering=(0.5, 0.45))
fitted.save(PROCESSED_PHOTO, "JPEG", quality=95)
print(f"[*] Updated {PROCESSED_PHOTO} with size {fitted.size}")
