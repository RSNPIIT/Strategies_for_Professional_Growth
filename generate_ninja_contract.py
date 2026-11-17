import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.xmlchemy import OxmlElement

from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph

# Helper to disable spell-check squiggles in PowerPoint
def disable_spellcheck(run):
    rPr = run._r.get_or_add_rPr()
    rPr.set('noProof', '1')

# =============================================================================
# 1. POWERPOINT PRESENTATION (NINJA AESTHETIC)
# =============================================================================
def build_pptx():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]
    
    # Palette: Sleek Stealth / Steel Ninja Theme
    # Deep midnight canvas or crisp dark slate
    C_BG = RGBColor(245, 247, 250)          # Clean cool slate background
    C_STEEL_DARK = RGBColor(17, 24, 39)     # Deep obsidian/steel 900
    C_ACCENT_BLUE = RGBColor(30, 64, 175)   # Deep Blue 700
    C_TEXT = RGBColor(31, 41, 55)           # Gray 800
    C_MUTED = RGBColor(107, 114, 128)       # Gray 500
    C_CARD_BG = RGBColor(255, 255, 255)     # Crisp White
    C_BORDER = RGBColor(209, 213, 219)      # Gray 300
    
    def add_ninja_frame(slide, title_text, left_star="ninja_star_4pt.png", right_star="ninja_star_curved.png"):
        # Side Ninja Stars (Sleek corner watermark accents)
        if os.path.exists(left_star):
            slide.shapes.add_picture(left_star, Inches(0.2), Inches(0.2), Inches(1.2), Inches(1.2))
            
        if os.path.exists(right_star):
            slide.shapes.add_picture(right_star, Inches(11.9), Inches(5.9), Inches(1.3), Inches(1.3))
            
        # Top Header Title
        t_box = slide.shapes.add_textbox(Inches(1.5), Inches(0.35), Inches(8.5), Inches(0.85))
        tf_t = t_box.text_frame
        p_t = tf_t.paragraphs[0]
        r = p_t.add_run()
        r.text = title_text
        r.font.bold = True
        r.font.size = Pt(24)
        r.font.color.rgb = C_STEEL_DARK
        disable_spellcheck(r)
        
        # Sleek metallic divider line
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.5), Inches(1.15), Inches(9.5), Inches(0.04))
        line.fill.solid()
        line.fill.fore_color.rgb = C_STEEL_DARK
        line.line.fill.background()
        
        # IIT Madras Logo top right - PROMINENT & SHARP
        if os.path.exists("iitm_logo_clean.png"):
            slide.shapes.add_picture("iitm_logo_clean.png", Inches(11.6), Inches(0.25), Inches(1.35), Inches(1.35))
            
        # Bottom discreet footer line
        f_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.5), Inches(7.05), Inches(10.3), Inches(0.02))
        f_line.fill.solid()
        f_line.fill.fore_color.rgb = C_BORDER
        f_line.line.fill.background()
        
        f_box = slide.shapes.add_textbox(Inches(1.5), Inches(7.1), Inches(10.3), Inches(0.3))
        pf = f_box.text_frame.paragraphs[0]
        rf = pf.add_run()
        rf.text = "Strategies for Professional Growth (BSGN3001)  •  Team 114  •  Systems Thinking & Engineering Sense"
        rf.font.size = Pt(9.5)
        rf.font.color.rgb = C_MUTED
        disable_spellcheck(rf)

    # --- Slide 1: Mission & Team Structure ---
    s1 = prs.slides.add_slide(blank_layout)
    add_ninja_frame(s1, "TEAM CONTRACT", left_star="ninja_star_4pt.png", right_star="ninja_star_curved.png")
    
    # Purpose Box
    b1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(1.45), Inches(10.3), Inches(2.3))
    b1.fill.solid()
    b1.fill.fore_color.rgb = C_CARD_BG
    b1.line.color.rgb = C_BORDER
    b1.line.width = Pt(1.5)
    
    tf1 = b1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = Inches(0.4)
    tf1.margin_top = Inches(0.25)
    
    p = tf1.paragraphs[0]
    r = p.add_run()
    r.text = "Purpose of the Project"
    r.font.bold = True
    r.font.size = Pt(16)
    r.font.color.rgb = C_STEEL_DARK
    disable_spellcheck(r)
    p.space_after = Pt(8)
    
    p_desc = tf1.add_paragraph()
    r = p_desc.add_run()
    r.text = (
        "This project investigates how Systems Thinking principles (Course Week 10) and Engineering Sense (Week 11) "
        "can diagnose and mitigate organizational bottlenecks, technical debt accumulation, and cognitive overload in "
        "high-velocity technical teams. Anchored in systems archetypes ('Fixes that Fail', 'Shifting the Burden') and the "
        "WEF Future of Jobs 2025 Skills Outlook (Cognitive Skills: Analytical & Systems Thinking), our objective is to map an "
        "actionable influence model identifying high-leverage intervention points for sustainable, high-velocity engineering organizations."
    )
    r.font.size = Pt(11.5)
    r.font.color.rgb = C_TEXT
    disable_spellcheck(r)
    
    # Team Details Box
    b2 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(4.0), Inches(10.3), Inches(2.85))
    b2.fill.solid()
    b2.fill.fore_color.rgb = C_CARD_BG
    b2.line.color.rgb = C_BORDER
    b2.line.width = Pt(1.5)
    
    tf2 = b2.text_frame
    tf2.word_wrap = True
    tf2.margin_left = Inches(0.4)
    tf2.margin_top = Inches(0.2)
    
    p2 = tf2.paragraphs[0]
    r = p2.add_run()
    r.text = "Team Details (Team 114)"
    r.font.bold = True
    r.font.size = Pt(16)
    r.font.color.rgb = C_STEEL_DARK
    disable_spellcheck(r)
    p2.space_after = Pt(10)
    
    members = [
        ("Ramrup Satpati", "24f3004027@ds.study.iitm.ac.in", "Team Leader & Project Coordinator", True),
        ("Rishabh Barthwal", "Core Team Member", "Systems Thinking Research & Synthesis", False),
        ("Samyabrata Roy", "Core Team Member", "Qualitative Industry Interviews", False),
        ("Abir Saha", "Core Team Member", "Systems Dynamic Modeling & Case Study", False),
        ("Piyush Tilokchandani", "Core Team Member", "Analysis & Presentation Curation", False)
    ]
    for name, detail, role, is_lead in members:
        pm = tf2.add_paragraph()
        r1 = pm.add_run()
        r1.text = f"{name}  "
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = C_STEEL_DARK
        disable_spellcheck(r1)
        
        r2 = pm.add_run()
        r2.text = f"({detail})   —   "
        r2.font.size = Pt(11)
        r2.font.color.rgb = C_MUTED
        disable_spellcheck(r2)
        
        r3 = pm.add_run()
        r3.text = role
        r3.font.bold = is_lead
        r3.font.size = Pt(11)
        r3.font.color.rgb = C_ACCENT_BLUE if is_lead else C_TEXT
        disable_spellcheck(r3)
        pm.space_after = Pt(3)

    # --- Slide 2: Transition Processes ---
    s2 = prs.slides.add_slide(blank_layout)
    add_ninja_frame(s2, "TRANSITION PROCESSES", left_star="ninja_star_8pt.png", right_star="ninja_star_faceted.png")
    
    intro2 = s2.shapes.add_textbox(Inches(1.5), Inches(1.3), Inches(10.3), Inches(0.6))
    p = intro2.text_frame.paragraphs[0]
    r = p.add_run()
    r.text = (
        "The transition process defines how our team moves from individual contributors to a unified, goal-driven group. "
        "It involves setting clear performance goals, identifying learning objectives, and building psychological safety."
    )
    r.font.size = Pt(11)
    r.font.color.rgb = C_TEXT
    disable_spellcheck(r)
    
    # Left Q Box
    q_b2 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(2.0), Inches(4.2), Inches(4.85))
    q_b2.fill.solid()
    q_b2.fill.fore_color.rgb = C_CARD_BG
    q_b2.line.color.rgb = C_BORDER
    q_b2.line.width = Pt(1.5)
    
    tf_q2 = q_b2.text_frame
    tf_q2.word_wrap = True
    tf_q2.margin_left = Inches(0.3)
    tf_q2.margin_top = Inches(0.2)
    p = tf_q2.paragraphs[0]
    r = p.add_run()
    r.text = "Suggested Questions"
    r.font.bold = True
    r.font.size = Pt(15)
    r.font.color.rgb = C_STEEL_DARK
    disable_spellcheck(r)
    p.space_after = Pt(12)
    
    q2_items = [
        ("a. Performance Goals", "What are our performance goals (e.g. grade targets, analytical depth, deliverable quality, and innovation)?"),
        ("b. Learning Goals", "What knowledge and/or technical skill development will we focus on together?"),
        ("c. People Goals", "What are our interpersonal goals (e.g. enjoying teamwork, psychological safety, and forming lasting professional networks)?")
    ]
    for qt, qd in q2_items:
        pq = tf_q2.add_paragraph()
        r = pq.add_run()
        r.text = qt
        r.font.bold = True
        r.font.size = Pt(11.5)
        r.font.color.rgb = C_STEEL_DARK
        disable_spellcheck(r)
        
        pqd = tf_q2.add_paragraph()
        r = pqd.add_run()
        r.text = qd
        r.font.size = Pt(10)
        r.font.color.rgb = C_MUTED
        disable_spellcheck(r)
        pqd.space_after = Pt(14)
        
    # Right A Box
    a_b2 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.9), Inches(2.0), Inches(5.9), Inches(4.85))
    a_b2.fill.solid()
    a_b2.fill.fore_color.rgb = C_CARD_BG
    a_b2.line.color.rgb = C_BORDER
    a_b2.line.width = Pt(1.5)
    
    tf_a2 = a_b2.text_frame
    tf_a2.word_wrap = True
    tf_a2.margin_left = Inches(0.35)
    tf_a2.margin_top = Inches(0.2)
    p = tf_a2.paragraphs[0]
    r = p.add_run()
    r.text = "Team Action Plan"
    r.font.bold = True
    r.font.size = Pt(15)
    r.font.color.rgb = C_ACCENT_BLUE
    disable_spellcheck(r)
    p.space_after = Pt(10)
    
    a2_items = [
        ("a. Performance Goals:", 
         "Each member will conduct at least one in-depth qualitative interview with an industry engineering lead. "
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
        r = pa.add_run()
        r.text = at
        r.font.bold = True
        r.font.size = Pt(11)
        r.font.color.rgb = C_STEEL_DARK
        disable_spellcheck(r)
        
        pad = tf_a2.add_paragraph()
        r = pad.add_run()
        r.text = ad
        r.font.size = Pt(10)
        r.font.color.rgb = C_TEXT
        disable_spellcheck(r)
        pad.space_after = Pt(8)

    # --- Slide 3: Action Processes (1/2) ---
    s3 = prs.slides.add_slide(blank_layout)
    add_ninja_frame(s3, "ACTION PROCESSES (1/2)", left_star="ninja_star_curved.png", right_star="ninja_star_4pt.png")
    
    q_b3 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(1.4), Inches(4.2), Inches(5.4))
    q_b3.fill.solid()
    q_b3.fill.fore_color.rgb = C_CARD_BG
    q_b3.line.color.rgb = C_BORDER
    q_b3.line.width = Pt(1.5)
    tf_q3 = q_b3.text_frame
    tf_q3.word_wrap = True
    tf_q3.margin_left = Inches(0.3)
    tf_q3.margin_top = Inches(0.2)
    p = tf_q3.paragraphs[0]
    r = p.add_run()
    r.text = "Suggested Questions"
    r.font.bold = True
    r.font.size = Pt(15)
    r.font.color.rgb = C_STEEL_DARK
    disable_spellcheck(r)
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
        r = pq.add_run()
        r.text = q_item
        r.font.bold = True
        r.font.size = Pt(10.5)
        r.font.color.rgb = C_STEEL_DARK
        disable_spellcheck(r)
        pq.space_after = Pt(14)
        
    a_b3 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.9), Inches(1.4), Inches(5.9), Inches(5.4))
    a_b3.fill.solid()
    a_b3.fill.fore_color.rgb = C_CARD_BG
    a_b3.line.color.rgb = C_BORDER
    a_b3.line.width = Pt(1.5)
    tf_a3 = a_b3.text_frame
    tf_a3.word_wrap = True
    tf_a3.margin_left = Inches(0.35)
    tf_a3.margin_top = Inches(0.2)
    p = tf_a3.paragraphs[0]
    r = p.add_run()
    r.text = "Team Action Plan"
    r.font.bold = True
    r.font.size = Pt(15)
    r.font.color.rgb = C_ACCENT_BLUE
    disable_spellcheck(r)
    p.space_after = Pt(8)
    
    a3_items = [
        ("a. Leadership:",
         "Leadership is collaborative and supportive. The Project Coordinator schedules meetings, tracks milestone deadlines, "
         "and ensures submission compliance, while task ownership is shared equally across all five members."),
        ("b. Roles of Other Members:",
         "Every member conducts 1 external professional interview. Cross-functional responsibilities (literature review synthesis, "
         "qualitative transcript coding, influence diagram modeling, deck design, and APA referencing) are distributed by individual strengths."),
        ("c. Decision Making:",
         "Consensus-first via transparent discussion. If consensus cannot be reached after structured debate, decisions will be resolved "
         "by simple majority vote, with minority perspectives formally recorded and respected."),
        ("d. Working Together:",
         "Phased workflow: (1) Collaborative kickoff to align on interview protocols; (2) Autonomous execution of individual interviews and transcripts; "
         "(3) Synchronized regrouping to synthesize themes, construct the influence model, and rehearse the presentation."),
        ("e. Communication Mode:",
         "WhatsApp group for instant daily coordination, Google Space/Discourse for official updates, Google Drive for collaborative "
         "document drafting, and Google Meet for weekly structured milestone check-ins.")
    ]
    for at, ad in a3_items:
        pa = tf_a3.add_paragraph()
        r = pa.add_run()
        r.text = at
        r.font.bold = True
        r.font.size = Pt(11)
        r.font.color.rgb = C_STEEL_DARK
        disable_spellcheck(r)
        
        pad = tf_a3.add_paragraph()
        r = pad.add_run()
        r.text = ad
        r.font.size = Pt(9.5)
        r.font.color.rgb = C_TEXT
        disable_spellcheck(r)
        pad.space_after = Pt(6)

    # --- Slide 4: Action Processes (2/2) ---
    s4 = prs.slides.add_slide(blank_layout)
    add_ninja_frame(s4, "ACTION PROCESSES (2/2)", left_star="ninja_star_faceted.png", right_star="ninja_star_8pt.png")
    
    q_b4 = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(1.4), Inches(4.2), Inches(5.4))
    q_b4.fill.solid()
    q_b4.fill.fore_color.rgb = C_CARD_BG
    q_b4.line.color.rgb = C_BORDER
    q_b4.line.width = Pt(1.5)
    tf_q4 = q_b4.text_frame
    tf_q4.word_wrap = True
    tf_q4.margin_left = Inches(0.3)
    tf_q4.margin_top = Inches(0.2)
    p = tf_q4.paragraphs[0]
    r = p.add_run()
    r.text = "Suggested Questions"
    r.font.bold = True
    r.font.size = Pt(15)
    r.font.color.rgb = C_STEEL_DARK
    disable_spellcheck(r)
    p.space_after = Pt(12)
    
    q4_items = [
        "f. When and where will we hold our meetings?",
        "g. How will we share the workload? What will we do if a member does more (or less) work?",
        "h. How will we help team members (sharing knowledge and resources)?",
        "i. When and how will we review progress on goals? What is our process for setting deadlines?"
    ]
    for q_item in q4_items:
        pq = tf_q4.add_paragraph()
        r = pq.add_run()
        r.text = q_item
        r.font.bold = True
        r.font.size = Pt(10.5)
        r.font.color.rgb = C_STEEL_DARK
        disable_spellcheck(r)
        pq.space_after = Pt(18)
        
    a_b4 = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.9), Inches(1.4), Inches(5.9), Inches(5.4))
    a_b4.fill.solid()
    a_b4.fill.fore_color.rgb = C_CARD_BG
    a_b4.line.color.rgb = C_BORDER
    a_b4.line.width = Pt(1.5)
    tf_a4 = a_b4.text_frame
    tf_a4.word_wrap = True
    tf_a4.margin_left = Inches(0.35)
    tf_a4.margin_top = Inches(0.2)
    p = tf_a4.paragraphs[0]
    r = p.add_run()
    r.text = "Team Action Plan"
    r.font.bold = True
    r.font.size = Pt(15)
    r.font.color.rgb = C_ACCENT_BLUE
    disable_spellcheck(r)
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
        r = pa.add_run()
        r.text = at
        r.font.bold = True
        r.font.size = Pt(11)
        r.font.color.rgb = C_STEEL_DARK
        disable_spellcheck(r)
        
        pad = tf_a4.add_paragraph()
        r = pad.add_run()
        r.text = ad
        r.font.size = Pt(9.5)
        r.font.color.rgb = C_TEXT
        disable_spellcheck(r)
        pad.space_after = Pt(8)

    # --- Slide 5: Interpersonal Processes ---
    s5 = prs.slides.add_slide(blank_layout)
    add_ninja_frame(s5, "INTERPERSONAL PROCESSES", left_star="ninja_star_4pt.png", right_star="ninja_star_curved.png")
    
    intro5 = s5.shapes.add_textbox(Inches(1.5), Inches(1.3), Inches(10.3), Inches(0.6))
    p = intro5.text_frame.paragraphs[0]
    r = p.add_run()
    r.text = (
        "Interpersonal processes define how our team connects, communicates, and navigates interpersonal challenges. "
        "They focus on building mutual trust, resolving friction constructively, supporting one another, and celebrating shared achievements."
    )
    r.font.size = Pt(11)
    r.font.color.rgb = C_TEXT
    disable_spellcheck(r)
    
    q_b5 = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(2.0), Inches(4.2), Inches(4.85))
    q_b5.fill.solid()
    q_b5.fill.fore_color.rgb = C_CARD_BG
    q_b5.line.color.rgb = C_BORDER
    q_b5.line.width = Pt(1.5)
    tf_q5 = q_b5.text_frame
    tf_q5.word_wrap = True
    tf_q5.margin_left = Inches(0.3)
    tf_q5.margin_top = Inches(0.2)
    p = tf_q5.paragraphs[0]
    r = p.add_run()
    r.text = "Suggested Questions"
    r.font.bold = True
    r.font.size = Pt(15)
    r.font.color.rgb = C_STEEL_DARK
    disable_spellcheck(r)
    p.space_after = Pt(12)
    
    q5_items = [
        "a. How will we manage conflict if it becomes personal and not task-related?",
        "b. What will we do to make the experience of working together a positive one?",
        "c. How will we celebrate successes & commiserate goals we do not meet?"
    ]
    for q_item in q5_items:
        pq = tf_q5.add_paragraph()
        r = pq.add_run()
        r.text = q_item
        r.font.bold = True
        r.font.size = Pt(11)
        r.font.color.rgb = C_STEEL_DARK
        disable_spellcheck(r)
        pq.space_after = Pt(20)
        
    a_b5 = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.9), Inches(2.0), Inches(5.9), Inches(4.85))
    a_b5.fill.solid()
    a_b5.fill.fore_color.rgb = C_CARD_BG
    a_b5.line.color.rgb = C_BORDER
    a_b5.line.width = Pt(1.5)
    tf_a5 = a_b5.text_frame
    tf_a5.word_wrap = True
    tf_a5.margin_left = Inches(0.35)
    tf_a5.margin_top = Inches(0.2)
    p = tf_a5.paragraphs[0]
    r = p.add_run()
    r.text = "Team Action Plan"
    r.font.bold = True
    r.font.size = Pt(15)
    r.font.color.rgb = C_ACCENT_BLUE
    disable_spellcheck(r)
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
        r = pa.add_run()
        r.text = at
        r.font.bold = True
        r.font.size = Pt(11)
        r.font.color.rgb = C_STEEL_DARK
        disable_spellcheck(r)
        
        pad = tf_a5.add_paragraph()
        r = pad.add_run()
        r.text = ad
        r.font.size = Pt(10)
        r.font.color.rgb = C_TEXT
        disable_spellcheck(r)
        pad.space_after = Pt(10)
        
    prs.save("Team_114_SPG_TC_Sep_2026.pptx")
    print("[*] Successfully saved ninja PowerPoint: Team_114_SPG_TC_Sep_2026.pptx")

