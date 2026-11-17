import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_contract_pptx():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    
    blank_layout = prs.slide_layouts[6]
    
    # Palette
    COLOR_BG = RGBColor(255, 255, 255)
    COLOR_TEXT_MAIN = RGBColor(30, 41, 59)     # Slate 800
    COLOR_TEXT_MUTED = RGBColor(100, 116, 139) # Slate 500
    COLOR_PRIMARY = RGBColor(15, 23, 42)       # Slate 900
    COLOR_ACCENT = RGBColor(180, 83, 9)        # Amber 700 / Warm Gold
    CARD_BG = RGBColor(248, 250, 252)          # Slate 50
    CARD_BORDER = RGBColor(226, 232, 240)      # Slate 200
    
    def add_common_header(slide, title_text):
        # Header Badge
        badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.5), Inches(3.4), Inches(0.7))
        badge.fill.solid()
        badge.fill.fore_color.rgb = RGBColor(241, 245, 249)
        badge.line.color.rgb = RGBColor(15, 23, 42)
        badge.line.width = Pt(2.5)
        
        tf = badge.text_frame
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        p.text = title_text
        p.font.bold = True
        p.font.size = Pt(16)
        p.font.color.rgb = RGBColor(15, 23, 42)
        
        # Horizontal accent line
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(4.3), Inches(0.82), Inches(6.8), Inches(0.04))
        line.fill.solid()
        line.fill.fore_color.rgb = RGBColor(15, 23, 42)
        line.line.fill.background()
        
        # IIT Madras Logo top right
        if os.path.exists("iitm_logo.png"):
            slide.shapes.add_picture("iitm_logo.png", Inches(11.6), Inches(0.35), Inches(1.1), Inches(1.1))

    # =========================================================================
    # SLIDE 1: Team Contract Overview & Members
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    add_common_header(s1, "TEAM CONTRACT")
    
    # Purpose of Project Box
    box1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(11.7), Inches(2.1))
    box1.fill.solid()
    box1.fill.fore_color.rgb = CARD_BG
    box1.line.color.rgb = CARD_BORDER
    box1.line.width = Pt(1)
    
    tf1 = box1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = Inches(0.35)
    tf1.margin_right = Inches(0.35)
    tf1.margin_top = Inches(0.2)
    
    p = tf1.paragraphs[0]
    p.text = "• Purpose of the Project"
    p.font.bold = True
    p.font.size = Pt(17)
    p.font.color.rgb = COLOR_PRIMARY
    p.space_after = Pt(8)
    
    p_desc = tf1.add_paragraph()
    p_desc.text = (
        "This project investigates how Systems Thinking principles (Course Week 10) and Engineering Sense (Week 11) "
        "can diagnose and mitigate organizational bottlenecks, technical debt accumulation, and cognitive burnout in "
        "high-velocity technical teams. Anchored in systems archetypes ('Fixes that Fail', 'Shifting the Burden') and the "
        "WEF Future of Jobs 2025 Skills Outlook (Cognitive Skills: Analytical & Systems Thinking), our objective is to map an "
        "actionable influence model identifying high-leverage intervention points for sustainable organizational performance."
    )
    p_desc.font.size = Pt(12)
    p_desc.font.color.rgb = COLOR_TEXT_MAIN
    
    # Team Details Box
    box2 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(3.9), Inches(11.7), Inches(3.0))
    box2.fill.solid()
    box2.fill.fore_color.rgb = CARD_BG
    box2.line.color.rgb = CARD_BORDER
    box2.line.width = Pt(1)
    
    tf2 = box2.text_frame
    tf2.word_wrap = True
    tf2.margin_left = Inches(0.35)
    tf2.margin_top = Inches(0.2)
    
    p2 = tf2.paragraphs[0]
    p2.text = "• Team Details (Team 114)"
    p2.font.bold = True
    p2.font.size = Pt(17)
    p2.font.color.rgb = COLOR_PRIMARY
    p2.space_after = Pt(10)
    
    members = [
        ("RAMRUP SATPATI", "24f3004027@ds.study.iitm.ac.in", "(TEAM LEADER / COORDINATOR)"),
        ("RISHABH BARTHWAL", "23f2004000@ds.study.iitm.ac.in", "(Core Team Member)"),
        ("SAMYABRATA ROY", "24f2000000@ds.study.iitm.ac.in", "(Core Team Member)"),
        ("ABIR SAHA", "24f3000000@ds.study.iitm.ac.in", "(Core Team Member)"),
        ("PIYUSH TILOKCHANDANI", "23f3000000@ds.study.iitm.ac.in", "(Core Team Member)")
    ]
    
    for name, email, role in members:
        pm = tf2.add_paragraph()
        r_n = pm.add_run()
        r_n.text = f"{name} "
        r_n.font.bold = True
        r_n.font.size = Pt(12)
        r_n.font.color.rgb = COLOR_PRIMARY
        
        r_e = pm.add_run()
        r_e.text = f"({email})  "
        r_e.font.size = Pt(11)
        r_e.font.color.rgb = COLOR_TEXT_MUTED
        
        r_r = pm.add_run()
        r_r.text = f"{role}"
        r_r.font.bold = True
        r_r.font.size = Pt(11)
        r_r.font.color.rgb = COLOR_ACCENT if "LEADER" in role else COLOR_TEXT_MUTED
        pm.space_after = Pt(3)

    # =========================================================================
    # SLIDE 2: Transition Processes
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_common_header(s2, "TRANSITION PROCESSES")
    
    # Intro Banner
    intro2 = s2.shapes.add_textbox(Inches(0.8), Inches(1.3), Inches(11.7), Inches(0.65))
    tf_i2 = intro2.text_frame
    tf_i2.word_wrap = True
    p = tf_i2.paragraphs[0]
    p.text = (
        "The transition process defines how our team of five moves from individual contributors to a unified, "
        "goal-driven group. It involves setting clear performance goals, identifying learning objectives, and building psychological safety."
    )
    p.font.size = Pt(12)
    p.font.color.rgb = COLOR_TEXT_MAIN
    
    # Left Box: Questions
    q_box2 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.1), Inches(4.3), Inches(4.9))
    q_box2.fill.solid()
    q_box2.fill.fore_color.rgb = CARD_BG
    q_box2.line.color.rgb = CARD_BORDER
    
    tf_q2 = q_box2.text_frame
    tf_q2.word_wrap = True
    tf_q2.margin_left = Inches(0.25)
    tf_q2.margin_top = Inches(0.2)
    
    p = tf_q2.paragraphs[0]
    p.text = "Suggested Questions"
    p.font.bold = True
    p.font.size = Pt(15)
    p.font.color.rgb = COLOR_PRIMARY
    p.space_after = Pt(12)
    
    q2_items = [
        ("a. What are our performance goals?", "(e.g., grade, innovation, depth, quality of deliverables)?"),
        ("b. What are our learning goals?", "What knowledge and/or skill development will we focus on together?"),
        ("c. What are our people goals?", "(e.g., enjoying teamwork, psychological safety, forming lasting professional connections)?")
    ]
    for q_t, q_d in q2_items:
        p_qt = tf_q2.add_paragraph()
        p_qt.text = q_t
        p_qt.font.bold = True
        p_qt.font.size = Pt(11.5)
        p_qt.font.color.rgb = COLOR_PRIMARY
        
        p_qd = tf_q2.add_paragraph()
        p_qd.text = q_d
        p_qd.font.size = Pt(10)
        p_qd.font.color.rgb = COLOR_TEXT_MUTED
        p_qd.space_after = Pt(14)
        
    # Right Box: Action Plan
    a_box2 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.3), Inches(2.1), Inches(7.2), Inches(4.9))
    a_box2.fill.solid()
    a_box2.fill.fore_color.rgb = CARD_BG
    a_box2.line.color.rgb = CARD_BORDER
    
    tf_a2 = a_box2.text_frame
    tf_a2.word_wrap = True
    tf_a2.margin_left = Inches(0.3)
    tf_a2.margin_top = Inches(0.2)
    
    p = tf_a2.paragraphs[0]
    p.text = "Team Action Plan"
    p.font.bold = True
    p.font.size = Pt(15)
    p.font.color.rgb = COLOR_ACCENT
    p.space_after = Pt(10)
    
    a2_items = [
        ("a. Performance Goals:", 
         "Each member will conduct at least one in-depth qualitative interview with an industry engineering/tech lead. "
         "Together, we target an 'S' grade by synthesizing findings into a rigorous systems dynamics influence model, "
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
        p_at = tf_a2.add_paragraph()
        p_at.text = at
        p_at.font.bold = True
        p_at.font.size = Pt(12)
        p_at.font.color.rgb = COLOR_PRIMARY
        
        p_ad = tf_a2.add_paragraph()
        p_ad.text = ad
        p_ad.font.size = Pt(10.5)
        p_ad.font.color.rgb = COLOR_TEXT_MAIN
        p_ad.space_after = Pt(8)

    # =========================================================================
    # SLIDE 3: Action Processes (Part 1)
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_common_header(s3, "ACTION PROCESSES (1/2)")
    
    # Left Box: Questions
    q_box3 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(4.3), Inches(5.5))
    q_box3.fill.solid()
    q_box3.fill.fore_color.rgb = CARD_BG
    q_box3.line.color.rgb = CARD_BORDER
    
    tf_q3 = q_box3.text_frame
    tf_q3.word_wrap = True
    tf_q3.margin_left = Inches(0.25)
    tf_q3.margin_top = Inches(0.18)
    
    p = tf_q3.paragraphs[0]
    p.text = "Suggested Questions"
    p.font.bold = True
    p.font.size = Pt(15)
    p.font.color.rgb = COLOR_PRIMARY
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
        pq.font.size = Pt(11)
        pq.font.color.rgb = COLOR_PRIMARY
        pq.space_after = Pt(14)
        
    # Right Box: Action Plan
    a_box3 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.3), Inches(1.5), Inches(7.2), Inches(5.5))
    a_box3.fill.solid()
    a_box3.fill.fore_color.rgb = CARD_BG
    a_box3.line.color.rgb = CARD_BORDER
    
    tf_a3 = a_box3.text_frame
    tf_a3.word_wrap = True
    tf_a3.margin_left = Inches(0.3)
    tf_a3.margin_top = Inches(0.18)
    
    p = tf_a3.paragraphs[0]
    p.text = "Team Action Plan"
    p.font.bold = True
    p.font.size = Pt(15)
    p.font.color.rgb = COLOR_ACCENT
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
        p_at = tf_a3.add_paragraph()
        p_at.text = at
        p_at.font.bold = True
        p_at.font.size = Pt(11.5)
        p_at.font.color.rgb = COLOR_PRIMARY
        
        p_ad = tf_a3.add_paragraph()
        p_ad.text = ad
        p_ad.font.size = Pt(10)
        p_ad.font.color.rgb = COLOR_TEXT_MAIN
        p_ad.space_after = Pt(6)

    # =========================================================================
    # SLIDE 4: Action Processes (Part 2)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_common_header(s4, "ACTION PROCESSES (2/2)")
    
    # Left Box: Questions
    q_box4 = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(4.3), Inches(5.5))
    q_box4.fill.solid()
    q_box4.fill.fore_color.rgb = CARD_BG
    q_box4.line.color.rgb = CARD_BORDER
    
    tf_q4 = q_box4.text_frame
    tf_q4.word_wrap = True
    tf_q4.margin_left = Inches(0.25)
    tf_q4.margin_top = Inches(0.18)
    
    p = tf_q4.paragraphs[0]
    p.text = "Suggested Questions"
    p.font.bold = True
    p.font.size = Pt(15)
    p.font.color.rgb = COLOR_PRIMARY
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
        pq.font.size = Pt(11)
        pq.font.color.rgb = COLOR_PRIMARY
        pq.space_after = Pt(18)
        
    # Right Box: Action Plan
    a_box4 = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.3), Inches(1.5), Inches(7.2), Inches(5.5))
    a_box4.fill.solid()
    a_box4.fill.fore_color.rgb = CARD_BG
    a_box4.line.color.rgb = CARD_BORDER
    
    tf_a4 = a_box4.text_frame
    tf_a4.word_wrap = True
    tf_a4.margin_left = Inches(0.3)
    tf_a4.margin_top = Inches(0.18)
    
    p = tf_a4.paragraphs[0]
    p.text = "Team Action Plan"
    p.font.bold = True
    p.font.size = Pt(15)
    p.font.color.rgb = COLOR_ACCENT
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
        p_at = tf_a4.add_paragraph()
        p_at.text = at
        p_at.font.bold = True
        p_at.font.size = Pt(11.5)
        p_at.font.color.rgb = COLOR_PRIMARY
        
        p_ad = tf_a4.add_paragraph()
        p_ad.text = ad
        p_ad.font.size = Pt(10)
        p_ad.font.color.rgb = COLOR_TEXT_MAIN
        p_ad.space_after = Pt(8)

    # =========================================================================
    # SLIDE 5: Interpersonal Processes
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_common_header(s5, "INTERPERSONAL PROCESSES")
    
    intro5 = s5.shapes.add_textbox(Inches(0.8), Inches(1.3), Inches(11.7), Inches(0.65))
    tf_i5 = intro5.text_frame
    tf_i5.word_wrap = True
    p = tf_i5.paragraphs[0]
    p.text = (
        "Interpersonal processes define how our team connects, communicates, and navigates interpersonal challenges. "
        "They focus on building mutual trust, resolving friction constructively, supporting one another, and celebrating shared achievements."
    )
    p.font.size = Pt(12)
    p.font.color.rgb = COLOR_TEXT_MAIN
    
    # Left Box: Questions
    q_box5 = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.1), Inches(4.3), Inches(4.9))
    q_box5.fill.solid()
    q_box5.fill.fore_color.rgb = CARD_BG
    q_box5.line.color.rgb = CARD_BORDER
    
    tf_q5 = q_box5.text_frame
    tf_q5.word_wrap = True
    tf_q5.margin_left = Inches(0.25)
    tf_q5.margin_top = Inches(0.2)
    
    p = tf_q5.paragraphs[0]
    p.text = "Suggested Questions"
    p.font.bold = True
    p.font.size = Pt(15)
    p.font.color.rgb = COLOR_PRIMARY
    p.space_after = Pt(12)
    
    q5_items = [
        ("a. How will we manage conflict if it becomes personal and not task related?", ""),
        ("b. What will we do to make the experience of working together a positive one?", ""),
        ("c. How will we celebrate successes & commiserate goals we do not meet?", "")
    ]
    for q_t, _ in q5_items:
        p_qt = tf_q5.add_paragraph()
        p_qt.text = q_t
        p_qt.font.bold = True
        p_qt.font.size = Pt(11.5)
        p_qt.font.color.rgb = COLOR_PRIMARY
        p_qt.space_after = Pt(20)
        
    # Right Box: Action Plan
    a_box5 = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.3), Inches(2.1), Inches(7.2), Inches(4.9))
    a_box5.fill.solid()
    a_box5.fill.fore_color.rgb = CARD_BG
    a_box5.line.color.rgb = CARD_BORDER
    
    tf_a5 = a_box5.text_frame
    tf_a5.word_wrap = True
    tf_a5.margin_left = Inches(0.3)
    tf_a5.margin_top = Inches(0.2)
    
    p = tf_a5.paragraphs[0]
    p.text = "Team Action Plan"
    p.font.bold = True
    p.font.size = Pt(15)
    p.font.color.rgb = COLOR_ACCENT
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
        p_at = tf_a5.add_paragraph()
        p_at.text = at
        p_at.font.bold = True
        p_at.font.size = Pt(12)
        p_at.font.color.rgb = COLOR_PRIMARY
        
        p_ad = tf_a5.add_paragraph()
        p_ad.text = ad
        p_ad.font.size = Pt(10.5)
        p_ad.font.color.rgb = COLOR_TEXT_MAIN
        p_ad.space_after = Pt(10)
        
    pptx_filename = "Team_114_SPG_TC_Sep_2026.pptx"
    prs.save(pptx_filename)
    print(f"[*] Successfully created {pptx_filename}")

create_contract_pptx()
