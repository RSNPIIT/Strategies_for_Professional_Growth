"""
Team 114 (Iterate) - GP2 Deliverable 1.a: Unified Format Interim Reports Generator
Compiles all 5 individual member reports into the exact same standardized 4-section layout:
  1. External Participant
  2. Key Interview Questions and Discussion Points (Navy Table)
  3. Key Findings and Interpretations (Navy Table with Verbatim Quotes & Timestamps)
  4. Personal Reflection, Observations and Learning

Outputs:
  - Team_114_SPG_IR_Sep_2026.pdf (Master 5-Page Standardized Dossier)
  - Team_114_Iterate_Interim_Report.pdf (Alias)
  - Team_114_SPG_GP2_Deliverable_1a.pdf (Alias)
"""

import os
import shutil
import pypdfium2 as pdfium

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfgen import canvas

# =============================================================================
# COLOR PALETTE (Exact Match to Abir & Ramrup's Clean Theme)
# =============================================================================
HEX_NAVY_HDR   = HexColor("#1e3a8a")   # Royal navy header
HEX_OCEAN_DARK = HexColor("#0f2942")   # Dark navy title
HEX_CORAL_RED  = HexColor("#be123c")   # Crimson accent
HEX_TEXT_MAIN  = HexColor("#1e293b")   # Charcoal body
HEX_TEXT_MUTED = HexColor("#475569")   # Muted slate
HEX_BORDER     = HexColor("#cbd5e1")   # Border grey
HEX_TABLE_BG   = HexColor("#1e3a8a")   # Table header background
HEX_ROW_ALT    = HexColor("#f8fafc")   # Alternate row background


def draw_top_down(flowable, c, x, y_top, max_w, max_h):
    w, h = flowable.wrap(max_w, max_h)
    flowable.drawOn(c, x, y_top - h)
    return h


