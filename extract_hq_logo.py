import pypdfium2 as pdfium
from PIL import Image

pdf = pdfium.PdfDocument('/Users/ramrupsatpati/.gemini/antigravity/brain/58faa843-d2fc-401a-a000-1fd5f6e320d5/.user_uploaded/media_1792120349090_70123d65.pdf')
p0 = pdf[0].render(scale=5).to_pil()
w, h = p0.size

# Precise crop of the IITM logo
logo = p0.crop((int(w * 0.84), int(h * 0.04), int(w * 0.965), int(h * 0.26)))
# Trim pure white border
logo.save('iitm_logo_hq.png')
print('HQ Logo saved:', logo.size)
