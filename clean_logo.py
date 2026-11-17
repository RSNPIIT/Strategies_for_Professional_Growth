from PIL import Image
import numpy as np

img = Image.open('iitm_logo_hq.png').convert("RGBA")
data = np.array(img)
r, g, b, a = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]
# Outside the circle make transparent
h, w = r.shape
cy, cx = h / 2.0, w / 2.0
radius = min(h, w) * 0.47

y, x = np.ogrid[:h, :w]
dist_from_center = np.sqrt((x - cx)**2 + (y - cy)**2)
mask_outside = dist_from_center > radius
data[mask_outside, 3] = 0

clean_img = Image.fromarray(data)
clean_img.save("iitm_logo_clean.png")
print("Saved iitm_logo_clean.png!")