def build_single_member_report(data, out_pdf_path, page_num=2):
    # Standard Letter Portrait: 612 x 792 pt
    c = canvas.Canvas(out_pdf_path, pagesize=letter)
    PAGE_WIDTH, PAGE_HEIGHT = letter

    margin_x = 36
    margin_top = 26
    margin_bottom = 24
    w_content = PAGE_WIDTH - 2 * margin_x

    n_q = len(data['questions'])
    # Calibrate spacing based on whether there are 6 or 8 rows
    is_dense = (n_q >= 8)
    
    font_body_sz   = 7.0 if is_dense else 7.8
    leading_body   = 9.2 if is_dense else 10.6
    
    font_tbl_sz    = 6.4 if is_dense else 7.2
    leading_tbl    = 8.2 if is_dense else 9.4
    pad_tbl        = 2.6 if is_dense else 4.5

    font_ref_sz    = 6.8 if is_dense else 7.6
    leading_ref    = 8.8 if is_dense else 10.4
    gap_sec        = 10  if is_dense else 15

    # -------------------------------------------------------------------------
    # TOP HEADER
    # -------------------------------------------------------------------------
    c.setFillColor(HEX_NAVY_HDR)
    c.setFont("Helvetica-Bold", 13.5)
    c.drawString(margin_x, PAGE_HEIGHT - margin_top - 12, "Interim Report – Qualitative Findings")

    c.setFillColor(HEX_TEXT_MAIN)
    c.setFont("Helvetica-Oblique", 8.2)
    c.drawString(margin_x, PAGE_HEIGHT - margin_top - 24, "Beyond Quick Fixes: Diagnosing Technical Debt & Developer Burnout Through Systems Thinking")

    c.setFillColor(HEX_OCEAN_DARK)
    c.setFont("Helvetica-Bold", 7.6)
    c.drawString(margin_x, PAGE_HEIGHT - margin_top - 36,
                 f"Course: Strategies for Professional Growth (BSGN3001)   |   Team: 114 – ITERATE   |   Interviewer: {data['interviewer']}")

    c.setStrokeColor(HEX_BORDER)
    c.setLineWidth(0.8)
    c.line(margin_x, PAGE_HEIGHT - margin_top - 42, PAGE_WIDTH - margin_x, PAGE_HEIGHT - margin_top - 42)

    y_cur = PAGE_HEIGHT - margin_top - 54

    # -------------------------------------------------------------------------
    # SECTION 1: EXTERNAL PARTICIPANT
    # -------------------------------------------------------------------------
    c.setFillColor(HEX_NAVY_HDR)
    c.setFont("Helvetica-Bold", 9.0)
    c.drawString(margin_x, y_cur, "1. External Participant")
    y_cur -= 4

    p_part = Paragraph(f"<font size='{font_body_sz}' color='#1e293b'>{data['participant_text']}</font>",
                       ParagraphStyle('PartP', fontName='Helvetica', fontSize=font_body_sz, leading=leading_body))
    h_part = draw_top_down(p_part, c, margin_x, y_cur, w_content, 90)
    y_cur -= (h_part + gap_sec)

    # -------------------------------------------------------------------------
    # SECTION 2: KEY INTERVIEW QUESTIONS AND DISCUSSION POINTS
    # -------------------------------------------------------------------------
    c.setFillColor(HEX_NAVY_HDR)
    c.setFont("Helvetica-Bold", 9.0)
    c.drawString(margin_x, y_cur, "2. Key Interview Questions and Discussion Points")
    y_cur -= 4

    th_s = ParagraphStyle('TH_S', fontName='Helvetica-Bold', fontSize=font_tbl_sz + 0.4, leading=leading_tbl + 0.4, textColor=colors.white)
    td_f = ParagraphStyle('TD_F', fontName='Helvetica-Bold', fontSize=font_tbl_sz, leading=leading_tbl, textColor=HEX_OCEAN_DARK)
    td_q = ParagraphStyle('TD_Q', fontName='Helvetica', fontSize=font_tbl_sz, leading=leading_tbl, textColor=HEX_TEXT_MAIN)

    q_table_data = [
        [Paragraph("<b>Finding / Topic</b>", th_s), Paragraph("<b>Key interview question / discussion prompt</b>", th_s)]
    ]
    for f_title, f_q in data['questions']:
        q_table_data.append([Paragraph(f_title, td_f), Paragraph(f_q, td_q)])

    t_q = Table(q_table_data, colWidths=[150, w_content - 150])
    t_q.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HEX_NAVY_HDR),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), pad_tbl),
        ('BOTTOMPADDING', (0, 0), (-1, -1), pad_tbl),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('GRID', (0, 0), (-1, -1), 0.5, HEX_BORDER),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, HEX_ROW_ALT]),
    ]))

    w_tq, h_tq = t_q.wrap(w_content, 260)
    t_q.drawOn(c, margin_x, y_cur - h_tq)
    y_cur -= (h_tq + gap_sec)

    # -------------------------------------------------------------------------
    # SECTION 3: KEY FINDINGS AND INTERPRETATIONS
    # -------------------------------------------------------------------------
    c.setFillColor(HEX_NAVY_HDR)
    c.setFont("Helvetica-Bold", 9.0)
    c.drawString(margin_x, y_cur, "3. Key Findings and Interpretations")
    y_cur -= 4

    td_kf_title = ParagraphStyle('TDKF_T', fontName='Helvetica-Bold', fontSize=font_tbl_sz - 0.2, leading=leading_tbl - 0.2, textColor=HEX_OCEAN_DARK)
    td_kf_sum   = ParagraphStyle('TDKF_S', fontName='Helvetica', fontSize=font_tbl_sz - 0.3, leading=leading_tbl - 0.3, textColor=HEX_TEXT_MAIN)
    td_kf_verb  = ParagraphStyle('TDKF_V', fontName='Helvetica-Oblique', fontSize=font_tbl_sz - 0.4, leading=leading_tbl - 0.4, textColor=HexColor("#334155"))

    f_table_data = [
        [Paragraph("<b>Finding</b>", th_s), Paragraph("<b>Summary / interpretation</b>", th_s), Paragraph("<b>Verbatim statement</b>", th_s)]
    ]
    for f_title, f_sum, f_verb in data['findings']:
        f_table_data.append([
            Paragraph(f_title, td_kf_title),
            Paragraph(f_sum, td_kf_sum),
            Paragraph(f_verb, td_kf_verb)
        ])

    col_w3 = [118, 226, w_content - 344]
    t_f = Table(f_table_data, colWidths=col_w3)
    t_f.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HEX_NAVY_HDR),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), pad_tbl),
        ('BOTTOMPADDING', (0, 0), (-1, -1), pad_tbl),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('GRID', (0, 0), (-1, -1), 0.5, HEX_BORDER),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, HEX_ROW_ALT]),
    ]))

    w_tf, h_tf = t_f.wrap(w_content, 320)
    t_f.drawOn(c, margin_x, y_cur - h_tf)
    y_cur -= (h_tf + gap_sec)

    # -------------------------------------------------------------------------
    # SECTION 4: PERSONAL REFLECTION, OBSERVATIONS AND LEARNING
    # -------------------------------------------------------------------------
    c.setFillColor(HEX_NAVY_HDR)
    c.setFont("Helvetica-Bold", 9.0)
    c.drawString(margin_x, y_cur, "4. Personal Reflection, Observations and Learning")
    y_cur -= 4

    p_ref = Paragraph(f"<font size='{font_ref_sz}' color='#1e293b'>{data['reflection_text']}</font>",
                      ParagraphStyle('RefP', fontName='Helvetica', fontSize=font_ref_sz, leading=leading_ref))
    w_ref, h_ref = p_ref.wrap(w_content, 180)
    p_ref.drawOn(c, margin_x, y_cur - h_ref)

    # -------------------------------------------------------------------------
    # RUNNING FOOTER (Consistent across all 6 pages)
    # -------------------------------------------------------------------------
    c.setStrokeColor(HEX_BORDER)
    c.setLineWidth(0.6)
    c.line(margin_x, margin_bottom + 14, PAGE_WIDTH - margin_x, margin_bottom + 14)

    c.setFillColor(HexColor("#64748b"))
    c.setFont("Helvetica", 6.8)
    c.drawString(margin_x, margin_bottom + 4, "Team 114: Iterate  •  Deliverable 1.a: Interim Report  •  IIT Madras BS Programme")

    c.setFillColor(HEX_NAVY_HDR)
    c.setFont("Helvetica-Bold", 6.8)
    c.drawRightString(PAGE_WIDTH - margin_x, margin_bottom + 4, f"Page {page_num} of 6  |  Individual Qualitative Findings")

    rem_margin = y_cur - h_ref - (margin_bottom + 14)

    c.showPage()
    c.save()
    print(f"[*] Generated calibrated unified report: {out_pdf_path} (Page {page_num} of 6, remaining bottom clearance: {rem_margin:.1f} pt)")