# =============================================================================
# 2. VECTOR PDF (NINJA AESTHETIC - REPORTLAB)
# =============================================================================
def build_pdf():
    pdf_filename = "Team_114_SPG_TC_Sep_2026.pdf"
    PAGE_WIDTH = 960
    PAGE_HEIGHT = 540
    
    c = canvas.Canvas(pdf_filename, pagesize=(PAGE_WIDTH, PAGE_HEIGHT))
    
    BG_COOL = HexColor("#f8fafc")       # Slate 50
    CARD_BG = HexColor("#ffffff")       # Pure White
    CARD_BORDER = HexColor("#cbd5e1")   # Slate 300
    TEXT_STEEL = HexColor("#111827")    # Deep Gray 900
    TEXT_ACCENT = HexColor("#1e40af")   # Deep Blue 800
    TEXT_MUTED = HexColor("#6b7280")    # Gray 500
    TEXT_BODY = HexColor("#374151")     # Gray 700
    LINE_BORDER = HexColor("#111827")   # Deep steel line
    
    def draw_top_down(p, x, top_y, max_w, max_h):
        w, h = p.wrapOn(c, max_w, max_h)
        p.drawOn(c, x, top_y - h)
        return h

    def draw_ninja_page_frame(title_text, left_star="ninja_star_4pt.png", right_star="ninja_star_curved.png"):
        # Canvas background
        c.setFillColor(BG_COOL)
        c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)
        
        # Ninja Star Watermarks on sides/corners
        if os.path.exists(left_star):
            c.drawImage(left_star, 15, PAGE_HEIGHT - 95, width=75, height=75, mask='auto')
            
        if os.path.exists(right_star):
            c.drawImage(right_star, PAGE_WIDTH - 85, 15, width=70, height=70, mask='auto')
            
        # Top Header Title
        c.setFillColor(TEXT_STEEL)
        c.setFont("Helvetica-Bold", 19)
        c.drawString(105, PAGE_HEIGHT - 55, title_text)
        
        # Sleek steel divider line
        c.setStrokeColor(LINE_BORDER)
        c.setLineWidth(2)
        c.line(105, PAGE_HEIGHT - 66, PAGE_WIDTH - 120, PAGE_HEIGHT - 66)
        
        # IIT Madras Logo top right - PROMINENT & HIGH RES
        if os.path.exists("iitm_logo_clean.png"):
            c.drawImage("iitm_logo_clean.png", PAGE_WIDTH - 105, PAGE_HEIGHT - 78, width=75, height=75, mask='auto')
            
        # Subtle Bottom status bar
        c.setStrokeColor(HexColor("#e2e8f0"))
        c.setLineWidth(1)
        c.line(105, 24, PAGE_WIDTH - 105, 24)
        
        c.setFillColor(TEXT_MUTED)
        c.setFont("Helvetica", 8)
        c.drawString(105, 12, "Strategies for Professional Growth (BSGN3001)  •  Team 114  •  Systems Thinking & Engineering Sense")
        c.drawRightString(PAGE_WIDTH - 105, 12, "GP1 Deliverable 1.c")

    # --- Page 1 ---
    draw_ninja_page_frame("TEAM CONTRACT", left_star="ninja_star_4pt.png", right_star="ninja_star_curved.png")
    
    b1_x = 105
    b1_y = PAGE_HEIGHT - 215
    b1_w = PAGE_WIDTH - 210
    b1_h = 135
    
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.setLineWidth(1.2)
    c.roundRect(b1_x, b1_y, b1_w, b1_h, 8, fill=1, stroke=1)
    
    c.setFillColor(TEXT_STEEL)
    c.setFont("Helvetica-Bold", 12.5)
    c.drawString(b1_x + 20, b1_y + b1_h - 26, "Purpose of the Project")
    
    purpose_html = (
        "This project investigates how <b>Systems Thinking principles (Course Week 10)</b> and <b>Engineering Sense (Week 11)</b> "
        "can diagnose and mitigate organizational bottlenecks, technical debt accumulation, and cognitive overload in "
        "high-velocity technical teams. Anchored in systems archetypes (<i>'Fixes that Fail'</i>, <i>'Shifting the Burden'</i>) and the "
        "<b>WEF Future of Jobs 2025 Skills Outlook (Cognitive Skills: Analytical & Systems Thinking)</b>, our objective is to map an "
        "actionable causal influence model identifying high-leverage intervention points for sustainable, high-velocity engineering organizations."
    )
    style_p = ParagraphStyle('P1', fontName='Helvetica', fontSize=10, leading=15.5, textColor=TEXT_BODY)
    draw_top_down(Paragraph(purpose_html, style_p), b1_x + 20, b1_y + b1_h - 38, b1_w - 40, b1_h - 45)
    
    # Team Details Box
    b2_y = 38
    b2_h = b1_y - b2_y - 18
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.roundRect(b1_x, b2_y, b1_w, b2_h, 8, fill=1, stroke=1)
    
    c.setFillColor(TEXT_STEEL)
    c.setFont("Helvetica-Bold", 12.5)
    c.drawString(b1_x + 20, b2_y + b2_h - 26, "Team Details (Team 114)")
    
    members = [
        ("Ramrup Satpati", "24f3004027@ds.study.iitm.ac.in", "Team Leader & Project Coordinator", True),
        ("Rishabh Barthwal", "Core Team Member", "Systems Thinking Research & Synthesis", False),
        ("Samyabrata Roy", "Core Team Member", "Qualitative Industry Interviews", False),
        ("Abir Saha", "Core Team Member", "Systems Dynamic Modeling & Case Study", False),
        ("Piyush Tilokchandani", "Core Team Member", "Analysis & Presentation Curation", False)
    ]
    m_y = b2_y + b2_h - 52
    for name, detail, role, is_lead in members:
        c.setFillColor(TEXT_STEEL)
        c.setFont("Helvetica-Bold", 10.5)
        c.drawString(b1_x + 25, m_y, name)
        
        c.setFillColor(TEXT_MUTED)
        c.setFont("Helvetica", 9.5)
        c.drawString(b1_x + 195, m_y, f"({detail})")
        
        c.setFillColor(TEXT_ACCENT if is_lead else TEXT_BODY)
        c.setFont("Helvetica-Bold" if is_lead else "Helvetica", 9.5)
        c.drawString(b1_x + 460, m_y, f"—   {role}")
        m_y -= 23
        
    c.showPage()
    
    # --- Page 2 ---
    draw_ninja_page_frame("TRANSITION PROCESSES", left_star="ninja_star_8pt.png", right_star="ninja_star_faceted.png")
    
    intro_txt = (
        "The transition process defines how our team moves from individual contributors to a unified, goal-driven group. "
        "It involves setting clear performance goals, identifying learning objectives, and building psychological safety."
    )
    p_intro = Paragraph(intro_txt, ParagraphStyle('Intro', fontName='Helvetica', fontSize=10, leading=14.5, textColor=TEXT_BODY))
    draw_top_down(p_intro, 105, PAGE_HEIGHT - 76, PAGE_WIDTH - 230, 40)
    
    q_w = 300
    a_w = PAGE_WIDTH - 210 - q_w - 20
    boxes_y = 38
    boxes_h = PAGE_HEIGHT - 165
    
    # Left Q Card
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.setLineWidth(1.2)
    c.roundRect(105, boxes_y, q_w, boxes_h, 8, fill=1, stroke=1)
    
    c.setFillColor(TEXT_STEEL)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(125, boxes_y + boxes_h - 26, "Suggested Questions")
    
    q2_content = (
        "<b>a. Performance Goals:</b><br/>"
        "<font color='#6b7280' size='9'>What are our performance goals (grade targets, analytical depth, deliverable quality, and innovation)?</font><br/><br/>"
        "<b>b. Learning Goals:</b><br/>"
        "<font color='#6b7280' size='9'>What knowledge and/or technical skill development will we focus on together?</font><br/><br/>"
        "<b>c. People Goals:</b><br/>"
        "<font color='#6b7280' size='9'>What are our interpersonal goals (enjoying teamwork, psychological safety, and forming lasting professional networks)?</font>"
    )
    p_q2 = Paragraph(q2_content, ParagraphStyle('Q2', fontName='Helvetica', fontSize=10, leading=15, textColor=TEXT_STEEL))
    draw_top_down(p_q2, 125, boxes_y + boxes_h - 40, q_w - 35, boxes_h - 50)
    
    # Right A Card
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.roundRect(105 + q_w + 20, boxes_y, a_w, boxes_h, 8, fill=1, stroke=1)
    
    c.setFillColor(TEXT_ACCENT)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(105 + q_w + 40, boxes_y + boxes_h - 26, "Team Action Plan")
    
    a2_content = (
        "<b>a. Performance Goals:</b><br/>"
        "Each member will conduct at least one in-depth qualitative interview with an industry engineering lead. "
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
    p_a2 = Paragraph(a2_content, ParagraphStyle('A2', fontName='Helvetica', fontSize=9.5, leading=14, textColor=TEXT_BODY))
    draw_top_down(p_a2, 105 + q_w + 40, boxes_y + boxes_h - 40, a_w - 40, boxes_h - 50)
    
    c.showPage()
    
    # --- Page 3 ---
    draw_ninja_page_frame("ACTION PROCESSES (1/2)", left_star="ninja_star_curved.png", right_star="ninja_star_4pt.png")
    
    boxes_h_act = PAGE_HEIGHT - 120
    boxes_y_act = 38
    
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.roundRect(105, boxes_y_act, q_w, boxes_h_act, 8, fill=1, stroke=1)
    
    c.setFillColor(TEXT_STEEL)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(125, boxes_y_act + boxes_h_act - 26, "Suggested Questions")
    
    q3_content = (
        "<b>a. How will we organise leadership for this project?</b><br/>"
        "<font color='#6b7280' size='9'>(e.g. project leader, sub-group coordinators)</font><br/><br/>"
        "<b>b. What functional roles will each member play?</b><br/><br/>"
        "<b>c. How are decisions made?</b><br/>"
        "<font color='#6b7280' size='9'>(e.g. consensus, majority, selected by leader)</font><br/><br/>"
        "<b>d. How will we collaborate across lifecycle stages?</b><br/>"
        "<font color='#6b7280' size='9'>(e.g. work separately then pool, simultaneous work)</font><br/><br/>"
        "<b>e. What communication modes will we employ and when?</b><br/>"
        "<font color='#6b7280' size='9'>(e.g. WhatsApp, email, Teams, Google Meet)</font>"
    )
    p_q3 = Paragraph(q3_content, ParagraphStyle('Q3', fontName='Helvetica', fontSize=10, leading=14, textColor=TEXT_STEEL))
    draw_top_down(p_q3, 125, boxes_y_act + boxes_h_act - 40, q_w - 35, boxes_h_act - 50)
    
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.roundRect(105 + q_w + 20, boxes_y_act, a_w, boxes_h_act, 8, fill=1, stroke=1)
    
    c.setFillColor(TEXT_ACCENT)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(105 + q_w + 40, boxes_y_act + boxes_h_act - 26, "Team Action Plan")
    
    a3_content = (
        "<b>a. Leadership:</b><br/>"
        "Leadership is collaborative and supportive. The Project Coordinator schedules meetings, tracks milestone deadlines, "
        "and ensures submission compliance, while task ownership is shared equally across all five members.<br/><br/>"
        "<b>b. Roles of Other Members:</b><br/>"
        "Every member conducts 1 external professional interview. Cross-functional responsibilities (literature review synthesis, "
        "qualitative transcript coding, influence diagram modeling, deck design, and APA referencing) are distributed by individual strengths.<br/><br/>"
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
    draw_top_down(p_a3, 105 + q_w + 40, boxes_y_act + boxes_h_act - 40, a_w - 40, boxes_h_act - 50)
    
    c.showPage()
    
    # --- Page 4 ---
    draw_ninja_page_frame("ACTION PROCESSES (2/2)", left_star="ninja_star_faceted.png", right_star="ninja_star_8pt.png")
    
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.roundRect(105, boxes_y_act, q_w, boxes_h_act, 8, fill=1, stroke=1)
    
    c.setFillColor(TEXT_STEEL)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(125, boxes_y_act + boxes_h_act - 26, "Suggested Questions")
    
    q4_content = (
        "<b>f. When and where will we hold our meetings?</b><br/><br/>"
        "<b>g. How will we share workload & resolve imbalances?</b><br/>"
        "<font color='#6b7280' size='9'>(quantity, quality, time)? What will we do if a member does more (or less) work than others?</font><br/><br/>"
        "<b>h. How will we share knowledge, tools & resources?</b><br/>"
        "<font color='#6b7280' size='9'>(centralized shared Drive, templates, interview transcripts)</font><br/><br/>"
        "<b>i. What is our mechanism for milestone tracking?</b><br/>"
        "<font color='#6b7280' size='9'>What is our process for setting internal deadlines?</font>"
    )
    p_q4 = Paragraph(q4_content, ParagraphStyle('Q4', fontName='Helvetica', fontSize=10, leading=14.5, textColor=TEXT_STEEL))
    draw_top_down(p_q4, 125, boxes_y_act + boxes_h_act - 40, q_w - 35, boxes_h_act - 50)
    
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.roundRect(105 + q_w + 20, boxes_y_act, a_w, boxes_h_act, 8, fill=1, stroke=1)
    
    c.setFillColor(TEXT_ACCENT)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(105 + q_w + 40, boxes_y_act + boxes_h_act - 26, "Team Action Plan")
    
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
    draw_top_down(p_a4, 105 + q_w + 40, boxes_y_act + boxes_h_act - 40, a_w - 40, boxes_h_act - 50)
    
    c.showPage()
    
    # --- Page 5 ---
    draw_ninja_page_frame("INTERPERSONAL PROCESSES", left_star="ninja_star_4pt.png", right_star="ninja_star_curved.png")
    
    intro_txt5 = (
        "Interpersonal processes define how our team connects, communicates, and navigates interpersonal challenges. "
        "They focus on building mutual trust, resolving friction constructively, supporting one another, and celebrating shared achievements."
    )
    p_intro5 = Paragraph(intro_txt5, ParagraphStyle('Intro5', fontName='Helvetica', fontSize=10, leading=14.5, textColor=TEXT_BODY))
    draw_top_down(p_intro5, 105, PAGE_HEIGHT - 76, PAGE_WIDTH - 230, 40)
    
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.roundRect(105, boxes_y, q_w, boxes_h, 8, fill=1, stroke=1)
    
    c.setFillColor(TEXT_STEEL)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(125, boxes_y + boxes_h - 26, "Suggested Questions")
    
    q5_content = (
        "<b>a. How will we manage conflict if it becomes personal and not task-related?</b><br/><br/><br/>"
        "<b>b. What will we do to make the experience of working together a positive one?</b><br/><br/><br/>"
        "<b>c. How will we celebrate successes & commiserate goals we do not meet?</b>"
    )
    p_q5 = Paragraph(q5_content, ParagraphStyle('Q5', fontName='Helvetica', fontSize=10, leading=15, textColor=TEXT_STEEL))
    draw_top_down(p_q5, 125, boxes_y + boxes_h - 40, q_w - 35, boxes_h - 50)
    
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.roundRect(105 + q_w + 20, boxes_y, a_w, boxes_h, 8, fill=1, stroke=1)
    
    c.setFillColor(TEXT_ACCENT)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(105 + q_w + 40, boxes_y + boxes_h - 26, "Team Action Plan")
    
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
    p_a5 = Paragraph(a5_content, ParagraphStyle('A5', fontName='Helvetica', fontSize=9.5, leading=14, textColor=TEXT_BODY))
    draw_top_down(p_a5, 105 + q_w + 40, boxes_y + boxes_h - 40, a_w - 40, boxes_h - 50)
    
    c.save()
    print(f"[*] Successfully generated ninja PDF: {pdf_filename}")

build_pptx()
build_pdf()
