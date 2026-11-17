"""
Team 114 (Iterate) - GP2 Deliverable 1.a: Consolidated Interim Report
Topic: Beyond Quick Fixes: Diagnosing Technical Debt & Developer Burnout Through Systems Thinking
Generates:
  - Team_114_SPG_IR_Sep_2026.pdf (Master Consolidated Edition: Cover + 5 Reports)
  - Team_114_Iterate_Interim_Report.pdf (Master Consolidated Edition Alias)
  - Team_114_SPG_GP2_Deliverable_1a.pdf (Master Consolidated Edition Alias)
  - Team_114_SPG_IR_Direct_5_Pages.pdf (Direct 5-Page Raw Compilation)
"""

import os
import shutil
import pypdfium2 as pdfium

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfgen import canvas

# =============================================================================
# COLOR PALETTE
# =============================================================================
HEX_OCEAN_DARK = HexColor("#0f2942")
HEX_TEAL_DEEP  = HexColor("#0f766e")
HEX_CORAL_RED  = HexColor("#be123c")
HEX_BLUE_ROYAL = HexColor("#1e3a8a")
HEX_AMBER_WARM = HexColor("#b45309")
HEX_TEXT_MAIN  = HexColor("#1e293b")
HEX_TEXT_MUTED = HexColor("#64748b")
HEX_BORDER     = HexColor("#cbd5e1")
HEX_BG_LIGHT   = HexColor("#f8fafc")
HEX_CARD_BG    = HexColor("#ffffff")


def draw_top_down(flowable, x, y_top, max_w, max_h):
    w, h = flowable.wrap(max_w, max_h)
    flowable.drawOn(c, x, y_top - h)
    return h


