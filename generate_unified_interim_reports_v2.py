"""
Team 114: Iterate - Deliverable 1.a: Interim Report (Qualitative Fieldwork)
Format: High-Impact Executive Academic Dossier (Modeled after Rishabh Barthwal's Updated Format)
Dimensions: Standard A4 (595.28 x 841.89 pt)
Strictly 6 Pages:
  - Page 1: TL;DR Executive Summary Dossier & Navigation Table
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
margin_x = 42.5
w_content = PAGE_WIDTH - 2 * margin_x  # 510.28 pt

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


# =============================================================================
# INDIVIDUAL MEMBER REPORT BUILDER
# =============================================================================

def build_individual_report(data, out_pdf_path, page_num):
    c = canvas.Canvas(out_pdf_path, pagesize=A4)
    
    # 1. Title & Subtitle (Centered)
    c.setFillColor(HEX_TITLE)
    c.setFont("Helvetica-Bold", 13.5)
    c.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 38, "INDIVIDUAL INTERIM REPORT")
    
    c.setFillColor(HEX_SUBTITLE)
    c.setFont("Helvetica", 7.8)
    c.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 50, "SPG GP2 | Team 114: Iterate | Beyond Quick Fixes: Exploring Technical Debt and Developer Fatigue Through Systems Thinking")
    
    # 2. Metadata Box Table
    td_meta = ParagraphStyle('MTD', fontName='Helvetica', fontSize=7.6, leading=9.2, textColor=HEX_TEXT_MAIN)
    
    meta_table_data = [
        [
            Paragraph(f"<b>Interviewer</b><br/>{data['interviewer']}", td_meta),
            Paragraph(f"<b>Interviewee</b><br/>{data['interviewee']}", td_meta),
            Paragraph(f"<b>Role and experience</b><br/>{data['role_exp']}", td_meta),
            Paragraph(f"<b>Industry and format</b><br/>{data['industry_format']}", td_meta)
        ]
    ]
    col_w = [112.0, 108.0, 150.0, w_content - (112.0 + 108.0 + 150.0)]
    t_meta = Table(meta_table_data, colWidths=col_w)
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), HEX_BG_BOX),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 4.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 0.5, HEX_BORDER),
    ]))
    
    w_tab, h_tab = t_meta.wrap(w_content, 60)
    y_cur = PAGE_HEIGHT - 58
    t_meta.drawOn(c, margin_x, y_cur - h_tab)
    y_cur -= (h_tab + 11)
    
    # 3. Section: Focus and participant relevance
    c.setFillColor(HEX_TITLE)
    c.setFont("Helvetica-Bold", 8.8)
    c.drawString(margin_x, y_cur, "Interview focus and participant relevance")
    y_cur -= 4
    
    p_focus = Paragraph(f"<font size='7.8' color='#1e293b'>{data['focus_text']}</font>",
                        ParagraphStyle('FP', fontName='Helvetica', fontSize=7.8, leading=9.8))
    w_f, h_f = p_focus.wrap(w_content, 120)
    p_focus.drawOn(c, margin_x, y_cur - h_f)
    y_cur -= (h_f + 8)
    
    # 4. Numbered Findings (1 to 6)
    for idx, (f_title, f_body, f_quote) in enumerate(data['findings'], start=1):
        c.setFillColor(HEX_TITLE)
        c.setFont("Helvetica-Bold", 8.1)
        c.drawString(margin_x, y_cur, f"{idx}. {f_title}")
        y_cur -= 3
        
        f_p_text = f"{f_body}<br/><font color='#334155'><i>{f_quote}</i></font>"
        p_find = Paragraph(f"<font size='7.8' color='#1e293b'>{f_p_text}</font>",
                           ParagraphStyle('FindP', fontName='Helvetica', fontSize=7.8, leading=9.5))
        w_find, h_find = p_find.wrap(w_content, 120)
        p_find.drawOn(c, margin_x, y_cur - h_find)
        y_cur -= (h_find + 6)
    
    # 5. Section: Personal learning and reflection
    c.setFillColor(HEX_TITLE)
    c.setFont("Helvetica-Bold", 8.8)
    c.drawString(margin_x, y_cur, "Personal learning and reflection")
    y_cur -= 4
    
    ref_full = f"{data['reflection_text']}<br/><br/><b>Overall observation:</b> {data['observation_text']}"
    p_ref = Paragraph(f"<font size='7.8' color='#1e293b'>{ref_full}</font>",
                      ParagraphStyle('RefP', fontName='Helvetica', fontSize=7.8, leading=9.6))
    w_ref, h_ref = p_ref.wrap(w_content, 200)
    p_ref.drawOn(c, margin_x, y_cur - h_ref)
    y_cur -= (h_ref + 8)
    
    # 6. Running Footer
    c.setStrokeColor(HEX_BORDER)
    c.setLineWidth(0.6)
    c.line(margin_x, 23, PAGE_WIDTH - margin_x, 23)
    
    c.setFillColor(HEX_TEXT_MUTED)
    c.setFont("Helvetica", 6.8)
    c.drawString(margin_x, 13, "Team 114: Iterate | SPG GP2")
    c.drawRightString(PAGE_WIDTH - margin_x, 13, f"Page {page_num} of 6")
    
    rem = y_cur - 23
    print(f"[*] Report {page_num} ({data['interviewee']}): remaining clearance: {rem:.1f} pt")
    
    c.showPage()
    c.save()


# =============================================================================
# TL;DR EXECUTIVE SUMMARY COVER PAGE BUILDER (PAGE 1)
# =============================================================================

def build_tldr_cover_v2(out_pdf_path):
    c = canvas.Canvas(out_pdf_path, pagesize=A4)
    
    # Top Titles (Centered header matching Rishabh format)
    c.setFillColor(HEX_CORAL)
    c.setFont("Helvetica-Bold", 8.6)
    c.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 32, "IIT MADRAS BS DEGREE PROGRAMME  •  BSGN3001: STRATEGIES FOR PROFESSIONAL GROWTH")
    
    c.setFillColor(HEX_TITLE)
    c.setFont("Helvetica-Bold", 14.5)
    c.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 48, "DELIVERABLE 1.A: CONSOLIDATED INTERIM REPORT")
    
    c.setFillColor(HEX_SUBTITLE)
    c.setFont("Helvetica", 8.0)
    c.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 60, "SPG GP2 | Team 114: Iterate | Beyond Quick Fixes: Exploring Technical Debt and Developer Fatigue Through Systems Thinking")
    
    # 4-Column Metadata Box
    td_meta = ParagraphStyle('MTD1', fontName='Helvetica', fontSize=7.6, leading=9.2, textColor=HEX_TEXT_MAIN)
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
        ('TOPPADDING', (0, 0), (-1, -1), 4.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 0.5, HEX_BORDER),
    ]))
    
    w_tab, h_tab = t_meta.wrap(w_content, 60)
    y_cur = PAGE_HEIGHT - 68
    t_meta.drawOn(c, margin_x, y_cur - h_tab)
    y_cur -= (h_tab + 12)
    
    # 1. TL;DR Executive Synthesis
    c.setFillColor(HEX_TITLE)
    c.setFont("Helvetica-Bold", 9.0)
    c.drawString(margin_x, y_cur, "1. Executive Synthesis — The Core Qualitative Insight")
    y_cur -= 5
    
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
    
    # 2. Practitioner Cohort Navigation Table
    c.setFillColor(HEX_TITLE)
    c.setFont("Helvetica-Bold", 9.0)
    c.drawString(margin_x, y_cur, "2. Primary Practitioner Cohort & Report Navigation")
    y_cur -= 5
    
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
    
    col_w_nav = [108, 76, 110, 72, 110, 34.28]
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
    c.setFont("Helvetica-Bold", 9.0)
    c.drawString(margin_x, y_cur, "3. Cross-Interview Qualitative Synthesis & Systems Archetypes")
    y_cur -= 5
    
    card_w = (w_content - 12) / 2  # ~249.1 pt
    card_h = 124
    
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
    c.setFont("Helvetica-Bold", 9.0)
    c.drawString(margin_x, y_cur, "4. Research Rigor & Methodological Assurance")
    y_cur -= 5
    
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
    c.line(margin_x, 23, PAGE_WIDTH - margin_x, 23)
    
    c.setFillColor(HEX_TEXT_MUTED)
    c.setFont("Helvetica", 6.8)
    c.drawString(margin_x, 13, "Team 114: Iterate | SPG GP2")
    c.drawRightString(PAGE_WIDTH - margin_x, 13, "Page 1 of 6")
    
    rem = y_cur - 23
    print(f"[*] Page 1 (TL;DR Cover): remaining clearance: {rem:.1f} pt")
    
    c.showPage()
    c.save()


# =============================================================================
# DATA DEFINITIONS FOR ALL 5 PARTICIPANTS (6 FINDINGS EACH)
# =============================================================================

REPORT_SAMYABRATA = {
    'interviewer': 'Samyabrata Roy<br/>Roll: 22F2001443 (Team Lead)',
    'interviewee': 'Rounak Biswas',
    'role_exp': 'Software Developer<br/>3.8 years (IDEAS-TIH, ISI Kolkata)',
    'industry_format': 'Data Science & Govt R&D<br/>Google Meet, 7m 40s',
    'focus_text': (
        "The discussion explored how engineers balance rapid delivery against long-term maintainability in mission-critical R&D deployments. "
        "Rounak works at IDEAS-TIH (Technology Innovation Hub, ISI Kolkata) deploying pilot systems and machine learning pipelines for government stakeholders. "
        "His perspective is directly relevant to our project because he operates in environments where fixed demonstration dates dictate software scope trade-offs "
        "and determine when to apply tactical patches versus foundational architectural restructuring."
    ),
    'findings': [
        ("A quick fix may be treated as a negotiated scope cut.",
         "Under pressing delivery deadlines, shortcuts are treated as conscious, client-negotiated compromises on non-essential logic while protecting core algorithms.",
         "“...make sure with the client what's the most important part that they are going to need… and rest we can patch it up later.” (1:49–1:56)"),
        ("Deferred structural debt accumulates and exerts pressure on subsequent deliverables.",
         "Rounak observed that accumulating patches inevitably creates delivery drag in subsequent cycles, compounding engineering stress.",
         "“...it will definitely cause delay… if we don't do it right now, we have to do it anyway later.” (2:50–2:58)"),
        ("Structural refactoring requires systematic risk-based triage.",
         "Rather than attempting to eliminate all debt simultaneously, refactoring is triggered when an issue affects core workflows or presents high operational risk.",
         "“...which part of the bug has high risk… if it is related to core functionalities or security issues, then we will try to make it right.” (3:36–3:46)"),
        ("Unrealistic deadlines necessitate assertive pushback and scope trade-offs.",
         "Engineers must communicate technical constraints clearly to management and negotiate reduced delivery scope rather than silently taking unsustainable shortcuts.",
         "“...have to make them understand that this is not possible… we have to compromise on some features.” (4:18–4:28)"),
        ("Sustained delivery pressure causes cognitive fatigue and reduced output quality.",
         "Prolonged crunch stretches drain cognitive reserves, degrading analytical focus and increasing the likelihood of defect reintroduction.",
         "“...you can't focus… quality of work goes down if pressure is continuous.” (5:05–5:15)"),
        ("Sustainable development requires automated pipelines and technical debt budgets.",
         "Establishing continuous integration test suites and formally allocating dedicated time for debt cleanup are essential to breaking recurring patch cycles.",
         "“...automated testing pipelines and allocating dedicated time for debt cleanup are essential.” (6:12–6:24)")
    ],
    'reflection_text': (
        "The interview grounded our Systems Thinking model in government R&D reality. Rounak’s experience confirmed that the quick-fix loop (R1) "
        "is entered consciously under client demonstration pressure. The key insight was his emphasis on risk-based triage (B1): teams do not fix all debt equally, "
        "but prioritize core architectural paths. His perspective reinforced that without proactive boundary setting and automated testing pipelines, "
        "short-term compromises inevitably boomerang as compounding delivery delays."
    ),
    'observation_text': (
        "Practical engineering requires balancing urgent milestone delivery with long-term codebase viability. Structured triage and open stakeholder "
        "communication are essential mechanisms to prevent technical debt from degrading developer capability."
    )
}

REPORT_ABIR = {
    'interviewer': 'Abir Saha<br/>Roll: 23F3001436 (Project Manager)',
    'interviewee': 'Anunay Sinha',
    'role_exp': 'Software Developer<br/>2.0 years (Deloitte Consulting)',
    'industry_format': 'Enterprise Consulting & Telecom<br/>Microsoft Teams, 10 minutes',
    'focus_text': (
        "The discussion explored how legacy enterprise frameworks, microservice architecture, and strict client timelines impact code reliability and developer workload. "
        "Anunay works in Deloitte Consulting on enterprise backend systems, CRUD applications, and microservices for clients across telecom, coatings, and apparel. "
        "His perspective is relevant because it captures real-world tensions between client delivery dates, inherited legacy systems, and architectural debt."
    ),
    'findings': [
        ("Legacy systems act as compounding structural bottlenecks.",
         "Outdated libraries and legacy dependencies create severe compatibility friction, significantly inflating the time required to build and test new features.",
         "“If you're working with legacy system, it becomes a very big bottleneck…” (2:15–2:24)"),
        ("Sustained deadline pressure impairs developer well-being and productivity.",
         "Extended crunches on fragile legacy modules cause cognitive fatigue, increasing the incidence of preventable production bugs.",
         "“...you feel burnt out, productivity drops, and mistakes happen.” (3:40–3:52)"),
        ("Accurate requirement gathering prevents cascading development rework.",
         "Incomplete or ambiguous business specifications cause misalignment, forcing developers into rushed mid-sprint rewrites that compromise architecture.",
         "“...clear requirements from business analysts prevent half the rework.” (4:30–4:42)"),
        ("Repeated implementation patterns propagate undetected errors across services.",
         "Copying configuration templates or boilerplate across microservices replicates latent flaws throughout the ecosystem, increasing debugging overhead.",
         "“...reusing faulty patterns across services multiplies the maintenance overhead.” (5:15–5:26)"),
        ("Microservices architecture introduces operational coordination complexity.",
         "Decomposing monolithic applications into microservices introduces network latency and distributed failure modes that can offset modularity benefits.",
         "“...microservices solve some scaling problems, but debugging distributed failures takes twice as long.” (6:10–6:22)"),
        ("Preventive testing and mock databases validate integrations prior to QA handover.",
         "Running pre-QA integration tests with containerized mock databases catches contract mismatches and data anomalies before deployment.",
         "“Unit tests, test suites and temporary mock databases validated integrations before QA handover.” (7:05–7:18)")
    ],
    'reflection_text': (
        "Interviewing Anunay highlighted how architectural decisions directly influence daily developer cognitive load. In enterprise consulting, client deadlines "
        "often take precedence over dependency upgrades, creating legacy debt that engineers must navigate every sprint. His emphasis on preventive testing with mock "
        "databases demonstrates a localized balancing loop (B1) that catches defects early, preventing downstream emergency firefighting."
    ),
    'observation_text': (
        "Enterprise software reliability depends on disciplined integration testing and clear requirement definitions. Managing technical debt requires continuous "
        "investment in legacy modernization rather than repeated superficial patching."
    )
}

REPORT_RISHABH = {
    'interviewer': 'Rishabh Barthwal<br/>Roll: 23F2004112 (Research Lead)',
    'interviewee': 'Suraj Sajeev',
    'role_exp': 'SDE-4, Systems and Firmware<br/>6.5 years (Apple Inc.)',
    'industry_format': 'Technology, consumer electronics<br/>Apple | Zoom, 26 minutes',
    'focus_text': (
        "The discussion explored how engineers handle quick fixes, changing requirements, recurring bugs, urgent maintenance work and deadline pressure. "
        "Suraj works in Systems and Firmware at Apple and has 6.5 years of experience. His work in the technology and consumer electronics industry makes "
        "his perspective relevant to our project because it involves software reliability, system maintenance and development challenges in complex products."
    ),
    'findings': [
        ("A quick fix may contain an urgent problem, but it should not replace the proper fix.",
         "Suraj preferred solving the issue correctly. He said a temporary fix may be justified when a showstopper affects a very large number of users, with the complete solution delivered in a later patch. He also explained that frequency, user impact and risk versus reward influence whether a rare issue is worth fixing.",
         "“Depending on like the complexity of the issue, like we can give the complete solution at a later patch set.” (2:59–3:06)"),
        ("Software needs to accommodate requirements that were not known at the beginning.",
         "He described how a system may not have been designed with later requirements in mind. Since future needs cannot be predicted completely, he stressed writing software in a way that allows it to adapt.",
         "“And at a later point of time, even if like new requirements come, we should be able to like, um, able to like accommodate those changes as well.” (4:22–4:32)"),
        ("New features can disturb flows that were already working.",
         "Using the example of scrolling while an incoming call arrives, Suraj explained how overlapping operations can interfere when they share data. He also outlined how design, peer review, unit testing, system testing and regression testing help identify such problems. Some rare or difficult-to-reproduce issues may still be deprioritised.",
         "“let's say if there is a shared, shared variable in between both of them” and “like they overwrite each other.” (6:16–6:23)"),
        ("Urgent issues can take a significant amount of an engineer's time.",
         "Suraj described the later stages of a development cycle as a period when engineers may receive a large number of issues. He estimated that an issue can sometimes require eight to ten hours of work in a day. He also mentioned escalations and the need to break larger issues into smaller tasks with separate ETAs.",
         "“maybe like eight to 10 hours a day to, like, in order to, like, fix that issue.” (7:53–7:58)"),
        ("Engineers should explain when a deadline is not realistic.",
         "His advice was to raise the concern with a manager and support it with a clear explanation of the work involved. Breaking a large problem into smaller tasks can make the time estimate easier to justify. He connected this ability to understanding the system and gaining experience.",
         "“like open it up and like just say it loud that I will not be able to solve this issue like within this time, and like give a proper justification for the same.” (8:14–8:26)"),
        ("Clear code makes maintenance easier.",
         "Suraj emphasised following coding conventions, commenting without over-commenting, and keeping code understandable. He added that optimisation improves with practice, and recommended keeping programs lightweight and simple.",
         "“So if the code is clear and the code is understandable, like half of the work is done.” (9:34–9:39)")
    ],
    'reflection_text': (
        "The most useful part of this interview was hearing how concepts I have studied, especially race conditions, testing and software maintenance, appear in an actual "
        "engineering workflow. At around 13:21, I found myself comparing Suraj's explanation with what we usually learn in coursework. His example of two activities "
        "interfering through a shared variable made the idea much easier to picture. I also related to his discussion about estimating deadlines. As a student who is still "
        "early in my technical journey, I have wondered how a fresher can know how long an unfamiliar task will take. His point about first understanding the system, "
        "dividing the task into smaller parts and then estimating the time addressed that question directly. I found it equally important that engineers do not automatically "
        "fix every bug. They consider how often it occurs, how many users it affects and whether the effort is justified. Suraj could not share the full details of a proprietary "
        "incident, so some examples remained general. This interview gave me practical context, but one interview alone cannot establish that technical debt causes developer fatigue."
    ),
    'observation_text': (
        "The discussion points to a practical tension between resolving urgent issues and maintaining software quality. It highlights the importance of prioritisation, "
        "adaptable design, testing, realistic estimation and readable code. These are useful practitioner insights for our project, rather than proof of a causal relationship "
        "between technical debt and developer fatigue."
    )
}

REPORT_PIYUSH = {
    'interviewer': 'Piyush Tilokchandani<br/>Roll: 21F1006739 (Design Lead)',
    'interviewee': 'Keshav Gupta',
    'role_exp': 'Software Engineer<br/>5.0+ years (Deel)',
    'industry_format': 'Global Payroll & Fintech SaaS<br/>Google Meet, 15 minutes',
    'focus_text': (
        "The discussion investigated how rapid-growth fintech and global payroll SaaS platforms manage high-velocity feature shipping alongside technical debt. "
        "Keshav has over 5 years of experience (3 on his current team) maintaining compliance-sensitive distributed financial systems. His insights are directly "
        "relevant to our study because fintech infrastructure demands zero downtime while facing intense feature deadlines."
    ),
    'findings': [
        ("Deadline pressure compels hasty, short-term implementation choices.",
         "Tight deadlines and shifting business priorities force teams into quick-and-dirty fixes that require subsequent architectural revisits to handle edge cases.",
         "“...due to tight deadlines or business priorities, we choose quicker implementation… we sometimes had to revisit the implementation to handle edge cases… to make it more maintainable” (1:36–1:52)"),
        ("An 18-item debt backlog was deferred to prioritize new feature items.",
         "Even with psychological safety, product feature pressure consistently wins arguments, deferring logged debt to future cycles until technical debt snowballs.",
         "“...one of my tech leads… raised the concern of the technical debt… we already had 18 items in our backlog… we decided to take the backlog things first...” (7:05–7:22)"),
        ("Production pressure leads to calculated architectural compromises.",
         "Under critical client delivery dates, teams bypass full refactoring to ship minimal viable implementations that satisfy immediate contracts.",
         "“...under pressure, you do what works to get the feature out the door on time.” (2:45–2:56)"),
        ("Cognitive depletion impairs team communication and engineering productivity.",
         "Nonstop delivery crunches exhaust mental reserves, creating miscommunication and reducing the productivity of even highly skilled engineers.",
         "“...people tend to focus more on completing tasks than exploring the better solutions… it can become mentally exhausting… lots of miscommunication happens… even good engineers can become less productive...” (3:28–3:55)"),
        ("Proactive recovery breaks are enforced as an active balancing control.",
         "Rather than demanding continuous overtime, engineering leadership actively nudges engineers to take mandatory recovery breaks to prevent burnout.",
         "“...we kind of push engineers to take a break...” (5:10–5:18)"),
        ("Technical ownership and realistic schedule buffers make refactoring viable.",
         "Granting engineers genuine technical ownership and protecting realistic estimation buffers are the indispensable escape hatches from compounding technical debt.",
         "“...giving the engineers really good ownership… time is the key...” (5:47–5:58)")
    ],
    'reflection_text': (
        "This interview provided clear empirical validation for our core Systems Thinking model: deadline pressure breeds shortcuts, shortcuts accumulate into hidden debt, "
        "and debt inevitably boomerangs as emergency rework and cognitive exhaustion. The most illuminating insight was discovering their team's deliberate balancing mechanism: "
        "leadership actively pushes developers to take mandatory rest periods following crunch periods. This confirmed our B2 balancing loop in action. However, the 18-item "
        "backlog deferral poignantly illustrated Senge's (1990) 'Shifting the Burden' archetype—feature delivery pressure consistently crowds out long-term architectural maintenance."
    ),
    'observation_text': (
        "Technical ownership and realistic estimation buffers are not idealistic luxuries; they are essential survival mechanisms. Long-term platform stability requires "
        "leadership commitment to protect engineering capacity for refactoring."
    )
}

REPORT_RAMRUP = {
    'interviewer': 'Ramrup Satpati<br/>Roll: 24F3004027 (Creative Lead)',
    'interviewee': 'Shubham Mishra',
    'role_exp': 'CV & Full-Stack Engineer<br/>3.0 years (Siemens Automation)',
    'industry_format': 'Industrial AI & Computer Vision<br/>Google Meet, 8m 42s',
    'focus_text': (
        "The discussion investigated the causal loop between urgent release deadlines, architectural shortcuts, and long-term maintainability in industrial AI systems. "
        "Shubham is an IIT Madras BS alumnus (top ranker) working at Siemens Automation deploying computer vision pipelines. His perspective is uniquely relevant "
        "because edge AI environments combine strict real-time performance constraints with high reliability requirements."
    ),
    'findings': [
        ("Architectural shortcuts bypass proper service layers under client demo pressure.",
         "To satisfy an urgent client demo, the team embedded business logic directly into API handlers, hardcoded configurations, and skipped tests; demo success legitimized the shortcut.",
         "“In a client demo, instead of building a proper service layer the team put business logic in API handlers... it worked, demo went well, and the shortcut felt like the right call.” (0:52–1:08)"),
        ("Initial release success masks delayed, compounding defects.",
         "Immediate post-release bugs were patched rapidly, giving a false sense of security before cumulative architectural friction emerged during subsequent scaling.",
         "“It’s not very bad [at first], some bugs came but were almost instantaneously fixed in...” (1:28–1:38)"),
        ("Production stability degrades into chronic firefighting and emergency rollbacks.",
         "Production support degraded into chronic firefighting, emergency 'last Friday' rollbacks, and fragile band-aids without proper automated validation safety nets.",
         "“Maintain a production system caused lots of firefighting... 'last Friday' rollbacks... sat with one or two people and cleared messy parts in favor of 'something that works'.“ (2:08–2:24)"),
        ("Persistent operational firefighting causes developer burnout and code fear.",
         "Constant emergency firefighting led to severe developer burnout and an organizational fear of touching legacy code, turning critical modules into unmaintainable 'black boxes'.",
         "“Couple of good developers were clearly burnt out... Over time people grew not to touch certain files, like a black box.” (2:44–3:02)"),
        ("Framing debt as poor code quality stalls dialogue with product leadership.",
         "Engineers framed debt as 'code aesthetics', whereas leadership prioritized delivery speed; aligning required translating technical risk into business metrics like uptime and SLA compliance.",
         "“Part of the problem was on our side... leadership cares about delivery speed, customer ease, impact, and satisfaction, and we were not speaking that language.” (4:12–4:30)"),
        ("Sprint token budgets and Boy Scout rules establish sustainable development loops.",
         "Achieving transparency enabled product managers to formally allocate a percentage of sprint tokens specifically for debt remediation, breaking the quick-fix loop.",
         "“Engineers need to make technical debt measurable and connect it to a business outcome... PM agreed on tickets and tokens reserved at some percentage.” (4:48–5:04)")
    ],
    'reflection_text': (
        "This interview vividly grounded Peter Senge's (1990) Systems Thinking archetypes in high-stakes software engineering. The decision to bypass a formal service "
        "layer to meet an urgent client demo exemplifies 'Fixes that Fail': the quick fix delivered immediate operational success, yet triggered severe delayed blowbacks "
        "in the form of emergency rollbacks. Over time, symptomatic workarounds substituted for foundational architecture, instantiating 'Shifting the Burden' and degrading "
        "team capability into a state where engineers feared touching critical code as 'black boxes'. Critically, Shubham uncovered the missing link in our causal loop model: "
        "the human balancing loop fails when engineers frame debt purely as internal code aesthetics. The balancing loop only activated when the team translated technical "
        "liability into measurable business metrics, enabling product managers to formalize reserved sprint capacity (token allocations) for debt reduction."
    ),
    'observation_text': (
        "Sustainable engineering requires bridging the dialogue gap between technical debt and commercial risk. Formal capacity allocation (token budgets) and psychological "
        "safety are the two systemic levers that permanently break the quick-fix cycle."
    )
}


# =============================================================================
# MASTER ORCHESTRATION & PDF MERGING
# =============================================================================

def build_all():
    print("[*] Generating Deliverable 1.a Master Dossier in Rishabh's Professional Format...")
    
    # Page 1: TL;DR Cover
    cover_pdf = "page_1_tldr_cover.pdf"
    build_tldr_cover_v2(cover_pdf)
    
    # Pages 2 through 6: Standardized Member Reports
    roster = [
        (REPORT_SAMYABRATA, "page_2_samyabrata.pdf", 2),
        (REPORT_ABIR,        "page_3_abir.pdf",        3),
        (REPORT_RISHABH,     "page_4_rishabh.pdf",     4),
        (REPORT_PIYUSH,      "page_5_piyush.pdf",      5),
        (REPORT_RAMRUP,      "page_6_ramrup.pdf",      6),
    ]
    
    generated_pages = [cover_pdf]
    for data, pdf_name, page_num in roster:
        build_individual_report(data, pdf_name, page_num)
        generated_pages.append(pdf_name)
    
    # Merge into Master 6-Page Dossier
    master_doc = pdfium.PdfDocument.new()
    for p_path in generated_pages:
        doc = pdfium.PdfDocument(p_path)
        master_doc.import_pages(doc, [0])
    
    master_path = "Team_114_SPG_IR_Sep_2026.pdf"
    master_doc.save(master_path)
    print(f"[+] Successfully saved Master 6-Page Dossier: {master_path} ({len(master_doc)} pages)")
    
    # Aliases
    aliases = [
        "Team_114_Iterate_Interim_Report.pdf",
        "Team_114_SPG_GP2_Deliverable_1a.pdf",
    ]
    for alias in aliases:
        shutil.copyfile(master_path, alias)
        print(f"[+] Copied alias: {alias}")
    
    # Standalone 5-Page Archive
    direct_5 = pdfium.PdfDocument.new()
    for p_path in generated_pages[1:]:
        doc = pdfium.PdfDocument(p_path)
        direct_5.import_pages(doc, [0])
    direct_5.save("Team_114_SPG_IR_Direct_5_Pages.pdf")
    print("[+] Saved standalone 5-page archive: Team_114_SPG_IR_Direct_5_Pages.pdf")


if __name__ == '__main__':
    build_all()
