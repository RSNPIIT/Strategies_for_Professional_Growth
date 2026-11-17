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

# 1. Create Gradient Accent Bar Image
grad_w, grad_h = 516, 4
grad_im = Image.new("RGB", (grad_w, grad_h))
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
grad_path = '/tmp/grad_bar_accent.png'
grad_im.save(grad_path)

def build_positive_page_1(out_pdf_path):
    c = canvas.Canvas(out_pdf_path, pagesize=A4)
    
    # IITM Logo Top Right
    if os.path.exists("iitm_logo_clean.png"):
        c.drawImage("iitm_logo_clean.png", 501.75, 751.92, width=54, height=53.25, mask='auto')
        
    # Header Titles
    c.setFillColor(HEX_CORAL)
    c.setFont("Helvetica-Bold", 8.6)
    c.drawString(margin_x, 804, "IIT MADRAS BS DEGREE PROGRAMME")
    
    c.setFillColor(HEX_TEXT_MUTED)
    c.setFont("Helvetica", 7.8)
    c.drawString(margin_x, 792, "BSGN3001 · Strategies for Professional Growth · Group Project 2 (GP2)")
    
    c.setFillColor(HEX_TITLE)
    c.setFont("Helvetica-Bold", 17.5)
    c.drawString(margin_x, 768, "Deliverable 1.a: Interim Report")
    
    c.setFillColor(HEX_NAVY_HDR)
    c.setFont("Helvetica-Bold", 9.6)
    c.drawString(margin_x, 750, "Beyond Quick Fixes: Exploring Technical Debt & Developer Fatigue Through Systems Thinking")
    
    c.setFillColor(HEX_TEXT_MUTED)
    c.setFont("Helvetica", 7.8)
    c.drawString(margin_x, 737, "Team 114: Iterate · Sep 2026 term · Compiled by Samyabrata Roy (Team Lead, 22F2001443)")
    
    # Gradient Accent Bar
    c.drawImage(grad_path, margin_x, 729, width=w_content, height=2.2)
    
    y_cur = 716
    
    # CONTENTS Section
    c.setFillColor(HEX_TITLE)
    c.setFont("Helvetica-Bold", 9.8)
    c.drawString(margin_x, y_cur, "CONTENTS")
    y_cur -= 12
    
    c.setFillColor(HEX_TEXT_MAIN)
    c.setFont("Helvetica", 7.6)
    c.drawString(margin_x, y_cur, "Each page that follows is one member's 1-page individual report on the discussion they conducted with one external participant.")
    y_cur -= 8
    
    # Contents Table
    th_s = ParagraphStyle('THC', fontName='Helvetica-Bold', fontSize=7.4, leading=8.8, textColor=HEX_TITLE)
    td_s = ParagraphStyle('TDC', fontName='Helvetica', fontSize=7.2, leading=8.6, textColor=HEX_TEXT_MAIN)
    td_b = ParagraphStyle('TDCB', fontName='Helvetica-Bold', fontSize=7.4, leading=8.8, textColor=HEX_TITLE)
    td_p = ParagraphStyle('TDCP', fontName='Helvetica-Bold', fontSize=7.6, leading=8.8, textColor=HEX_CORAL, alignment=1)
    
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
        ('TOPPADDING', (0, 0), (-1, -1), 3.2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.2),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('GRID', (0, 0), (-1, -1), 0.5, HEX_BORDER),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, HEX_ROW_ALT]),
    ]))
    
    w_tc, h_tc = t_c.wrap(w_content, 180)
    t_c.drawOn(c, margin_x, y_cur - h_tc)
    y_cur -= (h_tc + 14)
    
    # WHAT THE FIVE DISCUSSIONS DEMONSTRATE Section (Positively Framed!)
    c.setFillColor(HEX_TITLE)
    c.setFont("Helvetica-Bold", 9.8)
    c.drawString(margin_x, y_cur, "WHAT THE FIVE DISCUSSIONS DEMONSTRATE")
    y_cur -= 12
    
    synth_p = (
        "Across 5 independent practitioner discussions (spanning AI R&D, Enterprise Consulting, Consumer Firmware, Global SaaS, and Industrial Automation; "
        "totaling 20.3 cumulative years of engineering experience), our qualitative fieldwork provides strong multi-paradigm validation for the core reinforcing loops (R1, R2) "
        "and systemic balancing mechanisms (B1, B2). Shortcuts provide immediate release velocity but accumulate latent debt that boomerangs as friction, requiring "
        "formal debt token capacity and psychological safety to sustain engineering health."
    )
    p_syn = Paragraph(f"<font size='7.4' color='#1e293b'>{synth_p}</font>",
                      ParagraphStyle('SynP', fontName='Helvetica', fontSize=7.4, leading=9.4))
    w_s, h_s = p_syn.wrap(w_content, 80)
    p_syn.drawOn(c, margin_x, y_cur - h_s)
    y_cur -= (h_s + 8)
    
    # Systems Validation Table (Positive, rigorous, constructive!)
    th_v = ParagraphStyle('THV', fontName='Helvetica-Bold', fontSize=7.2, leading=8.6, textColor=HEX_TITLE)
    td_v_bold = ParagraphStyle('TDVB', fontName='Helvetica-Bold', fontSize=7.0, leading=8.4, textColor=HEX_TITLE)
    td_v_sub  = ParagraphStyle('TDVS', fontName='Helvetica', fontSize=6.6, leading=8.0, textColor=HEX_TEXT_MUTED)
    td_v_body = ParagraphStyle('TDVD', fontName='Helvetica', fontSize=6.8, leading=8.4, textColor=HEX_TEXT_MAIN)
    td_v_tag  = ParagraphStyle('TDVT', fontName='Helvetica-Bold', fontSize=6.8, leading=8.4, textColor=HEX_TEAL, alignment=1)
    
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
            Paragraph("<b>Validated across all 5 inquiries:</b> Shortcuts provide immediate launch success but trigger delayed rework (P1: client scope cuts; P2: legacy patches; P3: showstopper patches; P4: quicker implementation to hit dates; P5: API handler bypass).", td_v_body),
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
        ('TOPPADDING', (0, 0), (-1, -1), 3.0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.0),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('GRID', (0, 0), (-1, -1), 0.5, HEX_BORDER),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, HEX_ROW_ALT]),
    ]))
    
    w_tv, h_tv = t_v.wrap(w_content, 260)
    t_v.drawOn(c, margin_x, y_cur - h_tv)
    y_cur -= (h_tv + 12)
    
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
    print("Generated positive Page 1 successfully.")

build_positive_page_1('/tmp/new_page_1_positive.pdf')