def create_cover_page(out_pdf_path):
    # A4 Portrait page: 595.28 x 841.89 pt
    c = canvas.Canvas(out_pdf_path, pagesize=A4)
    PAGE_WIDTH, PAGE_HEIGHT = A4

    # Outer border / margins
    margin = 32
    w_content = PAGE_WIDTH - 2 * margin

    # Subtle background
    c.setFillColor(HEX_BG_LIGHT)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    # Top banner background card
    c.setFillColor(HEX_CARD_BG)
    c.setStrokeColor(HEX_BORDER)
    c.setLineWidth(1.0)
    c.roundRect(margin, margin, w_content, PAGE_HEIGHT - 2 * margin, 6, fill=1, stroke=1)

    # Top-right IITM Logo
    if os.path.exists("iitm_logo_clean.png"):
        c.drawImage("iitm_logo_clean.png", PAGE_WIDTH - margin - 65, PAGE_HEIGHT - margin - 65, width=54, height=54, mask='auto')

    # Header Text
    c.setFillColor(HEX_CORAL_RED)
    c.setFont("Helvetica-Bold", 8.8)
    c.drawString(margin + 20, PAGE_HEIGHT - margin - 26, "IIT MADRAS BS DEGREE PROGRAMME")

    c.setFillColor(HEX_TEXT_MUTED)
    c.setFont("Helvetica-Bold", 7.8)
    c.drawString(margin + 20, PAGE_HEIGHT - margin - 38, "BSGN3001: STRATEGIES FOR PROFESSIONAL GROWTH  •  GROUP PROJECT 2 (GP2)")

    c.setFillColor(HEX_OCEAN_DARK)
    c.setFont("Helvetica-Bold", 14.5)
    c.drawString(margin + 20, PAGE_HEIGHT - margin - 58, "DELIVERABLE 1.A: CONSOLIDATED INTERIM REPORT")

    c.setFillColor(HEX_TEAL_DEEP)
    c.setFont("Helvetica-Bold", 9.2)
    c.drawString(margin + 20, PAGE_HEIGHT - margin - 74, "Beyond Quick Fixes: Exploring Technical Debt & Developer Burnout Through Systems Thinking")

    c.setFillColor(HEX_TEXT_MUTED)
    c.setFont("Helvetica-Oblique", 7.6)
    c.drawString(margin + 20, PAGE_HEIGHT - margin - 88, "Consolidated Qualitative Fieldwork (N = 5 Practitioner Interviews)  |  Team 114: Iterate")

    # Dividing rule
    c.setStrokeColor(HEX_CORAL_RED)
    c.setLineWidth(1.2)
    c.line(margin + 20, PAGE_HEIGHT - margin - 96, PAGE_WIDTH - margin - 20, PAGE_HEIGHT - margin - 96)

    # Section 1: Executive Overview & Leadership Attestation
    y_cursor = PAGE_HEIGHT - margin - 108

    c.setFillColor(HEX_OCEAN_DARK)
    c.setFont("Helvetica-Bold", 8.8)
    c.drawString(margin + 20, y_cursor, "1. EXECUTIVE OVERVIEW & TEAM LEADERSHIP COMPILATION")

    ov_text = (
        "In accordance with SPG GP2 Deliverable 1.a requirements, all 5 members of <b>Team 114 (Iterate)</b> independently "
        "identified, scheduled, and conducted primary semi-structured interviews with experienced industry software practitioners (totaling "
        "20.3 years of cumulative industry experience across diverse paradigms: AI R&D, Enterprise Consulting, Embedded Systems, Global SaaS, "
        "and Industrial Automation). Each member authored a dedicated 1-page individual interim report analyzing key discussion points, "
        "extracting verbatim statements mapped to qualitative themes, and articulating personal reflections and learnings. "
        "This consolidated dossier compiles all 5 verified individual reports into a single submission document, cross-synthesizing empirical findings "
        "against Peter Senge's (1990) Systems Thinking archetypes and DORA delivery benchmarks (Forsgren et al., 2018)."
    )
    p_ov = Paragraph(f"<font size='6.8' color='#1e293b'>{ov_text}</font>",
                     ParagraphStyle('Ov', fontName='Helvetica', fontSize=6.8, leading=9.0))
    w_used, h_used = p_ov.wrap(w_content - 40, 100)
    p_ov.drawOn(c, margin + 20, y_cursor - h_used - 4)

    y_cursor -= (h_used + 16)

    # Section 2: Comprehensive Team Roster & Interviewee Mapping
    c.setFillColor(HEX_OCEAN_DARK)
    c.setFont("Helvetica-Bold", 8.8)
    c.drawString(margin + 20, y_cursor, "2. TEAM ROSTER & PRIMARY INTERVIEWEE SUMMARY")

    table_y = y_cursor - 8

    # Explicit ParagraphStyles with matched fontSize and leading (NO overlapping text!)
    th_style = ParagraphStyle('TH', fontName='Helvetica-Bold', fontSize=6.8, leading=8.6, textColor=HEX_OCEAN_DARK)
    td_style = ParagraphStyle('TD', fontName='Helvetica', fontSize=6.2, leading=8.0, textColor=HEX_TEXT_MAIN)
    td_bold  = ParagraphStyle('TDB', fontName='Helvetica-Bold', fontSize=6.5, leading=8.2, textColor=HEX_OCEAN_DARK)
    td_page  = ParagraphStyle('TDP', fontName='Helvetica-Bold', fontSize=6.5, leading=8.0, textColor=HEX_CORAL_RED, alignment=1)

    table_data = [
        [
            Paragraph("Team Member (Roll & Role)", th_style),
            Paragraph("External Participant", th_style),
            Paragraph("Role & Organization", th_style),
            Paragraph("YoE & Domain", th_style),
            Paragraph("Key Systems Contribution", th_style),
            Paragraph("Page", th_style)
        ],
        [
            Paragraph("<b>Samyabrata Roy</b><br/><font color='#64748b'>Roll: 22F2001443 (Team Lead)</font>", td_style),
            Paragraph("<b>Rounak Biswas</b>", td_bold),
            Paragraph("Software Developer<br/>IDEAS-TIH (ISI Kolkata)", td_style),
            Paragraph("3.8 YoE<br/>Data Science & Govt R&D", td_style),
            Paragraph("Scope triage; motivating pressure dynamics; risk-based debt rules (B1).", td_style),
            Paragraph("<b>Page 2</b>", td_page)
        ],
        [
            Paragraph("<b>Abir Saha</b><br/><font color='#64748b'>Roll: 23F3001436 (Project Manager)</font>", td_style),
            Paragraph("<b>Anunay Sinha</b>", td_bold),
            Paragraph("Software Developer<br/>Deloitte Consulting", td_style),
            Paragraph("2.0 YoE<br/>Enterprise Backend & Consulting", td_style),
            Paragraph("Inherited legacy frameworks; microservices overhead; pre-QA mock DBs.", td_style),
            Paragraph("<b>Page 3</b>", td_page)
        ],
        [
            Paragraph("<b>Rishabh Barthwal</b><br/><font color='#64748b'>Roll: 23F2004112 (Research Lead)</font>", td_style),
            Paragraph("<b>Suraj Sajeev</b>", td_bold),
            Paragraph("SDE-4 Systems & Firmware<br/>Apple Inc.", td_style),
            Paragraph("6.5 YoE<br/>Consumer Tech & Embedded", td_style),
            Paragraph("Urgent 8-10h/day debugging; multi-ETA pushback (B2); readable code.", td_style),
            Paragraph("<b>Page 4</b>", td_page)
        ],
        [
            Paragraph("<b>Piyush Tilokchandani</b><br/><font color='#64748b'>Roll: 21F1006739 (Design Lead)</font>", td_style),
            Paragraph("<b>Keshav Gupta</b>", td_bold),
            Paragraph("Software Engineer<br/>Deel (Payroll SaaS)", td_style),
            Paragraph("5.0+ YoE<br/>Global Fintech & SaaS", td_style),
            Paragraph("18-item debt backlog deferral; developer cognitive depletion; recovery breaks.", td_style),
            Paragraph("<b>Page 5</b>", td_page)
        ],
        [
            Paragraph("<b>Ramrup Satpati</b><br/><font color='#64748b'>Roll: 24F3004027 (Creative Lead)</font>", td_style),
            Paragraph("<b>Shubham Mishra</b>", td_bold),
            Paragraph("CV & Full-Stack Engineer<br/>Siemens Automation", td_style),
            Paragraph("3.0 YoE<br/>Industrial AI, IITM Diploma Top", td_style),
            Paragraph("API handler bypass; black-box code fear; sprint token capacity allocation.", td_style),
            Paragraph("<b>Page 6</b>", td_page)
        ],
    ]

    col_widths = [115, 75, 95, 88, 128, 30]
    t = Table(table_data, colWidths=col_widths)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HexColor("#f1f5f9")),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('GRID', (0, 0), (-1, -1), 0.5, HEX_BORDER),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [HexColor("#ffffff"), HexColor("#f8fafc")]),
    ]))

    w_tab, h_tab = t.wrap(w_content - 40, 250)
    t.drawOn(c, margin + 20, table_y - h_tab)

    y_cursor = table_y - h_tab - 14

    # Section 3: Synthesis Across 4 Systems Thinking Feedback Loops
    c.setFillColor(HEX_OCEAN_DARK)
    c.setFont("Helvetica-Bold", 8.8)
    c.drawString(margin + 20, y_cursor, "3. CROSS-INTERVIEW QUALITATIVE SYNTHESIS & SYSTEMS ARCHETYPES")

    y_cursor -= 8

    # 4 Loop Cards in a 2x2 grid
    grid_w = (w_content - 48) / 2
    grid_h = 70
    g_gap_x = 8
    g_gap_y = 6

    loop_summaries = [
        ("R1: Quick-Fix Trap Spiral (Reinforcing)",
         "Prevalence: Supported by 4 of 5 (Directly seen by 3; temporary patches by 1)",
         HEX_CORAL_RED, HexColor("#fff1f2"), HexColor("#fecdd3"),
         "Under market launches or urgent demos, teams embed business logic in API handlers or skip test suites. Immediate success legitimizes the shortcut, but delayed technical debt triggers rework and ongoing firefighting (Senge, 1990)."),

        ("R2: Developer Burnout Trap (Reinforcing)",
         "Prevalence: Supported by 4 of 5; code fear described by Participant 5",
         HEX_CORAL_RED, HexColor("#fff1f2"), HexColor("#fecdd3"),
         "Chronic firefighting and weekend rollbacks exhaust cognitive capacity. Over time, engineers fear touching fragile files, treating them like unmaintainable 'black boxes', directly depleting development velocity and morale (Forsgren et al., 2018)."),

        ("B1: Sprint Debt Token Allocation (Balancing)",
         "Prevalence: Described by Participant 5; triage rules by Part. 1 & Part. 3",
         HEX_TEAL_DEEP, HexColor("#f0fdfa"), HexColor("#99f6e4"),
         "Refactoring requests consistently stall when framed as abstract 'code hygiene'. Breaking the loop requires translating debt into commercial business metrics (uptime, SLA compliance), enabling PMs to allocate a formal sprint budget (tokens) for debt."),

        ("B2: Psychological Safety & Pushback (Balancing)",
         "Prevalence: Supported by Participant 3 (multi-ETAs), Part. 4 (recovery), Part. 1",
         HEX_TEAL_DEEP, HexColor("#f0fdfa"), HexColor("#99f6e4"),
         "Fatigue increases the necessity for scope pushback, but pushback can only function when psychological safety is established (Edmondson, 1999). Transparent justifications and multi-stage delivery milestones de-escalate unrealistic pressure.")
    ]

    for idx, (ltitle, lprev, lcol, lbg, lbord, ldesc) in enumerate(loop_summaries):
        col_idx = idx % 2
        row_idx = idx // 2
        gx = margin + 20 + col_idx * (grid_w + g_gap_x)
        gy = y_cursor - (row_idx + 1) * grid_h - row_idx * g_gap_y

        c.setFillColor(lbg)
        c.setStrokeColor(lbord)
        c.setLineWidth(0.8)
        c.roundRect(gx, gy, grid_w, grid_h, 4, fill=1, stroke=1)

        c.setFillColor(lcol)
        c.setFont("Helvetica-Bold", 7.2)
        c.drawString(gx + 8, gy + grid_h - 12, ltitle)

        c.setFillColor(HEX_OCEAN_DARK)
        c.setFont("Helvetica-Bold", 6.0)
        c.drawString(gx + 8, gy + grid_h - 22, lprev)

        p_ld = Paragraph(f"<font size='5.8' color='#1e293b'>{ldesc}</font>",
                         ParagraphStyle('LD', fontName='Helvetica', fontSize=5.8, leading=7.4))
        p_ld.wrap(grid_w - 16, grid_h - 26)
        p_ld.drawOn(c, gx + 8, gy + 6)

    y_cursor -= (2 * grid_h + g_gap_y + 12)

    # Section 4: Academic Grounding & Methodology Compliance
    c.setFillColor(HEX_OCEAN_DARK)
    c.setFont("Helvetica-Bold", 8.8)
    c.drawString(margin + 20, y_cursor, "4. METHODOLOGICAL COMPLIANCE & RESEARCH INTEGRITY")

    meth_text = (
        "• <b>Interview Standards:</b> All 5 discussions were conducted virtually with dual video cameras enabled, strictly complying with IITM BSGN3001 "
        "assessment protocols. Informed written consent was captured via email prior to recording, with recording disclosures re-confirmed on camera.<br/>"
        "• <b>Transcription & Coding:</b> High-fidelity audio streams were extracted and processed via automated speech transcription, followed by "
        "manual multi-pass verification to guarantee domain terminology precision (e.g., race conditions, microservices, token budgets).<br/>"
        "• <b>Academic References:</b> Edmondson, A. (1999). <i>Adm. Sci. Q.</i>; Forsgren, N. et al. (2018). <i>Accelerate</i>; "
        "Senge, P. M. (1990). <i>The Fifth Discipline</i>; Waters Center for Systems Thinking. (2020)."
    )
    p_meth = Paragraph(f"<font size='6.3' color='#1e293b'>{meth_text}</font>",
                       ParagraphStyle('Meth', fontName='Helvetica', fontSize=6.3, leading=8.2))
    w_m, h_m = p_meth.wrap(w_content - 40, 80)
    p_meth.drawOn(c, margin + 20, y_cursor - h_m - 4)

    # Bottom Footer Divider & Signature
    c.setStrokeColor(HEX_BORDER)
    c.setLineWidth(0.8)
    c.line(margin + 20, margin + 26, PAGE_WIDTH - margin - 20, margin + 26)

    c.setFillColor(HEX_TEXT_MUTED)
    c.setFont("Helvetica", 6.8)
    c.drawString(margin + 20, margin + 14, "Compiled by Team 114: Iterate  •  Deliverable 1.a Master Dossier  •  IIT Madras BS Degree Programme")

    c.setFillColor(HEX_CORAL_RED)
    c.setFont("Helvetica-Bold", 6.8)
    c.drawRightString(PAGE_WIDTH - margin - 20, margin + 14, "Cover Page | Master Dossier (6 Pages Total)")

    c.showPage()
    c.save()
    print(f"[*] Generated Cover Page: {out_pdf_path}")