# =============================================================================
# DATA DEFINITIONS FOR ALL 5 TEAM MEMBERS
# =============================================================================

REPORT_SAMYABRATA = {
    'interviewer': 'Samyabrata Roy (Roll: 22F2001443, Team Lead)',
    'participant_text': (
        "<b>Rounak Biswas</b> is a Software Developer at IDEAS-TIH (Technology Innovation Hub, Indian Statistical Institute, Kolkata) "
        "with 3 years and 9 months of industry experience. His domain spans Data Science, Machine Learning pipelines, and government-funded "
        "technology innovation projects. His primary role involves deploying real-time client pilots and production demos against rigid stakeholder "
        "milestones, making decisions on when to apply temporary tactical patches versus performing foundational refactoring. "
        "Discussion details: 7m 40s recorded Google Meet, both cameras enabled per IITM rubrics, informed written consent confirmed via email."
    ),
    'questions': [
        ("1. Deadline Pressures & Scope Triage", "When a fixed date (a pilot or demo) forces you to ship something that isn't fully ready, what do you cut and what trade-offs are accepted?"),
        ("2. Patch Backlog & Compounding Pressure", "Do resulting bugs, fragile patches, and subsequent rework add cumulative pressure to your next delivery deadline?"),
        ("3. Structural Refactoring Triggers", "When you finally get development time, what specific criteria decide whether to fix something structurally versus patching it again?"),
        ("4. Handling Unrealistic Deadlines", "How do you handle unrealistic delivery deadlines when management or clients request features within impossible timeframes?"),
        ("5. Cognitive Load & Well-being", "How do sustained high-pressure delivery stretches impact your focus, cognitive energy, and life outside work?"),
        ("6. High-Leverage Sustainable Practices", "What three key practices or cultural norms would you institute to permanently break the recurring quick-fix cycle?")
    ],
    'findings': [
        ("1. Quick fixes as negotiated scope cuts",
         "Under delivery deadlines, shortcuts are treated as conscious, client-negotiated compromises on non-essential logic.",
         "“...make sure with the client what's the most important part that they are going to need… and rest we can patch it up later.” [01:49]"),
        ("2. Patch backlog adds accepted pressure",
         "Rework adds friction, but engineers normalize it as an inherent cost of agile software delivery compromises.",
         "“Of course, it adds a little bit of pressure, but I believe it comes with the work, since we have to make a compromise either this way or that way.” [02:20]"),
        ("3. Risk-based triage for refactoring",
         "Structural refactoring is triggered when a defect threatens future architecture and would cause major restructuring later.",
         "“...if it's something that I notice that it might be a problem later in the line, and it might lead to a lot of code restructuring later, I try to fix it right away.” [03:50]"),
        ("4. Early pushback on unrealistic goals",
         "Unrealistic deadlines are mitigated by communicating constraints and technical debt liabilities well in advance.",
         "“...it does add some pressure, and I try to communicate it very well with them in advance…” [04:54]"),
        ("5. Motivating pressure vs. cognitive drain",
         "Challenging the assumption of immediate burnout, pressure can act as an energizing motivator when the technical work is enjoyable.",
         "“...if I'm working on something that I actually do enjoy, then high pressure does actually end up motivating me more to work on it.” [05:42]"),
        ("6. Upfront client expectation setting",
         "Sustainable engineering starts with transparent stakeholder communication regarding the delayed consequences of rushed jobs.",
         "“...being very clear with the client for first and foremost… make them understand the consequences of doing a very quick and fast job…” [06:20]")
    ],
    'reflection_text': (
        "This interview challenged my initial assumption that deadline pressure automatically leads directly to developer fatigue. "
        "Rounak described technical shortcuts not as careless mistakes, but as conscious trade-offs, and viewed delivery pressure as energizing "
        "when working on engaging tasks. This insight was pivotal for our Systems Thinking model: developer fatigue is not a guaranteed linear output, "
        "but a conditional state influenced by work autonomy, code ownership, and stakeholder transparency. "
        "Methodologically, the interview ran shorter than planned (7m 40s), which limited deep quantitative probing into specific incident metrics. "
        "In future interviews, I learned to anchor questions immediately in a single concrete codebase incident rather than abstract generalities, "
        "and to avoid leading phrasing that invites simple agreement. Ultimately, breaking the quick-fix spiral requires aligning client expectations early."
    )
}

