import pypdfium2 as pdfium
from PIL import Image

pdf = pdfium.PdfDocument('/Users/ramrupsatpati/.gemini/antigravity/brain/58faa843-d2fc-401a-a000-1fd5f6e320d5/.user_uploaded/media_1792120349090_70123d65.pdf')

# Page 1 stickers:
# Question cat: near Purpose of Project
p0 = pdf[0].render(scale=3).to_pil()
w, h = p0.size
# Question cat is around x: 0.44 to 0.52, y: 0.18 to 0.32
cat_q = p0.crop((int(w * 0.43), int(h * 0.20), int(w * 0.52), int(h * 0.30)))
cat_q.save('cat_q.png')

# Team cats: near Team Details
cat_team = p0.crop((int(w * 0.33), int(h * 0.48), int(w * 0.43), int(h * 0.59)))
cat_team.save('cat_team.png')

# Page 2: cat reading on bottom left
p1 = pdf[1].render(scale=3).to_pil()
w, h = p1.size
cat_reading = p1.crop((int(w * 0.02), int(h * 0.72), int(w * 0.14), int(h * 0.95)))
cat_reading.save('cat_reading.png')

# Page 3: megaphone cat
p2 = pdf[2].render(scale=3).to_pil()
w, h = p2.size
cat_megaphone = p2.crop((int(w * 0.05), int(h * 0.22), int(w * 0.15), int(h * 0.34)))
cat_megaphone.save('cat_megaphone.png')

# Page 2: peering cat behind header
cat_peering = p1.crop((int(w * 0.65), int(h * 0.08), int(w * 0.75), int(h * 0.18)))
cat_peering.save('cat_peering.png')

print("Extracted sticker crops successfully!")
