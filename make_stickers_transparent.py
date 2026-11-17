from PIL import Image
import numpy as np

for name in ['cat_q', 'cat_team', 'cat_reading', 'cat_megaphone', 'cat_peering']:
    try:
        img = Image.open(f'{name}.png').convert("RGBA")
        data = np.array(img)
        r, g, b, a = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]
        white_mask = (r > 240) & (g > 240) & (b > 240)
        data[white_mask, 3] = 0
        res = Image.fromarray(data)
        res.save(f'{name}_trans.png')
        print(f"Processed {name}_trans.png")
    except Exception as e:
        print(f"Error {name}: {e}")
