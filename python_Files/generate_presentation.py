import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_pptx():
    prs = Presentation()
    # Set 16:9 Widescreen dimensions
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    
    blank_slide_layout = prs.slide_layouts[6]
    
    # Color palette
    BG_DARK = RGBColor(18, 20, 24)       # Deep charcoal background #121418
    HEADER_BG = RGBColor(38, 42, 50)     # Header bar #262a32
    CARD_BG = RGBColor(28, 32, 40)       # Card background #1c2028
    CARD_BORDER = RGBColor(55, 65, 81)   # Border #374151
    ACCENT_GOLD = RGBColor(230, 165, 50) # Photo frame gold #e6a532
    TEXT_WHITE = RGBColor(255, 255, 255)
    TEXT_MUTED = RGBColor(180, 190, 205)
    LINK_BLUE = RGBColor(96, 165, 250)   # #60a5fa
    
    def add_header(slide):
        # Header background banner
        hdr = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.85))
        hdr.fill.solid()
        hdr.fill.fore_color.rgb = HEADER_BG
        hdr.line.color.rgb = HEADER_BG
        
        # Left header text (Name & Roll)
        tx_box = slide.shapes.add_textbox(Inches(0.6), Inches(0.12), Inches(6.0), Inches(0.6))
        tf = tx_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        r1 = p.add_run()
        r1.text = "Ramrup Satpati"
        r1.font.bold = True
        r1.font.size = Pt(20)
        r1.font.color.rgb = TEXT_WHITE
        
        r2 = p.add_run()
        r2.text = "   |   Roll No: 24f3004027"
        r2.font.size = Pt(16)
        r2.font.color.rgb = TEXT_MUTED
        
        # Right header text (Type & Clickable link)
        tx_box_r = slide.shapes.add_textbox(Inches(8.0), Inches(0.12), Inches(4.7), Inches(0.6))
        tf_r = tx_box_r.text_frame
        p_r = tf_r.paragraphs[0]
        p_r.alignment = PP_ALIGN.RIGHT
        
        r3 = p_r.add_run()
        r3.text = "Type: ENFJ-A   |   "
        r3.font.bold = True
        r3.font.size = Pt(18)
        r3.font.color.rgb = TEXT_WHITE
        
        r4 = p_r.add_run()
        r4.text = "Test Result"
        r4.font.bold = True
        r4.font.size = Pt(18)
        r4.font.color.rgb = LINK_BLUE
        r4.font.underline = True
        r4.hyperlink.address = "https://www.16personalities.com/enfj-personality"

    # =========================================================================
    # SLIDE 1: Profile & Core Traits
    # =========================================================================
    s1 = prs.slides.add_slide(blank_slide_layout)
    
    # Background fill
    bg = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = BG_DARK
    bg.line.color.rgb = BG_DARK
    
    add_header(s1)
    
    # Photo Frame (Gold border)
    gold_frame = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.6), Inches(1.2), Inches(4.3), Inches(5.7))
    gold_frame.fill.solid()
    gold_frame.fill.fore_color.rgb = RGBColor(25, 28, 35)
    gold_frame.line.color.rgb = ACCENT_GOLD
    gold_frame.line.width = Pt(3.5)
    
    # Add Profile Photo
    if os.path.exists("profile_photo_framed.png"):
        s1.shapes.add_picture("profile_photo_framed.png", Inches(0.7), Inches(1.3), Inches(4.1), Inches(5.5))
        
    # Title: Core Personality Traits
    title_box = s1.shapes.add_textbox(Inches(5.4), Inches(1.15), Inches(7.3), Inches(0.6))
    p = title_box.text_frame.paragraphs[0]
    p.text = "CORE PERSONALITY TRAITS"
    p.font.bold = True
    p.font.size = Pt(24)
    p.font.color.rgb = TEXT_WHITE
    
    # 5 Trait Bars
    traits = [
        ("Extraverted", "67%", "Introverted", RGBColor(56, 189, 248), 0.67),   # Cyan
        ("Intuitive", "72%", "Observant", RGBColor(245, 158, 11), 0.72),     # Amber
        ("Feeling", "68%", "Thinking", RGBColor(16, 185, 129), 0.68),        # Emerald
        ("Judging", "74%", "Prospecting", RGBColor(168, 85, 247), 0.74),     # Purple
        ("Assertive", "78%", "Turbulent", RGBColor(244, 63, 94), 0.78)       # Rose/Coral
    ]
    
    y_start = 1.85
    for left_label, pct_str, right_label, color, frac in traits:
        # Labels
        tb = s1.shapes.add_textbox(Inches(5.4), Inches(y_start - 0.22), Inches(7.3), Inches(0.35))
        tf = tb.text_frame
        p = tf.paragraphs[0]
        
        r_l = p.add_run()
        r_l.text = f"{pct_str} {left_label}"
        r_l.font.size = Pt(12)
        r_l.font.bold = True
        r_l.font.color.rgb = color
        
        # Spacer
        r_sp = p.add_run()
        r_sp.text = " " * 45
        
        r_r = p.add_run()
        r_r.text = right_label
        r_r.font.size = Pt(11)
        r_r.font.color.rgb = TEXT_MUTED
        
        # Base bar track (Dark gray)
        track = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.4), Inches(y_start + 0.12), Inches(7.3), Inches(0.12))
        track.fill.solid()
        track.fill.fore_color.rgb = RGBColor(45, 52, 65)
        track.line.fill.background()
        
        # Filled active bar
        fill_width = 7.3 * frac
        active_bar = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.4), Inches(y_start + 0.12), Inches(fill_width), Inches(0.12))
        active_bar.fill.solid()
        active_bar.fill.fore_color.rgb = color
        active_bar.line.fill.background()
        
        y_start += 0.68
        
    # Academic & Career Bio Box
    bio_box = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.4), Inches(5.35), Inches(7.3), Inches(1.6))
    bio_box.fill.solid()
    bio_box.fill.fore_color.rgb = CARD_BG
    bio_box.line.color.rgb = CARD_BORDER
    bio_box.line.width = Pt(1)
    
    bio_tf = bio_box.text_frame
    bio_tf.word_wrap = True
    bio_tf.margin_left = Inches(0.3)
    bio_tf.margin_right = Inches(0.3)
    bio_tf.margin_top = Inches(0.18)
    p_bio = bio_tf.paragraphs[0]
    p_bio.text = (
        "I am a student in the BS in Data Science and Applications program at IIT Madras (Roll No: 24f3004027). "
        "Having completed my Foundational and Diploma coursework, my core focus areas include Machine Learning, "
        "Deep Learning, and Generative AI architectures. As an ENFJ-A, I am passionate about bridging complex "
        "computational models with human-centered applications, combining analytical problem-solving with empathetic "
        "collaboration to drive high-impact team outcomes."
    )
    p_bio.font.size = Pt(13)
    p_bio.font.color.rgb = RGBColor(220, 225, 235)
    
    # =========================================================================
    # SLIDE 2: Team Dynamics & Personal Growth
    # =========================================================================
    s2 = prs.slides.add_slide(blank_slide_layout)
    bg2 = s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg2.fill.solid()
    bg2.fill.fore_color.rgb = BG_DARK
    bg2.line.color.rgb = BG_DARK
    
    add_header(s2)
    
    # Left Column: Heading & Narrative Reflection
    l_box = s2.shapes.add_textbox(Inches(0.6), Inches(1.15), Inches(5.8), Inches(4.5))
    l_tf = l_box.text_frame
    l_tf.word_wrap = True
    
    p1 = l_tf.paragraphs[0]
    p1.text = "NAVIGATING TEAM DYNAMICS AND PERSONAL GROWTH"
    p1.font.bold = True
    p1.font.size = Pt(22)
    p1.font.color.rgb = TEXT_WHITE
    p1.space_after = Pt(16)
    
    p2 = l_tf.add_paragraph()
    p2.text = (
        "As an ENFJ-A (Protagonist), my approach to teamwork is anchored in empathetic leadership, "
        "collective alignment, and proactive communication. I naturally gravitate towards energizing "
        "collaborative environments, unblocking bottlenecks, and ensuring every team member's input is "
        "integrated into our strategic direction.\n\n"
        "In technical projects—such as investigating Systems Thinking and organizational complexity—I actively "
        "synthesize technical depth with shared accountability. While I hold high standards for collective execution, "
        "I consciously balance my enthusiasm by practicing structured delegation, objective milestone tracking, and "
        "maintaining healthy cognitive boundaries across the team."
    )
    p2.font.size = Pt(13.5)
    p2.font.color.rgb = RGBColor(215, 222, 232)
    
    # Right Column Top Card: Relationship Dynamics
    card1 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.2), Inches(5.9), Inches(2.2))
    card1.fill.solid()
    card1.fill.fore_color.rgb = CARD_BG
    card1.line.color.rgb = CARD_BORDER
    card1.line.width = Pt(1)
    
    c1_tf = card1.text_frame
    c1_tf.word_wrap = True
    c1_tf.margin_left = Inches(0.3)
    c1_tf.margin_top = Inches(0.18)
    
    p_c1_t = c1_tf.paragraphs[0]
    p_c1_t.text = "RELATIONSHIP DYNAMICS"
    p_c1_t.font.bold = True
    p_c1_t.font.size = Pt(15)
    p_c1_t.font.color.rgb = RGBColor(96, 165, 250)
    p_c1_t.space_after = Pt(6)
    
    c1_bullets = [
        "Empathetic, clear, and articulate communicator.",
        "Proactively builds psychological safety and team trust.",
        "Naturally aligns team milestones, deliverables, and timelines.",
        "Bridges technical complexity with human perspective.",
        "Actively seeks and embraces constructive critique."
    ]
    for b in c1_bullets:
        p_b = c1_tf.add_paragraph()
        p_b.text = f"•  {b}"
        p_b.font.size = Pt(11.5)
        p_b.font.color.rgb = RGBColor(220, 225, 235)
        p_b.space_after = Pt(2)
        
    # Right Column Middle Card: Core Challenges
    card2 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(3.6), Inches(5.9), Inches(1.9))
    card2.fill.solid()
    card2.fill.fore_color.rgb = CARD_BG
    card2.line.color.rgb = CARD_BORDER
    card2.line.width = Pt(1)
    
    c2_tf = card2.text_frame
    c2_tf.word_wrap = True
    c2_tf.margin_left = Inches(0.3)
    c2_tf.margin_top = Inches(0.18)
    
    p_c2_t = c2_tf.paragraphs[0]
    p_c2_t.text = "CORE CHALLENGES"
    p_c2_t.font.bold = True
    p_c2_t.font.size = Pt(15)
    p_c2_t.font.color.rgb = RGBColor(248, 113, 113) # Coral red
    p_c2_t.space_after = Pt(6)
    
    c2_bullets = [
        "Tendency to absorb collective workload and hesitate to say no.",
        "Vulnerability to idealism when project execution hits friction.",
        "Reluctance to deliver blunt criticism out of concern for team harmony."
    ]
    for b in c2_bullets:
        p_b = c2_tf.add_paragraph()
        p_b.text = f"•  {b}"
        p_b.font.size = Pt(11.5)
        p_b.font.color.rgb = RGBColor(220, 225, 235)
        p_b.space_after = Pt(2)
        
    # Bottom Banner: Action Plan
    banner = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(5.75), Inches(12.1), Inches(1.2))
    banner.fill.solid()
    banner.fill.fore_color.rgb = RGBColor(24, 28, 36)
    banner.line.color.rgb = RGBColor(75, 85, 99)
    banner.line.width = Pt(1)
    
    # White accent indicator on left
    accent = s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.7), Inches(5.85), Inches(0.1), Inches(1.0))
    accent.fill.solid()
    accent.fill.fore_color.rgb = RGBColor(255, 255, 255)
    accent.line.fill.background()
    
    b_tf = banner.text_frame
    b_tf.word_wrap = True
    b_tf.margin_left = Inches(0.4)
    b_tf.margin_top = Inches(0.16)
    
    p_b_t = b_tf.paragraphs[0]
    p_b_t.text = "ACTION PLAN FOR PERSONAL GROWTH"
    p_b_t.font.bold = True
    p_b_t.font.size = Pt(13)
    p_b_t.font.color.rgb = TEXT_WHITE
    p_b_t.space_after = Pt(4)
    
    p_b_desc = b_tf.add_paragraph()
    p_b_desc.text = "Practicing radical candor with empathetic feedback, establishing strict delegation boundaries to prevent burnout, and grounding team vision in objective milestone metrics."
    p_b_desc.font.size = Pt(12)
    p_b_desc.font.color.rgb = RGBColor(210, 218, 230)
    
    prs.save("24f3004027_SPG_SA_Sep_2026.pptx")
    print("[*] Successfully generated 24f3004027_SPG_SA_Sep_2026.pptx")

create_pptx()