REPORT_ABIR = {
    'interviewer': 'Abir Saha (Roll: 23F3001436, Project Manager)',
    'participant_text': (
        "<b>Anunay Sinha</b> is a Software Developer at Deloitte Consulting with about two years of experience. He has delivered enterprise "
        "solutions across telecom, painting/coatings, and textile/apparel industries (B2B and B2C), covering backend architectures, CRUD services, "
        "vulnerability assessments, ML-based vulnerability tooling, and microservices ecosystems. His work provided practical grounding in "
        "managing inherited legacy frameworks, developer well-being under release crunches, QA coordination, and architectural trade-offs. "
        "Discussion details: Recorded Google Meet, dual cameras on per IITM guidelines, informed written consent confirmed prior to call."
    ),
    'questions': [
        ("1. Legacy Systems & Accumulated Debt", "What challenges have you faced with legacy systems, especially outdated libraries, framework dependencies, and compatibility issues?"),
        ("2. Deadline Pressure & Developer Well-being", "Can you describe an experience where strict delivery commitments required you to work beyond normal working hours?"),
        ("3. Accurate Requirement Gathering", "How do unclear client requirements affect development, and what role do business analysts play in preventing misalignments?"),
        ("4. Repeated Implementation Patterns", "Do developers reuse code or configurations from earlier services, and what problems arise when old design decisions carry forward?"),
        ("5. Architectural Decisions & Trade-offs", "Has an architecture such as microservices introduced unnecessary operational complexity, and how did your team address it?"),
        ("6. Preventive Testing Practices", "What testing do developers conduct before QA hand-off, and how do mock databases or test suites prevent regression rework?"),
        ("7. Developer–QA Coordination", "Have you encountered friction with QA over API status codes (e.g., 401 vs 409) or input validation, and how was it resolved?"),
        ("8. AI-Assisted Development & Validation", "How has AI code generation affected delivery velocity, and what critical validation responsibilities remain with developers?")
    ],
    'findings': [
        ("1. Legacy systems as structural bottlenecks",
         "Outdated libraries and legacy dependencies create severe compatibility friction and hinder modern environment integration.",
         "“If you're working with legacy system, it becomes a very big bottleneck…” [02:15]"),
        ("2. Weekend delivery crunches with management",
         "Strict client commitments forced overtime weekend sessions with managers to stabilize releases before live customer demos.",
         "“My manager is sitting with me. I'm also sitting with him and we are working on the weekend.” [05:40]"),
        ("3. Business analysts as requirement anchors",
         "Incomplete requirement gathering creates compounding development rework; business analysts are essential to bridge client needs.",
         "“…like the business analyst, their roles are to collect the proper requirements from the client.” [08:20]"),
        ("4. Reused patterns propagate debt",
         "Carrying forward legacy configurations accelerates initial setup but silently propagates architectural debt and inconsistencies.",
         "“Because we as developers carry our previous work also.” [11:10]"),
        ("5. Microservices complexity forced monolith return",
         "Excessive communication overhead and configuration bloat in microservices prompted the team to refactor back to a unified monolith.",
         "“What we did is we shifted from micro to monolithic.” [14:35]"),
        ("6. Mock environments prevent QA regressions",
         "Implementing temporary mock databases and unit suites before QA hand-off prevented repeated integration defects.",
         "“We made a mock database for a certain period of time.” [17:50]"),
        ("7. Disagreements on HTTP status codes",
         "Mismatched interpretations between developers and QA over error codes (401 vs 409) caused testing friction and rework.",
         "“We made sure that test cases passed” [21:15]"),
        ("8. Developer accountability in AI validation",
         "While AI tools accelerate boilerplate generation, developers retain full accountability for architectural fit and security validation.",
         "“Now, the validation part now depends on the developers.” [24:40]")
    ],
    'reflection_text': (
        "This interaction closely connected Systems Thinking concepts with real-world enterprise engineering. I had initially conceptualized "
        "technical debt primarily as hurried quick fixes and sloppy code. However, Anunay demonstrated that debt often emerges from external sources: "
        "inherited legacy libraries, incomplete requirement definitions, and over-engineered architectural paradigms. His team's deliberate decision to "
        "migrate from microservices back to a monolith powerfully demonstrated that modern architectural trends are not inherently superior for every scale. "
        "Furthermore, observing that strict deadlines led to weekend work highlighted the vital importance of psychological safety and realistic estimation. "
        "Sustainable software engineering requires seamless cross-functional alignment between developers, business analysts, QA, and leadership."
    )
}

