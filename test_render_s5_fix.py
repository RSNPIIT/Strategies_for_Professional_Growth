import os
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
import pypdfium2 as pdfium
from PIL import Image

HEX_OCEAN_DARK = HexColor("#0f172a")     # Slate 900
HEX_CORAL_RED  = HexColor("#e11d48")     # Rose 600
HEX_TEAL_DEEP  = HexColor("#0d9488")     # Teal 600
HEX_BLUE_ROYAL = HexColor("#1d4ed8")     # Royal Blue 700
HEX_INDIGO     = HexColor("#4f46e5")     # Indigo 600
HEX_AMBER_WARM = HexColor("#ea580c")     # Amber Orange 600
HEX_TEXT_MAIN  = HexColor("#1e293b")     # Slate 800
HEX_TEXT_MUTED = HexColor("#64748b")     # Slate 500
HEX_BG_S5      = HexColor("#f6f9fa")
HEX_CARD_RES   = HexColor("#fffdf5")
HEX_BORDER_RES = HexColor("#fef08a")

W_PT = 13.333 * 72 # 960
H_PT = 7.5 * 72    # 540

def draw_top_down(c, p, x, y_top, w, h_box):
    w_used, h_used = p.wrap(w, h_box)
    p.drawOn(c, x, y_top - h_used)
    return h_used

def draw_coral_page_frame(c, title_text, category_text, coral_img, bg_color=None):
    if bg_color:
        c.setFillColor(bg_color)
        c.rect(0, 0, W_PT, H_PT, fill=1, stroke=0)

    # Top banner bar
    c.setFillColor(HexColor("#ffffff"))
    c.setStrokeColor(HexColor("#e2e8f0"))
    c.rect(0, H_PT - 72, W_PT, 72, fill=1, stroke=1)

    c.setFillColor(HEX_CORAL_RED)
    c.setFont("Helvetica-Bold", 8.0)
    c.drawString(104, H_PT - 28, category_text.upper())

    c.setFillColor(HEX_OCEAN_DARK)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(104, H_PT - 50, title_text)

    if os.path.exists(coral_img):
        c.drawImage(coral_img, W_PT - 100, H_PT - 68, width=64, height=64, mask='auto', preserveAspectRatio=True)

    # Bottom footer bar
    c.setStrokeColor(HexColor("#e2e8f0"))
    c.line(104, 32, W_PT - 104, 32)

    c.setFillColor(HEX_TEXT_MUTED)
    c.setFont("Helvetica", 7.5)
    c.drawString(104, 20, "IIT Madras BS Degree • BSGN3001: Strategies for Professional Growth (SPG)")
    c.drawRightString(W_PT - 104, 20, "Team 114 (Iterate) • GP1 Deliverable 2 Pitch Deck")

c = canvas.Canvas("test_s5_fix.pdf", pagesize=(W_PT, H_PT))
draw_coral_page_frame(c, "Topic Selection: Primary & Secondary Resource Identification", "TOPIC SELECTION & RESOURCES (SLIDE 2 OF 2)", "coral_blue.png", bg_color=HEX_BG_S5)

s_x = 104.4
b_y = 43.2
b_w = 751.2
b_h = 399.6

left_w = (b_w - 14) * 0.58
right_w = (b_w - 14) * 0.42
right_x = s_x + left_w + 14

# Left Card: Primary Resources (Planned Practitioner Cohort N=5)
c.setFillColor(HexColor("#f8fafc"))
c.setStrokeColor(HexColor("#cbd5e1"))
c.roundRect(s_x, b_y, left_w, b_h, 6, fill=1, stroke=1)

c.setFillColor(HEX_OCEAN_DARK)
c.setFont("Helvetica-Bold", 10.5)
c.drawString(s_x + 14, b_y + b_h - 20, "Primary Resources: Planned Practitioner Cohort (N = 5)")

c.setFillColor(HEX_TEXT_MUTED)
c.setFont("Helvetica", 7.0)
c.drawString(s_x + 14, b_y + b_h - 32, "Empirical qualitative inquiry: 1 interview per member with practicing software engineers (≥3 Yrs Exp)")

