import pypdfium2 as pdfium
from PIL import Image, ImageDraw

# Load user PDF
f = '/Users/ramrupsatpati/.gemini/antigravity/brain/58faa843-d2fc-401a-a000-1fd5f6e320d5/.user_uploaded/media_1794925123203_dd8aa44c.pdf'
doc = pdfium.PdfDocument(f)

# Create a subtle gradient image for the header accent bar
grad_w, grad_h = 516, 3
grad_im = Image.new("RGB", (grad_w, grad_h))
draw = ImageDraw.Draw(grad_im)
# Gradient from coral #be123c (190, 18, 60) to navy #1e3a8a (30, 58, 138) to teal #0f766e (15, 118, 110)
for x in range(grad_w):
    ratio = x / grad_w
    if ratio < 0.5:
        r2 = ratio / 0.5
        r = int(190 * (1 - r2) + 30 * r2)
        g = int(18 * (1 - r2) + 58 * r2)
        b = int(60 * (1 - r2) + 138 * r2)
    else:
        r2 = (ratio - 0.5) / 0.5
        r = int(30 * (1 - r2) + 15 * r2)
        g = int(58 * (1 - r2) + 118 * r2)
        b = int(138 * (1 - r2) + 110 * r2)
    for y in range(grad_h):
        grad_im.putpixel((x, y), (r, g, b))

grad_im.save('/tmp/grad_bar.png')

# Load IITM logo
logo = Image.open('iitm_logo_clean.png').convert('RGB')

# Test overlaying on page 2 (index 1)
page2 = doc[1]

# Insert gradient bar
grad_obj = pdfium.PdfImage.new(doc)
grad_obj.set_bitmap(pdfium.PdfBitmap.from_pil(grad_im))
# Position: x=39.75, y=755, w=516, h=2.5
grad_obj.set_matrix(pdfium.PdfMatrix(516, 0, 0, 2.5, 39.75, 755))
page2.insert_obj(grad_obj)

# Insert logo at top right
logo_obj = pdfium.PdfImage.new(doc)
logo_obj.set_bitmap(pdfium.PdfBitmap.from_pil(logo))
logo_obj.set_matrix(pdfium.PdfMatrix(45, 0, 0, 45, 510, 782))
page2.insert_obj(logo_obj)

page2.gen_content()

doc.save('/tmp/test_overlaid_p2.pdf')
print("Successfully overlaid gradient and logo on page 2!")

# Render to check
doc_out = pdfium.PdfDocument('/tmp/test_overlaid_p2.pdf')
bitmap = doc_out[1].render(scale=2)
bitmap.to_pil().save('/tmp/rendered_overlaid_p2.png')
print("Rendered to /tmp/rendered_overlaid_p2.png")