REPORT_RISHABH = {
    'interviewer': 'Rishabh Barthwal (Roll: 23F2004112, Research Lead)',
    'participant_text': (
        "<b>Suraj Sajeev</b> is an SDE-4 Systems and Firmware Software Engineer at Apple Inc. with 6.5 years of industry experience. "
        "His specialization encompasses low-level systems programming, firmware stability, and consumer electronics device drivers. "
        "His perspective is uniquely valuable to our project because firmware engineering operates under strict hardware-software constraints, "
        "where quick fixes cannot be patched over-the-air effortlessly, making code readability, race condition prevention, and realistic estimation critical. "
        "Discussion details: 26-minute recorded Zoom session, dual video feeds active per IITM criteria, written consent documented over email."
    ),
    'questions': [
        ("1. Containment vs. Root-Cause Fixes", "When an urgent production defect arises, how do you balance implementing a temporary containment patch versus fixing the underlying root cause?"),
        ("2. Designing for Unforeseen Requirements", "How do you architect software systems when initial specifications cannot anticipate future requirements or hardware revisions?"),
        ("3. Concurrency, Race Conditions & Shared State", "How do new concurrent features disrupt existing stable workflows through shared variable corruption or race conditions?"),
        ("4. Production Firefighting Time Drain", "During intense pre-release milestones, how significantly do urgent bug escalations consume an engineer's daily working hours?"),
        ("5. Communicating Unrealistic Deadlines", "What effective mechanisms should engineers use to communicate and justify when an assigned delivery timeline is technically unrealistic?"),
        ("6. Code Readability as Maintenance Shield", "How does disciplined adherence to coding standards, lightweight comments, and clean architecture reduce long-term maintenance overhead?")
    ],
    'findings': [
        ("1. Temporary containment with phased patch sets",
         "A quick patch is justified only to contain critical showstoppers affecting massive user bases, provided a root-cause fix follows in a patch set.",
         "“Depending on like the complexity of the issue, like we can give the complete solution at a later patch set.” [03:14-03:21]"),
        ("2. Adaptive design for unknown future needs",
         "Because future hardware and product requirements cannot be predicted, engineers must write modular, decoupled code that adapts seamlessly.",
         "“And at a later point of time, even if like new requirements come, we should be able to... accommodate those changes as well.” [07:55-08:13]"),
        ("3. Shared variable corruption in overlapping flows",
         "Concurrency bugs, such as incoming calls during scrolling, occur when asynchronous operations collide and overwrite shared memory state.",
         "“let's say if there is a shared, shared variable in between both of them... like they overwrite each other.” [09:46-09:53]"),
        ("4. 8–10 hour daily escalations in late stages",
         "Late-stage release cycles generate heavy bug queues where resolving a single complex issue can consume 8 to 10 hours of intense firefighting.",
         "“maybe like eight to 10 hours a day to, like, in order to, like, fix that issue.” [15:23-15:48]"),
        ("5. Task decomposition for deadline pushback",
         "Engineers must proactively voice deadline pushback supported by task decomposition, establishing multi-stage ETAs for each sub-component.",
         "“like open it up and like just say it loud that, ‘I will not be able to solve this issue like within this time,’ and like give a proper justification...” [18:19-18:30]"),
        ("6. Clear, readable code represents half the battle",
         "Disciplined code readability, simplicity, and commenting conventions eliminate cognitive fog and represent half of maintenance success.",
         "“So if the code is clear and the code is understandable, like half of the work is done.” [24:03-24:17]")
    ],
    'reflection_text': (
        "The most profound learning from this interview was observing how abstract academic concepts—race conditions, regression suites, and memory "
        "contention—manifest in mission-critical commercial firmware workflows. Suraj's tangible example of UI scrolling conflicting with incoming call "
        "interrupts through a shared variable grounded the concept of systems fragility. Additionally, his approach to task estimation addressed a major "
        "personal question: how fresh engineers can estimate unfamiliar assignments. His methodology—deconstructing complex features into smaller modules "
        "and providing separate ETAs—directly reinforces our Systems Thinking balancing loop (B2: Scope Pushback Brake). "
        "However, proprietary firmware constraints prevented Suraj from sharing sensitive internal incident details, requiring some answers to remain high-level. "
        "Ultimately, this discussion emphasized that sustainable engineering relies on adaptable architecture, disciplined testing, and transparent communication."
    )
}