def merge_reports(cover_pdf, member_pdfs, output_master_path, output_direct_path):
    # 1. Master Consolidated Edition (Cover + 5 reports = 6 pages)
    master_doc = pdfium.PdfDocument.new()

    # Import Cover Page
    c_doc = pdfium.PdfDocument(cover_pdf)
    master_doc.import_pages(c_doc, [0])

    # Import 5 member reports
    for mp in member_pdfs:
        doc = pdfium.PdfDocument(mp)
        master_doc.import_pages(doc, [0])

    master_doc.save(output_master_path)
    print(f"[*] Successfully saved Master Consolidated Report: {output_master_path} ({len(master_doc)} pages)")

    # 2. Direct 5-Page Raw Compilation (5 reports without cover)
    direct_doc = pdfium.PdfDocument.new()
    for mp in member_pdfs:
        doc = pdfium.PdfDocument(mp)
        direct_doc.import_pages(doc, [0])

    direct_doc.save(output_direct_path)
    print(f"[*] Successfully saved Direct 5-Page Report: {output_direct_path} ({len(direct_doc)} pages)")

    # Copy aliases
    aliases = [
        "Team_114_Iterate_Interim_Report.pdf",
        "Team_114_SPG_GP2_Deliverable_1a.pdf",
    ]
    for alias in aliases:
        shutil.copyfile(output_master_path, alias)
        print(f"[*] Copied alias: {alias}")


if __name__ == '__main__':
    cover_pdf = "interim_report_cover.pdf"
    create_cover_page(cover_pdf)

    member_reports = [
        "interim_report_1_samyabrata.pdf",
        "interim_report_2_abir.pdf",
        "interim_report_3_rishabh.pdf",
        "interim_report_4_piyush.pdf",
        "interim_report_5_ramrup.pdf",
    ]

    master_pdf = "Team_114_SPG_IR_Sep_2026.pdf"
    direct_pdf = "Team_114_SPG_IR_Direct_5_Pages.pdf"

    merge_reports(cover_pdf, member_reports, master_pdf, direct_pdf)
