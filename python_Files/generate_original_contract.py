import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph

# =============================================================================
# 1. ORIGINAL EXECUTIVE / TECH-SYSTEMS POWERPOINT
# =============================================================================
def build_pptx():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]
    
    # Modern Executive Tech Palette
    C_BG = RGBColor(248, 250, 252)          # Slate 50
    C_NAVY = RGBColor(15, 23, 42)           # Slate 900
    C_BLUE = RGBColor(37, 99, 235)          # Royal Blue 600
    C_SLATE = RGBColor(71, 85, 105)         # Slate 600
    C_BODY = RGBColor(30, 41, 59)           # Slate 800
    C_CARD_BG = RGBColor(255, 255, 255)     # Pure White
    C_BORDER = RGBColor(226, 232, 240)      # Slate 200
    C_LINE = RGBColor(203, 213, 225)        # Slate 300
    
    def add_tech_header(slide, page_num_str, section_title):
        # Top metadata bar
        top_txt = slide.shapes.add_textbox(Inches(0.8), Inches(0.35), Inches(8.5), Inches(0.4))
        tf_t = top_txt.text_frame
        p_t = tf_t.paragraphs[0]
        r1 = p_t.add_run()
        r1.text = "IIT MADRAS BS DEGREE PROGRAM  |  BSGN3001: STRATEGIES FOR PROFESSIONAL GROWTH  |  TEAM 114"
        r1.font.bold = True
        r1.font.size = Pt(9.5)
        r1.font.color.rgb = C_BLUE
        
        # Section Category Pill
        pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.75), Inches(4.5), Inches(0.65))
        pill.fill.solid()
        pill.fill.fore_color.rgb = C_NAVY
        pill.line.fill.background()
        
        tf_p = pill.text_frame
        p_p = tf_p.paragraphs[0]
        p_p.alignment = PP_ALIGN.LEFT
        p_p.margin_left = Inches(0.2)
        r_num = p_p.add_run()
        r_num.text = f"[{page_num_str}]  "
        r_num.font.bold = True
        r_num.font.size = Pt(13)
        r_num.font.color.rgb = RGBColor(56, 189, 248) # Cyan accent
        
        r_title = p_p.add_run()
        r_title.text = section_title
        r_title.font.bold = True
        r_title.font.size = Pt(13)
        r_title.font.color.rgb = RGBColor(255, 255, 255)
        
        # Architectural grid line across top
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(5.5), Inches(1.05), Inches(5.8), Inches(0.02))
        line.fill.solid()
        line.fill.fore_color.rgb = C_LINE
        line.line.fill.background()
        
        # IIT Madras Logo top right (Bigger & Clean)
        if os.path.exists("iitm_logo_clean.png"):
            slide.shapes.add_picture("iitm_logo_clean.png", Inches(11.65), Inches(0.25), Inches(1.35), Inches(1.35))
            
        # Subtle Bottom status bar
        bot_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(7.05), Inches(11.733), Inches(0.02))
        bot_line.fill.solid()
        bot_line.fill.fore_color.rgb = C_LINE
        bot_line.line.fill.background()
        
        bot_txt = slide.shapes.add_textbox(Inches(0.8), Inches(7.1), Inches(11.733), Inches(0.3))
        p_b = bot_txt.text_frame.paragraphs[0]
        r_b = p_b.add_run()
        r_b.text = "GP1 Deliverable 1.c: Collaborative Team Contract  •  Theme: Systems Thinking & Engineering Sense  •  WEF 2025 Core Skills"
        r_b.font.size = Pt(9)
        r_b.font.color.rgb = C_SLATE

    # --- SLIDE 1 ---
    s1 = prs.slides.add_slide(blank_layout)
    add_tech_header(s1, "01/05", "PROJECT SCOPE & TEAM STRUCTURE")
    
    # Purpose Box
    b1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(11.733), Inches(2.2))
    b1.fill.solid()
    b1.fill.fore_color.rgb = C_CARD_BG
    b1.line.color.rgb = C_BORDER
    b1.line.width = Pt(1.5)
    
    # Top blue accent line on box
    acc1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.6), Inches(11.733), Inches(0.06))
    acc1.fill.solid()
    acc1.fill.fore_color.rgb = C_BLUE
    acc1.line.fill.background()
    
    tf1 = b1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = Inches(0.35)
    tf1.margin_top = Inches(0.25)
    
    p = tf1.paragraphs[0]
    p.text = "PROJECT MISSION & RESEARCH PURPOSE"
    p.font.bold = True
    p.font.size = Pt(14)
    p.font.color.rgb = C_NAVY
    p.space_after = Pt(8)
    
    p_desc = tf1.add_paragraph()
    p_desc.text = (
        "This project investigates how Systems Thinking principles (Course Week 10) and Engineering Sense (Week 11) "
        "can diagnose and mitigate organizational bottlenecks, technical debt accumulation, and cognitive overload in "
        "high-velocity technical teams. Anchored in systems archetypes ('Fixes that Fail', 'Shifting the Burden') and the "
        "WEF Future of Jobs 2025 Skills Outlook (Cognitive Skills: Analytical & Systems Thinking), our objective is to map an "
        "actionable influence model identifying high-leverage intervention points for sustainable, high-velocity engineering organizations."
    )
    p_desc.font.size = Pt(11.5)
    p_desc.font.color.rgb = C_BODY
    
    # Team Details Box
    b2 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.05), Inches(11.733), Inches(2.85))
    b2.fill.solid()
    b2.fill.fore_color.rgb = C_CARD_BG
    b2.line.color.rgb = C_BORDER
    b2.line.width = Pt(1.5)
    
    acc2 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(4.05), Inches(11.733), Inches(0.06))
    acc2.fill.solid()
    acc2.fill.fore_color.rgb = C_BLUE
    acc2.line.fill.background()
    
    tf2 = b2.text_frame
    tf2.word_wrap = True
    tf2.margin_left = Inches(0.35)
    tf2.margin_top = Inches(0.2)
    
    p2 = tf2.paragraphs[0]
    p2.text = "TEAM ROSTER & GOVERNANCE STRUCTURE (TEAM 114)"
    p2.font.bold = True
    p2.font.size = Pt(14)
    p2.font.color.rgb = C_NAVY
    p2.space_after = Pt(10)
    
    members = [
        ("RAMRUP SATPATI", "24f3004027@ds.study.iitm.ac.in", "PROJECT COORDINATOR & TEAM LEAD", True),
        ("RISHABH BARTHWAL", "23f2004000@ds.study.iitm.ac.in", "Core Member • Qualitative Systems Research", False),
        ("SAMYABRATA ROY", "24f2000000@ds.study.iitm.ac.in", "Core Member • Industry Data & Interview Analysis", False),
        ("ABIR SAHA", "24f3000000@ds.study.iitm.ac.in", "Core Member • Systems Archetype Modeling", False),
        ("PIYUSH TILOKCHANDANI", "23f3000000@ds.study.iitm.ac.in", "Core Member • Literature Synthesis & Reporting", False)
    ]
    for name, email, role, is_lead in members:
        pm = tf2.add_paragraph()
        r1 = pm.add_run()
        r1.text = f"{name}  "
        r1.font.bold = True
        r1.font.size = Pt(11)
        r1.font.color.rgb = C_NAVY
        
        r2 = pm.add_run()
        r2.text = f"[{email}]    —    "
        r2.font.size = Pt(10.5)
        r2.font.color.rgb = C_SLATE
        
        r3 = pm.add_run()
        r3.text = role
        r3.font.bold = is_lead
        r3.font.size = Pt(10.5)
        r3.font.color.rgb = C_BLUE if is_lead else C_BODY
        pm.space_after = Pt(3)

    # --- SLIDE 2 ---
    s2 = prs.slides.add_slide(blank_layout)
    add_tech_header(s2, "02/05", "TRANSITION PROCESSES")
    
    intro2 = s2.shapes.add_textbox(Inches(0.8), Inches(1.4), Inches(11.733), Inches(0.55))
    p = intro2.text_frame.paragraphs[0]
    p.text = (
        "TRANSITION FRAMEWORK: Defining how our team transitions from individual contributors to a unified, "
        "high-performing team by setting clear performance targets, shared learning objectives, and psychological safety."
    )
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_NAVY
    
    # Left Q Card
    q_b2 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.05), Inches(4.3), Inches(4.85))
    q_b2.fill.solid()
    q_b2.fill.fore_color.rgb = C_CARD_BG
    q_b2.line.color.rgb = C_BORDER
    q_b2.line.width = Pt(1.5)
    
    tf_q2 = q_b2.text_frame
    tf_q2.word_wrap = True
    tf_q2.margin_left = Inches(0.28)
    tf_q2.margin_top = Inches(0.2)
    p = tf_q2.paragraphs[0]
    p.text = "CORE INQUIRY QUESTIONS"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = C_BLUE
    p.space_after = Pt(12)
    
    q2_items = [
        ("a. Performance Goals", "What are our performance goals (e.g. grade targets, analytical depth, deliverable quality, and innovation)?"),
        ("b. Learning Goals", "What knowledge and/or technical skill development will we focus on together (e.g. Systems Thinking, interview coding)?"),
        ("c. People Goals", "What are our interpersonal goals (e.g. building trust, psychological safety, and forming lasting professional networks)?")
    ]
    for qt, qd in q2_items:
        pq = tf_q2.add_paragraph()
        pq.text = qt
        pq.font.bold = True
        pq.font.size = Pt(11.5)
        pq.font.color.rgb = C_NAVY
        
        pqd = tf_q2.add_paragraph()
        pqd.text = qd
        pqd.font.size = Pt(10)
        pqd.font.color.rgb = C_SLATE
        pqd.space_after = Pt(14)
        
    # Right A Card
    a_b2 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.3), Inches(2.05), Inches(7.233), Inches(4.85))
    a_b2.fill.solid()
    a_b2.fill.fore_color.rgb = C_CARD_BG
    a_b2.line.color.rgb = C_BORDER
    a_b2.line.width = Pt(1.5)
    
    tf_a2 = a_b2.text_frame
    tf_a2.word_wrap = True
    tf_a2.margin_left = Inches(0.35)
    tf_a2.margin_top = Inches(0.2)
    p = tf_a2.paragraphs[0]
    p.text = "TEAM ACTION PLAN & EXECUTION COMMITMENTS"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = C_BLUE
    p.space_after = Pt(10)
    
    a2_items = [
        ("a. Performance Target ('S' Grade Benchmark):",
         "Each member will conduct at least one in-depth qualitative interview with an industry engineering lead. "
         "Together, we target an 'S' grade (top 5%) by synthesizing findings into a rigorous causal loop influence model, "
         "delivering cohesive, professionally formatted GP1/GP2 reports, and producing an engaging video presentation with verified timestamps."),
        ("b. Competency & Learning Objectives:",
         "We will develop hands-on expertise in Systems Thinking archetypes, qualitative interview methodology, and influence diagramming. "
         "Each member will enhance active listening, thematic analysis, and the ability to connect academic theory (WEF 2025 Core Skills) "
         "to real-world organizational dynamics."),
        ("c. People & Culture Commitments:",
         "We commit to building an inclusive, psychologically safe, and supportive culture where constructive debate is welcomed and all five members "
         "contribute equally. Beyond completing course milestones, we aim to build lasting professional camaraderie and network connections.")
    ]
    for at, ad in a2_items:
        pa = tf_a2.add_paragraph()
        pa.text = at
        pa.font.bold = True
        pa.font.size = Pt(11)
        pa.font.color.rgb = C_NAVY
        
        pad = tf_a2.add_paragraph()
        pad.text = ad
        pad.font.size = Pt(10)
        pad.font.color.rgb = C_BODY
        pad.space_after = Pt(8)

    # --- SLIDE 3 ---
    s3 = prs.slides.add_slide(blank_layout)
    add_tech_header(s3, "03/05", "ACTION PROCESSES: GOVERNANCE & ROLES")
    
    q_b3 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(4.3), Inches(5.4))
    q_b3.fill.solid()
    q_b3.fill.fore_color.rgb = C_CARD_BG
    q_b3.line.color.rgb = C_BORDER
    q_b3.line.width = Pt(1.5)
    tf_q3 = q_b3.text_frame
    tf_q3.word_wrap = True
    tf_q3.margin_left = Inches(0.28)
    tf_q3.margin_top = Inches(0.2)
    p = tf_q3.paragraphs[0]
    p.text = "CORE INQUIRY QUESTIONS"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = C_BLUE
    p.space_after = Pt(10)
    
    q3_items = [
        "a. How will we organise leadership for this project?",
        "b. What specific functional roles will each member play?",
        "c. How are decisions made (consensus, majority, lead)?",
        "d. How will we collaborate across project lifecycle stages?",
        "e. What communication modes will we employ and when?"
    ]
    for q_item in q3_items:
        pq = tf_q3.add_paragraph()
        pq.text = q_item
        pq.font.bold = True
        pq.font.size = Pt(10.5)
        pq.font.color.rgb = C_NAVY
        pq.space_after = Pt(14)
        
    a_b3 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.3), Inches(1.5), Inches(7.233), Inches(5.4))
    a_b3.fill.solid()
    a_b3.fill.fore_color.rgb = C_CARD_BG
    a_b3.line.color.rgb = C_BORDER
    a_b3.line.width = Pt(1.5)
    tf_a3 = a_b3.text_frame
    tf_a3.word_wrap = True
    tf_a3.margin_left = Inches(0.35)
    tf_a3.margin_top = Inches(0.2)
    p = tf_a3.paragraphs[0]
    p.text = "OPERATIONAL ACTION PLAN & WORKFLOW PROTOCOL"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = C_BLUE
    p.space_after = Pt(8)
    
    a3_items = [
        ("a. Leadership Architecture:",
         "Leadership is collaborative and servant-driven. The Project Coordinator schedules meetings, tracks deadlines, and ensures compliance, "
         "while work package ownership is shared equally across all members."),
        ("b. Functional Role Distribution:",
         "Each member conducts 1 external interview. Sub-roles (literature review synthesis, qualitative transcript coding, influence modeling, "
         "presentation deck curation, and APA reference formatting) are distributed by member strengths."),
        ("c. Decision-Making Framework:",
         "Consensus-first via transparent discussion. If consensus is split after structured debate, decisions will be resolved "
         "by simple majority vote, with dissenting viewpoints documented for retrospective review."),
        ("d. Phased Collaboration Lifecycle:",
         "Phased workflow: (1) Collaborative kickoff to align on interview protocols; (2) Autonomous execution of individual interviews and transcripts; "
         "(3) Synchronized regrouping to synthesize themes, construct the influence model, and rehearse the presentation."),
        ("e. Multi-Channel Communication Stack:",
         "WhatsApp group for instant daily coordination, Google Space/Discourse for official updates, Google Drive for collaborative "
         "document drafting, and Google Meet for weekly structured milestone check-ins.")
    ]
    for at, ad in a3_items:
        pa = tf_a3.add_paragraph()
        pa.text = at
        pa.font.bold = True
        pa.font.size = Pt(11)
        pa.font.color.rgb = C_NAVY
        
        pad = tf_a3.add_paragraph()
        pad.text = ad
        pad.font.size = Pt(9.5)
        pad.font.color.rgb = C_BODY
        pad.space_after = Pt(6)

    # --- SLIDE 4 ---
    s4 = prs.slides.add_slide(blank_layout)
    add_tech_header(s4, "04/05", "ACTION PROCESSES: LOGISTICS & CADENCE")
    
    q_b4 = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(4.3), Inches(5.4))
    q_b4.fill.solid()
    q_b4.fill.fore_color.rgb = C_CARD_BG
    q_b4.line.color.rgb = C_BORDER
    q_b4.line.width = Pt(1.5)
    tf_q4 = q_b4.text_frame
    tf_q4.word_wrap = True
    tf_q4.margin_left = Inches(0.28)
    tf_q4.margin_top = Inches(0.2)
    p = tf_q4.paragraphs[0]
    p.text = "CORE INQUIRY QUESTIONS"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = C_BLUE
    p.space_after = Pt(12)
    
    q4_items = [
        "f. When and where will we hold our meetings?",
        "g. How will we share workload & resolve imbalances?",
        "h. How will we share knowledge, tools & resources?",
        "i. What is our mechanism for milestone tracking?"
    ]
    for q_item in q4_items:
        pq = tf_q4.add_paragraph()
        pq.text = q_item
        pq.font.bold = True
        pq.font.size = Pt(10.5)
        pq.font.color.rgb = C_NAVY
        pq.space_after = Pt(18)
        
    a_b4 = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.3), Inches(1.5), Inches(7.233), Inches(5.4))
    a_b4.fill.solid()
    a_b4.fill.fore_color.rgb = C_CARD_BG
    a_b4.line.color.rgb = C_BORDER
    a_b4.line.width = Pt(1.5)
    tf_a4 = a_b4.text_frame
    tf_a4.word_wrap = True
    tf_a4.margin_left = Inches(0.35)
    tf_a4.margin_top = Inches(0.2)
    p = tf_a4.paragraphs[0]
    p.text = "EXECUTION CADENCE & ACCOUNTABILITY PLAN"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = C_BLUE
    p.space_after = Pt(8)
    
    a4_items = [
        ("f. Meeting Cadence & Virtual Workspace:",
         "Weekly video meetings via Google Meet every weekend (Sunday evenings) at a mutually agreed time. "
         "Agendas are shared 24 hours in advance, and brief meeting minutes are logged in our shared Drive."),
        ("g. Fair Workload Distribution & Rebalancing:",
         "Work is partitioned into clear, balanced work packages. If an individual faces unexpected academic/work constraints, "
         "workload is proactively redistributed. If a member under-contributes, the coordinator initiates a supportive 1-on-1 check-in "
         "to identify blockers before escalating."),
        ("h. Knowledge Infrastructure & Peer Support:",
         "We maintain a central shared Google Drive with literature papers, interview guides, consent templates, and transcript logs. "
         "Members offer peer-feedback on draft interview questions and presentation slides."),
        ("i. Deadline Management & Buffer Protocol:",
         "Progress is tracked using a live Work Breakdown Structure (WBS) sheet. Internal team deadlines are set 48 hours prior to official "
         "IITM portal deadlines to provide a comfortable buffer for peer review and formatting.")
    ]
    for at, ad in a4_items:
        pa = tf_a4.add_paragraph()
        pa.text = at
        pa.font.bold = True
        pa.font.size = Pt(11)
        pa.font.color.rgb = C_NAVY
        
        pad = tf_a4.add_paragraph()
        pad.text = ad
        pad.font.size = Pt(9.5)
        pad.font.color.rgb = C_BODY
        pad.space_after = Pt(8)

    # --- SLIDE 5 ---
    s5 = prs.slides.add_slide(blank_layout)
    add_tech_header(s5, "05/05", "INTERPERSONAL PROCESSES: DYNAMICS & CULTURE")
    
    intro5 = s5.shapes.add_textbox(Inches(0.8), Inches(1.4), Inches(11.733), Inches(0.55))
    p = intro5.text_frame.paragraphs[0]
    p.text = (
        "INTERPERSONAL CULTURE: Defining how our team communicates, resolves friction constructively, "
        "cultivates psychological safety, and celebrates shared accomplishments throughout the semester."
    )
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_NAVY
    
    q_b5 = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.05), Inches(4.3), Inches(4.85))
    q_b5.fill.solid()
    q_b5.fill.fore_color.rgb = C_CARD_BG
    q_b5.line.color.rgb = C_BORDER
    q_b5.line.width = Pt(1.5)
    tf_q5 = q_b5.text_frame
    tf_q5.word_wrap = True
    tf_q5.margin_left = Inches(0.28)
    tf_q5.margin_top = Inches(0.2)
    p = tf_q5.paragraphs[0]
    p.text = "CORE INQUIRY QUESTIONS"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = C_BLUE
    p.space_after = Pt(12)
    
    q5_items = [
        "a. How will we manage conflict if it becomes personal and not task-related?",
        "b. What specific practices will ensure our collaboration remains positive?",
        "c. How will we celebrate successes & commiserate setbacks together?"
    ]
    for q_item in q5_items:
        pq = tf_q5.add_paragraph()
        pq.text = q_item
        pq.font.bold = True
        pq.font.size = Pt(10.5)
        pq.font.color.rgb = C_NAVY
        pq.space_after = Pt(20)
        
    a_b5 = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.3), Inches(2.05), Inches(7.233), Inches(4.85))
    a_b5.fill.solid()
    a_b5.fill.fore_color.rgb = C_CARD_BG
    a_b5.line.color.rgb = C_BORDER
    a_b5.line.width = Pt(1.5)
    tf_a5 = a_b5.text_frame
    tf_a5.word_wrap = True
    tf_a5.margin_left = Inches(0.35)
    tf_a5.margin_top = Inches(0.2)
    p = tf_a5.paragraphs[0]
    p.text = "INTERPERSONAL CODE & RESOLUTION PROTOCOLS"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = C_BLUE
    p.space_after = Pt(10)
    
    a5_items = [
        ("a. Constructive Conflict Mediation Protocol:",
         "If interpersonal tensions arise, we will pause and address them through private, respectful 1-on-1 conversations. "
         "We practice separating personalities from ideas, focusing on shared objectives, and relying on active listening. "
         "The team coordinator steps in as an impartial mediator if consensus is delayed."),
        ("b. Cultivating Psychological Safety & Morale:",
         "We foster an atmosphere of psychological safety, open encouragement, and intellectual curiosity. "
         "All members' viewpoints are actively solicited during brainstorms, ensuring an enjoyable, respectful, and equitable learning environment."),
        ("c. Celebrating Successes & Blameless Retrospectives:",
         "We recognize milestone completions and individual contributions through shout-outs in our group chat. "
         "If a deliverable faces setbacks or rubric penalties, we conduct a blameless post-mortem retrospective to diagnose systemic causes and adapt.")
    ]
    for at, ad in a5_items:
        pa = tf_a5.add_paragraph()
        pa.text = at
        pa.font.bold = True
        pa.font.size = Pt(11)
        pa.font.color.rgb = C_NAVY
        
        pad = tf_a5.add_paragraph()
        pad.text = ad
        pad.font.size = Pt(10)
        pad.font.color.rgb = C_BODY
        pad.space_after = Pt(10)
        
    prs.save("Team_114_SPG_TC_Sep_2026.pptx")
    print("[*] Generated clean, original Team_114_SPG_TC_Sep_2026.pptx")

