import os
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph

def generate_pdf():
    pdf_filename = "24f3004027_SPG_SA_Sep_2026.pdf"
    
    # 16:9 Widescreen in points: 960 x 540
    PAGE_WIDTH = 960
    PAGE_HEIGHT = 540
    
    c = canvas.Canvas(pdf_filename, pagesize=(PAGE_WIDTH, PAGE_HEIGHT))
    
    # Colors
    BG_DARK = HexColor("#121418")
    HEADER_BG = HexColor("#262a32")
    CARD_BG = HexColor("#1c2028")
    CARD_BORDER = HexColor("#374151")
    ACCENT_GOLD = HexColor("#e6a532")
    TEXT_WHITE = HexColor("#ffffff")
    TEXT_MUTED = HexColor("#94a3b8")
    LINK_BLUE = HexColor("#60a5fa")
    TRACK_BG = HexColor("#2d3441")
    
    def draw_header():
        # Header bar
        c.setFillColor(HEADER_BG)
        c.rect(0, PAGE_HEIGHT - 45, PAGE_WIDTH, 45, fill=1, stroke=0)
        
        # Left Text
        c.setFillColor(TEXT_WHITE)
        c.setFont("Helvetica-Bold", 14)
        c.drawString(35, PAGE_HEIGHT - 28, "Ramrup Satpati")
        
        c.setFillColor(TEXT_MUTED)
        c.setFont("Helvetica", 11)
        c.drawString(155, PAGE_HEIGHT - 28, "|   Roll No: 24f3004027")
        
        # Right Text
        c.setFillColor(TEXT_WHITE)
        c.setFont("Helvetica-Bold", 13)
        right_txt = "Type: ENFJ-A   |   "
        c.drawRightString(PAGE_WIDTH - 110, PAGE_HEIGHT - 28, right_txt)
        
        c.setFillColor(LINK_BLUE)
        c.drawString(PAGE_WIDTH - 105, PAGE_HEIGHT - 28, "Test Result")
        # Underline
        c.setStrokeColor(LINK_BLUE)
        c.setLineWidth(1)
        c.line(PAGE_WIDTH - 105, PAGE_HEIGHT - 30, PAGE_WIDTH - 35, PAGE_HEIGHT - 30)
        
        # Clickable Hyperlink Annotation
        test_url = "https://www.16personalities.com/enfj-personality"
        c.linkURL(test_url, (PAGE_WIDTH - 110, PAGE_HEIGHT - 35, PAGE_WIDTH - 30, PAGE_HEIGHT - 12), relative=0)

    # =========================================================================
    # SLIDE 1
    # =========================================================================
    # Background
    c.setFillColor(BG_DARK)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)
    
    draw_header()
    
    # Left: Photo Frame
    photo_x = 35
    photo_y = 45
    photo_w = 320
    photo_h = 425
    
    c.setFillColor(HexColor("#191c23"))
    c.setStrokeColor(ACCENT_GOLD)
    c.setLineWidth(3)
    c.rect(photo_x, photo_y, photo_w, photo_h, fill=1, stroke=1)
    
    if os.path.exists("profile_photo_framed.png"):
        c.drawImage("profile_photo_framed.png", photo_x + 5, photo_y + 5, width=photo_w - 10, height=photo_h - 10)
        
    # Right: Title
    c.setFillColor(TEXT_WHITE)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(390, PAGE_HEIGHT - 85, "CORE PERSONALITY TRAITS")
    
    # Trait bars
    traits = [
        ("67% Extraverted", "Introverted", HexColor("#38bdf8"), 0.67),
        ("72% Intuitive", "Observant", HexColor("#f59e0b"), 0.72),
        ("68% Feeling", "Thinking", HexColor("#10b981"), 0.68),
        ("74% Judging", "Prospecting", HexColor("#a855f7"), 0.74),
        ("78% Assertive", "Turbulent", HexColor("#f43f5e"), 0.78)
    ]
    
    bar_y = PAGE_HEIGHT - 128
    bar_w = 530
    for left_label, right_label, color, frac in traits:
        # Left label
        c.setFillColor(color)
        c.setFont("Helvetica-Bold", 10.5)
        c.drawString(390, bar_y + 8, left_label)
        
        # Right label
        c.setFillColor(TEXT_MUTED)
        c.setFont("Helvetica", 10)
        c.drawRightString(390 + bar_w, bar_y + 8, right_label)
        
        # Track background
        c.setFillColor(TRACK_BG)
        c.roundRect(390, bar_y - 6, bar_w, 8, 4, fill=1, stroke=0)
        
        # Active progress bar
        c.setFillColor(color)
        c.roundRect(390, bar_y - 6, bar_w * frac, 8, 4, fill=1, stroke=0)
        
        # Indicator knob
        c.setFillColor(TEXT_WHITE)
        c.circle(390 + (bar_w * frac), bar_y - 2, 6, fill=1, stroke=0)
        c.setFillColor(color)
        c.circle(390 + (bar_w * frac), bar_y - 2, 4, fill=1, stroke=0)
        
        bar_y -= 46
        
    # Bio / Academic Profile Box
    bio_box_y = 45
    bio_box_h = 135
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.setLineWidth(1)
    c.roundRect(390, bio_box_y, bar_w, bio_box_h, 8, fill=1, stroke=1)
    
    bio_text = (
        "<b>I am a third-year student in the BS in Data Science and Applications program at IIT Madras</b> "
        "(Roll No: 24f3004027). Having completed my Foundational and Diploma level coursework, my technical "
        "interests center on Machine Learning, Deep Learning, and Generative AI systems. As an ENFJ-A (Protagonist), "
        "I am passionate about bridging complex computational models with human-centered applications, combining "
        "analytical rigor with empathetic collaboration to lead high-impact technical initiatives."
    )
    
    style_bio = ParagraphStyle(
        'BioStyle',
        fontName='Helvetica',
        fontSize=10.5,
        leading=16,
        textColor=HexColor("#dbeafe")
    )
    p_bio = Paragraph(bio_text, style_bio)
    p_bio.wrapOn(c, bar_w - 30, bio_box_h - 20)
    p_bio.drawOn(c, 405, bio_box_y + 20)
    
    c.showPage()
    
    # =========================================================================
    # SLIDE 2
    # =========================================================================
    # Background
    c.setFillColor(BG_DARK)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)
    
    draw_header()
    
    # Left Column: Heading & Narrative
    c.setFillColor(TEXT_WHITE)
    c.setFont("Helvetica-Bold", 17)
    c.drawString(35, PAGE_HEIGHT - 85, "NAVIGATING TEAM DYNAMICS AND")
    c.drawString(35, PAGE_HEIGHT - 108, "PERSONAL GROWTH")
    
    narrative_text = (
        "As an <b>ENFJ-A (Protagonist)</b>, my approach to collaboration is anchored in empathetic "
        "leadership, collective alignment, and active communication. I naturally gravitate towards energizing "
        "collaborative environments, unblocking interpersonal bottlenecks, and ensuring every team member's "
        "voice is synthesized into our strategic direction.<br/><br/>"
        "In technical projects—such as investigating <b>Systems Thinking</b> and organizational complexity—I actively "
        "bridge analytical depth with team consensus. While I naturally hold high standards for collective execution, "
        "I consciously balance my enthusiasm by practicing structured delegation, objective milestone tracking, and "
        "maintaining healthy cognitive boundaries across the team."
    )
    
    style_narrative = ParagraphStyle(
        'NarrativeStyle',
        fontName='Helvetica',
        fontSize=11,
        leading=17,
        textColor=HexColor("#cbd5e1")
    )
    p_nar = Paragraph(narrative_text, style_narrative)
    p_nar.wrapOn(c, 420, 270)
    p_nar.drawOn(c, 35, 140)
    
    # Right Column Top Card: Relationship Dynamics
    card_w = 445
    card1_h = 150
    card1_y = PAGE_HEIGHT - 215
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.setLineWidth(1)
    c.roundRect(480, card1_y, card_w, card1_h, 8, fill=1, stroke=1)
    
    c.setFillColor(HexColor("#60a5fa"))
    c.setFont("Helvetica-Bold", 12)
    c.drawString(500, card1_y + card1_h - 24, "RELATIONSHIP DYNAMICS")
    
    c1_bullets = [
        "Empathetic, clear, and articulate communicator.",
        "Proactively builds psychological safety and mutual team trust.",
        "Naturally aligns team milestones, deliverables, and timelines.",
        "Bridges technical complexity with human perspective.",
        "Actively seeks and embraces constructive critique."
    ]
    b_y = card1_y + card1_h - 46
    for b in c1_bullets:
        c.setFillColor(HexColor("#60a5fa"))
        c.circle(505, b_y + 3, 2.5, fill=1, stroke=0)
        c.setFillColor(HexColor("#e2e8f0"))
        c.setFont("Helvetica", 9.5)
        c.drawString(516, b_y, b)
        b_y -= 21
        
    # Right Column Middle Card: Core Challenges
    card2_h = 125
    card2_y = card1_y - 140
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.setLineWidth(1)
    c.roundRect(480, card2_y, card_w, card2_h, 8, fill=1, stroke=1)
    
    c.setFillColor(HexColor("#f87171"))
    c.setFont("Helvetica-Bold", 12)
    c.drawString(500, card2_y + card2_h - 24, "CORE CHALLENGES")
    
    c2_bullets = [
        "Tendency to absorb collective workload and hesitate to say no.",
        "Vulnerability to idealism when project execution faces friction.",
        "Reluctance to deliver blunt criticism out of concern for team harmony."
    ]
    b_y2 = card2_y + card2_h - 46
    for b in c2_bullets:
        c.setFillColor(HexColor("#f87171"))
        c.circle(505, b_y2 + 3, 2.5, fill=1, stroke=0)
        c.setFillColor(HexColor("#e2e8f0"))
        c.setFont("Helvetica", 9.5)
        c.drawString(516, b_y2, b)
        b_y2 -= 23
        
    # Bottom Banner: Action Plan
    banner_y = 35
    banner_h = 80
    banner_w = PAGE_WIDTH - 70
    c.setFillColor(HexColor("#181c24"))
    c.setStrokeColor(HexColor("#4b5563"))
    c.setLineWidth(1)
    c.roundRect(35, banner_y, banner_w, banner_h, 8, fill=1, stroke=1)
    
    # White accent line on left
    c.setFillColor(TEXT_WHITE)
    c.roundRect(43, banner_y + 12, 4, banner_h - 24, 2, fill=1, stroke=0)
    
    c.setFont("Helvetica-Bold", 11)
    c.drawString(60, banner_y + banner_h - 28, "ACTION PLAN FOR PERSONAL GROWTH")
    
    plan_text = "Balancing empathetic leadership with objective accountability, enforcing clear delegation boundaries to prevent burnout, and grounding visionary ideals in measurable milestone metrics."
    c.setFillColor(HexColor("#cbd5e1"))
    c.setFont("Helvetica", 10)
    c.drawString(60, banner_y + 24, plan_text)
    
    c.save()
    print(f"[*] Successfully generated {pdf_filename}")

generate_pdf()