# 5 Practitioner cards
interviewees = [
    {
        "name": "Aakash Verma",
        "role": "Staff Backend Engineer",
        "exp": "7+ Yrs Exp",
        "color": HEX_CORAL_RED,
        "interviewer": "Samyabrata Roy (Team Lead)",
        "domain": "FinTech & Payment Gateways (Razorpay / PayU ecosystem)",
        "relevance": "Designs ultra-low-latency settlement APIs under strict SLAs. Manages trade-offs between festive release deadlines and compounding database indexing debt."
    },
    {
        "name": "Tanvi Mehrotra",
        "role": "Principal SRE / DevOps Lead",
        "exp": "6+ Yrs Exp",
        "color": HEX_TEAL_DEEP,
        "interviewer": "Abir Saha (Project Manager)",
        "domain": "Cloud Infrastructure & Distributed Enterprise SaaS (Freshworks ecosystem)",
        "relevance": "Leads 24/7 on-call rotations and post-mortems; direct frontline exposure to developer cognitive fatigue and brittle microservices from quick deployment patches."
    },
    {
        "name": "Vikramaditya Sharma",
        "role": "Platform Architecture Lead",
        "exp": "8+ Yrs Exp",
        "color": HEX_BLUE_ROYAL,
        "interviewer": "Rishabh Barthwal (Research Lead)",
        "domain": "High-Scale Consumer Tech & E-Commerce (Swiggy / Flipkart ecosystem)",
        "relevance": "Direct perspective on Senge's 'Shifting the Burden': tactical quick patches for flash delivery spikes degrading core service modularity and triggering senior attrition."
    },
    {
        "name": "Rohan Nambiar",
        "role": "Senior Full-Stack Engineer",
        "exp": "4.5 Yrs Exp",
        "color": HEX_AMBER_WARM,
        "interviewer": "Piyush Tilokchandani (Design Lead)",
        "domain": "Enterprise SaaS & Collaborative Workflows (Zoho ecosystem)",
        "relevance": "Balances sprint delivery velocity against front-end modularity; provides frontline insight into velocity pressure vs. engineering discipline and tech debt accumulation."
    },
    {
        "name": "Ananya Sengupta",
        "role": "Senior Distributed Systems Engineer",
        "exp": "5+ Yrs Exp",
        "color": HEX_INDIGO,
        "interviewer": "Ramrup Satpati (Editor / Lead)",
        "domain": "HealthTech & Clinical Data Infrastructure (Siemens / Philips ecosystem)",
        "relevance": "Operates under zero-downtime and regulatory standards; evaluates how team psychological safety empowers engineers to push back against unrealistic deadlines."
    }
]

card_gap = 6
card_h = (b_h - 44 - (4 * card_gap)) / 5 # ~64.3 pt each

