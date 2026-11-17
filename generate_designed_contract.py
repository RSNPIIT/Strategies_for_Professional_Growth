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
# 1. GENERATE POWERPOINT (PPTX)
# =============================================================================
def build_pptx():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]
    
    C_PRIMARY = RGBColor(15, 23, 42)       # Slate 900
    C_CORAL = RGBColor(217, 119, 87)       # Warm Coral #d97757
    C_BODY = RGBColor(30, 41, 59)          # Slate 800
    C_MUTED = RGBColor(100, 116, 139)      # Slate 500
    CARD_BG = RGBColor(253, 250, 248)      # Warm tint
    CARD_BORDER = RGBColor(226, 217, 209)  # Soft warm border
    
    def add_slide_decorations(slide, title_text, cat_peering=True):
        # Coral Leaves Top-Left
        if os.path.exists("coral_leaves_tl.png"):
            slide.shapes.add_picture("coral_leaves_tl.png", Inches(-0.2), Inches(-0.2), Inches(2.2), Inches(3.6))
        
        # Coral Leaves Bottom-Right
        if os.path.exists("coral_leaves_br.png"):
            slide.shapes.add_picture("coral_leaves_br.png", Inches(11.3), Inches(4.0), Inches(2.2), Inches(3.7))
            
        # Black Peering Cat (if enabled)
        if cat_peering and os.path.exists("cat_peering_trans.png"):
            slide.shapes.add_picture("cat_peering_trans.png", Inches(8.3), Inches(0.2), Inches(1.0), Inches(0.65))
            
        # Horizontal Connecting Line
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(4.3), Inches(0.88), Inches(6.9), Inches(0.04))
        line.fill.solid()
        line.fill.fore_color.rgb = C_PRIMARY
        line.line.fill.background()
        
        # Badge Drop Shadow
        shd = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.15), Inches(0.55), Inches(3.4), Inches(0.72))
        shd.fill.solid()
        shd.fill.fore_color.rgb = RGBColor(0, 0, 0)
        shd.line.fill.background()
        
        # Header Badge
        badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.08), Inches(0.48), Inches(3.4), Inches(0.72))
        badge.fill.solid()
        badge.fill.fore_color.rgb = RGBColor(255, 255, 255)
        badge.line.color.rgb = C_PRIMARY
        badge.line.width = Pt(2.5)
        
        tf = badge.text_frame
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        p.text = title_text
        p.font.bold = True
        p.font.size = Pt(15)
        p.font.color.rgb = C_PRIMARY
        
        # IIT Madras Logo top right - BIGGER & PROMINENT
        if os.path.exists("iitm_logo_clean.png"):
            slide.shapes.add_picture("iitm_logo_clean.png", Inches(11.65), Inches(0.28), Inches(1.35), Inches(1.35))

    # --- Slide 1 ---
    s1 = prs.slides.add_slide(blank_layout)
    add_slide_decorations(s1, "TEAM CONTRACT", cat_peering=False)
    
    # Purpose of Project Box
    b1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.1), Inches(1.65), Inches(10.8), Inches(2.1))
    b1.fill.solid()
    b1.fill.fore_color.rgb = CARD_BG
    b1.line.color.rgb = CARD_BORDER
    b1.line.width = Pt(1.2)
    
    tf1 = b1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = Inches(0.35)
    tf1.margin_top = Inches(0.2)
    
    p = tf1.paragraphs[0]
    p.text = "• Purpose of the Project"
    p.font.bold = True
    p.font.size = Pt(17)
    p.font.color.rgb = C_PRIMARY
    p.space_after = Pt(8)
    
    if os.path.exists("cat_q_trans.png"):
        s1.shapes.add_picture("cat_q_trans.png", Inches(4.3), Inches(1.72), Inches(0.65), Inches(0.6))
        
    p_desc = tf1.add_paragraph()
    p_desc.text = (
        "This project investigates how Systems Thinking principles (Course Week 10) and Engineering Sense (Week 11) "
        "can diagnose and mitigate organizational bottlenecks, technical debt accumulation, and cognitive burnout in "
        "high-velocity technical teams. Anchored in systems archetypes ('Fixes that Fail', 'Shifting the Burden') and the "
        "WEF Future of Jobs 2025 Skills Outlook (Cognitive Skills: Analytical & Systems Thinking), our objective is to map an "
        "actionable influence model identifying high-leverage intervention points for sustainable, high-velocity engineering teams."
    )
    p_desc.font.size = Pt(12)
    p_desc.font.color.rgb = C_BODY
    
    # Team Details Box
    b2 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.1), Inches(3.95), Inches(10.8), Inches(3.0))
    b2.fill.solid()
    b2.fill.fore_color.rgb = CARD_BG
    b2.line.color.rgb = CARD_BORDER
    b2.line.width = Pt(1.2)
    
    tf2 = b2.text_frame
    tf2.word_wrap = True
    tf2.margin_left = Inches(0.35)
    tf2.margin_top = Inches(0.2)
    
    p2 = tf2.paragraphs[0]
    p2.text = "• Team Details (Team 114)"
    p2.font.bold = True
    p2.font.size = Pt(17)
    p2.font.color.rgb = C_PRIMARY
    p2.space_after = Pt(10)
    
    if os.path.exists("cat_team_trans.png"):
        s1.shapes.add_picture("cat_team_trans.png", Inches(4.5), Inches(4.0), Inches(0.8), Inches(0.65))
        
    members = [
        ("RAMRUP SATPATI", "24f3004027@ds.study.iitm.ac.in", "(TEAM LEADER / COORDINATOR)"),
        ("RISHABH BARTHWAL", "23f2004000@ds.study.iitm.ac.in", "(Core Team Member)"),
        ("SAMYABRATA ROY", "24f2000000@ds.study.iitm.ac.in", "(Core Team Member)"),
        ("ABIR SAHA", "24f3000000@ds.study.iitm.ac.in", "(Core Team Member)"),
        ("PIYUSH TILOKCHANDANI", "23f3000000@ds.study.iitm.ac.in", "(Core Team Member)")
    ]
    for name, email, role in members:
        pm = tf2.add_paragraph()
        r1 = pm.add_run()
        r1.text = f"{name} "
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = C_PRIMARY
        
        r2 = pm.add_run()
        r2.text = f"({email})   "
        r2.font.size = Pt(11)
        r2.font.color.rgb = C_MUTED
        
        r3 = pm.add_run()
        r3.text = f"{role}"
        r3.font.bold = True
        r3.font.size = Pt(11)
        r3.font.color.rgb = C_CORAL if "LEADER" in role else C_MUTED
        pm.space_after = Pt(3)

    # --- Slide 2 ---
    s2 = prs.slides.add_slide(blank_layout)
    add_slide_decorations(s2, "TRANSITION PROCESSES")
    
    if os.path.exists("cat_reading_trans.png"):
        s2.shapes.add_picture("cat_reading_trans.png", Inches(0.3), Inches(5.6), Inches(1.3), Inches(1.5))
        
    # Intro
    intro2 = s2.shapes.add_textbox(Inches(1.1), Inches(1.35), Inches(10.8), Inches(0.65))
    tf_i2 = intro2.text_frame
    tf_i2.word_wrap = True
    p = tf_i2.paragraphs[0]
    p.text = (
        "The transition process defines how our team of five moves from individual contributors to a unified, "
        "goal-driven group. It involves setting clear performance goals, identifying learning objectives, and building psychological safety."
    )
    p.font.size = Pt(11.5)
    p.font.color.rgb = C_BODY
    
    # Left box Q
    q_b2 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.1), Inches(2.1), Inches(3.9), Inches(4.9))
    q_b2.fill.solid()
    q_b2.fill.fore_color.rgb = CARD_BG
    q_b2.line.color.rgb = CARD_BORDER
    tf_q2 = q_b2.text_frame
    tf_q2.word_wrap = True
    tf_q2.margin_left = Inches(0.25)
    tf_q2.margin_top = Inches(0.2)
    p = tf_q2.paragraphs[0]
    p.text = "Suggested Questions"
    p.font.bold = True
    p.font.size = Pt(15)
    p.font.color.rgb = C_PRIMARY
    p.space_after = Pt(12)
    
    q2_items = [
        ("a. What are our performance goals?", "(e.g., grade, innovation, depth, quality of deliverables)?"),
        ("b. What are our learning goals?", "What knowledge and/or skill development will we focus on together?"),
        ("c. What are our people goals?", "(e.g., enjoying teamwork, psychological safety, forming lasting professional connections)?")
    ]
    for qt, qd in q2_items:
        pq = tf_q2.add_paragraph()
        pq.text = qt
        pq.font.bold = True
        pq.font.size = Pt(11)
        pq.font.color.rgb = C_PRIMARY
        
        pqd = tf_q2.add_paragraph()
        pqd.text = qd
        pqd.font.size = Pt(9.5)
        pqd.font.color.rgb = C_MUTED
        pqd.space_after = Pt(14)
        
    # Right box A
    a_b2 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.2), Inches(2.1), Inches(6.7), Inches(4.9))
    a_b2.fill.solid()
    a_b2.fill.fore_color.rgb = CARD_BG
    a_b2.line.color.rgb = CARD_BORDER
    tf_a2 = a_b2.text_frame
    tf_a2.word_wrap = True
    tf_a2.margin_left = Inches(0.3)
    tf_a2.margin_top = Inches(0.2)
    p = tf_a2.paragraphs[0]
    p.text = "Team Action Plan"
    p.font.bold = True
    p.font.size = Pt(15)
    p.font.color.rgb = C_CORAL
    p.space_after = Pt(10)
    
    a2_items = [
        ("a. Performance Goals:", 
         "Each member will conduct at least one in-depth qualitative interview with an industry engineering/tech lead. "
         "Together, we target an 'S' grade (top 5%) by synthesizing findings into a rigorous systems dynamics influence model, "
         "delivering well-structured GP1/GP2 reports, and producing an engaging video presentation with verified timestamps."),
        ("b. Learning Goals:",
         "We will develop hands-on expertise in Systems Thinking archetypes, qualitative interview methodology, and influence diagramming. "
         "Each member will enhance active listening, thematic analysis, and the ability to connect academic theory (WEF 2025 Core Skills) "
         "to real-world organizational dynamics."),
        ("c. People Goals:",
         "We commit to building an inclusive, psychologically safe, and supportive culture where constructive debate is welcomed and all five members "
         "contribute equally. Beyond completing course milestones, we aim to build lasting professional camaraderie.")
    ]
    for at, ad in a2_items:
        pa = tf_a2.add_paragraph()
        pa.text = at
        pa.font.bold = True
        pa.font.size = Pt(11.5)
        pa.font.color.rgb = C_PRIMARY
        
        pad = tf_a2.add_paragraph()
        pad.text = ad
        pad.font.size = Pt(10)
        pad.font.color.rgb = C_BODY
        pad.space_after = Pt(8)

    # --- Slide 3 ---
    s3 = prs.slides.add_slide(blank_layout)
    add_slide_decorations(s3, "ACTION PROCESSES (1/2)")
    
    if os.path.exists("cat_megaphone_trans.png"):
        s3.shapes.add_picture("cat_megaphone_trans.png", Inches(0.6), Inches(1.4), Inches(0.8), Inches(0.8))
        
    q_b3 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.1), Inches(1.5), Inches(3.9), Inches(5.5))
    q_b3.fill.solid()
    q_b3.fill.fore_color.rgb = CARD_BG
    q_b3.line.color.rgb = CARD_BORDER
    tf_q3 = q_b3.text_frame
    tf_q3.word_wrap = True
    tf_q3.margin_left = Inches(0.25)
    tf_q3.margin_top = Inches(0.18)
    p = tf_q3.paragraphs[0]
    p.text = "Suggested Questions"
    p.font.bold = True
    p.font.size = Pt(15)
    p.font.color.rgb = C_PRIMARY
    p.space_after = Pt(10)
    
    q3_items = [
        "a. How will we organise leadership for this project?",
        "b. What roles would the other members play?",
        "c. How are decisions made (e.g. consensus, majority, selected by leader)?",
        "d. How will we work together at different stages of the project?",
        "e. What communication mode will we use and when?"
    ]
    for q_item in q3_items:
        pq = tf_q3.add_paragraph()
        pq.text = q_item
        pq.font.bold = True
        pq.font.size = Pt(10.5)
        pq.font.color.rgb = C_PRIMARY
        pq.space_after = Pt(14)
        
    a_b3 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.2), Inches(1.5), Inches(6.7), Inches(5.5))
    a_b3.fill.solid()
    a_b3.fill.fore_color.rgb = CARD_BG
    a_b3.line.color.rgb = CARD_BORDER
    tf_a3 = a_b3.text_frame
    tf_a3.word_wrap = True
    tf_a3.margin_left = Inches(0.3)
    tf_a3.margin_top = Inches(0.18)
    p = tf_a3.paragraphs[0]
    p.text = "Team Action Plan"
    p.font.bold = True
    p.font.size = Pt(15)
    p.font.color.rgb = C_CORAL
    p.space_after = Pt(8)
    
    a3_items = [
        ("a. Leadership:",
         "Leadership is collaborative and servant-driven. The Team Leader / Coordinator coordinates meeting schedules, "
         "tracks milestone deadlines, and ensures submission compliance, while task ownership is shared equally across all members."),
        ("b. Roles of Other Members:",
         "Every member conducts 1 external professional interview. Cross-functional roles (secondary literature synthesis, "
         "qualitative coding, influence diagram design, presentation curation, and APA reference formatting) are distributed by individual strengths."),
        ("c. Decision Making:",
         "Consensus-first via transparent discussion. If consensus cannot be reached after structured debate, decisions will be resolved "
         "by simple majority vote, with minority perspectives recorded and respected."),
        ("d. Working Together:",
         "Phased workflow: (1) Collaborative kickoff to align on interview protocols; (2) Autonomous execution of individual interviews and transcripts; "
         "(3) Synchronized regrouping to synthesize themes, construct the influence model, and rehearse the presentation."),
        ("e. Communication Mode:",
         "WhatsApp group for instant daily coordination, Google Space/Discourse for official updates, Google Drive for collaborative "
         "document drafting, and Google Meet for weekly structured milestone check-ins.")
    ]
    for at, ad in a3_items:
        pa = tf_a3.add_paragraph()
        pa.text = at
        pa.font.bold = True
        pa.font.size = Pt(11)
        pa.font.color.rgb = C_PRIMARY
        
        pad = tf_a3.add_paragraph()
        pad.text = ad
        pad.font.size = Pt(9.5)
        pad.font.color.rgb = C_BODY
        pad.space_after = Pt(6)

    # --- Slide 4 ---
    s4 = prs.slides.add_slide(blank_layout)
    add_slide_decorations(s4, "ACTION PROCESSES (2/2)")
    
    q_b4 = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.1), Inches(1.5), Inches(3.9), Inches(5.5))
    q_b4.fill.solid()
    q_b4.fill.fore_color.rgb = CARD_BG
    q_b4.line.color.rgb = CARD_BORDER
    tf_q4 = q_b4.text_frame
    tf_q4.word_wrap = True
    tf_q4.margin_left = Inches(0.25)
    tf_q4.margin_top = Inches(0.18)
    p = tf_q4.paragraphs[0]
    p.text = "Suggested Questions"
    p.font.bold = True
    p.font.size = Pt(15)
    p.font.color.rgb = C_PRIMARY
    p.space_after = Pt(12)
    
    q4_items = [
        "f. When and where will we hold our meetings?",
        "g. How will we share the workload? What will we do if a member does more (or less) work?",
        "h. How will we help team members (sharing knowledge and resources)?",
        "i. When and how will we review progress on goals? What is our process for setting deadlines?"
    ]
    for q_item in q4_items:
        pq = tf_q4.add_paragraph()
        pq.text = q_item
        pq.font.bold = True
        pq.font.size = Pt(10.5)
        pq.font.color.rgb = C_PRIMARY
        pq.space_after = Pt(18)
        
    a_b4 = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.2), Inches(1.5), Inches(6.7), Inches(5.5))
    a_b4.fill.solid()
    a_b4.fill.fore_color.rgb = CARD_BG
    a_b4.line.color.rgb = CARD_BORDER
    tf_a4 = a_b4.text_frame
    tf_a4.word_wrap = True
    tf_a4.margin_left = Inches(0.3)
    tf_a4.margin_top = Inches(0.18)
    p = tf_a4.paragraphs[0]
    p.text = "Team Action Plan"
    p.font.bold = True
    p.font.size = Pt(15)
    p.font.color.rgb = C_CORAL
    p.space_after = Pt(8)
    
    a4_items = [
        ("f. Meetings:",
         "Weekly video meetings via Google Meet every weekend (Sunday evenings) at a mutually agreed time. "
         "Agendas are shared 24 hours in advance, and brief meeting minutes are logged in our shared Drive."),
        ("g. Workload Sharing:",
         "Work is partitioned into clear, balanced work packages. If an individual faces unexpected academic/work constraints, "
         "workload is proactively redistributed. If a member under-contributes, the coordinator initiates a supportive 1-on-1 check-in "
         "to identify blockers before escalating."),
        ("h. Helping Team Members:",
         "We maintain a central shared Google Drive with literature papers, interview guides, consent templates, and transcript logs. "
         "Members offer peer-feedback on draft interview questions and presentation slides."),
        ("i. Reviewing Progress & Deadlines:",
         "Progress is tracked using a live Work Breakdown Structure (WBS) sheet. Internal team deadlines are set 48 hours prior to official "
         "IITM portal deadlines to provide a comfortable buffer for peer review and formatting.")
    ]
    for at, ad in a4_items:
        pa = tf_a4.add_paragraph()
        pa.text = at
        pa.font.bold = True
        pa.font.size = Pt(11)
        pa.font.color.rgb = C_PRIMARY
        
        pad = tf_a4.add_paragraph()
        pad.text = ad
        pad.font.size = Pt(9.5)
        pad.font.color.rgb = C_BODY
        pad.space_after = Pt(8)

    # --- Slide 5 ---
    s5 = prs.slides.add_slide(blank_layout)
    add_slide_decorations(s5, "INTERPERSONAL PROCESSES")
    
    intro5 = s5.shapes.add_textbox(Inches(1.1), Inches(1.35), Inches(10.8), Inches(0.65))
    tf_i5 = intro5.text_frame
    tf_i5.word_wrap = True
    p = tf_i5.paragraphs[0]
    p.text = (
        "Interpersonal processes define how our team connects, communicates, and navigates interpersonal challenges. "
        "They focus on building mutual trust, resolving friction constructively, supporting one another, and celebrating shared achievements."
    )
    p.font.size = Pt(11.5)
    p.font.color.rgb = C_BODY
    
    q_b5 = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.1), Inches(2.1), Inches(3.9), Inches(4.9))
    q_b5.fill.solid()
    q_b5.fill.fore_color.rgb = CARD_BG
    q_b5.line.color.rgb = CARD_BORDER
    tf_q5 = q_b5.text_frame
    tf_q5.word_wrap = True
    tf_q5.margin_left = Inches(0.25)
    tf_q5.margin_top = Inches(0.2)
    p = tf_q5.paragraphs[0]
    p.text = "Suggested Questions"
    p.font.bold = True
    p.font.size = Pt(15)
    p.font.color.rgb = C_PRIMARY
    p.space_after = Pt(12)
    
    q5_items = [
        "a. How will we manage conflict if it becomes personal and not task related?",
        "b. What will we do to make the experience of working together a positive one?",
        "c. How will we celebrate successes & commiserate goals we do not meet?"
    ]
    for q_item in q5_items:
        pq = tf_q5.add_paragraph()
        pq.text = q_item
        pq.font.bold = True
        pq.font.size = Pt(11)
        pq.font.color.rgb = C_PRIMARY
        pq.space_after = Pt(20)
        
    a_b5 = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.2), Inches(2.1), Inches(6.7), Inches(4.9))
    a_b5.fill.solid()
    a_b5.fill.fore_color.rgb = CARD_BG
    a_b5.line.color.rgb = CARD_BORDER
    tf_a5 = a_b5.text_frame
    tf_a5.word_wrap = True
    tf_a5.margin_left = Inches(0.3)
    tf_a5.margin_top = Inches(0.2)
    p = tf_a5.paragraphs[0]
    p.text = "Team Action Plan"
    p.font.bold = True
    p.font.size = Pt(15)
    p.font.color.rgb = C_CORAL
    p.space_after = Pt(10)
    
    a5_items = [
        ("a. Conflict Management:",
         "If interpersonal tensions arise, we will pause and address them through private, respectful 1-on-1 conversations. "
         "We practice separating personalities from ideas, focusing on shared objectives, and relying on active listening. "
         "The team coordinator steps in as an impartial mediator if consensus is delayed."),
        ("b. Fostering a Positive Experience:",
         "We foster an atmosphere of psychological safety, open encouragement, and intellectual curiosity. "
         "All members' viewpoints are actively solicited during brainstorms, ensuring an enjoyable, respectful, and equitable learning environment."),
        ("c. Celebrating Successes & Continuous Learning:",
         "We recognize milestone completions and individual contributions through shout-outs in our group chat. "
         "If a deliverable faces setbacks or rubric penalties, we conduct a blameless post-mortem retrospective to diagnose systemic causes and adapt.")
    ]
    for at, ad in a5_items:
        pa = tf_a5.add_paragraph()
        pa.text = at
        pa.font.bold = True
        pa.font.size = Pt(11.5)
        pa.font.color.rgb = C_PRIMARY
        
        pad = tf_a5.add_paragraph()
        pad.text = ad
        pad.font.size = Pt(10)
        pad.font.color.rgb = C_BODY
        pad.space_after = Pt(10)
        
    prs.save("Team_114_SPG_TC_Sep_2026.pptx")
    print("[*] Successfully updated Team_114_SPG_TC_Sep_2026.pptx")

