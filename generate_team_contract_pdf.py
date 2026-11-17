import os
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph

def generate_tc_pdf():
    pdf_filename = "Team_114_SPG_TC_Sep_2026.pdf"
    PAGE_WIDTH = 960
    PAGE_HEIGHT = 540
    
    c = canvas.Canvas(pdf_filename, pagesize=(PAGE_WIDTH, PAGE_HEIGHT))
    
    # Colors
    BG_WHITE = HexColor("#ffffff")
    BADGE_BG = HexColor("#f1f5f9")
    TEXT_PRIMARY = HexColor("#0f172a") # Slate 900
    TEXT_MUTED = HexColor("#64748b")   # Slate 500
    TEXT_BODY = HexColor("#1e293b")    # Slate 800
    ACCENT_AMBER = HexColor("#b45309") # Amber 700
    CARD_BG = HexColor("#f8fafc")      # Slate 50
    CARD_BORDER = HexColor("#cbd5e1")  # Slate 300
    LINE_DARK = HexColor("#0f172a")
    
    def draw_common_header(title_text):
        badge_x = 40
        badge_y = PAGE_HEIGHT - 65
        badge_w = 260
        badge_h = 42
        
        c.setFillColor(BADGE_BG)
        c.setStrokeColor(LINE_DARK)
        c.setLineWidth(2.5)
        c.roundRect(badge_x, badge_y, badge_w, badge_h, 8, fill=1, stroke=1)
        
        c.setFillColor(TEXT_PRIMARY)
        c.setFont("Helvetica-Bold", 14)
        c.drawCentredString(badge_x + badge_w / 2, badge_y + 13, title_text)
        
        # Horizontal connecting line
        c.setStrokeColor(LINE_DARK)
        c.setLineWidth(2)
        c.line(badge_x + badge_w + 15, badge_y + 21, PAGE_WIDTH - 120, badge_y + 21)
        
        # IIT Madras Logo top right
        if os.path.exists("iitm_logo.png"):
            c.drawImage("iitm_logo.png", PAGE_WIDTH - 105, PAGE_HEIGHT - 75, width=65, height=65, mask='auto')

    def draw_top_down(p, x, top_y, max_w, max_h):
        w, h = p.wrapOn(c, max_w, max_h)
        p.drawOn(c, x, top_y - h)
        return h

    # =========================================================================
    # PAGE 1: Overview & Team Details
    # =========================================================================
    c.setFillColor(BG_WHITE)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)
    draw_common_header("TEAM CONTRACT")
    
    # Purpose of Project Box
    b1_x = 40
    b1_y = PAGE_HEIGHT - 225
    b1_w = PAGE_WIDTH - 80
    b1_h = 140
    
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.setLineWidth(1)
    c.roundRect(b1_x, b1_y, b1_w, b1_h, 8, fill=1, stroke=1)
    
    c.setFillColor(TEXT_PRIMARY)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(b1_x + 20, b1_y + b1_h - 26, "•  Purpose of the Project")
    
    purpose_html = (
        "This project investigates how <b>Systems Thinking principles (Course Week 10)</b> and <b>Engineering Sense (Week 11)</b> "
        "can diagnose and mitigate organizational bottlenecks, technical debt accumulation, and cognitive burnout in "
        "high-velocity technical teams. Anchored in systems archetypes (<i>'Fixes that Fail'</i>, <i>'Shifting the Burden'</i>) and the "
        "<b>WEF Future of Jobs 2025 Skills Outlook (Cognitive Skills: Analytical & Systems Thinking)</b>, our objective is to map an "
        "actionable causal influence model identifying high-leverage intervention points for sustainable, high-velocity engineering teams."
    )
    style_p = ParagraphStyle('PurposeStyle', fontName='Helvetica', fontSize=10.5, leading=16, textColor=TEXT_BODY)
    p_obj = Paragraph(purpose_html, style_p)
    draw_top_down(p_obj, b1_x + 20, b1_y + b1_h - 38, b1_w - 40, b1_h - 45)
    
    # Team Details Box
    b2_y = 35
    b2_h = b1_y - b2_y - 20
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.roundRect(b1_x, b2_y, b1_w, b2_h, 8, fill=1, stroke=1)
    
    c.setFillColor(TEXT_PRIMARY)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(b1_x + 20, b2_y + b2_h - 26, "•  Team Details (Team 114)")
    
    members = [
        ("RAMRUP SATPATI", "24f3004027@ds.study.iitm.ac.in", "(TEAM LEADER / COORDINATOR)"),
        ("RISHABH BARTHWAL", "23f2004000@ds.study.iitm.ac.in", "(Core Team Member)"),
        ("SAMYABRATA ROY", "24f2000000@ds.study.iitm.ac.in", "(Core Team Member)"),
        ("ABIR SAHA", "24f3000000@ds.study.iitm.ac.in", "(Core Team Member)"),
        ("PIYUSH TILOKCHANDANI", "23f3000000@ds.study.iitm.ac.in", "(Core Team Member)")
    ]
    
    m_y = b2_y + b2_h - 52
    for name, email, role in members:
        c.setFillColor(TEXT_PRIMARY)
        c.setFont("Helvetica-Bold", 10.5)
        c.drawString(b1_x + 25, m_y, name)
        
        c.setFillColor(TEXT_MUTED)
        c.setFont("Helvetica", 10)
        c.drawString(b1_x + 205, m_y, f"({email})")
        
        c.setFillColor(ACCENT_AMBER if "LEADER" in role else TEXT_MUTED)
        c.setFont("Helvetica-Bold" if "LEADER" in role else "Helvetica", 10)
        c.drawString(b1_x + 475, m_y, role)
        
        m_y -= 23
        
    c.showPage()
    
    # =========================================================================
    # PAGE 2: Transition Processes
    # =========================================================================
    c.setFillColor(BG_WHITE)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)
    draw_common_header("TRANSITION PROCESSES")
    
    intro_txt = (
        "The transition process defines how our team of five moves from individual contributors to a unified, "
        "goal-driven group. It involves setting clear performance goals, identifying learning objectives, and building psychological safety."
    )
    p_intro = Paragraph(intro_txt, ParagraphStyle('Intro', fontName='Helvetica', fontSize=10.5, leading=15, textColor=TEXT_BODY))
    draw_top_down(p_intro, 40, PAGE_HEIGHT - 80, PAGE_WIDTH - 80, 40)
    
    # Boxes
    q_w = 340
    a_w = PAGE_WIDTH - 80 - q_w - 20
    boxes_y = 35
    boxes_h = PAGE_HEIGHT - 160
    
    # Left Box
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.roundRect(40, boxes_y, q_w, boxes_h, 8, fill=1, stroke=1)
    
    c.setFillColor(TEXT_PRIMARY)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(55, boxes_y + boxes_h - 26, "Suggested Questions")
    
    q2_content = (
        "<b>a. What are our performance goals?</b><br/>"
        "<font color='#64748b' size='9'>(e.g. grade target, depth, innovation, quality of work)</font><br/><br/>"
        "<b>b. What are our learning goals?</b><br/>"
        "<font color='#64748b' size='9'>What knowledge and/or skill development will we focus on together?</font><br/><br/>"
        "<b>c. What are our people goals?</b><br/>"
        "<font color='#64748b' size='9'>(e.g. enjoying teamwork, psychological safety, forming lasting professional colleagues)</font>"
    )
    p_q2 = Paragraph(q2_content, ParagraphStyle('Q2', fontName='Helvetica', fontSize=10.5, leading=15, textColor=TEXT_PRIMARY))
    draw_top_down(p_q2, 55, boxes_y + boxes_h - 40, q_w - 30, boxes_h - 50)
    
    # Right Box
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.roundRect(40 + q_w + 20, boxes_y, a_w, boxes_h, 8, fill=1, stroke=1)
    
    c.setFillColor(ACCENT_AMBER)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(40 + q_w + 40, boxes_y + boxes_h - 26, "Team Action Plan")
    
    a2_content = (
        "<b>a. Performance Goals:</b><br/>"
        "Each member will conduct at least one in-depth qualitative interview with an industry engineering/tech lead. "
        "Together, we target an 'S' grade (top 5%) by synthesizing findings into a rigorous systems dynamics influence model, "
        "delivering cohesive, professionally formatted GP1/GP2 reports, and producing an engaging video presentation with verified timestamps.<br/><br/>"
        "<b>b. Learning Goals:</b><br/>"
        "We will develop hands-on expertise in Systems Thinking archetypes, qualitative interview methodology, and influence diagramming. "
        "Each member will enhance active listening, thematic coding, and the ability to connect academic theory (WEF 2025 Core Skills) "
        "to real-world organizational dynamics.<br/><br/>"
        "<b>c. People Goals:</b><br/>"
        "We commit to building an inclusive, psychologically safe, and supportive culture where constructive debate is welcomed and all five members "
        "contribute equally. Beyond completing course milestones, we aim to build lasting professional camaraderie and network connections."
    )
    p_a2 = Paragraph(a2_content, ParagraphStyle('A2', fontName='Helvetica', fontSize=10, leading=14.5, textColor=TEXT_BODY))
    draw_top_down(p_a2, 40 + q_w + 40, boxes_y + boxes_h - 40, a_w - 40, boxes_h - 50)
    
    c.showPage()
    
    # =========================================================================
    # PAGE 3: Action Processes (1/2)
    # =========================================================================
    c.setFillColor(BG_WHITE)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)
    draw_common_header("ACTION PROCESSES (1/2)")
    
    boxes_h_act = PAGE_HEIGHT - 110
    boxes_y_act = 35
    
    # Left Box
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.roundRect(40, boxes_y_act, q_w, boxes_h_act, 8, fill=1, stroke=1)
    
    c.setFillColor(TEXT_PRIMARY)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(55, boxes_y_act + boxes_h_act - 26, "Suggested Questions")
    
    q3_content = (
        "<b>a. How will we organise leadership for this project?</b><br/>"
        "<font color='#64748b' size='9'>(e.g. project leader, sub-group coordinators)</font><br/><br/>"
        "<b>b. What roles would the other members play?</b><br/><br/>"
        "<b>c. How are decisions made?</b><br/>"
        "<font color='#64748b' size='9'>(e.g. consensus, majority, selected by leader)</font><br/><br/>"
        "<b>d. How will we work together at different stages of the project?</b><br/>"
        "<font color='#64748b' size='9'>(e.g. work separately then pool, simultaneous work)</font><br/><br/>"
        "<b>e. What communication mode will we use and when?</b><br/>"
        "<font color='#64748b' size='9'>(e.g. WhatsApp, email, Teams, Google Meet)</font>"
    )
    p_q3 = Paragraph(q3_content, ParagraphStyle('Q3', fontName='Helvetica', fontSize=10, leading=14, textColor=TEXT_PRIMARY))
    draw_top_down(p_q3, 55, boxes_y_act + boxes_h_act - 40, q_w - 30, boxes_h_act - 50)
    
    # Right Box
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.roundRect(40 + q_w + 20, boxes_y_act, a_w, boxes_h_act, 8, fill=1, stroke=1)
    
    c.setFillColor(ACCENT_AMBER)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(40 + q_w + 40, boxes_y_act + boxes_h_act - 26, "Team Action Plan")
    
    a3_content = (
        "<b>a. Leadership:</b><br/>"
        "Leadership is collaborative and servant-driven. The Team Leader / Coordinator coordinates meeting schedules, "
        "tracks milestone deadlines, and ensures submission compliance, while task ownership is shared equally across all members.<br/><br/>"
        "<b>b. Roles of Other Members:</b><br/>"
        "Every member conducts 1 external professional interview. Cross-functional roles (secondary literature synthesis, "
        "qualitative coding, influence diagram design, presentation curation, and APA reference formatting) are distributed by individual strengths.<br/><br/>"
        "<b>c. Decision Making:</b><br/>"
        "Consensus-first via transparent discussion. If consensus cannot be reached after structured debate, decisions will be resolved "
        "by simple majority vote, with minority perspectives formally recorded and respected.<br/><br/>"
        "<b>d. Working Together:</b><br/>"
        "Phased workflow: (1) Collaborative kickoff to align on interview protocols; (2) Autonomous execution of individual interviews and transcripts; "
        "(3) Synchronized regrouping to synthesize themes, construct the influence model, and rehearse the presentation.<br/><br/>"
        "<b>e. Communication Mode:</b><br/>"
        "WhatsApp group for instant daily coordination, Google Space/Discourse for official updates, Google Drive for collaborative "
        "document drafting, and Google Meet for weekly structured milestone check-ins."
    )
    p_a3 = Paragraph(a3_content, ParagraphStyle('A3', fontName='Helvetica', fontSize=9.5, leading=13.5, textColor=TEXT_BODY))
    draw_top_down(p_a3, 40 + q_w + 40, boxes_y_act + boxes_h_act - 40, a_w - 40, boxes_h_act - 50)
    
    c.showPage()
    
    # =========================================================================
    # PAGE 4: Action Processes (2/2)
    # =========================================================================
    c.setFillColor(BG_WHITE)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)
    draw_common_header("ACTION PROCESSES (2/2)")
    
    # Left Box
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.roundRect(40, boxes_y_act, q_w, boxes_h_act, 8, fill=1, stroke=1)
    
    c.setFillColor(TEXT_PRIMARY)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(55, boxes_y_act + boxes_h_act - 26, "Suggested Questions")
    
    q4_content = (
        "<b>f. When and where will we hold our meetings?</b><br/><br/>"
        "<b>g. How will we share the workload?</b><br/>"
        "<font color='#64748b' size='9'>(quantity, quality, time)? What will we do when a team member is doing more (or less) work than others?</font><br/><br/>"
        "<b>h. How will we help team members?</b><br/>"
        "<font color='#64748b' size='9'>(sharing knowledge, tools, and resources)?</font><br/><br/>"
        "<b>i. When and how will we review progress on goals?</b><br/>"
        "<font color='#64748b' size='9'>What is our process for setting and meeting deadlines?</font>"
    )
    p_q4 = Paragraph(q4_content, ParagraphStyle('Q4', fontName='Helvetica', fontSize=10, leading=14.5, textColor=TEXT_PRIMARY))
    draw_top_down(p_q4, 55, boxes_y_act + boxes_h_act - 40, q_w - 30, boxes_h_act - 50)
    
    # Right Box
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.roundRect(40 + q_w + 20, boxes_y_act, a_w, boxes_h_act, 8, fill=1, stroke=1)
    
    c.setFillColor(ACCENT_AMBER)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(40 + q_w + 40, boxes_y_act + boxes_h_act - 26, "Team Action Plan")
    
    a4_content = (
        "<b>f. Meetings:</b><br/>"
        "Weekly video meetings via Google Meet every weekend (Sunday evenings) at a mutually agreed time. "
        "Agendas are shared 24 hours in advance, and brief meeting minutes are logged in our shared Drive.<br/><br/>"
        "<b>g. Workload Sharing:</b><br/>"
        "Work is partitioned into clear, balanced work packages. If an individual faces unexpected academic/work constraints, "
        "workload is proactively redistributed. If a member under-contributes, the coordinator initiates a supportive 1-on-1 check-in "
        "to identify blockers before escalating.<br/><br/>"
        "<b>h. Helping Team Members:</b><br/>"
        "We maintain a central shared Google Drive with literature papers, interview guides, consent templates, and transcript logs. "
        "Members offer peer-feedback on draft interview questions and presentation slides.<br/><br/>"
        "<b>i. Reviewing Progress & Deadlines:</b><br/>"
        "Progress is tracked using a live Work Breakdown Structure (WBS) sheet. Internal team deadlines are set 48 hours prior to official "
        "IITM portal deadlines to provide a comfortable buffer for peer review and formatting."
    )
    p_a4 = Paragraph(a4_content, ParagraphStyle('A4', fontName='Helvetica', fontSize=9.5, leading=14, textColor=TEXT_BODY))
    draw_top_down(p_a4, 40 + q_w + 40, boxes_y_act + boxes_h_act - 40, a_w - 40, boxes_h_act - 50)
    
    c.showPage()
    
    # =========================================================================
    # PAGE 5: Interpersonal Processes
    # =========================================================================
    c.setFillColor(BG_WHITE)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)
    draw_common_header("INTERPERSONAL PROCESSES")
    
    intro_txt5 = (
        "Interpersonal processes define how our team connects, communicates, and navigates interpersonal challenges. "
        "They focus on building mutual trust, resolving friction constructively, supporting one another, and celebrating shared achievements."
    )
    p_intro5 = Paragraph(intro_txt5, ParagraphStyle('Intro5', fontName='Helvetica', fontSize=10.5, leading=15, textColor=TEXT_BODY))
    draw_top_down(p_intro5, 40, PAGE_HEIGHT - 80, PAGE_WIDTH - 80, 40)
    
    # Left Box
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.roundRect(40, boxes_y, q_w, boxes_h, 8, fill=1, stroke=1)
    
    c.setFillColor(TEXT_PRIMARY)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(55, boxes_y + boxes_h - 26, "Suggested Questions")
    
    q5_content = (
        "<b>a. How will we manage conflict if it becomes personal and not task related?</b><br/><br/><br/>"
        "<b>b. What will we do to make the experience of working together a positive one?</b><br/><br/><br/>"
        "<b>c. How will we celebrate successes & commiserate goals we do not meet?</b>"
    )
    p_q5 = Paragraph(q5_content, ParagraphStyle('Q5', fontName='Helvetica', fontSize=10.5, leading=15, textColor=TEXT_PRIMARY))
    draw_top_down(p_q5, 55, boxes_y + boxes_h - 40, q_w - 30, boxes_h - 50)
    
    # Right Box
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.roundRect(40 + q_w + 20, boxes_y, a_w, boxes_h, 8, fill=1, stroke=1)
    
    c.setFillColor(ACCENT_AMBER)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(40 + q_w + 40, boxes_y + boxes_h - 26, "Team Action Plan")
    
    a5_content = (
        "<b>a. Conflict Management:</b><br/>"
        "If interpersonal tensions arise, we will pause and address them through private, respectful 1-on-1 conversations. "
        "We practice separating personalities from ideas, focusing on shared objectives, and relying on active listening. "
        "The team coordinator steps in as an impartial mediator if consensus is delayed.<br/><br/>"
        "<b>b. Fostering a Positive Experience:</b><br/>"
        "We foster an atmosphere of psychological safety, open encouragement, and intellectual curiosity. "
        "All members' viewpoints are actively solicited during brainstorms, ensuring an enjoyable, respectful, and equitable learning environment.<br/><br/>"
        "<b>c. Celebrating Successes & Continuous Learning:</b><br/>"
        "We recognize milestone completions and individual contributions through shout-outs in our group chat. "
        "If a deliverable faces setbacks or rubric penalties, we conduct a blameless post-mortem retrospective to diagnose systemic causes and adapt."
    )
    p_a5 = Paragraph(a5_content, ParagraphStyle('A5', fontName='Helvetica', fontSize=10, leading=14.5, textColor=TEXT_BODY))
    draw_top_down(p_a5, 40 + q_w + 40, boxes_y + boxes_h - 40, a_w - 40, boxes_h - 50)
    
    c.save()
    print(f"[*] Successfully regenerated {pdf_filename}")

generate_tc_pdf()