REPORT_PIYUSH = {
    'interviewer': 'Piyush Tilokchandani (Roll: 21F1006739, Design Lead)',
    'participant_text': (
        "<b>Keshav Gupta</b> is a Software Engineer at Deel (a global HR-tech and payroll platform) with over 5 years of industry experience "
        "(approximately 3 years on his current team). His work involves shipping high-velocity features in agile sprints with strict compliance "
        "and financial deadlines. He has experienced firsthand how cutting architectural corners to hit release dates creates compounding post-release "
        "liabilities. Discussion details: 8m 45s recorded video interview on 16 Nov 2026, dual cameras active, consent formally documented over email "
        "and re-confirmed at the start of the recording (00:15). As a professional acquaintance, high psychological safety fostered candid disclosures."
    ),
    'questions': [
        ("1. Shortcut Triggers Under Hard Deadlines", "Can you describe a moment when tight business deadlines forced your team to take a shortcut, and what changed in the following weeks?"),
        ("2. Delayed Defect & Edge-Case Penalties", "What impact did that quick fix have on subsequent sprints regarding unexpected bugs, rework, and emergency late-night troubleshooting?"),
        ("3. Sustained Pressure & Cognitive Exhaustion", "Under nonstop sprint delivery pressure, what happened to your personal cognitive energy, and how did it affect overall team productivity?"),
        ("4. Rest and Recovery as System Controls", "How does your team treat developer rest—is recovery viewed as an optional luxury or as an essential control mechanism against burnout?"),
        ("5. The Refactoring Deferral Paradox", "When technical debt was flagged in retrospectives, how did product leadership respond, and why did remediation get deferred?"),
        ("6. Autonomy, Ownership & Sustainable Timelines", "What practical mechanisms have proven most effective in your experience to help engineering teams escape the compounding quick-fix spiral?")
    ],
    'findings': [
        ("1. Deadline pressure compels hasty implementation",
         "Tight deadlines and shifting business priorities force teams into quick-and-dirty fixes that require subsequent architectural revisits.",
         "“...due to tight deadlines or business priorities, we choose quicker implementation… we sometimes had to revisit the implementation to handle edge cases… to make it more maintainable” [01:36]"),
        ("2. Immediate fixes create delayed systemic messes",
         "Solving immediate symptoms without modeling comprehensive edge scenarios breeds delayed architectural chaos and compounding friction.",
         "“...we implement something that we solve immediately without really considering all possible scenarios… sometimes this creates a whole kind of a mess...” [02:47]"),
        ("3. Chronic heat dulls cognitive performance",
         "Nonstop delivery crunches exhaust mental reserves, creating miscommunication and reducing the productivity of even highly skilled engineers.",
         "“...people tend to focus more on completing tasks than exploring the better solutions… it can become mentally exhausting… lots of miscommunication happens… even good engineers can become less productive...” [03:28-03:55]"),
        ("4. Proactive rest enforced as balancing control",
         "Rather than demanding continuous overtime, engineering leadership actively nudges engineers to take recovery breaks to avoid burnout.",
         "“...we kind of push engineers to take a break...” [05:10]"),
        ("5. 18-item backlog deferred for new features",
         "Even with psychological safety, product feature pressure consistently wins arguments, deferring logged debt to a 'next sprint' that never arrives.",
         "“...one of my tech leads… raised the concern of the technical debt… we already had 18 items in our backlog… we decided to take the backlog things first...” [07:05]"),
        ("6. Technical ownership and realistic time buffers",
         "Granting engineers genuine technical ownership and protecting realistic schedule estimation are the indispensable escape hatches from debt.",
         "“...giving the engineers really good ownership… time is the key...” [05:47]")
    ],
    'reflection_text': (
        "This interview provided clear empirical validation for our core Systems Thinking model: deadline pressure breeds shortcuts, shortcuts "
        "accumulate into hidden debt, and debt inevitably boomerangs as emergency rework and cognitive exhaustion. The most illuminating insight was "
        "discovering their team's deliberate balancing mechanism: leadership actively pushes developers to take mandatory rest periods following crunch periods. "
        "This confirmed our B2 balancing loop in action. However, the 18-item backlog deferral poignantly illustrated Senge's (1990) 'Shifting the Burden' "
        "archetype—feature delivery pressure consistently crowds out long-term architectural maintenance. "
        "A key personal takeaway: technical ownership and realistic estimation buffers are not idealistic luxuries; they are essential survival mechanisms. "
        "In future interviews, I will focus on digging into specific codebase file structures to capture quantitative technical debt metrics."
    )
}