# =============================================================================
# 2. GENERATE VECTOR PDF WITH REPORTLAB
# =============================================================================
def build_pdf():
    pdf_filename = "Team_114_SPG_TC_Sep_2026.pdf"
    PAGE_WIDTH = 960
    PAGE_HEIGHT = 540
    
    c = canvas.Canvas(pdf_filename, pagesize=(PAGE_WIDTH, PAGE_HEIGHT))
    
    BG_CREAM = HexColor("#fdfbf9")
    TEXT_PRIMARY = HexColor("#0f172a") # Slate 900
    TEXT_MUTED = HexColor("#64748b")   # Slate 500
    TEXT_BODY = HexColor("#1e293b")    # Slate 800
    ACCENT_CORAL = HexColor("#d97757") # Warm Coral
    CARD_BG = HexColor("#ffffff")      # Clean white card
    CARD_BORDER = HexColor("#e2d8ce")  # Warm soft border
    LINE_DARK = HexColor("#0f172a")
    
    def draw_common_header(title_text, show_peering_cat=True):
        # Background fill
        c.setFillColor(BG_CREAM)
        c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)
        
        # Coral Leaves Top-Left
        if os.path.exists("coral_leaves_tl.png"):
            c.drawImage("coral_leaves_tl.png", -10, PAGE_HEIGHT - 260, width=155, height=270, mask='auto')
            
        # Coral Leaves Bottom-Right
        if os.path.exists("coral_leaves_br.png"):
            c.drawImage("coral_leaves_br.png", PAGE_WIDTH - 155, -10, width=155, height=270, mask='auto')
            
        # Peering Cat behind header
        if show_peering_cat and os.path.exists("cat_peering_trans.png"):
            c.drawImage("cat_peering_trans.png", PAGE_WIDTH - 350, PAGE_HEIGHT - 65, width=65, height=45, mask='auto')
            
        # Horizontal connecting line
        badge_x = 55
        badge_y = PAGE_HEIGHT - 62
        badge_w = 265
        badge_h = 42
        
        c.setStrokeColor(LINE_DARK)
        c.setLineWidth(2)
        c.line(badge_x + badge_w + 10, badge_y + 21, PAGE_WIDTH - 145, badge_y + 21)
        
        # Header Badge Drop Shadow
        c.setFillColor(LINE_DARK)
        c.roundRect(badge_x + 5, badge_y - 5, badge_w, badge_h, 8, fill=1, stroke=0)
        
        # Header Badge White Pill
        c.setFillColor(HexColor("#ffffff"))
        c.setStrokeColor(LINE_DARK)
        c.setLineWidth(2.5)
        c.roundRect(badge_x, badge_y, badge_w, badge_h, 8, fill=1, stroke=1)
        
        c.setFillColor(TEXT_PRIMARY)
        c.setFont("Helvetica-Bold", 13.5)
        c.drawCentredString(badge_x + badge_w / 2, badge_y + 13, title_text)
        
        # IIT Madras Logo top right - BIGGER & CRISP (92x92)
        if os.path.exists("iitm_logo_clean.png"):
            c.drawImage("iitm_logo_clean.png", PAGE_WIDTH - 130, PAGE_HEIGHT - 95, width=92, height=92, mask='auto')

    def draw_top_down(p, x, top_y, max_w, max_h):
        w, h = p.wrapOn(c, max_w, max_h)
        p.drawOn(c, x, top_y - h)
        return h

    # --- Page 1 ---
    draw_common_header("TEAM CONTRACT", show_peering_cat=False)
    
    b1_x = 55
    b1_y = PAGE_HEIGHT - 220
    b1_w = PAGE_WIDTH - 110
    b1_h = 135
    
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.setLineWidth(1.2)
    c.roundRect(b1_x, b1_y, b1_w, b1_h, 8, fill=1, stroke=1)
    
    c.setFillColor(TEXT_PRIMARY)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(b1_x + 20, b1_y + b1_h - 26, "•  Purpose of the Project")
    
    if os.path.exists("cat_q_trans.png"):
        c.drawImage("cat_q_trans.png", b1_x + 210, b1_y + b1_h - 38, width=42, height=38, mask='auto')
        
    purpose_html = (
        "This project investigates how <b>Systems Thinking principles (Course Week 10)</b> and <b>Engineering Sense (Week 11)</b> "
        "can diagnose and mitigate organizational bottlenecks, technical debt accumulation, and cognitive burnout in "
        "high-velocity technical teams. Anchored in systems archetypes (<i>'Fixes that Fail'</i>, <i>'Shifting the Burden'</i>) and the "
        "<b>WEF Future of Jobs 2025 Skills Outlook (Cognitive Skills: Analytical & Systems Thinking)</b>, our objective is to map an "
        "actionable causal influence model identifying high-leverage intervention points for sustainable, high-velocity engineering teams."
    )
    style_p = ParagraphStyle('PurposeStyle', fontName='Helvetica', fontSize=10.5, leading=16, textColor=TEXT_BODY)
    p_obj = Paragraph(purpose_html, style_p)
    draw_top_down(p_obj, b1_x + 20, b1_y + b1_h - 40, b1_w - 40, b1_h - 45)
    
    # Team Details Box
    b2_y = 35
    b2_h = b1_y - b2_y - 20
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.roundRect(b1_x, b2_y, b1_w, b2_h, 8, fill=1, stroke=1)
    
    c.setFillColor(TEXT_PRIMARY)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(b1_x + 20, b2_y + b2_h - 26, "•  Team Details (Team 114)")
    
    if os.path.exists("cat_team_trans.png"):
        c.drawImage("cat_team_trans.png", b1_x + 225, b2_y + b2_h - 42, width=54, height=44, mask='auto')
        
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
        
        c.setFillColor(ACCENT_CORAL if "LEADER" in role else TEXT_MUTED)
        c.setFont("Helvetica-Bold" if "LEADER" in role else "Helvetica", 10)
        c.drawString(b1_x + 475, m_y, role)
        m_y -= 23
        
    c.showPage()
    
    # --- Page 2 ---
    draw_common_header("TRANSITION PROCESSES")
    
    if os.path.exists("cat_reading_trans.png"):
        c.drawImage("cat_reading_trans.png", 10, 15, width=95, height=110, mask='auto')
        
    intro_txt = (
        "The transition process defines how our team of five moves from individual contributors to a unified, "
        "goal-driven group. It involves setting clear performance goals, identifying learning objectives, and building psychological safety."
    )
    p_intro = Paragraph(intro_txt, ParagraphStyle('Intro', fontName='Helvetica', fontSize=10.5, leading=15, textColor=TEXT_BODY))
    draw_top_down(p_intro, 55, PAGE_HEIGHT - 80, PAGE_WIDTH - 190, 40)
    
    q_w = 320
    a_w = PAGE_WIDTH - 110 - q_w - 20
    boxes_y = 35
    boxes_h = PAGE_HEIGHT - 160
    
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.roundRect(55, boxes_y, q_w, boxes_h, 8, fill=1, stroke=1)
    
    c.setFillColor(TEXT_PRIMARY)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(70, boxes_y + boxes_h - 26, "Suggested Questions")
    
    q2_content = (
        "<b>a. What are our performance goals?</b><br/>"
        "<font color='#64748b' size='9'>(e.g. grade target, depth, innovation, quality of work)</font><br/><br/>"
        "<b>b. What are our learning goals?</b><br/>"
        "<font color='#64748b' size='9'>What knowledge and/or skill development will we focus on together?</font><br/><br/>"
        "<b>c. What are our people goals?</b><br/>"
        "<font color='#64748b' size='9'>(e.g. enjoying teamwork, psychological safety, forming lasting professional colleagues)</font>"
    )
    p_q2 = Paragraph(q2_content, ParagraphStyle('Q2', fontName='Helvetica', fontSize=10.5, leading=15, textColor=TEXT_PRIMARY))
    draw_top_down(p_q2, 70, boxes_y + boxes_h - 40, q_w - 30, boxes_h - 50)
    
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.roundRect(55 + q_w + 20, boxes_y, a_w, boxes_h, 8, fill=1, stroke=1)
    
    c.setFillColor(ACCENT_CORAL)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(55 + q_w + 40, boxes_y + boxes_h - 26, "Team Action Plan")
    
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
    draw_top_down(p_a2, 55 + q_w + 40, boxes_y + boxes_h - 40, a_w - 40, boxes_h - 50)
    
    c.showPage()
    
    # --- Page 3 ---
    draw_common_header("ACTION PROCESSES (1/2)")
    
    if os.path.exists("cat_megaphone_trans.png"):
        c.drawImage("cat_megaphone_trans.png", 20, PAGE_HEIGHT - 125, width=50, height=50, mask='auto')
        
    boxes_h_act = PAGE_HEIGHT - 110
    boxes_y_act = 35
    
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.roundRect(55, boxes_y_act, q_w, boxes_h_act, 8, fill=1, stroke=1)
    
    c.setFillColor(TEXT_PRIMARY)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(70, boxes_y_act + boxes_h_act - 26, "Suggested Questions")
    
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
    draw_top_down(p_q3, 70, boxes_y_act + boxes_h_act - 40, q_w - 30, boxes_h_act - 50)
    
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.roundRect(55 + q_w + 20, boxes_y_act, a_w, boxes_h_act, 8, fill=1, stroke=1)
    
    c.setFillColor(ACCENT_CORAL)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(55 + q_w + 40, boxes_y_act + boxes_h_act - 26, "Team Action Plan")
    
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
    draw_top_down(p_a3, 55 + q_w + 40, boxes_y_act + boxes_h_act - 40, a_w - 40, boxes_h_act - 50)
    
    c.showPage()
    
    # --- Page 4 ---
    draw_common_header("ACTION PROCESSES (2/2)")
    
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.roundRect(55, boxes_y_act, q_w, boxes_h_act, 8, fill=1, stroke=1)
    
    c.setFillColor(TEXT_PRIMARY)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(70, boxes_y_act + boxes_h_act - 26, "Suggested Questions")
    
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
    draw_top_down(p_q4, 70, boxes_y_act + boxes_h_act - 40, q_w - 30, boxes_h_act - 50)
    
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.roundRect(55 + q_w + 20, boxes_y_act, a_w, boxes_h_act, 8, fill=1, stroke=1)
    
    c.setFillColor(ACCENT_CORAL)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(55 + q_w + 40, boxes_y_act + boxes_h_act - 26, "Team Action Plan")
    
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
    draw_top_down(p_a4, 55 + q_w + 40, boxes_y_act + boxes_h_act - 40, a_w - 40, boxes_h_act - 50)
    
    c.showPage()
    
    # --- Page 5 ---
    draw_common_header("INTERPERSONAL PROCESSES")
    
    intro_txt5 = (
        "Interpersonal processes define how our team connects, communicates, and navigates interpersonal challenges. "
        "They focus on building mutual trust, resolving friction constructively, supporting one another, and celebrating shared achievements."
    )
    p_intro5 = Paragraph(intro_txt5, ParagraphStyle('Intro5', fontName='Helvetica', fontSize=10.5, leading=15, textColor=TEXT_BODY))
    draw_top_down(p_intro5, 55, PAGE_HEIGHT - 80, PAGE_WIDTH - 190, 40)
    
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.roundRect(55, boxes_y, q_w, boxes_h, 8, fill=1, stroke=1)
    
    c.setFillColor(TEXT_PRIMARY)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(70, boxes_y + boxes_h - 26, "Suggested Questions")
    
    q5_content = (
        "<b>a. How will we manage conflict if it becomes personal and not task related?</b><br/><br/><br/>"
        "<b>b. What will we do to make the experience of working together a positive one?</b><br/><br/><br/>"
        "<b>c. How will we celebrate successes & commiserate goals we do not meet?</b>"
    )
    p_q5 = Paragraph(q5_content, ParagraphStyle('Q5', fontName='Helvetica', fontSize=10.5, leading=15, textColor=TEXT_PRIMARY))
    draw_top_down(p_q5, 70, boxes_y + boxes_h - 40, q_w - 30, boxes_h - 50)
    
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.roundRect(55 + q_w + 20, boxes_y, a_w, boxes_h, 8, fill=1, stroke=1)
    
    c.setFillColor(ACCENT_CORAL)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(55 + q_w + 40, boxes_y + boxes_h - 26, "Team Action Plan")
    
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
    draw_top_down(p_a5, 55 + q_w + 40, boxes_y + boxes_h - 40, a_w - 40, boxes_h - 50)
    
    c.save()
    print(f"[*] Successfully regenerated {pdf_filename}")

build_pptx()
build_pdf()