# =============================================================================
# 2. ORIGINAL EXECUTIVE / TECH-SYSTEMS PDF (REPORTLAB)
# =============================================================================
def build_pdf():
    pdf_filename = "Team_114_SPG_TC_Sep_2026.pdf"
    PAGE_WIDTH = 960
    PAGE_HEIGHT = 540
    
    c = canvas.Canvas(pdf_filename, pagesize=(PAGE_WIDTH, PAGE_HEIGHT))
    
    BG_CANVAS = HexColor("#f8fafc")       # Slate 50
    CARD_BG = HexColor("#ffffff")         # Pure White
    CARD_BORDER = HexColor("#cbd5e1")     # Slate 300
    TEXT_NAVY = HexColor("#0f172a")       # Slate 900
    TEXT_BLUE = HexColor("#2563eb")       # Royal Blue
    TEXT_CYAN = HexColor("#0284c7")       # Cyan 600
    TEXT_SLATE = HexColor("#64748b")      # Slate 500
    TEXT_BODY = HexColor("#1e293b")       # Slate 800
    LINE_BORDER = HexColor("#e2e8f0")     # Slate 200
    
    def draw_top_down(p, x, top_y, max_w, max_h):
        w, h = p.wrapOn(c, max_w, max_h)
        p.drawOn(c, x, top_y - h)
        return h

    def draw_tech_frame(page_num_str, section_title):
        # Background
        c.setFillColor(BG_CANVAS)
        c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)
        
        # Subtle architectural grid / corner ticks
        c.setStrokeColor(HexColor("#cbd5e1"))
        c.setLineWidth(1)
        c.line(20, PAGE_HEIGHT - 20, 40, PAGE_HEIGHT - 20)
        c.line(20, PAGE_HEIGHT - 20, 20, PAGE_HEIGHT - 40)
        c.line(PAGE_WIDTH - 20, PAGE_HEIGHT - 20, PAGE_WIDTH - 40, PAGE_HEIGHT - 20)
        c.line(PAGE_WIDTH - 20, PAGE_HEIGHT - 20, PAGE_WIDTH - 20, PAGE_HEIGHT - 40)
        
        # Top metadata bar
        c.setFillColor(TEXT_BLUE)
        c.setFont("Helvetica-Bold", 8.5)
        c.drawString(45, PAGE_HEIGHT - 28, "IIT MADRAS BS DEGREE  •  BSGN3001: STRATEGIES FOR PROFESSIONAL GROWTH  •  TEAM 114")
        
        # Header category pill
        pill_x = 45
        pill_y = PAGE_HEIGHT - 68
        pill_w = 340
        pill_h = 32
        c.setFillColor(TEXT_NAVY)
        c.roundRect(pill_x, pill_y, pill_w, pill_h, 6, fill=1, stroke=0)
        
        c.setFillColor(HexColor("#38bdf8")) # Cyan accent
        c.setFont("Helvetica-Bold", 10.5)
        c.drawString(pill_x + 14, pill_y + 10, f"[{page_num_str}]")
        
        c.setFillColor(HexColor("#ffffff"))
        c.drawString(pill_x + 58, pill_y + 10, section_title)
        
        # Line connecting pill across to logo
        c.setStrokeColor(LINE_BORDER)
        c.setLineWidth(1.5)
        c.line(pill_x + pill_w + 15, pill_y + 16, PAGE_WIDTH - 130, pill_y + 16)
        
        # IIT Madras Logo top right - PROMINENT & HIGH RES (88x88)
        if os.path.exists("iitm_logo_clean.png"):
            c.drawImage("iitm_logo_clean.png", PAGE_WIDTH - 118, PAGE_HEIGHT - 85, width=85, height=85, mask='auto')
            
        # Bottom status bar
        c.setStrokeColor(LINE_BORDER)
        c.setLineWidth(1)
        c.line(45, 26, PAGE_WIDTH - 45, 26)
        
        c.setFillColor(TEXT_SLATE)
        c.setFont("Helvetica", 8)
        c.drawString(45, 14, "GP1 Deliverable 1.c: Collaborative Team Contract  |  Theme: Systems Thinking & Engineering Sense  |  WEF 2025 Core Skills")
        c.drawRightString(PAGE_WIDTH - 45, 14, f"Page {page_num_str} of 05")

    # --- Page 1 ---
    draw_tech_frame("01/05", "PROJECT SCOPE & TEAM STRUCTURE")
    
    b1_x = 45
    b1_y = PAGE_HEIGHT - 215
    b1_w = PAGE_WIDTH - 90
    b1_h = 135
    
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.setLineWidth(1.2)
    c.roundRect(b1_x, b1_y, b1_w, b1_h, 6, fill=1, stroke=1)
    
    # Top blue accent stripe
    c.setFillColor(TEXT_BLUE)
    c.roundRect(b1_x, b1_y + b1_h - 4, b1_w, 4, 2, fill=1, stroke=0)
    
    c.setFillColor(TEXT_NAVY)
    c.setFont("Helvetica-Bold", 12.5)
    c.drawString(b1_x + 20, b1_y + b1_h - 26, "PROJECT MISSION & RESEARCH PURPOSE")
    
    purpose_html = (
        "This project investigates how <b>Systems Thinking principles (Course Week 10)</b> and <b>Engineering Sense (Week 11)</b> "
        "can diagnose and mitigate organizational bottlenecks, technical debt accumulation, and cognitive overload in "
        "high-velocity technical teams. Anchored in systems archetypes (<i>'Fixes that Fail'</i>, <i>'Shifting the Burden'</i>) and the "
        "<b>WEF Future of Jobs 2025 Skills Outlook (Cognitive Skills: Analytical & Systems Thinking)</b>, our objective is to map an "
        "actionable causal influence model identifying high-leverage intervention points for sustainable organizational velocity."
    )
    style_p = ParagraphStyle('P1', fontName='Helvetica', fontSize=10, leading=15.5, textColor=TEXT_BODY)
    draw_top_down(Paragraph(purpose_html, style_p), b1_x + 20, b1_y + b1_h - 38, b1_w - 40, b1_h - 45)
    
    # Team Details Box
    b2_y = 42
    b2_h = b1_y - b2_y - 18
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.roundRect(b1_x, b2_y, b1_w, b2_h, 6, fill=1, stroke=1)
    
    c.setFillColor(TEXT_BLUE)
    c.roundRect(b1_x, b2_y + b2_h - 4, b1_w, 4, 2, fill=1, stroke=0)
    
    c.setFillColor(TEXT_NAVY)
    c.setFont("Helvetica-Bold", 12.5)
    c.drawString(b1_x + 20, b2_y + b2_h - 26, "TEAM ROSTER & GOVERNANCE STRUCTURE (TEAM 114)")
    
    members = [
        ("RAMRUP SATPATI", "24f3004027@ds.study.iitm.ac.in", "PROJECT COORDINATOR & TEAM LEAD", True),
        ("RISHABH BARTHWAL", "23f2004000@ds.study.iitm.ac.in", "Core Member • Qualitative Systems Research", False),
        ("SAMYABRATA ROY", "24f2000000@ds.study.iitm.ac.in", "Core Member • Industry Data & Interview Analysis", False),
        ("ABIR SAHA", "24f3000000@ds.study.iitm.ac.in", "Core Member • Systems Archetype Modeling", False),
        ("PIYUSH TILOKCHANDANI", "23f3000000@ds.study.iitm.ac.in", "Core Member • Literature Synthesis & Reporting", False)
    ]
    m_y = b2_y + b2_h - 52
    for name, email, role, is_lead in members:
        c.setFillColor(TEXT_NAVY)
        c.setFont("Helvetica-Bold", 10.5)
        c.drawString(b1_x + 25, m_y, name)
        
        c.setFillColor(TEXT_SLATE)
        c.setFont("Helvetica", 9.5)
        c.drawString(b1_x + 210, m_y, f"[{email}]")
        
        c.setFillColor(TEXT_BLUE if is_lead else TEXT_BODY)
        c.setFont("Helvetica-Bold" if is_lead else "Helvetica", 9.5)
        c.drawString(b1_x + 480, m_y, f"—   {role}")
        m_y -= 23
        
    c.showPage()
    
    # --- Page 2 ---
    draw_tech_frame("02/05", "TRANSITION PROCESSES")
    
    intro_txt = (
        "<b>TRANSITION FRAMEWORK:</b> Defining how our team transitions from individual contributors to a unified, "
        "high-performing group by setting clear performance targets, shared learning objectives, and psychological safety."
    )
    p_intro = Paragraph(intro_txt, ParagraphStyle('Intro', fontName='Helvetica', fontSize=10, leading=14.5, textColor=TEXT_NAVY))
    draw_top_down(p_intro, 45, PAGE_HEIGHT - 76, PAGE_WIDTH - 180, 40)
    
    q_w = 340
    a_w = PAGE_WIDTH - 90 - q_w - 20
    boxes_y = 42
    boxes_h = PAGE_HEIGHT - 165
    
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.setLineWidth(1.2)
    c.roundRect(45, boxes_y, q_w, boxes_h, 6, fill=1, stroke=1)
    c.setFillColor(TEXT_BLUE)
    c.roundRect(45, boxes_y + boxes_h - 4, q_w, 4, 2, fill=1, stroke=0)
    
    c.setFillColor(TEXT_NAVY)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(65, boxes_y + boxes_h - 26, "CORE INQUIRY QUESTIONS")
    
    q2_content = (
        "<b>a. Performance Goals:</b><br/>"
        "<font color='#64748b' size='9'>What are our performance goals (grade targets, analytical depth, deliverable quality, and innovation)?</font><br/><br/>"
        "<b>b. Learning Goals:</b><br/>"
        "<font color='#64748b' size='9'>What knowledge and/or technical skill development will we focus on together?</font><br/><br/>"
        "<b>c. People Goals:</b><br/>"
        "<font color='#64748b' size='9'>What are our interpersonal goals (enjoying teamwork, psychological safety, and forming lasting professional networks)?</font>"
    )
    p_q2 = Paragraph(q2_content, ParagraphStyle('Q2', fontName='Helvetica', fontSize=10, leading=15, textColor=TEXT_NAVY))
    draw_top_down(p_q2, 65, boxes_y + boxes_h - 40, q_w - 40, boxes_h - 50)
    
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.roundRect(45 + q_w + 20, boxes_y, a_w, boxes_h, 6, fill=1, stroke=1)
    c.setFillColor(TEXT_BLUE)
    c.roundRect(45 + q_w + 20, boxes_y + boxes_h - 4, a_w, 4, 2, fill=1, stroke=0)
    
    c.setFillColor(TEXT_NAVY)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(45 + q_w + 40, boxes_y + boxes_h - 26, "TEAM ACTION PLAN & EXECUTION COMMITMENTS")
    
    a2_content = (
        "<b>a. Performance Target ('S' Grade Benchmark):</b><br/>"
        "Each member will conduct at least one in-depth qualitative interview with an industry engineering lead. "
        "Together, we target an 'S' grade (top 5%) by synthesizing findings into a rigorous systems dynamics influence model, "
        "delivering cohesive, professionally formatted GP1/GP2 reports, and producing an engaging video presentation with verified timestamps.<br/><br/>"
        "<b>b. Competency & Learning Objectives:</b><br/>"
        "We will develop hands-on expertise in Systems Thinking archetypes, qualitative interview methodology, and influence diagramming. "
        "Each member will enhance active listening, thematic coding, and the ability to connect academic theory (WEF 2025 Core Skills) "
        "to real-world organizational dynamics.<br/><br/>"
        "<b>c. People & Culture Commitments:</b><br/>"
        "We commit to building an inclusive, psychologically safe, and supportive culture where constructive debate is welcomed and all five members "
        "contribute equally. Beyond completing course milestones, we aim to build lasting professional camaraderie and network connections."
    )
    p_a2 = Paragraph(a2_content, ParagraphStyle('A2', fontName='Helvetica', fontSize=9.5, leading=14, textColor=TEXT_BODY))
    draw_top_down(p_a2, 45 + q_w + 40, boxes_y + boxes_h - 40, a_w - 40, boxes_h - 50)
    
    c.showPage()
    
    # --- Page 3 ---
    draw_tech_frame("03/05", "ACTION PROCESSES: GOVERNANCE & ROLES")
    
    boxes_h_act = PAGE_HEIGHT - 120
    boxes_y_act = 42
    
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.roundRect(45, boxes_y_act, q_w, boxes_h_act, 6, fill=1, stroke=1)
    c.setFillColor(TEXT_BLUE)
    c.roundRect(45, boxes_y_act + boxes_h_act - 4, q_w, 4, 2, fill=1, stroke=0)
    
    c.setFillColor(TEXT_NAVY)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(65, boxes_y_act + boxes_h_act - 26, "CORE INQUIRY QUESTIONS")
    
    q3_content = (
        "<b>a. How will we organise leadership for this project?</b><br/>"
        "<font color='#64748b' size='9'>(e.g. project leader, sub-group coordinators)</font><br/><br/>"
        "<b>b. What functional roles will each member play?</b><br/><br/>"
        "<b>c. How are decisions made?</b><br/>"
        "<font color='#64748b' size='9'>(e.g. consensus, majority, selected by leader)</font><br/><br/>"
        "<b>d. How will we collaborate across lifecycle stages?</b><br/>"
        "<font color='#64748b' size='9'>(e.g. work separately then pool, simultaneous work)</font><br/><br/>"
        "<b>e. What communication modes will we employ and when?</b><br/>"
        "<font color='#64748b' size='9'>(e.g. WhatsApp, email, Teams, Google Meet)</font>"
    )
    p_q3 = Paragraph(q3_content, ParagraphStyle('Q3', fontName='Helvetica', fontSize=10, leading=14, textColor=TEXT_NAVY))
    draw_top_down(p_q3, 65, boxes_y_act + boxes_h_act - 40, q_w - 40, boxes_h_act - 50)
    
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.roundRect(45 + q_w + 20, boxes_y_act, a_w, boxes_h_act, 6, fill=1, stroke=1)
    c.setFillColor(TEXT_BLUE)
    c.roundRect(45 + q_w + 20, boxes_y_act + boxes_h_act - 4, a_w, 4, 2, fill=1, stroke=0)
    
    c.setFillColor(TEXT_NAVY)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(45 + q_w + 40, boxes_y_act + boxes_h_act - 26, "OPERATIONAL ACTION PLAN & WORKFLOW PROTOCOL")
    
    a3_content = (
        "<b>a. Leadership Architecture:</b><br/>"
        "Leadership is collaborative and servant-driven. The Project Coordinator schedules meetings, tracks deadlines, and ensures compliance, "
        "while work package ownership is shared equally across all members.<br/><br/>"
        "<b>b. Functional Role Distribution:</b><br/>"
        "Each member conducts 1 external interview. Sub-roles (literature review synthesis, qualitative transcript coding, influence modeling, "
        "presentation deck curation, and APA reference formatting) are distributed by member strengths.<br/><br/>"
        "<b>c. Decision-Making Framework:</b><br/>"
        "Consensus-first via transparent discussion. If consensus is split after structured debate, decisions will be resolved "
        "by simple majority vote, with dissenting viewpoints documented for retrospective review.<br/><br/>"
        "<b>d. Phased Collaboration Lifecycle:</b><br/>"
        "Phased workflow: (1) Collaborative kickoff to align on interview protocols; (2) Autonomous execution of individual interviews and transcripts; "
        "(3) Synchronized regrouping to synthesize themes, construct the influence model, and rehearse the presentation.<br/><br/>"
        "<b>e. Multi-Channel Communication Stack:</b><br/>"
        "WhatsApp group for instant daily coordination, Google Space/Discourse for official updates, Google Drive for collaborative "
        "document drafting, and Google Meet for weekly structured milestone check-ins."
    )
    p_a3 = Paragraph(a3_content, ParagraphStyle('A3', fontName='Helvetica', fontSize=9.5, leading=13.5, textColor=TEXT_BODY))
    draw_top_down(p_a3, 45 + q_w + 40, boxes_y_act + boxes_h_act - 40, a_w - 40, boxes_h_act - 50)
    
    c.showPage()
    
    # --- Page 4 ---
    draw_tech_frame("04/05", "ACTION PROCESSES: LOGISTICS & CADENCE")
    
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.roundRect(45, boxes_y_act, q_w, boxes_h_act, 6, fill=1, stroke=1)
    c.setFillColor(TEXT_BLUE)
    c.roundRect(45, boxes_y_act + boxes_h_act - 4, q_w, 4, 2, fill=1, stroke=0)
    
    c.setFillColor(TEXT_NAVY)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(65, boxes_y_act + boxes_h_act - 26, "CORE INQUIRY QUESTIONS")
    
    q4_content = (
        "<b>f. When and where will we hold our meetings?</b><br/><br/>"
        "<b>g. How will we share workload & resolve imbalances?</b><br/>"
        "<font color='#64748b' size='9'>(quantity, quality, time)? What will we do if a member does more (or less) work than others?</font><br/><br/>"
        "<b>h. How will we share knowledge, tools & resources?</b><br/>"
        "<font color='#64748b' size='9'>(centralized shared Drive, templates, interview transcripts)</font><br/><br/>"
        "<b>i. What is our mechanism for milestone tracking?</b><br/>"
        "<font color='#64748b' size='9'>What is our process for setting internal deadlines?</font>"
    )
    p_q4 = Paragraph(q4_content, ParagraphStyle('Q4', fontName='Helvetica', fontSize=10, leading=14.5, textColor=TEXT_NAVY))
    draw_top_down(p_q4, 65, boxes_y_act + boxes_h_act - 40, q_w - 40, boxes_h_act - 50)
    
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.roundRect(45 + q_w + 20, boxes_y_act, a_w, boxes_h_act, 6, fill=1, stroke=1)
    c.setFillColor(TEXT_BLUE)
    c.roundRect(45 + q_w + 20, boxes_y_act + boxes_h_act - 4, a_w, 4, 2, fill=1, stroke=0)
    
    c.setFillColor(TEXT_NAVY)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(45 + q_w + 40, boxes_y_act + boxes_h_act - 26, "EXECUTION CADENCE & ACCOUNTABILITY PLAN")
    
    a4_content = (
        "<b>f. Meeting Cadence & Virtual Workspace:</b><br/>"
        "Weekly video meetings via Google Meet every weekend (Sunday evenings) at a mutually agreed time. "
        "Agendas are shared 24 hours in advance, and brief meeting minutes are logged in our shared Drive.<br/><br/>"
        "<b>g. Fair Workload Distribution & Rebalancing:</b><br/>"
        "Work is partitioned into clear, balanced work packages. If an individual faces unexpected academic/work constraints, "
        "workload is proactively redistributed. If a member under-contributes, the coordinator initiates a supportive 1-on-1 check-in "
        "to identify blockers before escalating.<br/><br/>"
        "<b>h. Knowledge Infrastructure & Peer Support:</b><br/>"
        "We maintain a central shared Google Drive with literature papers, interview guides, consent templates, and transcript logs. "
        "Members offer peer-feedback on draft interview questions and presentation slides.<br/><br/>"
        "<b>i. Deadline Management & Buffer Protocol:</b><br/>"
        "Progress is tracked using a live Work Breakdown Structure (WBS) sheet. Internal team deadlines are set 48 hours prior to official "
        "IITM portal deadlines to provide a comfortable buffer for peer review and formatting."
    )
    p_a4 = Paragraph(a4_content, ParagraphStyle('A4', fontName='Helvetica', fontSize=9.5, leading=14, textColor=TEXT_BODY))
    draw_top_down(p_a4, 45 + q_w + 40, boxes_y_act + boxes_h_act - 40, a_w - 40, boxes_h_act - 50)
    
    c.showPage()
    
    # --- Page 5 ---
    draw_tech_frame("05/05", "INTERPERSONAL PROCESSES: DYNAMICS & CULTURE")
    
    intro_txt5 = (
        "<b>INTERPERSONAL CULTURE:</b> Defining how our team communicates, resolves friction constructively, "
        "cultivates psychological safety, and celebrates shared accomplishments throughout the semester."
    )
    p_intro5 = Paragraph(intro_txt5, ParagraphStyle('Intro5', fontName='Helvetica', fontSize=10, leading=14.5, textColor=TEXT_NAVY))
    draw_top_down(p_intro5, 45, PAGE_HEIGHT - 76, PAGE_WIDTH - 180, 40)
    
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.roundRect(45, boxes_y, q_w, boxes_h, 6, fill=1, stroke=1)
    c.setFillColor(TEXT_BLUE)
    c.roundRect(45, boxes_y + boxes_h - 4, q_w, 4, 2, fill=1, stroke=0)
    
    c.setFillColor(TEXT_NAVY)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(65, boxes_y + boxes_h - 26, "CORE INQUIRY QUESTIONS")
    
    q5_content = (
        "<b>a. How will we manage conflict if it becomes personal and not task-related?</b><br/><br/><br/>"
        "<b>b. What specific practices will ensure our collaboration remains positive?</b><br/><br/><br/>"
        "<b>c. How will we celebrate successes & commiserate setbacks together?</b>"
    )
    p_q5 = Paragraph(q5_content, ParagraphStyle('Q5', fontName='Helvetica', fontSize=10, leading=15, textColor=TEXT_NAVY))
    draw_top_down(p_q5, 65, boxes_y + boxes_h - 40, q_w - 40, boxes_h - 50)
    
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.roundRect(45 + q_w + 20, boxes_y, a_w, boxes_h, 6, fill=1, stroke=1)
    c.setFillColor(TEXT_BLUE)
    c.roundRect(45 + q_w + 20, boxes_y + boxes_h - 4, a_w, 4, 2, fill=1, stroke=0)
    
    c.setFillColor(TEXT_NAVY)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(45 + q_w + 40, boxes_y + boxes_h - 26, "INTERPERSONAL CODE & RESOLUTION PROTOCOLS")
    
    a5_content = (
        "<b>a. Constructive Conflict Mediation Protocol:</b><br/>"
        "If interpersonal tensions arise, we will pause and address them through private, respectful 1-on-1 conversations. "
        "We practice separating personalities from ideas, focusing on shared objectives, and relying on active listening. "
        "The team coordinator steps in as an impartial mediator if consensus is delayed.<br/><br/>"
        "<b>b. Cultivating Psychological Safety & Morale:</b><br/>"
        "We foster an atmosphere of psychological safety, open encouragement, and intellectual curiosity. "
        "All members' viewpoints are actively solicited during brainstorms, ensuring an enjoyable, respectful, and equitable learning environment.<br/><br/>"
        "<b>c. Celebrating Successes & Blameless Retrospectives:</b><br/>"
        "We recognize milestone completions and individual contributions through shout-outs in our group chat. "
        "If a deliverable faces setbacks or rubric penalties, we conduct a blameless post-mortem retrospective to diagnose systemic causes and adapt."
    )
    p_a5 = Paragraph(a5_content, ParagraphStyle('A5', fontName='Helvetica', fontSize=9.5, leading=14, textColor=TEXT_BODY))
    draw_top_down(p_a5, 45 + q_w + 40, boxes_y + boxes_h - 40, a_w - 40, boxes_h - 50)
    
    c.save()
    print(f"[*] Successfully generated {pdf_filename}")

build_pptx()
build_pdf()