REPORT_RAMRUP = {
    'interviewer': 'Ramrup Satpati (Roll: 24F3004027, Creative Lead)',
    'participant_text': (
        "<b>Shubham Mishra</b> is a Computer Vision and Full-Stack Software Engineer at Siemens with about 3 years of industry experience. "
        "Concurrently pursuing the Diploma level in the IIT Madras BS Degree Programme, he is a recognized Project Topper across multiple Diploma "
        "projects and leads the educational community LazyIITians, providing mentoring and coaching for Diploma-level subjects. His professional "
        "domain spans deep learning vision pipelines, full-stack API architectures, and real-time inference optimization under strict latency SLAs, "
        "offering unique dual insights into industrial deadline pressures, academic project excellence, black-box legacy debt, and engineering–leadership alignment. "
        "Discussion details: Recorded Google Meet, dual video cameras enabled, informed written consent confirmed over email and recording."
    ),
    'questions': [
        ("1. Architectural Shortcuts & Logic Bypass", "Can you walk me through a project where tight deadlines forced shortcuts? What was cut and what was the immediate payoff? [00:35]"),
        ("2. Initial Payoff vs. Delayed Defects", "What happened in the weeks following that release when subsequent feature requests and edge-case bug fixes arrived? [01:15]"),
        ("3. Production Firefighting & Stability", "What was the day-to-day reality of maintaining that system in production? How did rollbacks and missing tests affect operations? [01:50]"),
        ("4. Developer Fatigue & Black-Box Code", "How did persistent operational firefighting impact developer well-being, morale, and willingness to modify legacy modules? [02:30]"),
        ("5. The Refactoring Deferral Dilemma", "Did the team attempt to push back or request cleanup sprints in standups/retros? How did product management respond? [03:10]"),
        ("6. Engineering–Leadership Dialogue Gap", "Why do technical debt concerns often stall with leadership? How can engineers reframe code quality into business priorities? [03:55]"),
        ("7. Balanced Governance & Token Allocation", "How did your team ultimately align with product managers to reserve sprint capacity specifically for debt remediation? [04:35]"),
        ("8. High-Leverage Sustainable Practices", "What specific technical safety nets (e.g., CI/CD, Boy Scout rule) and cultural norms best break the cycle of recurring debt? [05:10]")
    ],
    'findings': [
        ("1. Architectural shortcuts & logic bypass",
         "To satisfy an urgent client demo, the team embedded business logic directly into API handlers, hardcoded configs, and skipped tests; demo success legitimized the shortcut.",
         "“In a client demo, instead of building a proper service layer the team put business logic in API handlers... it worked, demo went well, and the shortcut felt like the right call.” [00:52]"),
        ("2. Initial payoff vs. delayed defects",
         "Immediate post-release bugs were patched rapidly, giving a false sense of security before cumulative architectural friction emerged during subsequent scaling.",
         "“It’s not very bad [at first], some bugs came but were almost instantaneously fixed in...” [01:28]"),
        ("3. Production firefighting & stability",
         "Production support degraded into chronic firefighting, emergency 'last Friday' rollbacks, and fragile band-aids without proper automated validation safety nets.",
         "“Maintain a production system caused lots of firefighting... 'last Friday' rollbacks... sat with one or two people and cleared messy parts in favor of 'something that works'.“ [02:08]"),
        ("4. Developer fatigue & black-box code",
         "Constant emergency firefighting led to severe developer burnout and an organizational fear of touching legacy code, turning critical modules into black boxes.",
         "“Couple of good developers were clearly burnt out... Over time people grew not to touch certain files, like a black box.” [02:44]"),
        ("5. Refactoring deferral dilemma",
         "Engineers repeatedly raised architectural degradation in standups and retros, but customer feature pressure consistently kicked remediation into a 'next sprint' that never arrived.",
         "“The pressure to keep shipping does take over... cleanup kept happening to the next sprint, and the next sprint just never came.” [03:25]"),
        ("6. Engineering–leadership dialogue gap",
         "Engineers framed debt as 'poor code quality', whereas leadership prioritized delivery speed and client impact; aligning required translating technical risk into business metrics.",
         "“Part of the problem was on our side... leadership cares about delivery speed, customer ease, impact, and satisfaction, and we were not speaking that language.” [04:12]"),
        ("7. Balanced governance & token allocation",
         "Achieving transparency enabled product managers to formally allocate a percentage of sprint tokens/tickets specifically for technical debt remediation and downtime prevention.",
         "“Engineers need to make technical debt measurable and connect it to a business outcome... PM agreed on tickets and tokens reserved at some percentage.” [04:48]"),
        ("8. High-leverage sustainable practices",
         "Combining continuous hygiene (Boy Scout rule, CI/CD safety nets, peer reviews) with cultural psychological safety creates resilient and sustainable engineering workflows.",
         "“Follow the Boy Scout rule... CI/CD pipelines used as a safety net... keep code sustainable, share knowledge with peers, and provide psychological safety.” [05:25]")
    ],
    'reflection_text': (
        "This interview vividly grounded Peter Senge's (1990) Systems Thinking archetypes in high-stakes software engineering. The decision to bypass a "
        "formal service layer to meet an urgent client demo exemplifies 'Fixes that Fail': the quick fix delivered immediate operational success, yet triggered "
        "severe delayed blowbacks in the form of emergency rollbacks. Over time, symptomatic workarounds substituted for foundational architecture, "
        "instantiating 'Shifting the Burden' and degrading team capability into a state where engineers feared touching critical code as 'black boxes'. "
        "Critically, Shubham uncovered the missing link in our causal loop model: the human balancing loop fails when engineers frame debt purely as internal "
        "code aesthetics. Leadership responds to delivery velocity and SLA compliance. The balancing loop only activated when the team translated technical liability "
        "into measurable business metrics, enabling product managers to formalize reserved sprint capacity (token allocations) for debt reduction."
    )
}


