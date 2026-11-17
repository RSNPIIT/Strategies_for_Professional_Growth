from PIL import Image
import numpy as np

img = Image.open('/Users/ramrupsatpati/.gemini/antigravity/brain/58faa843-d2fc-401a-a000-1fd5f6e320d5/.user_uploaded/media_1792122496996_1333a50c.png').convert("RGBA")
bg_color = np.array([49, 63, 100])

def isolate_star(crop_box, out_name):
    cropped = img.crop(crop_box)
    c_arr = np.array(cropped)
    rgb = c_arr[:, :, :3].astype(float)
    
    # Distance from true background color
    dist = np.sqrt(np.sum((rgb - bg_color)**2, axis=2))
    
    alpha = np.ones(dist.shape, dtype=np.uint8) * 255
    bg_mask = dist < 22
    alpha[bg_mask] = 0
    
    # Smooth fringe
    feather = (dist >= 22) & (dist < 40)
    factor = (dist[feather] - 22) / 18.0
    alpha[feather] = np.clip(factor * 255, 0, 255).astype(np.uint8)
    
    c_arr[:, :, 3] = alpha
    res = Image.fromarray(c_arr)
    res.save(out_name)
    print(f"Saved {out_name}")

w, h = img.size
isolate_star((int(w * 0.12), int(h * 0.02), int(w * 0.52), int(h * 0.46)), "ninja_star_4pt.png")
isolate_star((int(w * 0.61), int(h * 0.02), int(w * 0.98), int(h * 0.46)), "ninja_star_8pt.png")
isolate_star((int(w * 0.11), int(h * 0.52), int(w * 0.52), int(h * 0.98)), "ninja_star_faceted.png")
isolate_star((int(w * 0.62), int(h * 0.53), int(w * 0.98), int(h * 0.97)), "ninja_star_curved.png")
