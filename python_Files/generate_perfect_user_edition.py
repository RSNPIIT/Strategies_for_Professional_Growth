"""
Deliverable 1.a: Interim Report (Master 6-Page Unified Dossier)
Incorporating User's Three Mandates:
1. Subtle hints of colour gradients (Header gradient accent bars, table header washes)
2. Reframe Page 1 positively: Highlighting how the 5 discussions empirically validate our Systems Thinking model, removing defeatist 'cuts against' framing.
3. IITM Logo prominently placed on each page (Pages 1 through 6)
"""

import os
import shutil
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfgen import canvas
import pypdfium2 as pdfium
from PIL import Image, ImageDraw

PAGE_WIDTH, PAGE_HEIGHT = A4  # 595.28 x 841.89 pt
margin_x = 39.75
w_content = 555.75 - 39.75    # 516.0 pt

HEX_TITLE     = HexColor("#0f2942")   # Dark navy title
HEX_SUBTITLE  = HexColor("#334155")   # Slate subtitle
HEX_NAVY_HDR  = HexColor("#1e3a8a")   # Royal navy header
HEX_TEXT_MAIN = HexColor("#1e293b")   # Charcoal body
HEX_TEXT_MUTED= HexColor("#64748b")   # Muted slate
HEX_BORDER    = HexColor("#cbd5e1")   # Border grey
HEX_BG_BOX    = HexColor("#f8fafc")   # Light background
HEX_ROW_ALT   = HexColor("#f8fafc")   # Table alternating row
HEX_CORAL     = HexColor("#be123c")   # Crimson accent
HEX_TEAL      = HexColor("#0f766e")   # Deep teal

# 1. Create High-Fidelity Vector-Smooth Gradient Accent Bar
grad_w, grad_h = 1032, 6
grad_im = Image.new("RGB", (grad_w, grad_h))
# Three-point gradient: Crimson #be123c -> Navy #1e3a8a -> Teal #0f766e
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
grad_bar_path = '/tmp/grad_bar_accent_hq.png'
grad_im.save(grad_bar_path)

# Subtle Gradient Wash for Table Headers
th_grad_w, th_grad_h = 1032, 40
th_grad_im = Image.new("RGB", (th_grad_w, th_grad_h))
for x in range(th_grad_w):
    r_x = x / th_grad_w
    # Soft slate-to-ice tint: #f1f5f9 (241, 245, 249) -> #e2e8f0 (226, 232, 240)
    r = int(241 * (1 - r_x * 0.4) + 226 * (r_x * 0.4))
    g = int(245 * (1 - r_x * 0.4) + 232 * (r_x * 0.4))
    b = int(249 * (1 - r_x * 0.4) + 240 * (r_x * 0.4))
    for y in range(th_grad_h):
        th_grad_im.putpixel((x, y), (r, g, b))
th_grad_path = '/tmp/th_grad_wash.png'
th_grad_im.save(th_grad_path)


# =============================================================================
# BUILD POSITIVE, RIGOROUS PAGE 1
# =============================================================================

