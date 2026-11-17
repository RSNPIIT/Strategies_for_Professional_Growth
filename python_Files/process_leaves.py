from PIL import Image
import numpy as np

img = Image.open('sample_leaves_br.png').convert("RGBA")
data = np.array(img)

# White or near-white background removal
# If R, G, B are all > 245, make alpha = 0 or smooth feather
r, g, b, a = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]
# Calculate brightness
brightness = 0.299 * r + 0.587 * g + 0.114 * b

# Create smooth alpha mask
# When brightness is > 250 -> alpha 0
# When brightness is between 240 and 250 -> gradual fade
alpha = np.ones_like(brightness, dtype=np.uint8) * 255
white_mask = (r > 248) & (g > 248) & (b > 248)
alpha[white_mask] = 0

# Smooth transition for edge anti-aliasing
edge_mask = (r > 235) & (g > 235) & (b > 235) & (~white_mask)
factor = (255 - np.maximum.reduce([r, g, b])[edge_mask]) / 20.0
alpha[edge_mask] = np.clip(factor * 255, 0, 255).astype(np.uint8)

data[:,:,3] = alpha
result = Image.fromarray(data)
result.save("coral_leaves_br.png", "PNG")

# Also create flipped version for top-left
flipped = result.transpose(Image.FLIP_TOP_BOTTOM).transpose(Image.FLIP_LEFT_RIGHT)
flipped.save("coral_leaves_tl.png", "PNG")

print("Created coral_leaves_br.png and coral_leaves_tl.png with transparent alpha!")