for i, inv in enumerate(interviewees):
    cy = b_y + b_h - 40 - (i + 1) * card_h - (i * card_gap) + card_gap
    c.setFillColor(HexColor("#ffffff"))
    c.setStrokeColor(HexColor("#e2e8f0"))
    c.roundRect(s_x + 8, cy, left_w - 16, card_h, 4, fill=1, stroke=1)

    # Accent tab
    c.setFillColor(inv["color"])
    c.roundRect(s_x + 8, cy, 3.5, card_h, 2, fill=1, stroke=0)

    # Line 1: Candidate Name + Exp Pill on left; Interviewer on right
    c.setFillColor(HEX_OCEAN_DARK)
    c.setFont("Helvetica-Bold", 8.2)
    c.drawString(s_x + 18, cy + card_h - 13, inv['name'])
    
    w_name = c.stringWidth(inv['name'] + " ", "Helvetica-Bold", 8.2)
    c.setFont("Helvetica-Bold", 7.2)
    c.setFillColor(inv["color"])
    c.drawString(s_x + 18 + w_name, cy + card_h - 13, f"•  {inv['exp']}")

    c.setFont("Helvetica", 7.2)
    c.setFillColor(HEX_TEXT_MUTED)
    w_int = c.stringWidth(f"Interviewer: {inv['interviewer']}", "Helvetica-Bold", 7.2)
    c.drawString(s_x + left_w - 16 - w_int, cy + card_h - 13, "Interviewer: ")
    c.setFont("Helvetica-Bold", 7.2)
    c.setFillColor(HEX_OCEAN_DARK)
    w_lbl = c.stringWidth("Interviewer: ", "Helvetica", 7.2)
    c.drawString(s_x + left_w - 16 - w_int + w_lbl, cy + card_h - 13, inv['interviewer'])

    # Line 2: Role & Domain
    c.setFont("Helvetica-Bold", 6.8)
    c.setFillColor(HEX_TEXT_MUTED)
    c.drawString(s_x + 18, cy + card_h - 24, "ROLE & DOMAIN:")
    c.setFont("Helvetica-Bold", 6.8)
    c.setFillColor(HEX_TEXT_MAIN)
    c.drawString(s_x + 88, cy + card_h - 24, f"{inv['role']}  —  {inv['domain']}")

    # Line 3: Relevance & Fit
    c.setFont("Helvetica-Bold", 6.8)
    c.setFillColor(HEX_TEXT_MUTED)
    c.drawString(s_x + 18, cy + card_h - 35, "RELEVANCE:")
    
    p_rel = Paragraph(f"<font size='6.8' color='#334155'>{inv['relevance']}</font>",
                      ParagraphStyle('Rel', fontName='Helvetica', fontSize=6.8, leading=8.6))
    draw_top_down(c, p_rel, s_x + 88, cy + card_h - 27, left_w - 104, 26)

# Right Card: Secondary Literature
c.setFillColor(HEX_CARD_RES)
c.setStrokeColor(HEX_BORDER_RES)
c.roundRect(right_x, b_y, right_w, b_h, 6, fill=1, stroke=1)

c.setFillColor(HEX_OCEAN_DARK)
c.setFont("Helvetica-Bold", 10.5)
c.drawString(right_x + 14, b_y + b_h - 20, "Secondary Literature & Theoretical Frameworks")

c.setFillColor(HEX_TEXT_MUTED)
c.setFont("Helvetica", 7.0)
c.drawString(right_x + 14, b_y + b_h - 32, "Academic foundations grounding system dynamics & human resilience")

res_pdf = [
    ("Peter M. Senge (1990) — The Fifth Discipline",
     "Source of systems archetypes ('Fixes that Fail', 'Shifting the Burden'). Establishes how delayed feedback and local optimizations impair organizational capacity."),
    ("Waters Center for Systems Thinking (2020) — Habits of a Systems Thinker",
     "Core cognitive habits: observing how system dynamics change over time, anticipating unintended consequences, and pinpointing high-leverage intervention points."),
    ("Forsgren, Humble, & Kim (2018) — Accelerate (DORA Research)",
     "Empirical research linking software delivery performance, automated testing rigor, and architectural decoupling to reduced developer burnout."),
    ("Amy Edmondson (1999) — Psychological Safety & Team Learning",
     "Foundational framework demonstrating that teams where members feel safe to take interpersonal risks catch architectural failures far earlier."),
    ("World Economic Forum (2025) — Future of Jobs Report 2025",
     "Identifies Systems Thinking, Resilience & Flexibility, and Complex Problem-Solving as top core competencies for engineering professionals by 2030.")
]

ry_cur = b_y + b_h - 44
for rt, rd in res_pdf:
    c.setFillColor(HEX_OCEAN_DARK)
    c.setFont("Helvetica-Bold", 7.8)
    c.drawString(right_x + 14, ry_cur, f"•   {rt}")
    p_rd = Paragraph(f"<font size='7.0' color='#334155'>{rd}</font>",
                     ParagraphStyle('Res', fontName='Helvetica', fontSize=7.0, leading=9.2))
    draw_top_down(c, p_rd, right_x + 22, ry_cur - 8, right_w - 36, 45)
    ry_cur -= 66

c.save()
print("Saved test_s5_fix.pdf")
doc = pdfium.PdfDocument("test_s5_fix.pdf")
img = doc[0].render(scale=2.0).to_pil()
img.save("test_page_1_fixed.png")
print("Saved test_page_1_fixed.png")
