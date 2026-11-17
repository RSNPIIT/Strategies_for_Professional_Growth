"""
Team 114 (Iterate) - Deliverable 1.a: Interim Report (Qualitative Fieldwork Findings)
Standardized Unified Format across ALL Members modeled on Rishabh Barthwal's Executive Layout
Strictly 6 Pages Total (A4 Format: 595.28 x 841.89 pt)
- Page 1: TL;DR Executive Summary Dossier & Cohort Navigation Table
- Page 2: Samyabrata Roy (Team Lead) | Participant: Rounak Biswas (IDEAS-TIH, ISI Kolkata)
- Page 3: Abir Saha (Project Manager) | Participant: Anunay Sinha (Deloitte Consulting)
- Page 4: Rishabh Barthwal (Research Lead) | Participant: Suraj Sajeev (Apple Inc.)
- Page 5: Piyush Tilokchandani (Design Lead) | Participant: Keshav Gupta (Deel)
- Page 6: Ramrup Satpati (Creative Lead) | Participant: Shubham Mishra (Siemens Automation)
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

PAGE_WIDTH, PAGE_HEIGHT = A4  # 595.28 x 841.89 pt
margin_x = 42.1
w_content = 553.2 - 42.1      # 511.1 pt
body_x = 48.5
w_body = 503.6

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


def build_member_report(data, out_pdf_path, page_num):
    c = canvas.Canvas(out_pdf_path, pagesize=A4)
    
    # 1. Title
    c.setFillColor(HEX_TITLE)
    c.setFont("Helvetica-Bold", 14.0)
    c.drawCentredString(PAGE_WIDTH / 2, 788, "INDIVIDUAL INTERIM REPORT")
    
    # Subtitle
    c.setFillColor(HEX_SUBTITLE)
    c.setFont("Helvetica", 7.9)
    c.drawCentredString(PAGE_WIDTH / 2, 771, "SPG GP2 | Team 114: Iterate | Beyond Quick Fixes: Exploring Technical Debt and Developer Fatigue Through Systems")
    c.drawCentredString(PAGE_WIDTH / 2, 761, "Thinking")
    
    # 2. Metadata Box Table
    td_meta = ParagraphStyle('MTD', fontName='Helvetica', fontSize=7.4, leading=9.2, textColor=HEX_TEXT_MAIN)
    table_data = [
        [
            Paragraph(f"<b>Interviewer</b><br/>{data['interviewer']}", td_meta),
            Paragraph(f"<b>Interviewee</b><br/>{data['interviewee']}", td_meta),
            Paragraph(f"<b>Role and experience</b><br/>{data['role_exp']}", td_meta),
            Paragraph(f"<b>Industry and format</b><br/>{data['industry_format']}", td_meta)
        ]
    ]
    col_w = [108.1, 107.8, 155.9, 139.3]
    t = Table(table_data, colWidths=col_w)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), HEX_BG_BOX),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 3.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 6.5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6.5),
        ('GRID', (0, 0), (-1, -1), 0.5, HEX_BORDER),
    ]))
    
    w_tab, h_tab = t.wrap(w_content, 60)
    t.drawOn(c, margin_x, 715)
    
    y_cur = 694.4
    
    # 3. Focus
    c.setFillColor(HEX_TITLE)
    c.setFont("Helvetica-Bold", 8.8)
    c.drawString(body_x, y_cur, "Interview focus and participant relevance")
    y_cur -= 13
    
    p_focus = Paragraph(f"<font size='7.85' color='#1e293b'>{data['focus_text']}</font>",
                        ParagraphStyle('FP', fontName='Helvetica', fontSize=7.85, leading=10.0))
    w_f, h_f = p_focus.wrap(w_body, 120)
    p_focus.drawOn(c, body_x, y_cur - h_f)
    y_cur -= (h_f + 11)
    
    # 4. Findings (1 to 6)
    for idx, (f_title, f_body, f_quote) in enumerate(data['findings'], start=1):
        c.setFillColor(HEX_TITLE)
        c.setFont("Helvetica-Bold", 8.1)
        c.drawString(body_x, y_cur, f"{idx}. {f_title}")
        y_cur -= 11
        
        f_p_text = f"{f_body}<br/><font color='#334155'><i>{f_quote}</i></font>"
        p_find = Paragraph(f"<font size='7.85' color='#1e293b'>{f_p_text}</font>",
                           ParagraphStyle('FindP', fontName='Helvetica', fontSize=7.85, leading=10.0))
        w_find, h_find = p_find.wrap(w_body, 120)
        p_find.drawOn(c, body_x, y_cur - h_find)
        y_cur -= (h_find + 9)
    
    # 5. Reflection
    c.setFillColor(HEX_TITLE)
    c.setFont("Helvetica-Bold", 8.8)
    c.drawString(body_x, y_cur, "Personal learning and reflection")
    y_cur -= 13
    
    ref_full = f"{data['reflection_text']}<br/><br/><b>Overall observation:</b> {data['observation_text']}"
    p_ref = Paragraph(f"<font size='7.85' color='#1e293b'>{ref_full}</font>",
                      ParagraphStyle('RefP', fontName='Helvetica', fontSize=7.85, leading=10.0))
    w_ref, h_ref = p_ref.wrap(w_body, 220)
    p_ref.drawOn(c, body_x, y_cur - h_ref)
    y_cur -= (h_ref + 10)
    
    # 6. Footer
    c.setStrokeColor(HEX_BORDER)
    c.setLineWidth(0.6)
    c.line(42.1, 22.7, 553.2, 22.7)
    
    c.setFillColor(HEX_TEXT_MUTED)
    c.setFont("Helvetica", 6.8)
    c.drawString(42.5, 12.8, "Team 114: Iterate | SPG GP2")
    c.drawRightString(552.1, 12.8, f"Page {page_num} of 6")
    
    rem = y_cur - 22.7
    print(f"[*] Page {page_num} ({data['interviewee']}): remaining clearance: {rem:.1f} pt")
    
    c.showPage()
    c.save()


def build_tldr_cover_page(out_pdf_path):
    c = canvas.Canvas(out_pdf_path, pagesize=A4)
    
    # Header Titles
    c.setFillColor(HEX_CORAL)
    c.setFont("Helvetica-Bold", 8.6)
    c.drawCentredString(PAGE_WIDTH / 2, 792, "IIT MADRAS BS DEGREE PROGRAMME  •  BSGN3001: STRATEGIES FOR PROFESSIONAL GROWTH")
    
    c.setFillColor(HEX_TITLE)
    c.setFont("Helvetica-Bold", 14.5)
    c.drawCentredString(PAGE_WIDTH / 2, 774, "DELIVERABLE 1.A: CONSOLIDATED INTERIM REPORT")
    
    c.setFillColor(HEX_SUBTITLE)
    c.setFont("Helvetica", 8.0)
    c.drawCentredString(PAGE_WIDTH / 2, 760, "SPG GP2 | Team 114: Iterate | Beyond Quick Fixes: Exploring Technical Debt and Developer Fatigue Through Systems Thinking")
    
    # 4-Column Metadata Box
    td_meta = ParagraphStyle('MTD1', fontName='Helvetica', fontSize=7.4, leading=9.2, textColor=HEX_TEXT_MAIN)
    table_data = [
        [
            Paragraph("<b>Academic Programme</b><br/>IIT Madras BS Degree<br/>BSGN3001 (GP2)", td_meta),
            Paragraph("<b>Team Roster</b><br/>Team 114 (Iterate)<br/>5 Fieldwork Inquiries", td_meta),
            Paragraph("<b>Deliverable Scope</b><br/>Deliverable 1.a (Interim Report)<br/>Primary Fieldwork (N=5)", td_meta),
            Paragraph("<b>Leadership & Dossier</b><br/>Ramrup Satpati (24F3004027)<br/>Acting Lead Compilation", td_meta)
        ]
    ]
    col_w = [125.0, 115.0, 140.0, w_content - (125.0 + 115.0 + 140.0)]
    t_meta = Table(table_data, colWidths=col_w)
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), HEX_BG_BOX),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 3.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 6.5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6.5),
        ('GRID', (0, 0), (-1, -1), 0.5, HEX_BORDER),
    ]))
    
    w_tab, h_tab = t_meta.wrap(w_content, 60)
    t_meta.drawOn(c, margin_x, 715)
    
    y_cur = 696.0
    
    # 1. TL;DR Executive Synthesis
    c.setFillColor(HEX_TITLE)
    c.setFont("Helvetica-Bold", 8.8)
    c.drawString(margin_x, y_cur, "1. Executive Synthesis — The Core Qualitative Insight")
    y_cur -= 6
    
    tldr_text = (
        "Across 5 independent qualitative practitioner interviews (spanning AI R&D, Enterprise Consulting, Consumer Firmware, Global SaaS, "
        "and Industrial Automation; totaling 20.3 cumulative years of engineering experience), our fieldwork confirms that unrealistic delivery deadlines trigger a pervasive "
        "<b>Quick-Fix Trap (R1)</b>: teams intentionally bypass architectural service layers and automated test suites to hit immediate demo milestones. While short-term "
        "release goals are met, the resulting latent technical debt inevitably explodes into emergency weekend firefighting, severe cognitive fatigue, and an organizational "
        "fear of touching legacy code (<b>Burnout Trap, R2</b>). Breaking this self-reinforcing failure loop requires two systemic balancing interventions: "
        "<b>(1)</b> translating code maintenance into commercial business metrics (downtime cost, SLA adherence) so product managers allocate a protected sprint debt capacity "
        "(<b>Token Allocation, B1</b>), and <b>(2)</b> establishing team psychological safety where developers can push back on unrealistic deadlines using transparent, "
        "multi-stage delivery milestones (<b>Pushback Brake, B2</b>)."
    )
    p_tldr = Paragraph(f"<font size='7.4' color='#1e293b'>{tldr_text}</font>",
                       ParagraphStyle('TLDRP', fontName='Helvetica', fontSize=7.4, leading=9.8))
    w_t, h_t = p_tldr.wrap(w_content - 18, 120)
    
    tldr_box_h = h_t + 14
    c.setFillColor(HexColor("#f0fdfa"))
    c.setStrokeColor(HexColor("#99f6e4"))
    c.setLineWidth(0.8)
    c.roundRect(margin_x, y_cur - tldr_box_h, w_content, tldr_box_h, 4, fill=1, stroke=1)
    p_tldr.drawOn(c, margin_x + 9, y_cur - tldr_box_h + 7)
    y_cur -= (tldr_box_h + 12)
    
    # 2. Primary Practitioner Cohort & Report Navigation
    c.setFillColor(HEX_TITLE)
    c.setFont("Helvetica-Bold", 8.8)
    c.drawString(margin_x, y_cur, "2. Primary Practitioner Cohort & Report Navigation")
    y_cur -= 6
    
    th_s = ParagraphStyle('TH1', fontName='Helvetica-Bold', fontSize=7.0, leading=8.6, textColor=colors.white)
    td_s = ParagraphStyle('TD1', fontName='Helvetica', fontSize=6.6, leading=8.4, textColor=HEX_TEXT_MAIN)
    td_b = ParagraphStyle('TDB1', fontName='Helvetica-Bold', fontSize=6.8, leading=8.6, textColor=HEX_TITLE)
    td_p = ParagraphStyle('TDP1', fontName='Helvetica-Bold', fontSize=7.0, leading=8.4, textColor=HEX_CORAL, alignment=1)
    
    nav_table_data = [
        [
            Paragraph("<b>Team Member (Roll & Role)</b>", th_s),
            Paragraph("<b>External Participant</b>", th_s),
            Paragraph("<b>Role & Organization</b>", th_s),
            Paragraph("<b>YoE & Domain</b>", th_s),
            Paragraph("<b>Core Systems Thinking Insight</b>", th_s),
            Paragraph("<b>Report</b>", th_s)
        ],
        [
            Paragraph("<b>Samyabrata Roy</b><br/><font color='#64748b'>Roll: 22F2001443 (Team Lead)</font>", td_s),
            Paragraph("<b>Rounak Biswas</b>", td_b),
            Paragraph("Software Developer<br/>IDEAS-TIH (ISI Kolkata)", td_s),
            Paragraph("3.8 YoE<br/>AI & Govt R&D", td_s),
            Paragraph("Scope triage; motivating pressure dynamics; risk-based debt rules (B1).", td_s),
            Paragraph("<b>Page 2</b>", td_p)
        ],
        [
            Paragraph("<b>Abir Saha</b><br/><font color='#64748b'>Roll: 23F3001436 (Project Manager)</font>", td_s),
            Paragraph("<b>Anunay Sinha</b>", td_b),
            Paragraph("Software Developer<br/>Deloitte Consulting", td_s),
            Paragraph("2.0 YoE<br/>Enterprise Backend", td_s),
            Paragraph("Inherited legacy frameworks; microservices overhead; pre-QA mock DBs.", td_s),
            Paragraph("<b>Page 3</b>", td_p)
        ],
        [
            Paragraph("<b>Rishabh Barthwal</b><br/><font color='#64748b'>Roll: 23F2004112 (Research Lead)</font>", td_s),
            Paragraph("<b>Suraj Sajeev</b>", td_b),
            Paragraph("SDE-4 Systems & Firmware<br/>Apple Inc.", td_s),
            Paragraph("6.5 YoE<br/>Consumer Tech", td_s),
            Paragraph("Urgent 8-10h/day debugging; multi-ETA pushback (B2); readable code.", td_s),
            Paragraph("<b>Page 4</b>", td_p)
        ],
        [
            Paragraph("<b>Piyush Tilokchandani</b><br/><font color='#64748b'>Roll: 21F1006739 (Design Lead)</font>", td_s),
            Paragraph("<b>Keshav Gupta</b>", td_b),
            Paragraph("Software Engineer<br/>Deel (Payroll SaaS)", td_s),
            Paragraph("5.0+ YoE<br/>Fintech & SaaS", td_s),
            Paragraph("18-item debt backlog deferral; developer cognitive depletion; recovery breaks.", td_s),
            Paragraph("<b>Page 5</b>", td_p)
        ],
        [
            Paragraph("<b>Ramrup Satpati</b><br/><font color='#64748b'>Roll: 24F3004027 (Creative Lead)</font>", td_s),
            Paragraph("<b>Shubham Mishra</b>", td_b),
            Paragraph("CV & Full-Stack Engineer<br/>Siemens Automation", td_s),
            Paragraph("3.0 YoE<br/>Industrial AI", td_s),
            Paragraph("API handler bypass; black-box code fear; sprint token capacity allocation.", td_s),
            Paragraph("<b>Page 6</b>", td_p)
        ],
    ]
    
    col_w_nav = [108, 76, 110, 72, 110, 35.1]
    t_nav = Table(nav_table_data, colWidths=col_w_nav)
    t_nav.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HEX_NAVY_HDR),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 4.2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4.2),
        ('LEFTPADDING', (0, 0), (-1, -1), 5.5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5.5),
        ('GRID', (0, 0), (-1, -1), 0.5, HEX_BORDER),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, HEX_ROW_ALT]),
    ]))
    
    w_nav, h_nav = t_nav.wrap(w_content, 260)
    t_nav.drawOn(c, margin_x, y_cur - h_nav)
    y_cur -= (h_nav + 12)
    
    # 3. Cross-Interview Qualitative Synthesis (2 Side-by-Side Cards)
    c.setFillColor(HEX_TITLE)
    c.setFont("Helvetica-Bold", 8.8)
    c.drawString(margin_x, y_cur, "3. Cross-Interview Qualitative Synthesis & Systems Archetypes")
    y_cur -= 6
    
    card_w = (w_content - 12) / 2  # ~249.5 pt
    card_h = 126
    
    # Card Left: Reinforcing Traps
    c.setFillColor(HexColor("#fff1f2"))
    c.setStrokeColor(HexColor("#fecdd3"))
    c.setLineWidth(0.8)
    c.roundRect(margin_x, y_cur - card_h, card_w, card_h, 4, fill=1, stroke=1)
    
    c.setFillColor(HEX_CORAL)
    c.setFont("Helvetica-Bold", 7.6)
    c.drawString(margin_x + 8, y_cur - 13, "REINFORCING TRAPS: COMPOUNDING FRICTION (R1 & R2)")
    c.setFillColor(HEX_TEXT_MUTED)
    c.setFont("Helvetica-Bold", 6.4)
    c.drawString(margin_x + 8, y_cur - 24, "Prevalence: Supported across all 5 practitioner interviews")
    
    r_text = (
        "• <b>R1: Quick-Fix Trap Spiral:</b> Under demo or launch pressure, teams bypass service layers "
        "or test suites (Participant 5: API handler bypass; Participant 4: 18-item backlog deferred). Immediate success "
        "legitimizes the shortcut, but delayed technical debt triggers rework and ongoing firefighting.<br/><br/>"
        "• <b>R2: Developer Burnout Trap:</b> Chronic firefighting (Participant 3: 8-10h/day debugging) exhausts cognitive "
        "capacity. Over time, engineers fear touching fragile files, treating them like 'black boxes' (Participant 5), "
        "directly depleting development velocity and morale."
    )
    p_r = Paragraph(f"<font size='6.4' color='#1e293b'>{r_text}</font>",
                    ParagraphStyle('RText1', fontName='Helvetica', fontSize=6.4, leading=8.6))
    p_r.wrap(card_w - 16, card_h - 32)
    p_r.drawOn(c, margin_x + 8, y_cur - card_h + 8)
    
    # Card Right: Balancing Levers
    gx = margin_x + card_w + 12
    c.setFillColor(HexColor("#f0fdfa"))
    c.setStrokeColor(HexColor("#99f6e4"))
    c.setLineWidth(0.8)
    c.roundRect(gx, y_cur - card_h, card_w, card_h, 4, fill=1, stroke=1)
    
    c.setFillColor(HEX_TEAL)
    c.setFont("Helvetica-Bold", 7.6)
    c.drawString(gx + 8, y_cur - 13, "BALANCING LEVERS: STRUCTURAL SOLUTIONS (B1 & B2)")
    c.setFillColor(HEX_TEXT_MUTED)
    c.setFont("Helvetica-Bold", 6.4)
    c.drawString(gx + 8, y_cur - 24, "Prevalence: Implemented via token budgets & safety culture")
    
    b_text = (
        "• <b>B1: Sprint Debt Token Allocation:</b> Refactoring requests stall when framed as abstract 'code hygiene'. "
        "Breaking the trap requires translating debt into commercial business metrics (downtime cost, SLA compliance), "
        "enabling PMs to allocate a formal sprint budget (tokens) for debt reduction (Participant 5).<br/><br/>"
        "• <b>B2: Psychological Safety & Pushback:</b> Developer fatigue increases the necessity for scope pushback, "
        "which only functions when psychological safety is established (Participant 3: multi-stage ETAs; Participant 4: "
        "recovery breaks; Participant 1: scope cuts). Clear safety de-escalates unrealistic pressure."
    )
    p_b = Paragraph(f"<font size='6.4' color='#1e293b'>{b_text}</font>",
                    ParagraphStyle('BText1', fontName='Helvetica', fontSize=6.4, leading=8.6))
    p_b.wrap(card_w - 16, card_h - 32)
    p_b.drawOn(c, gx + 8, y_cur - card_h + 8)
    
    y_cur -= (card_h + 12)
    
    # 4. Methodology & Research Rigor
    c.setFillColor(HEX_TITLE)
    c.setFont("Helvetica-Bold", 8.8)
    c.drawString(margin_x, y_cur, "4. Research Rigor & Methodological Assurance")
    y_cur -= 6
    
    meth_h = 52
    c.setFillColor(HEX_BG_BOX)
    c.setStrokeColor(HEX_BORDER)
    c.setLineWidth(0.6)
    c.roundRect(margin_x, y_cur - meth_h, w_content, meth_h, 4, fill=1, stroke=1)
    
    m_text = (
        "• <b>Fieldwork Protocols:</b> 5 primary 1-on-1 virtual sessions (30–45 min duration) with dual webcams active per IITM evaluation rubrics; informed written consent gathered via email and confirmed on-camera.<br/>"
        "• <b>Transcription & Audit:</b> Audio extracted and transcribed via speech tools with multi-pass technical terminology verification (race conditions, token capacity, API handlers, microservices).<br/>"
        "• <b>Academic Frameworks:</b> Peter Senge's (1990) Systems Thinking archetypes; Amy Edmondson's (1999) Psychological Safety framework; DORA empirical delivery research (Forsgren, Humble, & Kim, 2018)."
    )
    p_m = Paragraph(f"<font size='6.5' color='#334155'>{m_text}</font>",
                    ParagraphStyle('MethP1', fontName='Helvetica', fontSize=6.5, leading=8.6))
    p_m.wrap(w_content - 16, meth_h - 10)
    p_m.drawOn(c, margin_x + 8, y_cur - meth_h + 6)
    y_cur -= (meth_h + 12)
    
    # Footer
    c.setStrokeColor(HEX_BORDER)
    c.setLineWidth(0.6)
    c.line(42.1, 22.7, 553.2, 22.7)
    
    c.setFillColor(HEX_TEXT_MUTED)
    c.setFont("Helvetica", 6.8)
    c.drawString(42.5, 12.8, "Team 114: Iterate | SPG GP2")
    c.drawRightString(552.1, 12.8, "Page 1 of 6")
    
    rem = y_cur - 22.7
    print(f"[*] Page 1 (TL;DR Cover): remaining clearance: {rem:.1f} pt")
    
    c.showPage()
    c.save()


# Import Member Data Dictionaries
from generate_unified_interim_reports_v2 import REPORT_SAMYABRATA, REPORT_ABIR, REPORT_RISHABH, REPORT_PIYUSH, REPORT_RAMRUP

def run_master_build():
    print("[*] Generating Master 6-Page Unified Dossier...")
    
    # Page 1
    cover_pdf = "page_1_tldr_cover.pdf"
    build_tldr_cover_page(cover_pdf)
    
    # Pages 2 to 6
    roster = [
        (REPORT_SAMYABRATA, "page_2_samyabrata.pdf", 2),
        (REPORT_ABIR,        "page_3_abir.pdf",        3),
        (REPORT_RISHABH,     "page_4_rishabh.pdf",     4),
        (REPORT_PIYUSH,      "page_5_piyush.pdf",      5),
        (REPORT_RAMRUP,      "page_6_ramrup.pdf",      6),
    ]
    
    pages = [cover_pdf]
    for data, path, num in roster:
        build_member_report(data, path, num)
        pages.append(path)
    
    # Combine into Master PDF
    master = pdfium.PdfDocument.new()
    for p in pages:
        doc = pdfium.PdfDocument(p)
        master.import_pages(doc, [0])
    
    master_path = "Team_114_SPG_IR_Sep_2026.pdf"
    master.save(master_path)
    print(f"[+] Master PDF saved: {master_path} ({len(master)} pages)")
    
    # Copy Aliases
    aliases = [
        "Team_114_Iterate_Interim_Report.pdf",
        "Team_114_SPG_GP2_Deliverable_1a.pdf",
    ]
    for a in aliases:
        shutil.copyfile(master_path, a)
        print(f"[+] Copied alias: {a}")
        
    # Also save standalone 5-page archive
    direct_5 = pdfium.PdfDocument.new()
    for p in pages[1:]:
        doc = pdfium.PdfDocument(p)
        direct_5.import_pages(doc, [0])
    direct_5.save("Team_114_SPG_IR_Direct_5_Pages.pdf")
    print("[+] Saved standalone 5-page archive: Team_114_SPG_IR_Direct_5_Pages.pdf")

if __name__ == '__main__':
    run_master_build()
