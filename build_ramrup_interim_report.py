import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)

def build_pdf(filename="24f3004027_SPG_IR_Ramrup_Satpati.pdf"):
    # Target: Exactly 1 page Letter (612 x 792 pt)
    # Margins: 32 pt (0.44 in) left/right, 24 pt top/bottom
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=32,
        rightMargin=32,
        topMargin=24,
        bottomMargin=24
    )

    styles = getSampleStyleSheet()

    # Colors
    c_primary = colors.HexColor("#0f3460")     # Deep professional navy
    c_header_bg = colors.HexColor("#1e3a8a")   # Table header navy
    c_text = colors.HexColor("#1e293b")        # Dark slate
    c_muted = colors.HexColor("#475569")       # Slate muted
    c_line = colors.HexColor("#cbd5e1")        # Light border
    c_alt_bg = colors.HexColor("#f8fafc")      # Subtle alternate row
    c_badge = colors.HexColor("#0369a1")       # Timestamp blue

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12.0,
        leading=14.0,
        textColor=c_primary,
        spaceAfter=1
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8.2,
        leading=10.0,
        textColor=c_muted,
        spaceAfter=2
    )

    meta_style = ParagraphStyle(
        'DocMeta',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.8,
        leading=9.5,
        textColor=c_text,
        spaceAfter=2
    )

    sec_heading_style = ParagraphStyle(
        'SecHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.4,
        leading=10.2,
        textColor=c_primary,
        spaceBefore=2.5,
        spaceAfter=1.5
    )

    body_style = ParagraphStyle(
        'BodyP',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=6.5,
        leading=8.2,
        textColor=c_text,
        alignment=4 # Justified
    )

    tbl_hdr_style = ParagraphStyle(
        'TblHdr',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=6.5,
        leading=8.0,
        textColor=colors.white
    )

    tbl_finding_style = ParagraphStyle(
        'TblFinding',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=6.0,
        leading=7.4,
        textColor=c_text
    )

    tbl_time_style = ParagraphStyle(
        'TblTime',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=6.0,
        leading=7.4,
        textColor=c_badge,
        alignment=1 # Centered
    )

    tbl_text_style = ParagraphStyle(
        'TblText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=5.8,
        leading=7.2,
        textColor=c_text
    )

    tbl_quote_style = ParagraphStyle(
        'TblQuote',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=5.7,
        leading=7.0,
        textColor=colors.HexColor("#0f172a")
    )

    story = []

    # Title & Metadata
    story.append(Paragraph("Interim Report – Qualitative Findings", title_style))
    story.append(Paragraph("Beyond Quick Fixes: Diagnosing Technical Debt & Developer Burnout Through Systems Thinking", subtitle_style))
    story.append(Paragraph("<b>Course:</b> Strategies for Professional Growth (BSGN3001) &nbsp;&nbsp;|&nbsp;&nbsp; <b>Team:</b> 114 – ITERATE &nbsp;&nbsp;|&nbsp;&nbsp; <b>Interviewer:</b> Ramrup Satpati", meta_style))
    story.append(HRFlowable(width="100%", thickness=0.8, color=colors.HexColor("#94a3b8"), spaceAfter=2.5, spaceBefore=0.5))

    # 1. External Participant
    story.append(Paragraph("1. External Participant", sec_heading_style))
    part_desc = (
        "<b>Shubham Mishra</b> is a Computer Vision and Full-Stack Software Engineer at Siemens with about 3 years of industry "
        "experience. Concurrently pursuing the Diploma level in the IIT Madras BS Degree Programme, he is a recognized Project Topper "
        "across multiple Diploma projects and leads the educational community <b>LazyIITians</b>, providing mentoring and coaching "
        "for Diploma-level subjects. His professional domain spans deep learning vision pipelines, full-stack API architectures, and "
        "real-time inference optimization under strict latency SLAs, offering unique dual insights into industrial deadline pressures, "
        "academic project excellence, black-box legacy debt, developer burnout, and engineering–leadership alignment."
    )
    story.append(Paragraph(part_desc, body_style))
    story.append(Spacer(1, 1.5))

    # 2. Key Interview Questions and Discussion Points
    story.append(Paragraph("2. Key Interview Questions and Discussion Points", sec_heading_style))
    
    q_data = [
        [Paragraph("Finding", tbl_hdr_style), Paragraph("Timestamp", tbl_hdr_style), Paragraph("Key interview question / discussion prompt", tbl_hdr_style)],
        [Paragraph("1. Architectural Shortcuts & Logic Bypass", tbl_finding_style),
         Paragraph("00:35", tbl_time_style),
         Paragraph("Can you walk me through a project where tight deadlines forced shortcuts? What was cut and what was the immediate payoff?", tbl_text_style)],
        [Paragraph("2. Initial Payoff vs. Delayed Defects", tbl_finding_style),
         Paragraph("01:15", tbl_time_style),
         Paragraph("What happened in the weeks following that release when subsequent feature requests and edge-case bug fixes arrived?", tbl_text_style)],
        [Paragraph("3. Production Firefighting & Stability", tbl_finding_style),
         Paragraph("01:50", tbl_time_style),
         Paragraph("What was the day-to-day reality of maintaining that system in production? How did rollbacks and missing tests affect routine operations?", tbl_text_style)],
        [Paragraph("4. Developer Fatigue & Black-Box Code", tbl_finding_style),
         Paragraph("02:30", tbl_time_style),
         Paragraph("How did persistent operational firefighting impact developer well-being, morale, and willingness to modify legacy modules?", tbl_text_style)],
        [Paragraph("5. The Refactoring Deferral Dilemma", tbl_finding_style),
         Paragraph("03:10", tbl_time_style),
         Paragraph("Did the team attempt to push back or request cleanup sprints in standups/retros? How did product management respond?", tbl_text_style)],
        [Paragraph("6. Engineering–Leadership Dialogue Gap", tbl_finding_style),
         Paragraph("03:55", tbl_time_style),
         Paragraph("Why do technical debt concerns often stall with leadership? How can engineers reframe code quality into business priorities?", tbl_text_style)],
        [Paragraph("7. Balanced Governance & Token Allocation", tbl_finding_style),
         Paragraph("04:35", tbl_time_style),
         Paragraph("How did your team ultimately align with product managers to reserve sprint capacity specifically for debt remediation?", tbl_text_style)],
        [Paragraph("8. High-Leverage Sustainable Practices", tbl_finding_style),
         Paragraph("05:10", tbl_time_style),
         Paragraph("What specific technical safety nets (e.g., CI/CD, Boy Scout rule) and cultural norms best break the cycle of recurring debt?", tbl_text_style)],
    ]

    # Available printable width: 612 - 64 = 548 pt
    t_q = Table(q_data, colWidths=[150, 48, 350])
    t_q.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), c_header_bg),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 1.2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1.2),
        ('LEFTPADDING', (0, 0), (-1, -1), 3.5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 3.5),
        ('GRID', (0, 0), (-1, -1), 0.5, c_line),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, c_alt_bg]),
    ]))
    story.append(t_q)
    story.append(Spacer(1, 1.5))

    # 3. Key Findings and Interpretations
    story.append(Paragraph("3. Key Findings and Interpretations", sec_heading_style))
    f_data = [
        [Paragraph("Finding", tbl_hdr_style), Paragraph("Timestamp", tbl_hdr_style), Paragraph("Summary / interpretation", tbl_hdr_style), Paragraph("Verbatim statement", tbl_hdr_style)],
        [
            Paragraph("1. Architectural shortcuts & logic bypass", tbl_finding_style),
            Paragraph("00:52", tbl_time_style),
            Paragraph("To satisfy an urgent client demo, the team embedded business logic directly into API handlers, hardcoded configs, and skipped tests; immediate success legitimized the shortcut.", tbl_text_style),
            Paragraph('“In a client demo, instead of building a proper service layer the team put business logic in API handlers... it worked, demo went well, and the shortcut felt like the right call.”', tbl_quote_style)
        ],
        [
            Paragraph("2. Initial payoff vs. delayed defects", tbl_finding_style),
            Paragraph("01:28", tbl_time_style),
            Paragraph("Immediate post-release bugs were patched rapidly, giving a false sense of security before cumulative architectural friction emerged during subsequent scaling.", tbl_text_style),
            Paragraph('“It’s not very bad [at first], some bugs came but were almost instantaneously fixed in...”', tbl_quote_style)
        ],
        [
            Paragraph("3. Production firefighting & stability", tbl_finding_style),
            Paragraph("02:08", tbl_time_style),
            Paragraph("Production support degraded into chronic firefighting, emergency 'last Friday' rollbacks, and fragile band-aids without proper automated validation safety nets.", tbl_text_style),
            Paragraph('“Maintain a production system caused lots of firefighting... \'last Friday\' rollbacks... sat with one or two people and cleared messy parts in favor of \'something that works\'.“', tbl_quote_style)
        ],
        [
            Paragraph("4. Developer fatigue & black-box code", tbl_finding_style),
            Paragraph("02:44", tbl_time_style),
            Paragraph("Constant emergency firefighting led to severe developer burnout and an organizational fear of touching legacy code, turning critical modules into black boxes.", tbl_text_style),
            Paragraph('“Couple of good developers were clearly burnt out... Over time people grew not to touch certain files, like a black box.”', tbl_quote_style)
        ],
        [
            Paragraph("5. Refactoring deferral dilemma", tbl_finding_style),
            Paragraph("03:25", tbl_time_style),
            Paragraph("Engineers repeatedly raised architectural degradation in standups and retros, but customer feature pressure consistently kicked remediation into a 'next sprint' that never arrived.", tbl_text_style),
            Paragraph('“The pressure to keep shipping does take over... cleanup kept happening to the next sprint, and the next sprint just never came.”', tbl_quote_style)
        ],
        [
            Paragraph("6. Engineering–leadership dialogue gap", tbl_finding_style),
            Paragraph("04:12", tbl_time_style),
            Paragraph("Engineers framed debt as 'poor code quality', whereas leadership prioritized delivery speed and client impact; aligning required translating technical risk into business metrics.", tbl_text_style),
            Paragraph('“Part of the problem was on our side... leadership cares about delivery speed, customer ease, impact, and satisfaction, and we were not speaking that language.”', tbl_quote_style)
        ],
        [
            Paragraph("7. Balanced governance & capacity", tbl_finding_style),
            Paragraph("04:48", tbl_time_style),
            Paragraph("Achieving transparency enabled product managers to formally allocate a percentage of sprint tokens/tickets specifically for technical debt remediation and downtime prevention.", tbl_text_style),
            Paragraph('“Engineers need to make technical debt measurable and connect it to a business outcome... PM agreed on tickets and tokens reserved at some percentage.”', tbl_quote_style)
        ],
        [
            Paragraph("8. High-leverage sustainable practices", tbl_finding_style),
            Paragraph("05:25", tbl_time_style),
            Paragraph("Combining continuous hygiene (Boy Scout rule, CI/CD safety nets, peer reviews) with cultural psychological safety creates resilient and sustainable engineering workflows.", tbl_text_style),
            Paragraph('“Follow the Boy Scout rule... CI/CD pipelines used as a safety net... keep code sustainable, share knowledge with peers, and provide psychological safety.”', tbl_quote_style)
        ],
    ]

    t_f = Table(f_data, colWidths=[105, 42, 226, 175])
    t_f.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), c_header_bg),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 1.2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1.2),
        ('LEFTPADDING', (0, 0), (-1, -1), 3.5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 3.5),
        ('GRID', (0, 0), (-1, -1), 0.5, c_line),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, c_alt_bg]),
    ]))
    story.append(t_f)
    story.append(Spacer(1, 1.5))

    # 4. Personal Reflection, Observations and Learning
    story.append(Paragraph("4. Personal Reflection, Observations and Learning", sec_heading_style))
    ref_p1 = (
        "This interview vividly grounded Peter Senge's (1990) Systems Thinking archetypes in high-stakes software engineering. "
        "The decision to bypass a formal service layer and hardcode configs to meet an urgent client demo exemplifies the <i>'Fixes that Fail'</i> "
        "archetype: the quick fix delivered immediate operational success, yet triggered severe delayed blowbacks in the form of 'last Friday' "
        "emergency rollbacks and unvalidated production patches. Over time, symptomatic workarounds substituted for foundational architecture, "
        "instantiating <i>'Shifting the Burden'</i> and degrading team capability into a state where engineers feared touching critical code, "
        "treating key modules as unmaintainable 'black boxes'."
    )
    ref_p2 = (
        "Critically, the participant uncovered the missing link in our conceptual causal loop diagram: the breakdown of the human balancing loop. "
        "While our model assumed that developer fatigue would naturally prompt organizational pushback, the interview revealed that "
        "refactoring requests stall when engineers describe debt purely as 'poor code quality'—an internal technical concern. Leadership "
        "operates on delivery velocity, customer satisfaction, and business impact. The balancing loop only activated when the team translated "
        "technical liability into measurable business outcomes, enabling product managers to formalize reserved capacity (sprint token allocations) "
        "for debt reduction."
    )
    ref_p3 = (
        "Finally, this interaction reinforced SPG Week 11's core principle of <i>Engineering Sense</i>. Sustainable velocity is not achieved by "
        "dogmatically rejecting shortcuts, but by establishing robust safety nets—continuous integration (CI/CD), rigorous code reviews, "
        "the Boy Scout rule ('leave code cleaner than you found it'), and psychological safety where developers can openly discuss trade-offs. "
        "True engineering excellence requires mastering both socio-technical dimensions: building disciplined automated technical barriers "
        "while actively communicating across organizational hierarchies in business-aligned terms."
    )
    story.append(Paragraph(ref_p1, body_style))
    story.append(Spacer(1, 1.2))
    story.append(Paragraph(ref_p2, body_style))
    story.append(Spacer(1, 1.2))
    story.append(Paragraph(ref_p3, body_style))

    doc.build(story)
    print(f"[*] Successfully built {filename}")

if __name__ == "__main__":
    build_pdf()
