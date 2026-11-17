import os
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
import pypdfium2 as pdfium
from PIL import Image

# Colors
HEX_OCEAN_DARK = HexColor("#0f172a")     # Slate 900
HEX_CORAL_RED  = HexColor("#e11d48")     # Rose 600
HEX_CORAL_SOFT = HexColor("#f43f5e")     # Rose 500
HEX_TEAL_DEEP  = HexColor("#0d9488")     # Teal 600
HEX_BLUE_ROYAL = HexColor("#1d4ed8")     # Royal Blue 700
HEX_INDIGO     = HexColor("#4f46e5")     # Indigo 600
HEX_AMBER_WARM = HexColor("#ea580c")     # Amber Orange 600
HEX_TEXT_MAIN  = HexColor("#1e293b")     # Slate 800
HEX_TEXT_MUTED = HexColor("#64748b")     # Slate 500
HEX_CARD_BG    = HexColor("#ffffff")     # White
HEX_BORDER     = HexColor("#cbd5e1")     # Slate 300

HEX_BG_S5 = HexColor("#f6f9fa")
HEX_BG_S6 = HexColor("#f8f7fc")

HEX_CARD_CLD     = HexColor("#f8fafc")
HEX_BORDER_CLD   = HexColor("#cbd5e1")
HEX_CARD_RES     = HexColor("#fffdf5")
HEX_BORDER_RES   = HexColor("#fef08a")

HEX_CARD_PROF    = HexColor("#f0fdfa")
HEX_BORDER_PROF  = HexColor("#99f6e4")
HEX_CARD_Q       = HexColor("#faf5ff")
HEX_BORDER_Q     = HexColor("#e9d5ff")

W_PT = 13.333 * 72 # 960
H_PT = 7.5 * 72    # 540

def draw_top_down(p, x, y_top, w, h_box):
    w_used, h_used = p.wrap(w, h_box)
    p.drawOn(c, x, y_top - h_used)
    return h_used

def draw_coral_page_frame(title_text, category_text, coral_img, bg_color=None):
    if bg_color:
        c.setFillColor(bg_color)
        c.rect(0, 0, W_PT, H_PT, fill=1, stroke=0)
    else:
        c.setFillColor(HexColor("#ffffff"))
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

c = canvas.Canvas("test_s5_s6.pdf", pagesize=(W_PT, H_PT))

# =========================================================================
# TEST SLIDE 5: TOPIC SELECTION: PRIMARY & SECONDARY RESOURCE IDENTIFICATION
# =========================================================================
draw_coral_page_frame("Topic Selection: Primary & Secondary Resource Identification", "TOPIC SELECTION & RESOURCES (SLIDE 2 OF 2)", "coral_blue.png", bg_color=HEX_BG_S5)

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
        "domain": "FinTech & Payment Gateway Systems (Razorpay / PayU ecosystem)",
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
    # draw sub card
    c.setFillColor(HexColor("#ffffff"))
    c.setStrokeColor(HexColor("#e2e8f0"))
    c.roundRect(s_x + 8, cy, left_w - 16, card_h, 4, fill=1, stroke=1)

    # Accent tab on left of card
    c.setFillColor(inv["color"])
    c.roundRect(s_x + 8, cy, 3.5, card_h, 2, fill=1, stroke=0)

    # Line 1: Candidate Name | Role | Exp Pill ... Interviewer
    c.setFillColor(HEX_OCEAN_DARK)
    c.setFont("Helvetica-Bold", 8.2)
    c.drawString(s_x + 18, cy + card_h - 13, f"{inv['name']}")
    
    c.setFont("Helvetica-Bold", 7.8)
    c.setFillColor(inv["color"])
    w_name = c.stringWidth(f"{inv['name']}   ", "Helvetica-Bold", 8.2)
    c.drawString(s_x + 18 + w_name, cy + card_h - 13, f"|   {inv['role']} ({inv['exp']})")

    c.setFont("Helvetica-Bold", 7.2)
    c.setFillColor(HEX_OCEAN_DARK)
    c.drawRightString(s_x + left_w - 16, cy + card_h - 13, f"Interviewer: {inv['interviewer']}")

    # Line 2: Domain
    c.setFont("Helvetica-Bold", 6.8)
    c.setFillColor(HEX_TEXT_MUTED)
    c.drawString(s_x + 18, cy + card_h - 24, "DOMAIN:")
    c.setFont("Helvetica", 6.8)
    c.setFillColor(HEX_TEXT_MAIN)
    c.drawString(s_x + 58, cy + card_h - 24, inv['domain'])

    # Line 3 & 4: Relevance & Fit
    c.setFont("Helvetica-Bold", 6.8)
    c.setFillColor(HEX_TEXT_MUTED)
    c.drawString(s_x + 18, cy + card_h - 35, "RELEVANCE:")
    
    p_rel = Paragraph(f"<font size='6.8' color='#334155'>{inv['relevance']}</font>",
                      ParagraphStyle('Rel', fontName='Helvetica', fontSize=6.8, leading=8.6))
    draw_top_down(p_rel, s_x + 72, cy + card_h - 27, left_w - 92, 26)