def generate_all():
    # 0. Ensure TL;DR Cover Page (Page 1) is built fresh
    from generate_tldr_cover import build_tldr_cover
    cover_pdf = "tldr_cover_page.pdf"
    build_tldr_cover(cover_pdf)

    # 1. Build 5 unified member reports (Pages 2 through 6)
    roster = [
        (REPORT_SAMYABRATA, "unified_report_1_samyabrata.pdf", 2),
        (REPORT_ABIR,        "unified_report_2_abir.pdf",        3),
        (REPORT_RISHABH,     "unified_report_3_rishabh.pdf",     4),
        (REPORT_PIYUSH,      "unified_report_4_piyush.pdf",      5),
        (REPORT_RAMRUP,      "unified_report_5_ramrup.pdf",      6),
    ]

    generated_pdfs = [cover_pdf]
    for data, pdf_name, page_num in roster:
        build_single_member_report(data, pdf_name, page_num=page_num)
        generated_pdfs.append(pdf_name)

    # 2. Master 6-Page Standardized Dossier (Page 1: TL;DR Cover + Pages 2-6: Individual Reports)
    master_doc = pdfium.PdfDocument.new()
    for pdf_path in generated_pdfs:
        doc = pdfium.PdfDocument(pdf_path)
        master_doc.import_pages(doc, [0])

    master_path = "Team_114_SPG_IR_Sep_2026.pdf"
    master_doc.save(master_path)
    print(f"[*] Successfully saved unified 6-page Master Dossier: {master_path} ({len(master_doc)} pages)")

    # Copy aliases
    aliases = [
        "Team_114_Iterate_Interim_Report.pdf",
        "Team_114_SPG_GP2_Deliverable_1a.pdf",
    ]
    for alias in aliases:
        shutil.copyfile(master_path, alias)
        print(f"[*] Copied alias: {alias}")

    # Also save direct 5-page version for standalone archival
    direct_5_doc = pdfium.PdfDocument.new()
    for pdf_path in generated_pdfs[1:]:
        doc = pdfium.PdfDocument(pdf_path)
        direct_5_doc.import_pages(doc, [0])
    direct_5_doc.save("Team_114_SPG_IR_Direct_5_Pages.pdf")
    print("[*] Saved standalone 5-page direct reports: Team_114_SPG_IR_Direct_5_Pages.pdf")


if __name__ == '__main__':
    generate_all()