def build_reimagined_page_1(out_pdf_path):
    c = canvas.Canvas(out_pdf_path, pagesize=A4)
    
    # Official IITM Emblem at Top Right
    if os.path.exists("iitm_logo_clean.png"):
        c.drawImage("iitm_logo_clean.png", 501.75, 751.92, width=54, height=53.25, mask='auto')
        
    # Header Titles
    c.setFillColor(HEX_CORAL)
    c.setFont("Helvetica-Bold", 8.8)
    c.drawString(margin_x, 804, "IIT MADRAS BS DEGREE PROGRAMME")
    
    c.setFillColor(HEX_TEXT_MUTED)
    c.setFont("Helvetica", 8.0)
    c.drawString(margin_x, 792, "BSGN3001 · Strategies for Professional Growth · Group Project 2 (GP2)")
    
    c.setFillColor(HEX_TITLE)
    c.setFont("Helvetica-Bold", 18.0)
    c.drawString(margin_x, 767, "Deliverable 1.a: Interim Report")
    
    c.setFillColor(HEX_NAVY_HDR)
    c.setFont("Helvetica-Bold", 9.8)
    c.drawString(margin_x, 749, "Beyond Quick Fixes: Exploring Technical Debt & Developer Fatigue Through Systems Thinking")
    
    c.setFillColor(HEX_TEXT_MUTED)
    c.setFont("Helvetica", 8.0)
    c.drawString(margin_x, 736, "Team 114: Iterate · Sep 2026 term · Compiled by Samyabrata Roy (Team Lead, 22F2001443)")
    
    # Sleek Gradient Accent Bar
    c.drawImage(grad_bar_path, margin_x, 727, width=w_content, height=2.4)
    
    y_cur = 712
    
    # CONTENTS Section
    c.setFillColor(HEX_TITLE)
    c.setFont("Helvetica-Bold", 10.2)
    c.drawString(margin_x, y_cur, "CONTENTS")
    y_cur -= 12
    
    c.setFillColor(HEX_TEXT_MAIN)
    c.setFont("Helvetica", 7.8)
    c.drawString(margin_x, y_cur, "Each page that follows is one member's 1-page individual report on the discussion they conducted with one external participant.")
    y_cur -= 8
    
    # Contents Table
    th_s = ParagraphStyle('THC', fontName='Helvetica-Bold', fontSize=7.6, leading=9.0, textColor=HEX_TITLE)
    td_s = ParagraphStyle('TDC', fontName='Helvetica', fontSize=7.4, leading=8.8, textColor=HEX_TEXT_MAIN)
    td_b = ParagraphStyle('TDCB', fontName='Helvetica-Bold', fontSize=7.6, leading=9.0, textColor=HEX_TITLE)
    td_p = ParagraphStyle('TDCP', fontName='Helvetica-Bold', fontSize=8.0, leading=9.2, textColor=HEX_CORAL, alignment=1)
    
    contents_data = [
        [
            Paragraph("<b>Team member</b>", th_s),
            Paragraph("<b>External participant</b>", th_s),
            Paragraph("<b>Role & organisation</b>", th_s),
            Paragraph("<b>Experience & domain</b>", th_s),
            Paragraph("<b>Page</b>", th_s)
        ],
        [
            Paragraph("<b>P1: Samyabrata Roy</b><br/><font color='#64748b'>22F2001443 · Team Lead</font>", td_s),
            Paragraph("<b>Rounak Biswas</b>", td_b),
            Paragraph("Software Developer, IDEAS-TIH (ISI Kolkata)", td_s),
            Paragraph("3 yrs 9 mos · Data science & AI R&D", td_s),
            Paragraph("<b>2</b>", td_p)
        ],
        [
            Paragraph("<b>P2: Abir Saha</b><br/><font color='#64748b'>23F3001436 · Project Manager</font>", td_s),
            Paragraph("<b>Anunay Sinha</b>", td_b),
            Paragraph("Software Developer, Deloitte USI", td_s),
            Paragraph("About 2 yrs · Enterprise backend & consulting", td_s),
            Paragraph("<b>3</b>", td_p)
        ],
        [
            Paragraph("<b>P3: Rishabh Barthwal</b><br/><font color='#64748b'>23F2004112 · Research Lead</font>", td_s),
            Paragraph("<b>Suraj Sajeev</b>", td_b),
            Paragraph("SDE-4, Systems & Firmware, Apple", td_s),
            Paragraph("6.5 yrs · Consumer electronics", td_s),
            Paragraph("<b>4</b>", td_p)
        ],
        [
            Paragraph("<b>P4: Piyush Tilokchandani</b><br/><font color='#64748b'>21F1006739 · Design Lead</font>", td_s),
            Paragraph("<b>Keshav Gupta</b>", td_b),
            Paragraph("Software Engineer, Deel", td_s),
            Paragraph("5+ yrs · HR-tech & payroll SaaS", td_s),
            Paragraph("<b>5</b>", td_p)
        ],
        [
            Paragraph("<b>P5: Ramrup Satpati</b><br/><font color='#64748b'>24F3004027 · Creative & Presentation Lead</font>", td_s),
            Paragraph("<b>Shubham Mishra</b>", td_b),
            Paragraph("CV & Full-Stack Engineer, Siemens", td_s),
            Paragraph("About 3 yrs · Industrial AI & full-stack", td_s),
            Paragraph("<b>6</b>", td_p)
        ],
    ]
    
    col_w_c = [120, 88, 142, 134, 32]
    t_c = Table(contents_data, colWidths=col_w_c)
    t_c.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HexColor("#f1f5f9")),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 3.8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.8),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('GRID', (0, 0), (-1, -1), 0.5, HEX_BORDER),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, HEX_ROW_ALT]),
    ]))
    
    w_tc, h_tc = t_c.wrap(w_content, 200)
    t_c.drawOn(c, margin_x, y_cur - h_tc)
    y_cur -= (h_tc + 14)
    
    # WHAT THE FIVE DISCUSSIONS DEMONSTRATE Section (Positive & Comprehensive!)
    c.setFillColor(HEX_TITLE)
    c.setFont("Helvetica-Bold", 10.2)
    c.drawString(margin_x, y_cur, "WHAT THE FIVE DISCUSSIONS DEMONSTRATE")
    y_cur -= 12
    
    synth_p = (
        "Across 5 independent practitioner discussions (spanning AI R&D, Enterprise Consulting, Consumer Firmware, Global SaaS, and Industrial Automation; "
        "totaling 20.3 cumulative years of engineering experience), our qualitative fieldwork provides strong multi-paradigm validation for the core reinforcing loops (R1, R2) "
        "and systemic balancing mechanisms (B1, B2). While operational contexts differ—from client-negotiated pilot triage to high-volume payroll microservices—the "
        "empirical evidence strongly confirms that short-term delivery pressure universally drives architectural shortcuts, accumulating latent friction that demands "
        "formal debt token capacity and psychological safety to sustain engineering health."
    )
    p_syn = Paragraph(f"<font size='7.6' color='#1e293b'>{synth_p}</font>",
                      ParagraphStyle('SynP', fontName='Helvetica', fontSize=7.6, leading=9.8))
    w_s, h_s = p_syn.wrap(w_content, 100)
    p_syn.drawOn(c, margin_x, y_cur - h_s)
    y_cur -= (h_s + 10)
    
    # Systems Validation Table (Constructive, Positive, Rigorous!)
    th_v = ParagraphStyle('THV', fontName='Helvetica-Bold', fontSize=7.4, leading=8.8, textColor=HEX_TITLE)
    td_v_bold = ParagraphStyle('TDVB', fontName='Helvetica-Bold', fontSize=7.2, leading=8.6, textColor=HEX_TITLE)
    td_v_sub  = ParagraphStyle('TDVS', fontName='Helvetica', fontSize=6.8, leading=8.2, textColor=HEX_TEXT_MUTED)
    td_v_body = ParagraphStyle('TDVD', fontName='Helvetica', fontSize=7.0, leading=8.6, textColor=HEX_TEXT_MAIN)
    td_v_tag  = ParagraphStyle('TDVT', fontName='Helvetica-Bold', fontSize=7.2, leading=8.6, textColor=HEX_TEAL, alignment=1)
    
    val_table_data = [
        [
            Paragraph("<b>Loop in our model</b>", th_v),
            Paragraph("<b>Core System Dynamics</b>", th_v),
            Paragraph("<b>Practitioner Evidence & Multi-Paradigm Grounding</b>", th_v),
            Paragraph("<b>Cohort Validation</b>", th_v)
        ],
        [
            Paragraph("<b>R1 Quick-fix spiral</b>", td_v_bold),
            Paragraph("Deadline pressure → shortcuts → latent technical debt → production rework", td_v_sub),
            Paragraph("<b>Validated across all 5 inquiries:</b> Shortcuts provide immediate launch success but trigger delayed rework (P1: deliberate client scope cuts; P2: legacy patches; P3: showstopper patches; P4: quicker implementation to hit dates; P5: API handler bypass).", td_v_body),
            Paragraph("<b>P1, P2, P3,<br/>P4, P5</b>", td_v_tag)
        ],
        [
            Paragraph("<b>R2 Fatigue & Burnout</b>", td_v_bold),
            Paragraph("Pressure & firefighting → cognitive fatigue → code fear & reduced velocity", td_v_sub),
            Paragraph("<b>Validated across high-workload crunches:</b> Chronic firefighting exhausts cognitive reserves (P5: developer burnout & 'black-box code fear'; P4: mental exhaustion & communication breakdown; P3: 8–10h urgent debugging marathons; P2: weekend release work). P1 notes high pressure is motivating initially, but depletes focus over sustained stretches.", td_v_body),
            Paragraph("<b>P2, P3,<br/>P4, P5</b>", td_v_tag)
        ],
        [
            Paragraph("<b>B1 Debt triage & refactoring</b>", td_v_bold),
            Paragraph("Transparent debt tracking → risk-based triage → capacity reservation", td_v_sub),
            Paragraph("<b>Empirically grounded:</b> Debt refactoring succeeds when linked to business risk and formal capacity (P1: risk triage for core functionality; P3: frequency and user-impact thresholds; P5: dedicated sprint token allocation agreed with PM; P4: explicit 18-item technical debt backlog).", td_v_body),
            Paragraph("<b>P1, P3,<br/>P4, P5</b>", td_v_tag)
        ],
        [
            Paragraph("<b>B2 Raising concerns & pushback</b>", td_v_bold),
            Paragraph("Psychological safety → deadline communication → scope trade-offs", td_v_sub),
            Paragraph("<b>Empirically grounded:</b> Pushback functions as a pressure release brake when psychological safety exists (P3: multi-stage ETAs with transparent justifications; P1: proactive scoping communication; P5: translating technical risk into business SLAs; P4: tech lead raising debt concerns).", td_v_body),
            Paragraph("<b>P1, P3,<br/>P4, P5</b>", td_v_tag)
        ],
        [
            Paragraph("<b>New: Proactive recovery breaks</b>", td_v_bold),
            Paragraph("Leadership rest enforcement → cognitive recovery → sustainable pace", td_v_sub),
            Paragraph("<b>Emergent balancing mechanism:</b> Engineering leadership actively nudges engineers to take mandatory recovery breaks after intense delivery crunches to prevent cumulative burnout (P4: Deel).", td_v_body),
            Paragraph("<b>P4</b>", td_v_tag)
        ]
    ]
    
    col_w_v = [105, 120, 239, 52]
    t_v = Table(val_table_data, colWidths=col_w_v)
    t_v.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HexColor("#f1f5f9")),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 3.8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.8),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('GRID', (0, 0), (-1, -1), 0.5, HEX_BORDER),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, HEX_ROW_ALT]),
    ]))
    
    w_tv, h_tv = t_v.wrap(w_content, 280)
    t_v.drawOn(c, margin_x, y_cur - h_tv)
    y_cur -= (h_tv + 14)
    
    # Footer
    c.setStrokeColor(HEX_BORDER)
    c.setLineWidth(0.6)
    c.line(margin_x, 22.7, margin_x + w_content, 22.7)
    
    c.setFillColor(HEX_TEXT_MUTED)
    c.setFont("Helvetica", 6.8)
    c.drawString(margin_x, 12.8, "Team 114: Iterate · SPG GP2 · Deliverable 1.a")
    c.drawRightString(margin_x + w_content, 12.8, "Cover · 6 pages in total")
    
    rem = y_cur - 22.7
    print(f"Page 1 remaining clearance: {rem:.1f} pt")
    
    c.showPage()
    c.save()
    print("[+] Saved reimagined Page 1")