# Right Card: Secondary Literature & Theoretical Frameworks
c.setFillColor(HEX_CARD_RES) # Warm Ivory Tint
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
    draw_top_down(p_rd, right_x + 22, ry_cur - 8, right_w - 36, 45)
    ry_cur -= 66

c.showPage()

# =========================================================================
# TEST SLIDE 6: DISCUSSION PLAN: INTERVIEW STRATEGY & DRAFT QUESTIONS
# =========================================================================
draw_coral_page_frame("Discussion Plan: Interview Strategy & Draft Questions", "DISCUSSION PLAN & DRAFT QUESTIONS (1 SLIDE)", "coral_red.png", bg_color=HEX_BG_S6)

left_w6 = (b_w - 14) * 0.42
right_w6 = (b_w - 14) * 0.58
right_x6 = s_x + left_w6 + 14

# Left Card: Interview Methodology & CLD Loop Synthesis
c.setFillColor(HexColor("#f0fdfa"))
c.setStrokeColor(HexColor("#99f6e4"))
c.roundRect(s_x, b_y, left_w6, b_h, 6, fill=1, stroke=1)

c.setFillColor(HEX_TEAL_DEEP)
c.setFont("Helvetica-Bold", 10.5)
c.drawString(s_x + 14, b_y + b_h - 20, "Interview Strategy & CLD Synthesis")

# Section 1: Methodology Protocol
c.setFillColor(HEX_OCEAN_DARK)
c.setFont("Helvetica-Bold", 7.6)
c.drawString(s_x + 14, b_y + b_h - 36, "QUALITATIVE EXECUTION PROTOCOL:")

proto_items = [
    ("Format & Scope:", "N = 5 semi-structured 45–60 min video calls (1 per member) via Google Meet / Zoom."),
    ("Ethics & Capture:", "Informed consent recorded; verbatim transcript generation via automated tooling."),
    ("Thematic Coding:", "Collaborative thematic synthesis to map patterns to systems archetypes.")
]
py_cur = b_y + b_h - 48
for p_lbl, p_val in proto_items:
    c.setFillColor(HEX_TEXT_MUTED)
    c.setFont("Helvetica-Bold", 6.8)
    c.drawString(s_x + 18, py_cur, p_lbl)
    p_p = Paragraph(f"<font size='6.8' color='#334155'>{p_val}</font>",
                    ParagraphStyle('PVal', fontName='Helvetica', fontSize=6.8, leading=8.5))
    draw_top_down(p_p, s_x + 82, py_cur + 6, left_w6 - 96, 20)
    py_cur -= 20

# Divider line
c.setStrokeColor(HexColor("#ccfbf1"))
c.line(s_x + 14, py_cur + 2, s_x + left_w6 - 14, py_cur + 2)

# Section 2: CLD Feedback Loops
c.setFillColor(HEX_OCEAN_DARK)
c.setFont("Helvetica-Bold", 7.6)
c.drawString(s_x + 14, py_cur - 12, "CONCEPTUAL CLD FEEDBACK LOOPS:")

