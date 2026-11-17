import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfgen import canvas
import pypdfium2 as pdfium

HEX_NAVY_HDR   = HexColor("#1e3a8a")   # Royal navy header
HEX_OCEAN_DARK = HexColor("#0f2942")   # Dark navy title
HEX_CORAL_RED  = HexColor("#be123c")   # Crimson accent
HEX_TEAL_DEEP  = HexColor("#0f766e")   # Deep teal
HEX_TEXT_MAIN  = HexColor("#1e293b")   # Charcoal body
HEX_TEXT_MUTED = HexColor("#64748b")   # Muted slate
HEX_BORDER     = HexColor("#cbd5e1")   # Border grey
HEX_BG_LIGHT   = HexColor("#f8fafc")   # Light background
HEX_ROW_ALT    = HexColor("#f8fafc")   # Alternate row background

def build_tldr_cover(pdf_path="tldr_cover_page.pdf"):
    c = canvas.Canvas(pdf_path, pagesize=letter)
    PAGE_WIDTH, PAGE_HEIGHT = letter

    margin_x = 36
    margin_top = 28
    margin_bottom = 24
    w_content = PAGE_WIDTH - 2 * margin_x  # 540 pt

    # Header Titles (matching Pages 2-6 clean style)
    if os.path.exists("iitm_logo_clean.png"):
        c.drawImage("iitm_logo_clean.png", PAGE_WIDTH - margin_x - 48, PAGE_HEIGHT - margin_top - 46, width=46, height=46, mask='auto')

    c.setFillColor(HEX_CORAL_RED)
    c.setFont("Helvetica-Bold", 8.6)
    c.drawString(margin_x, PAGE_HEIGHT - margin_top - 10, "IIT MADRAS BS DEGREE PROGRAMME")

    c.setFillColor(HEX_TEXT_MUTED)
    c.setFont("Helvetica-Bold", 7.4)
    c.drawString(margin_x, PAGE_HEIGHT - margin_top - 22, "BSGN3001: STRATEGIES FOR PROFESSIONAL GROWTH  •  GROUP PROJECT 2 (GP2)")

    c.setFillColor(HEX_OCEAN_DARK)
    c.setFont("Helvetica-Bold", 13.5)
    c.drawString(margin_x, PAGE_HEIGHT - margin_top - 40, "DELIVERABLE 1.A: INTERIM REPORT — QUALITATIVE FINDINGS")

    c.setFillColor(HEX_NAVY_HDR)
    c.setFont("Helvetica-Bold", 9.2)
    c.drawString(margin_x, PAGE_HEIGHT - margin_top - 54, "Beyond Quick Fixes: Diagnosing Technical Debt & Developer Burnout Through Systems Thinking")

    c.setFillColor(HEX_TEXT_MUTED)
    c.setFont("Helvetica-Oblique", 7.4)
    c.drawString(margin_x, PAGE_HEIGHT - margin_top - 66, "Executive Master Dossier (6 Pages Total: TL;DR Synthesis + 5 Standardized Member Fieldwork Reports)  |  Team 114: Iterate")

    # Separator line
    c.setStrokeColor(HEX_NAVY_HDR)
    c.setLineWidth(1.2)
    c.line(margin_x, PAGE_HEIGHT - margin_top - 72, PAGE_WIDTH - margin_x, PAGE_HEIGHT - margin_top - 72)

    y_cur = PAGE_HEIGHT - margin_top - 86

    # -------------------------------------------------------------------------
    # 1. TL;DR EXECUTIVE SYNTHESIS
    # -------------------------------------------------------------------------
    c.setFillColor(HEX_NAVY_HDR)
    c.setFont("Helvetica-Bold", 9.2)
    c.drawString(margin_x, y_cur, "1. TL;DR Executive Synthesis — The Core Fieldwork Insight")
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
                       ParagraphStyle('TLDRP', fontName='Helvetica', fontSize=7.4, leading=10.0))
    w_t, h_t = p_tldr.wrap(w_content - 20, 130)

    tldr_box_h = h_t + 16
    c.setFillColor(HexColor("#f0fdfa"))
    c.setStrokeColor(HexColor("#99f6e4"))
    c.setLineWidth(0.8)
    c.roundRect(margin_x, y_cur - tldr_box_h, w_content, tldr_box_h, 4, fill=1, stroke=1)

    p_tldr.drawOn(c, margin_x + 10, y_cur - tldr_box_h + 8)
    y_cur -= (tldr_box_h + 14)

    # -------------------------------------------------------------------------
    # 2. PARTICIPANT ROSTER & REPORT NAVIGATION TABLE
    # -------------------------------------------------------------------------
    c.setFillColor(HEX_NAVY_HDR)
    c.setFont("Helvetica-Bold", 9.2)
    c.drawString(margin_x, y_cur, "2. Primary Practitioner Cohort & Report Navigation")
    y_cur -= 6

    # Typography
    th_s = ParagraphStyle('TH', fontName='Helvetica-Bold', fontSize=7.0, leading=8.6, textColor=colors.white)
    td_s = ParagraphStyle('TD', fontName='Helvetica', fontSize=6.6, leading=8.4, textColor=HEX_TEXT_MAIN)
    td_b = ParagraphStyle('TDB', fontName='Helvetica-Bold', fontSize=6.8, leading=8.6, textColor=HEX_OCEAN_DARK)
    td_p = ParagraphStyle('TDP', fontName='Helvetica-Bold', fontSize=7.0, leading=8.4, textColor=HEX_CORAL_RED, alignment=1)

    table_data = [
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

    # Exactly 540 pt wide!
    col_widths = [112, 78, 114, 76, 122, 38]
    t = Table(table_data, colWidths=col_widths)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HEX_NAVY_HDR),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 4.8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4.8),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 0.5, HEX_BORDER),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, HEX_ROW_ALT]),
    ]))

    w_tab, h_tab = t.wrap(w_content, 260)
    t.drawOn(c, margin_x, y_cur - h_tab)
    y_cur -= (h_tab + 14)

    # -------------------------------------------------------------------------
    # 3. QUALITATIVE SYNTHESIS ACROSS 4 FEEDBACK LOOPS (Spacious 2-column cards)
    # -------------------------------------------------------------------------
    c.setFillColor(HEX_NAVY_HDR)
    c.setFont("Helvetica-Bold", 9.2)
    c.drawString(margin_x, y_cur, "3. Cross-Interview Qualitative Synthesis & Systems Archetypes")
    y_cur -= 6

    card_w = (w_content - 14) / 2  # 263 pt
    card_h = 126

    # Card Left: Reinforcing Traps
    c.setFillColor(HexColor("#fff1f2"))
    c.setStrokeColor(HexColor("#fecdd3"))
    c.setLineWidth(0.8)
    c.roundRect(margin_x, y_cur - card_h, card_w, card_h, 4, fill=1, stroke=1)

    c.setFillColor(HEX_CORAL_RED)
    c.setFont("Helvetica-Bold", 7.6)
    c.drawString(margin_x + 9, y_cur - 14, "REINFORCING TRAPS: COMPOUNDING FRICTION (R1 & R2)")
    c.setFillColor(HEX_TEXT_MUTED)
    c.setFont("Helvetica-Bold", 6.4)
    c.drawString(margin_x + 9, y_cur - 26, "Prevalence: Supported across all 5 practitioner interviews")

    r_text = (
        "• <b>R1: Quick-Fix Trap Spiral:</b> Under demo or launch pressure, teams bypass service layers "
        "or test suites (Participant 5: API handler bypass; Participant 4: 18-item backlog deferred). Immediate success "
        "legitimizes the shortcut, but delayed technical debt triggers rework and ongoing firefighting.<br/><br/>"
        "• <b>R2: Developer Burnout Trap:</b> Chronic firefighting (Participant 3: 8-10h/day debugging) exhausts cognitive "
        "capacity. Over time, engineers fear touching fragile files, treating them like 'black boxes' (Participant 5), "
        "directly depleting development velocity and morale."
    )
    p_r = Paragraph(f"<font size='6.4' color='#1e293b'>{r_text}</font>",
                    ParagraphStyle('RText', fontName='Helvetica', fontSize=6.4, leading=8.8))
    p_r.wrap(card_w - 18, card_h - 34)
    p_r.drawOn(c, margin_x + 9, y_cur - card_h + 8)

    # Card Right: Balancing Levers
    gx = margin_x + card_w + 14
    c.setFillColor(HexColor("#f0fdfa"))
    c.setStrokeColor(HexColor("#99f6e4"))
    c.setLineWidth(0.8)
    c.roundRect(gx, y_cur - card_h, card_w, card_h, 4, fill=1, stroke=1)

    c.setFillColor(HEX_TEAL_DEEP)
    c.setFont("Helvetica-Bold", 7.6)
    c.drawString(gx + 9, y_cur - 14, "BALANCING LEVERS: STRUCTURAL SOLUTIONS (B1 & B2)")
    c.setFillColor(HEX_TEXT_MUTED)
    c.setFont("Helvetica-Bold", 6.4)
    c.drawString(gx + 9, y_cur - 26, "Prevalence: Implemented via token budgets & safety culture")

    b_text = (
        "• <b>B1: Sprint Debt Token Allocation:</b> Refactoring requests stall when framed as abstract 'code hygiene'. "
        "Breaking the trap requires translating debt into commercial business metrics (downtime cost, SLA compliance), "
        "enabling PMs to allocate a formal sprint budget (tokens) for debt reduction (Participant 5).<br/><br/>"
        "• <b>B2: Psychological Safety & Pushback:</b> Developer fatigue increases the necessity for scope pushback, "
        "which only functions when psychological safety is established (Participant 3: multi-stage ETAs; Participant 4: "
        "recovery breaks; Participant 1: scope cuts). Clear safety de-escalates unrealistic pressure."
    )
    p_b = Paragraph(f"<font size='6.4' color='#1e293b'>{b_text}</font>",
                    ParagraphStyle('BText', fontName='Helvetica', fontSize=6.4, leading=8.8))
    p_b.wrap(card_w - 18, card_h - 34)
    p_b.drawOn(c, gx + 9, y_cur - card_h + 8)

    y_cur -= (card_h + 14)

    # -------------------------------------------------------------------------
    # 4. METHODOLOGY & RESEARCH RIGOR
    # -------------------------------------------------------------------------
    c.setFillColor(HEX_NAVY_HDR)
    c.setFont("Helvetica-Bold", 9.2)
    c.drawString(margin_x, y_cur, "4. Research Rigor & Methodological Assurance")
    y_cur -= 6

    meth_h = 56
    c.setFillColor(HexColor("#f8fafc"))
    c.setStrokeColor(HEX_BORDER)
    c.setLineWidth(0.6)
    c.roundRect(margin_x, y_cur - meth_h, w_content, meth_h, 4, fill=1, stroke=1)

    m_text = (
        "• <b>Fieldwork Protocols:</b> 5 primary 1-on-1 virtual sessions (30–45 min duration) with dual webcams active per IITM evaluation rubrics; informed written consent gathered via email and confirmed on-camera.<br/>"
        "• <b>Transcription & Audit:</b> Audio extracted and transcribed via speech tools with multi-pass technical terminology verification (race conditions, token capacity, API handlers, microservices).<br/>"
        "• <b>Academic Frameworks:</b> Peter Senge's (1990) Systems Thinking archetypes; Amy Edmondson's (1999) Psychological Safety framework; DORA empirical delivery research (Forsgren, Humble, & Kim, 2018)."
    )
    p_m = Paragraph(f"<font size='6.5' color='#334155'>{m_text}</font>",
                    ParagraphStyle('MethP', fontName='Helvetica', fontSize=6.5, leading=8.8))
    p_m.wrap(w_content - 18, meth_h - 10)
    p_m.drawOn(c, margin_x + 9, y_cur - meth_h + 6)

    y_cur -= (meth_h + 14)

    # Footer
    c.setStrokeColor(HEX_BORDER)
    c.setLineWidth(0.6)
    c.line(margin_x, margin_bottom + 14, PAGE_WIDTH - margin_x, margin_bottom + 14)

    c.setFillColor(HEX_TEXT_MUTED)
    c.setFont("Helvetica", 6.8)
    c.drawString(margin_x, margin_bottom + 4, "Team 114: Iterate  •  Deliverable 1.a: Interim Report  •  IIT Madras BS Programme")

    c.setFillColor(HEX_NAVY_HDR)
    c.setFont("Helvetica-Bold", 6.8)
    c.drawRightString(PAGE_WIDTH - margin_x, margin_bottom + 4, "Page 1 of 6  |  TL;DR Executive Summary Dossier")

    rem = y_cur - (margin_bottom + 14)
    print(f"Remaining bottom clearance: {rem:.1f} pt")

    c.showPage()
    c.save()
    print("Saved tldr_cover_page.pdf")

if __name__ == '__main__':
    build_tldr_cover('tldr_cover_page.pdf')