# =============================================================================
# COMPOSE MASTER DOSSIER (APPLYING IITM LOGO & GRADIENT BAR TO ALL PAGES)
# =============================================================================

def compose_master_dossier():
    # 1. Build Page 1
    p1_pdf = "/tmp/final_reimagined_page_1.pdf"
    build_reimagined_page_1(p1_pdf)
    
    # 2. Open User's Uploaded PDF for Pages 2 to 6
    user_pdf_path = '/Users/ramrupsatpati/.gemini/antigravity/brain/58faa843-d2fc-401a-a000-1fd5f6e320d5/.user_uploaded/media_1794925123203_dd8aa44c.pdf'
    user_doc = pdfium.PdfDocument(user_pdf_path)
    
    # Load IITM Logo for embedding
    logo_img = Image.open('iitm_logo_clean.png').convert('RGB')
    grad_bar_img = Image.open(grad_bar_path).convert('RGB')
    
    # Process Pages 2 to 6: Overlay IITM Logo & Gradient Accent Bar
    # Header positions for gradient bar across pages:
    # Page 2: y = 756 pt
    # Page 3: y = 772.5 pt
    # Page 4: y = 772.5 pt
    # Page 5: y = 757.5 pt
    # Page 6: y = 774 pt
    bar_y_coords = [756.0, 772.5, 772.5, 757.5, 774.0]
    
    for idx in range(1, 6):
        page = user_doc[idx]
        
        # Insert IITM Logo at top right: x=510, y=786, w=44, h=44
        logo_obj = pdfium.PdfImage.new(user_doc)
        logo_obj.set_bitmap(pdfium.PdfBitmap.from_pil(logo_img))
        logo_obj.set_matrix(pdfium.PdfMatrix(44, 0, 0, 44, 510, 786))
        page.insert_obj(logo_obj)
        
        # Insert Gradient Accent Bar right over the red line
        y_bar = bar_y_coords[idx - 1]
        grad_obj = pdfium.PdfImage.new(user_doc)
        grad_obj.set_bitmap(pdfium.PdfBitmap.from_pil(grad_bar_img))
        grad_obj.set_matrix(pdfium.PdfMatrix(w_content, 0, 0, 2.4, margin_x, y_bar))
        page.insert_obj(grad_obj)
        
        page.gen_content()
        print(f"[+] Overlaid IITM logo and gradient accent bar on Page {idx + 1}")
    
    # 3. Create Final Combined Master Document
    master = pdfium.PdfDocument.new()
    
    # Import Page 1
    doc_p1 = pdfium.PdfDocument(p1_pdf)
    master.import_pages(doc_p1, [0])
    
    # Import Pages 2 to 6
    master.import_pages(user_doc, [1, 2, 3, 4, 5])
    
    master_path = "Team_114_SPG_IR_Sep_2026.pdf"
    master.save(master_path)
    print(f"[+] Master 6-Page Dossier successfully saved: {master_path} ({len(master)} pages)")
    
    # Copy Aliases
    aliases = [
        "Team_114_Iterate_Interim_Report.pdf",
        "Team_114_SPG_GP2_Deliverable_1a.pdf",
    ]
    for alias in aliases:
        shutil.copyfile(master_path, alias)
        print(f"[+] Copied alias: {alias}")
        
    # Standalone 5-page archive
    direct_5 = pdfium.PdfDocument.new()
    direct_5.import_pages(user_doc, [1, 2, 3, 4, 5])
    direct_5.save("Team_114_SPG_IR_Direct_5_Pages.pdf")
    print("[+] Saved standalone 5-page archive: Team_114_SPG_IR_Direct_5_Pages.pdf")

if __name__ == '__main__':
    compose_master_dossier()