cld_loops_pdf = [
    ("R1 (The Quick Fix Spiral):", HEX_CORAL_RED,
     "Deadline Pressure (+) -> Shortcuts (+) -> Compounding Technical Debt (+) -> Delays (+) -> Deadline Pressure. (Vicious Reinforcing Cycle)"),
    ("R2 (Burnout & Firefighting Trap):", HEX_AMBER_WARM,
     "Technical Debt (+) -> Firefighting & Outages (+) -> Developer Fatigue (+) -> Attrition (+) -> Team Deficit (+) -> Pressure for Shortcuts."),
    ("B1 (Engineering Sense Refactoring):", HEX_TEAL_DEEP,
     "Technical Debt (+) -> Root-Cause Diagnostic (+) -> Refactoring Sprints (+) -> System Modularity & Health (-) -> Debt. (Stabilizer)"),
    ("B2 (Psychological Safety Pushback):", HEX_BLUE_ROYAL,
     "Developer Fatigue (+) -> Psychological Safety to Voice Concerns (+) -> Scope Renegotiation (-) -> Deadline Pressure. (Human Stabilizer)")
]

ly_cur = py_cur - 26
for lt, lc, ld in cld_loops_pdf:
    c.setFillColor(lc)
    c.setFont("Helvetica-Bold", 7.0)
    c.drawString(s_x + 18, ly_cur, lt)
    p_ld = Paragraph(f"<font size='6.6' color='#334155'>{ld}</font>",
                     ParagraphStyle('L6', fontName='Helvetica', fontSize=6.6, leading=8.6))
    draw_top_down(p_ld, s_x + 18, ly_cur - 7, left_w6 - 32, 42)
    ly_cur -= 56

# Right Card: Draft Semi-Structured Interview Protocol
c.setFillColor(HEX_CARD_Q) # Soft Lavender Tint
c.setStrokeColor(HEX_BORDER_Q)
c.roundRect(right_x6, b_y, right_w6, b_h, 6, fill=1, stroke=1)

c.setFillColor(HEX_INDIGO)
c.setFont("Helvetica-Bold", 10.5)
c.drawString(right_x6 + 14, b_y + b_h - 20, "Draft Semi-Structured Interview Protocol (5 Core Questions)")

draft_questions = [
    ("Q1 (Shortcuts & Immediate Payoffs):", HEX_TEAL_DEEP,
     "Can you describe a specific project where your team implemented a 'quick fix' or technical shortcut to meet a tight deadline? What was the immediate operational payoff?"),
    ("Q2 (Unintended Delays & Compounding Debt):", HEX_BLUE_ROYAL,
     "Over the following 3 to 6 months, how did that shortcut impact your codebase? Did it create hidden dependencies, unexpected bugs, or slow down subsequent feature releases?"),
    ("Q3 (Cognitive Load & Human Burnout):", HEX_AMBER_WARM,
     "How does working on a codebase heavily burdened with technical debt affect developer stress, on-call anxiety, and overall team morale over time?"),
    ("Q4 (Psychological Safety & Challenging Scope):", HEX_INDIGO,
     "In your organization, do engineers feel safe to push back against aggressive deadlines to address technical debt, or is there implicit pressure to keep shipping features at all costs?"),
    ("Q5 (High-Leverage Interventions & Engineering Sense):", HEX_CORAL_RED,
     "Looking back, what practical engineering practices or cultural interventions have you seen work best to break the cycle of quick fixes and restore sustainable team velocity?")
]

qy_cur = b_y + b_h - 44
for qt, qc, qd in draft_questions:
    c.setFillColor(qc)
    c.setFont("Helvetica-Bold", 8.0)
    c.drawString(right_x6 + 14, qy_cur, qt)
    p_qd = Paragraph(f"<font size='7.2' color='#334155'>{qd}</font>",
                     ParagraphStyle('QD', fontName='Helvetica', fontSize=7.2, leading=9.5))
    draw_top_down(p_qd, right_x6 + 20, qy_cur - 8, right_w6 - 36, 45)
    qy_cur -= 66

c.save()
print("Saved test_s5_s6.pdf successfully!")

# Render to images
doc = pdfium.PdfDocument("test_s5_s6.pdf")
for i, page in enumerate(doc):
    image = page.render(scale=2.0).to_pil()
    image.save(f"test_page_{i+1}.png")
    print(f"Rendered test_page_{i+1}.png")

