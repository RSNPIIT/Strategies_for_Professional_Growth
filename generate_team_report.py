"""
Team 114 (Iterate) - GP2 Deliverable 1.c: Team Project Report
Title: Beyond Quick Fixes: Exploring Technical Debt & Developer Fatigue Through Systems Thinking
Generates:
  - Team_114_Iterate_Team_Proj_Report.pptx
  - Team_114_Iterate_Team_Proj_Report.pdf
  - Team_114_SPG_GP2_Sep_2026.pptx
  - Team_114_SPG_GP2_Sep_2026.pdf
"""

import os
import shutil
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor

from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfgen import canvas

# =============================================================================
# COLOR SYSTEM & PALETTES
# =============================================================================
C_BG_S0 = RGBColor(248, 250, 252)       # Off-white / cool slate
C_BG_S1 = RGBColor(240, 249, 255)       # Alice blue / light sky
C_BG_S2 = RGBColor(254, 252, 246)       # Soft warm ivory
C_BG_S3 = RGBColor(240, 253, 250)       # Light mint
C_BG_S4 = RGBColor(255, 250, 245)       # Soft peach
C_BG_S5 = RGBColor(248, 250, 252)       # Cool slate tint

C_OCEAN_DARK = RGBColor(15, 41, 66)     # Primary navy
C_TEAL_DEEP  = RGBColor(15, 118, 110)   # Deep teal
C_CORAL_RED  = RGBColor(190, 18, 60)    # Crimson coral
C_BLUE_ROYAL = RGBColor(30, 58, 138)    # Royal navy blue
C_AMBER_WARM = RGBColor(180, 83, 9)     # Warm amber
C_TEXT_MAIN  = RGBColor(30, 41, 59)     # Slate text
C_TEXT_MUTED = RGBColor(100, 116, 139)  # Slate muted
C_CARD_BG    = RGBColor(255, 255, 255)  # Clean white
C_BORDER     = RGBColor(203, 213, 225)  # Soft slate border

HEX_BG_S0 = HexColor("#f8fafc")
HEX_BG_S1 = HexColor("#f0f9ff")
HEX_BG_S2 = HexColor("#fefcf6")
HEX_BG_S3 = HexColor("#f0fdfa")
HEX_BG_S4 = HexColor("#fffaf5")
HEX_BG_S5 = HexColor("#f8fafc")

HEX_OCEAN_DARK = HexColor("#0f2942")
HEX_TEAL_DEEP  = HexColor("#0f766e")
HEX_CORAL_RED  = HexColor("#be123c")
HEX_BLUE_ROYAL = HexColor("#1e3a8a")
HEX_AMBER_WARM = HexColor("#b45309")
HEX_TEXT_MAIN  = HexColor("#1e293b")
HEX_TEXT_MUTED = HexColor("#64748b")
HEX_CARD_BG    = HexColor("#ffffff")
HEX_BORDER     = HexColor("#cbd5e1")


def disable_spellcheck(run):
    """Disable spell check / proofing squiggles in PowerPoint."""
    rPr = run._r.get_or_add_rPr()
    rPr.set("noProof", "1")


# =============================================================================
# BUILD POWERPOINT PRESENTATION (.pptx)
# =============================================================================
def build_pptx():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    def add_slide_frame(slide, title_text, category_text, icon_name="icon_rocket.png", bg_color=C_BG_S1, apa_text=None):
        # Background
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = bg_color
        bg.line.fill.background()

        # Digital tech bubble top-left
        if os.path.exists(icon_name):
            slide.shapes.add_picture(icon_name, Inches(0.35), Inches(0.25), Inches(0.85), Inches(0.85))

        # Title Box
        hb = slide.shapes.add_textbox(Inches(1.35), Inches(0.28), Inches(10.4), Inches(0.95))
        tf = hb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p_cat = tf.paragraphs[0]
        r_cat = p_cat.add_run()
        r_cat.text = category_text.upper()
        r_cat.font.bold = True
        r_cat.font.size = Pt(8.8)
        r_cat.font.color.rgb = C_CORAL_RED
        disable_spellcheck(r_cat)

        p_t = tf.add_paragraph()
        r_t = p_t.add_run()
        r_t.text = title_text
        r_t.font.bold = True
        r_t.font.size = Pt(17.0)
        r_t.font.color.rgb = C_OCEAN_DARK
        disable_spellcheck(r_t)

        # Header underline
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.35), Inches(1.24), Inches(10.5), Inches(0.025))
        line.fill.solid()
        line.fill.fore_color.rgb = C_CORAL_RED
        line.line.fill.background()

        # Top-right IITM Logo
        if os.path.exists("iitm_logo_clean.png"):
            slide.shapes.add_picture("iitm_logo_clean.png", Inches(12.05), Inches(0.22), Inches(1.0), Inches(1.0))

        # Footer divider line
        fline = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.35), Inches(7.05), Inches(10.5), Inches(0.015))
        fline.fill.solid()
        fline.fill.fore_color.rgb = RGBColor(226, 232, 240)
        fline.line.fill.background()

        # Footer Text
        fb = slide.shapes.add_textbox(Inches(1.35), Inches(7.10), Inches(10.5), Inches(0.3))
        ftf = fb.text_frame
        ftf.margin_left = ftf.margin_top = ftf.margin_right = ftf.margin_bottom = 0
        fp = ftf.paragraphs[0]
        fr1 = fp.add_run()
        fr1.text = "Team 114: Iterate  •  Beyond Quick Fixes: Technical Debt & Fatigue  •  GP2 Deliverable 1.c"
        fr1.font.size = Pt(8.0)
        fr1.font.color.rgb = C_TEXT_MUTED
        disable_spellcheck(fr1)

        # Right footer citations
        if apa_text:
            fr_apa = fp.add_run()
            fr_apa.text = f"   |   Citations: {apa_text}"
            fr_apa.font.size = Pt(7.2)
            fr_apa.font.color.rgb = C_TEAL_DEEP
            disable_spellcheck(fr_apa)

        # Slide corner page curl at bottom right
        if os.path.exists("page_flip_corner.png"):
            slide.shapes.add_picture("page_flip_corner.png", Inches(12.55), Inches(6.3), Inches(0.78), Inches(1.2))

    # =========================================================================
    # SLIDE 0: COVER SLIDE - 5 MEMBER PHOTO CARDS (Centered in Middle)
    # =========================================================================
    s0 = prs.slides.add_slide(blank_layout)
    bg0 = s0.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg0.fill.solid()
    bg0.fill.fore_color.rgb = C_BG_S0
    bg0.line.fill.background()

    # Left Margin: Tech Icon Bubbles replacing flowers
    if os.path.exists("icon_rocket.png"):
        s0.shapes.add_picture("icon_rocket.png", Inches(0.4), Inches(0.4), Inches(0.85), Inches(0.85))
    if os.path.exists("icon_gears.png"):
        s0.shapes.add_picture("icon_gears.png", Inches(0.75), Inches(1.25), Inches(0.75), Inches(0.75))
    if os.path.exists("icon_trophy.png"):
        s0.shapes.add_picture("icon_trophy.png", Inches(0.35), Inches(2.0), Inches(0.7), Inches(0.7))

    if os.path.exists("icon_dollar.png"):
        s0.shapes.add_picture("icon_dollar.png", Inches(0.35), Inches(4.7), Inches(0.72), Inches(0.72))
    if os.path.exists("icon_search.png"):
        s0.shapes.add_picture("icon_search.png", Inches(0.75), Inches(5.35), Inches(0.75), Inches(0.75))
    if os.path.exists("icon_bulb.png"):
        s0.shapes.add_picture("icon_bulb.png", Inches(0.35), Inches(6.05), Inches(0.82), Inches(0.82))

    # Center Card
    card_x = Inches(1.6)
    card_y = Inches(0.65)
    card_w = Inches(10.3)
    card_h = Inches(6.2)

    card0 = s0.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, card_x, card_y, card_w, card_h)
    card0.fill.solid()
    card0.fill.fore_color.rgb = C_CARD_BG
    card0.line.color.rgb = C_BORDER
    card0.line.width = Pt(1.2)

    # Restore Frontpage Watermark inside the card
    if os.path.exists("cover_watermark.png"):
        s0.shapes.add_picture("cover_watermark.png", Inches(1.65), Inches(0.7), Inches(10.2), Inches(6.1))

    # Top-right IITM Logo inside card (fully visible, unhidden!)
    if os.path.exists("iitm_logo_clean.png"):
        s0.shapes.add_picture("iitm_logo_clean.png", Inches(10.4), Inches(0.85), Inches(1.25), Inches(1.25))

    # Title & Subtitle box at top of card
    tb0 = s0.shapes.add_textbox(Inches(1.9), Inches(0.85), Inches(8.3), Inches(1.75))
    tf0 = tb0.text_frame
    tf0.word_wrap = True
    tf0.margin_left = tf0.margin_right = tf0.margin_top = tf0.margin_bottom = 0

    p0 = tf0.paragraphs[0]
    r0 = p0.add_run()
    r0.text = "IIT MADRAS BS DEGREE PROGRAMME\n"
    r0.font.bold = True
    r0.font.size = Pt(10)
    r0.font.color.rgb = C_CORAL_RED
    disable_spellcheck(r0)

    r_crs = p0.add_run()
    r_crs.text = "BSGN3001: STRATEGIES FOR PROFESSIONAL GROWTH  •  GROUP PROJECT 2 (GP2)\n\n"
    r_crs.font.bold = True
    r_crs.font.size = Pt(8.5)
    r_crs.font.color.rgb = C_TEXT_MUTED
    disable_spellcheck(r_crs)

    r_title1 = p0.add_run()
    r_title1.text = "Beyond Quick Fixes: Exploring Technical Debt &\nDeveloper Fatigue Through Systems Thinking\n"
    r_title1.font.bold = True
    r_title1.font.size = Pt(16.5)
    r_title1.font.color.rgb = C_OCEAN_DARK
    disable_spellcheck(r_title1)

    r_sub = p0.add_run()
    r_sub.text = "Linking Systems Thinking (Week 10) and Engineering Sense (Week 11)   |   TEAM 114: ITERATE"
    r_sub.font.italic = True
    r_sub.font.size = Pt(9.5)
    r_sub.font.color.rgb = C_TEAL_DEEP
    disable_spellcheck(r_sub)

    # 5 Member Photo Cards in a horizontal row - POSITIONED IN THE MIDDLE WITH BIGGER CIRCLES
    members_roster = [
        ("Samyabrata Roy", "22F2001443", "Team Lead", "circle_samyabrata.png"),
        ("Abir Saha", "23F3001436", "Project Manager", "circle_abir.png"),
        ("Rishabh Barthwal", "23F2004112", "Research Lead", "circle_rishabh.png"),
        ("Piyush Tilokchandani", "21F1006739", "Design Lead", "circle_piyush.png"),
        ("Ramrup Satpati", "24F3004027", "Creative & Pres. Lead", "circle_ramrup.png"),
    ]

    mem_start_x = Inches(1.9)
    mem_w = Inches(1.86)
    mem_gap = Inches(0.12)
    mem_y = Inches(2.70)   # Vertically centered in the middle of the card
    mem_h = Inches(2.95)   # Taller card

    for idx, (mname, mroll, mrole, mavatar) in enumerate(members_roster):
        mx = mem_start_x + idx * (mem_w + mem_gap)
        mcard = s0.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, mx, mem_y, mem_w, mem_h)
        mcard.fill.solid()
        mcard.fill.fore_color.rgb = RGBColor(255, 255, 255)
        mcard.line.color.rgb = C_BORDER
        mcard.line.width = Pt(1.0)

        # Bigger Circular Avatar Photo
        if os.path.exists(mavatar):
            photo_size = Inches(1.42)
            photo_x = mx + (mem_w - photo_size) / 2
            photo_y = mem_y + Inches(0.14)
            s0.shapes.add_picture(mavatar, photo_x, photo_y, photo_size, photo_size)

        # Text below photo
        mtb = s0.shapes.add_textbox(mx + Inches(0.04), mem_y + Inches(1.62), mem_w - Inches(0.08), Inches(1.25))
        mtf = mtb.text_frame
        mtf.word_wrap = True
        mtf.margin_left = mtf.margin_right = mtf.margin_top = mtf.margin_bottom = 0

        mp_name = mtf.paragraphs[0]
        mp_name.alignment = PP_ALIGN.CENTER
        mr_name = mp_name.add_run()
        mr_name.text = f"{mname}\n"
        mr_name.font.bold = True
        mr_name.font.size = Pt(8.6)
        mr_name.font.color.rgb = C_OCEAN_DARK
        disable_spellcheck(mr_name)

        mr_roll = mp_name.add_run()
        mr_roll.text = f"Roll: {mroll}\n\n"
        mr_roll.font.size = Pt(7.2)
        mr_roll.font.color.rgb = C_TEXT_MUTED
        disable_spellcheck(mr_roll)

        mr_role = mp_name.add_run()
        mr_role.text = mrole
        mr_role.font.bold = True
        mr_role.font.size = Pt(7.4)
        mr_role.font.color.rgb = C_CORAL_RED
        disable_spellcheck(mr_role)

    # Bottom Pill
    pill = s0.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.9), Inches(5.75), Inches(9.78), Inches(0.95))
    pill.fill.solid()
    pill.fill.fore_color.rgb = RGBColor(241, 245, 249)
    pill.line.color.rgb = C_BORDER
    ptf = pill.text_frame
    ptf.word_wrap = True
    ptf.margin_left = ptf.margin_right = Inches(0.2)
    ptf.margin_top = Inches(0.12)

    pp = ptf.paragraphs[0]
    r_hdr = pp.add_run()
    r_hdr.text = "Deliverable Overview & Alignment: "
    r_hdr.font.bold = True
    r_hdr.font.size = Pt(8.2)
    r_hdr.font.color.rgb = C_OCEAN_DARK
    disable_spellcheck(r_hdr)

    r_txt = pp.add_run()
    r_txt.text = (
        "Consolidated synthesis of 5 primary practitioner interviews and secondary systems literature. "
        "Investigates the causal drivers of technical debt shortcuts, compounding friction, and developer burnout. "
        "Submitted for Evaluation | Term: September 2026."
    )
    r_txt.font.size = Pt(8.0)
    r_txt.font.color.rgb = C_TEXT_MAIN
    disable_spellcheck(r_txt)

    if os.path.exists("page_flip_corner.png"):
        s0.shapes.add_picture("page_flip_corner.png", Inches(12.55), Inches(6.3), Inches(0.78), Inches(1.2))

    # =========================================================================
    # SLIDE 1: METHODOLOGY (5 MARKS) - Dim Watermark Pic 4 (VR)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    add_slide_frame(s1, "How We Did the Study (Methodology)",
                    "RESEARCH METHODOLOGY (5 MARKS)", "icon_search.png", C_BG_S1,
                    "Edmondson (1999); Forsgren et al. (2018); Senge (1990); Waters Center (2020)")

    left_x = Inches(1.35)
    top_y = Inches(1.40)
    left_w = Inches(4.5)
    box_h = Inches(5.50)

    card_proc = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_x, top_y, left_w, box_h)
    card_proc.fill.solid()
    card_proc.fill.fore_color.rgb = RGBColor(255, 255, 255)
    card_proc.line.color.rgb = C_BORDER
    card_proc.line.width = Pt(1.0)

    right_x = Inches(6.0)
    right_w = Inches(5.9)
    cohort_h = Inches(3.2)

    card_c = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, right_x, top_y, right_w, cohort_h)
    card_c.fill.solid()
    card_c.fill.fore_color.rgb = RGBColor(255, 255, 255)
    card_c.line.color.rgb = C_BORDER
    card_c.line.width = Pt(1.0)

    samp_y = top_y + cohort_h + Inches(0.15)
    samp_h = box_h - cohort_h - Inches(0.15)
    card_s = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, right_x, samp_y, right_w, samp_h)
    card_s.fill.solid()
    card_s.fill.fore_color.rgb = RGBColor(254, 252, 246)
    card_s.line.color.rgb = RGBColor(253, 230, 138)
    card_s.line.width = Pt(1.0)

    # Dim Watermark ON TOP of cards
    if os.path.exists("watermark_slide_1.png"):
        s1.shapes.add_picture("watermark_slide_1.png", Inches(3.2), Inches(1.8), Inches(6.9), Inches(4.6))

    tf_p = card_proc.text_frame
    tf_p.word_wrap = True
    tf_p.margin_left = tf_p.margin_right = Inches(0.18)
    tf_p.margin_top = Inches(0.14)

    p_ph = tf_p.paragraphs[0]
    r_ph = p_ph.add_run()
    r_ph.text = "5-STAGE QUALITATIVE PROCESS FLOW\n"
    r_ph.font.bold = True
    r_ph.font.size = Pt(9.2)
    r_ph.font.color.rgb = C_TEAL_DEEP
    disable_spellcheck(r_ph)

    stages = [
        ("Stage 1: Study Design & Ethical Framing",
         "Anchored semi-structured interview protocol in Senge (1990) systems thinking archetypes. Captured written informed consent over email + recording disclosure."),
        ("Stage 2: Primary Data Collection (N=5)",
         "Conducted five 1-on-1 virtual interviews (30–45 min duration each) with dual cameras on per strict IITM assessment rubrics."),
        ("Stage 3: Verbatim Transcription & Audit",
         "Extracted audio streams; generated full verbatim transcripts using speech tooling; multi-pass human audit to verify domain terminology."),
        ("Stage 4: Qualitative Thematic Coding",
         "Coded transcripts across R1 (quick fixes), R2 (fatigue), B1 (refactoring), and B2 (psychological safety); identified recurring patterns."),
        ("Stage 5: Triangulation & Influence Modeling",
         "Cross-validated qualitative themes against DORA empirical delivery research benchmarks (Forsgren et al., 2018) to construct our causal loop model.")
    ]
    for st, sd in stages:
        p_st = tf_p.add_paragraph()
        r_st = p_st.add_run()
        r_st.text = f"• {st}\n  "
        r_st.font.bold = True
        r_st.font.size = Pt(7.6)
        r_st.font.color.rgb = C_OCEAN_DARK
        disable_spellcheck(r_st)
        r_sd = p_st.add_run()
        r_sd.text = sd
        r_sd.font.size = Pt(6.8)
        r_sd.font.color.rgb = C_TEXT_MAIN
        disable_spellcheck(r_sd)
        p_st.space_after = Pt(2)

    p_rig = tf_p.add_paragraph()
    r_rig = p_rig.add_run()
    r_rig.text = "\nMETHODOLOGICAL RIGOR & VALIDITY CONTROLS\n"
    r_rig.font.bold = True
    r_rig.font.size = Pt(8.6)
    r_rig.font.color.rgb = C_TEAL_DEEP
    disable_spellcheck(r_rig)

    safeguards_pptx = [
        ("Dual-Camera Engagement", "Active video participation & recording per IITM rubrics to verify authentic responses."),
        ("Multi-Pass Audit Trail", "Audio streams cross-audited across multiple passes to verify technical domain terminology."),
        ("Investigator Reflexivity", "Continuous peer debriefing & cross-coding among team members to prevent observer bias."),
        ("Ethical Compliance", "Informed consent captured prior to recording; full enterprise participant anonymization.")
    ]
    for sgh, sgd in safeguards_pptx:
        p_sg = tf_p.add_paragraph()
        r_sgh = p_sg.add_run()
        r_sgh.text = f"• {sgh}: "
        r_sgh.font.bold = True
        r_sgh.font.size = Pt(7.4)
        r_sgh.font.color.rgb = C_OCEAN_DARK
        disable_spellcheck(r_sgh)
        r_sgd = p_sg.add_run()
        r_sgd.text = sgd
        r_sgd.font.size = Pt(6.8)
        r_sgd.font.color.rgb = C_TEXT_MAIN
        disable_spellcheck(r_sgd)
        p_sg.space_after = Pt(2)

    tf_c = card_c.text_frame
    tf_c.word_wrap = True
    tf_c.margin_left = tf_c.margin_right = Inches(0.2)
    tf_c.margin_top = Inches(0.18)

    p_ch = tf_c.paragraphs[0]
    r_ch = p_ch.add_run()
    r_ch.text = "PRIMARY PRACTITIONER COHORT PROFILES (ANONYMIZED)\n"
    r_ch.font.bold = True
    r_ch.font.size = Pt(9.6)
    r_ch.font.color.rgb = C_BLUE_ROYAL
    disable_spellcheck(r_ch)

    cohort_pptx = [
        ("Participant 1 (3.8 YoE)", "Software Developer | AI & Data Science R&D (Govt-Funded)", "Scope triage; motivating pressure dynamics; risk-based debt rules (B1 balancing loop). Dual-camera verified [03:50]."),
        ("Participant 2 (2.0 YoE)", "Software Developer | Enterprise Backend & Consulting (Deloitte)", "Inherited legacy frameworks; microservices architecture overhead; pre-QA mock DB isolation and automated contract testing."),
        ("Participant 3 (6.5 YoE)", "SDE-4 Systems & Firmware | Consumer Tech & Embedded (Apple)", "Urgent bugs taking 8–10h/day; multi-ETA pushback (B2); readable code as primary maintenance leverage [07:53, 08:14, 09:34]."),
        ("Participant 4 (5.0+ YoE)", "Software Engineer | HR-Tech & Global Payroll SaaS (Deel)", "18-item debt backlog deferred under launch velocity; developer cognitive depletion; recovery breaks as critical control [05:10]."),
        ("Participant 5 (3.0 YoE)", "CV & Full-Stack Engineer | Industrial AI & Automation (Siemens)", "API handler bypass; fear of touching legacy black-box code; formal sprint debt token capacity allocation [00:52].")
    ]
    for p_head, p_sub, p_foc in cohort_pptx:
        p_item = tf_c.add_paragraph()
        r_ih = p_item.add_run()
        r_ih.text = f"• {p_head} — {p_sub}\n   "
        r_ih.font.bold = True
        r_ih.font.size = Pt(7.8)
        r_ih.font.color.rgb = C_OCEAN_DARK
        disable_spellcheck(r_ih)
        r_if = p_item.add_run()
        r_if.text = f"Qualitative Contribution: {p_foc}"
        r_if.font.italic = True
        r_if.font.size = Pt(7.1)
        r_if.font.color.rgb = C_TEXT_MUTED
        disable_spellcheck(r_if)
        p_item.space_after = Pt(4)

    tf_s = card_s.text_frame
    tf_s.word_wrap = True
    tf_s.margin_left = tf_s.margin_right = Inches(0.2)
    tf_s.margin_top = Inches(0.15)

    p_sh = tf_s.paragraphs[0]
    r_sh = p_sh.add_run()
    r_sh.text = "SAMPLING STRATEGY & SECONDARY LITERATURE SOURCES\n"
    r_sh.font.bold = True
    r_sh.font.size = Pt(9.0)
    r_sh.font.color.rgb = C_AMBER_WARM
    disable_spellcheck(r_sh)

    p_sb = tf_s.add_paragraph()
    r_sb1 = p_sb.add_run()
    r_sb1.text = (
        "Purposive Sampling Criteria: 4 practitioners with 3+ years of industry experience, plus 1 practitioner with 2 years "
        "in enterprise digital consulting (Deloitte). Encompasses diverse paradigms across Global SaaS, Embedded Firmware, Industrial AI, "
        "Enterprise Consulting, and Government R&D (20.3 cumulative years of engineering practice).\n"
        "Full Academic Literature Grounding (APA 7th Edition):\n"
        "• Edmondson, A. (1999). Psychological safety and learning behavior in work teams. Adm. Sci. Q., 44(2), 350-383.\n"
        "• Forsgren, N., Humble, J., & Kim, G. (2018). Accelerate: Science of lean software and DevOps. IT Rev. Press.\n"
        "• Senge, P. M. (1990). The fifth discipline: Art and practice of the learning organization. Doubleday.\n"
        "• Waters Center for Systems Thinking. (2020). Systems thinking in schools and organizations. Waters Center."
    )
    r_sb1.font.size = Pt(7.0)
    r_sb1.font.color.rgb = C_TEXT_MAIN
    disable_spellcheck(r_sb1)

    # =========================================================================
    # SLIDE 2: ANALYSIS & THEMATIC PATTERNS (5 MARKS) - Dim Watermark Pic 3 (Money)
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_slide_frame(s2, "Cross-Interview Thematic Patterns",
                    "EMPIRICAL ANALYSIS & THEMATIC FINDINGS (1 OF 2)", "icon_video.png", C_BG_S2,
                    "Edmondson (1999); Forsgren et al. (2018); Senge (1990); Waters Center (2020)")

    card_w = Inches(5.2)
    card_h = Inches(2.65)
    gap_x = Inches(0.2)
    gap_y = Inches(0.18)

    cards_s2 = []
    for cx, cy in [(left_x, top_y), (left_x + card_w + gap_x, top_y),
                   (left_x, top_y + card_h + gap_y), (left_x + card_w + gap_x, top_y + card_h + gap_y)]:
        card = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, cy, card_w, card_h)
        card.fill.solid()
        card.fill.fore_color.rgb = RGBColor(255, 255, 255)
        card.line.color.rgb = C_BORDER
        card.line.width = Pt(1.0)
        cards_s2.append(card)

    if os.path.exists("watermark_slide_2.png"):
        s2.shapes.add_picture("watermark_slide_2.png", Inches(3.6), Inches(1.8), Inches(6.1), Inches(4.6))

    themes_pptx = [
        (cards_s2[0],
         "Pattern 1: The 'Fixes That Fail' Quick-Fix Trap",
         "Supported by 4 of 5 (Directly seen by 3; temporary patches by 1)",
         C_CORAL_RED,
         "Under market launches or demo pressures, teams bypass service layers or skip automated tests. While immediate symptomatic success is achieved, it seeds delayed technical liabilities.",
         "“Due to tight deadlines or business priorities, we choose quicker implementation... [01:36] ...sometimes this creates a whole kind of a mess.” [02:47] (Participant 4 — SaaS)\n“Instead of building a proper service layer, the team put business logic in API handlers... it worked, demo went well, and the shortcut felt like the right call.” [00:52] (Participant 5 — AI/CV)",
         "Secondary Finding: Senge's (1990) Fixes that Fail archetype. Part. 2 noted unclear requirements & legacy systems also trigger debt."),

        (cards_s2[1],
         "Pattern 2: The 'Next Sprint Never Comes' Dilemma",
         "Described directly by 2 of 5 (Participant 4 & Participant 5)",
         C_AMBER_WARM,
         "Debt is openly recognized and logged in retrospectives, but new feature requests consistently take precedence. Because debt is invisible to non-technical leaders, remediation is kicked to a 'next sprint' that never arrives.",
         "“...we already had 18 items in our backlog... we decided to take the backlog things first...” [07:05] (Participant 4 — SaaS)\n“The pressure to keep shipping does take over... cleanup kept happening to the next sprint, and the next sprint just never came.” [03:25] (Participant 5 — AI/CV)",
         "Secondary Finding: Waters Center (2020) on Shifting the Burden and compounding structural delays."),

        (cards_s2[2],
         "Pattern 3: Developer Fatigue & the Burnout Trap",
         "2 of 5 directly (P4, P5), plus heavy workload for 2 (P2, P3)",
         C_BLUE_ROYAL,
         "Unvalidated shortcuts degrade system stability, forcing intensive emergency firefighting. The cognitive strain and fear of touching black-box files directly deplete productivity.",
         "“It can become mentally exhausting... lots of miscommunication happens... even good engineers can become less productive.” [03:28-03:55] (Participant 4 — SaaS)\n“Couple of good developers were clearly burnt out... Over time people grew not to touch certain files, like a black box.” [02:44] (Participant 5 — AI/CV)\n“Maybe like eight to 10 hours a day to, like, in order to, like, fix that issue.” [07:53–07:58] (Participant 3 — Firmware)",
         "Secondary Finding: Forsgren et al. (2018) / DORA linking deployment pain and rework to developer burnout."),

        (cards_s2[3],
         "Pattern 4: Communication Gap & Reframing Debt",
         "Supported by 3 of 5 (Part. 1, 4, 3; business reframing by Part. 5)",
         C_TEAL_DEEP,
         "Engineering concerns framed solely as 'code hygiene' are deprioritized by leadership. Breaking the cycle requires psychological safety and translating technical risks into business metrics.",
         "“...high pressure does actually end up motivating me more to work on it.” [05:42] (Participant 1 — R&D)\n“...we kind of push engineers to take a break... [05:10] ...giving the engineers really good ownership... time is the key...” [05:47] (Participant 4 — SaaS)\n“Part of the problem was on our side... leadership cares about delivery speed, impact... and we were not speaking that language.” [04:12] (Participant 5 — AI/CV)",
         "Secondary Finding: Edmondson (1999) on psychological safety: teams can only push back when culture permits open voice.")
    ]

    for card, ctitle, ccount, ccol, cexp, cquotes, csec in themes_pptx:
        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_left = ctf.margin_right = Inches(0.18)
        ctf.margin_top = Inches(0.12)

        p_t = ctf.paragraphs[0]
        r_t = p_t.add_run()
        r_t.text = f"{ctitle}\n"
        r_t.font.bold = True
        r_t.font.size = Pt(8.6)
        r_t.font.color.rgb = ccol
        disable_spellcheck(r_t)

        r_cnt = p_t.add_run()
        r_cnt.text = f"Empirical Prevalence: {ccount}\n"
        r_cnt.font.bold = True
        r_cnt.font.size = Pt(7.0)
        r_cnt.font.color.rgb = C_OCEAN_DARK
        disable_spellcheck(r_cnt)

        p_e = ctf.add_paragraph()
        r_e = p_e.add_run()
        r_e.text = f"{cexp}\n"
        r_e.font.size = Pt(6.8)
        r_e.font.color.rgb = C_TEXT_MAIN
        disable_spellcheck(r_e)

        r_q = p_e.add_run()
        r_q.text = f"{cquotes}\n"
        r_q.font.italic = True
        r_q.font.size = Pt(6.2)
        r_q.font.color.rgb = RGBColor(71, 85, 105)
        disable_spellcheck(r_q)

        r_sc = p_e.add_run()
        r_sc.text = f"{csec}"
        r_sc.font.bold = True
        r_sc.font.size = Pt(6.2)
        r_sc.font.color.rgb = ccol
        disable_spellcheck(r_sc)

    # =========================================================================
    # SLIDE 3: RECOMMENDATIONS (5 MARKS) - Dim Watermark Pic 2 (Fishing)
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_slide_frame(s3, "Actionable Engineering & Governance Recommendations",
                    "STRATEGIC RECOMMENDATIONS (2 OF 2)", "icon_bulb.png", C_BG_S3,
                    "Edmondson (1999); Forsgren et al. (2018); Waters Center (2020)")

    col_w = Inches(3.45)
    col_gap = Inches(0.2)

    cards_s3 = []
    for idx in range(3):
        rx = left_x + idx * (col_w + col_gap)
        card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, top_y, col_w, box_h)
        card.fill.solid()
        card.fill.fore_color.rgb = RGBColor(255, 255, 255)
        card.line.color.rgb = C_BORDER
        card.line.width = Pt(1.0)
        cards_s3.append(card)

    if os.path.exists("watermark_slide_3.png"):
        s3.shapes.add_picture("watermark_slide_3.png", Inches(3.5), Inches(1.8), Inches(6.3), Inches(4.6))

    recs_pptx = [
        (cards_s3[0],
         "1. Debt Budget & Triage",
         "Sprint Token Allocation & Risk Rules",
         C_CORAL_RED,
         "Target Problem & Root Cause:",
         "The 'Next Sprint Never Comes' paradox (Waters Center, 2020). Engineering refactoring requests framed as abstract 'code quality' stall because business leadership prioritizes near-term feature delivery.",
         "Actionable Implementation Protocol:",
         "• Formal Debt Budget: Reserve a fixed share of each sprint's story points/tokens explicitly for architectural refactoring, pre-negotiated with Product Management (Participant 5).\n• 2-Tier Risk Triage Matrix: Fix immediately if defect threatens cross-service contract stability or system scalability; apply temporary patch if localized and non-critical (Participant 1 [03:50], Participant 3 [02:59–03:06]).\n• Business Translation: Frame technical debt in commercial risk terms (SLA downtime penalty, user churn, cloud compute waste) rather than internal aesthetic code hygiene.",
         "Our suggested targets (not from interviews):",
         "• Dedicated Sprint Debt Ratio: Target ≥ 15% capacity allocated to debt tickets.\n• Backlog Debt Age: Max 45 days before compulsory review/remediation.\n• Unplanned Firefighting Ratio: Target < 10% of engineering hours.",
         "Academic Grounding & Validation:",
         "Grounding: Senge (1990) 'Fixes that Fail'; Waters Center (2020) 'Shifting the Burden'. Supported by Participant 1 and Participant 5.",
         "Core Systemic Leverage & Outcome:",
         "Balances the R1 Quick-Fix Trap by formalizing a non-negotiable B1 refactoring buffer. Prevents invisible architectural decay from compounding into catastrophic production outages."),

        (cards_s3[1],
         "2. Testing Safety Nets",
         "Automated Pipelines & Boy Scout Rule",
         C_BLUE_ROYAL,
         "Target Problem & Root Cause:",
         "The Quick-Fix Spiral (R1). Skipping test suites to meet urgent demo commitments creates hidden regression bugs, fragile shared state, and chronic weekend emergency firefighting.",
         "Actionable Implementation Protocol:",
         "• Automated CI/CD Gates: Mandate pre-merge automated linting, unit tests, and integration pipelines as non-bypassable deployment gates (Participant 3, Participant 5).\n• Boy Scout Engineering Norm: Institutionalize the standard of leaving every touched file cleaner, better tested, and better documented than found. Participant 3 noted readable code is 'half of the work' [09:34–09:39].\n• Contract & Mock Isolation: Build pre-release mock environments and automated contract tests (Participant 2) to prevent developer-QA environment mismatches and post-deploy failures.",
         "Our suggested targets (not from interviews):",
         "• DORA Change Failure Rate: Target < 5% of production releases.\n• Automated Test Coverage: Minimum 80% coverage on core business logic.\n• Mean Time to Restore (MTTR): Reduced from 8–10 hours to < 1 hour.",
         "Academic Grounding & Validation:",
         "Grounding: Forsgren et al. (2018) / DORA delivery research linking automated quality gates to reduced burnout. Supported by Participant 2, 3, and 5.",
         "Core Systemic Leverage & Outcome:",
         "Decouples delivery velocity from error injection. Automated quality gates eliminate developer-QA friction and ensure high release cadence without regression firefighting."),

        (cards_s3[2],
         "3. Safe to Push Back",
         "Psychological Safety & Recovery",
         C_TEAL_DEEP,
         "Target Problem & Root Cause:",
         "The Developer Burnout Trap (R2). When teams lack psychological safety, engineers absorb uncommunicated scope creep, silently cut corners, and experience severe cognitive exhaustion.",
         "Actionable Implementation Protocol:",
         "• Psychological Safety for Pushback: Establish cultural norms empowering engineers to challenge unrealistic delivery deadlines without fear of negative evaluation (Edmondson, 1999).\n• Multi-Stage Phased Delivery: Replace binary yes/no commitments with transparent multi-stage ETAs (e.g., MVP release vs. fully hardened architecture), providing clear trade-off dialogues (Participant 3 [08:14–08:26]).\n• Proactive Recovery Protocols: Enforce recovery breaks after intensive delivery crunches, grant genuine technical ownership, and recognize that 'time is the key' (Participant 4 [05:10, 05:47]).",
         "Our suggested targets (not from interviews):",
         "• Psychological Safety Index: Quarterly survey based on Edmondson (1999) scale.\n• Overtime Burnout Ratio: Max 1 weekend deployment per quarter per developer.\n• Engineering Retention Rate: 0% voluntary attrition due to burnout.",
         "Academic Grounding & Validation:",
         "Grounding: Edmondson (1999) on team psychological safety; Senge (1990) personal mastery. Supported by Participant 1, 3, and 4.",
         "Core Systemic Leverage & Outcome:",
         "Activates the B2 Pushback Brake to halt runaway developer cognitive depletion. Replaces arbitrary crunch with phased delivery and institutionalized recovery.")
    ]

    for card, rtitle, rsub, rcol, rch, rcd, rah, rad, rkh, rkd, rgh, rgd, roh, rod in recs_pptx:
        rtf = card.text_frame
        rtf.word_wrap = True
        rtf.margin_left = rtf.margin_right = Inches(0.18)
        rtf.margin_top = Inches(0.14)

        p_t = rtf.paragraphs[0]
        r_t = p_t.add_run()
        r_t.text = f"{rtitle}\n"
        r_t.font.bold = True
        r_t.font.size = Pt(9.8)
        r_t.font.color.rgb = rcol
        disable_spellcheck(r_t)

        r_s = p_t.add_run()
        r_s.text = f"Protocol: {rsub}\n\n"
        r_s.font.bold = True
        r_s.font.size = Pt(7.8)
        r_s.font.color.rgb = C_OCEAN_DARK
        disable_spellcheck(r_s)

        p_c = rtf.add_paragraph()
        for head, body, bcol in [
            (rch, rcd, C_TEXT_MAIN),
            (rah, rad, C_TEXT_MAIN),
            (rkh, rkd, C_OCEAN_DARK),
            (rgh, rgd, RGBColor(71, 85, 105)),
            (roh, rod, C_TEAL_DEEP)
        ]:
            rh = p_c.add_run()
            rh.text = f"{head}\n"
            rh.font.bold = True
            rh.font.size = Pt(7.4)
            rh.font.color.rgb = rcol
            disable_spellcheck(rh)

            rb = p_c.add_run()
            rb.text = f"{body}\n\n"
            rb.font.size = Pt(6.8)
            rb.font.color.rgb = bcol
            disable_spellcheck(rb)

    # =========================================================================
    # SLIDE 4: INFLUENCE MODEL (5 MARKS) - BIGGER, WIDER PICTURE + BOTTOM SUMMARY
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_slide_frame(s4, "Systems Thinking Influence Model: Causal Loop Analysis",
                    "SYSTEMS THINKING INFLUENCE MODEL (5 MARKS)", "icon_gears.png", C_BG_S4,
                    "Edmondson (1999); Forsgren et al. (2018); Senge (1990); Waters Center (2020)")

    cld_top_w = Inches(10.6)
    cld_top_h = Inches(4.15)
    if os.path.exists("influence_model_cld.png"):
        s4.shapes.add_picture("influence_model_cld.png", left_x, Inches(1.35), cld_top_w, cld_top_h)

    bot_y = Inches(5.60)
    bot_h = Inches(1.35)
    cld_card_w = Inches(2.55)
    cld_gap = Inches(0.13)

    cld_bottom_data = [
        ("R1: Quick-Fix Spiral (Reinforcing)",
         "Pressure (+) -> Quick Fixes (+) -> Tech Debt (+) -> Complexity & Rework (+) -> Production Firefighting (+) -> Pressure (+). Fits Senge (1990) Fixes that Fail.",
         C_CORAL_RED, RGBColor(255, 241, 242), RGBColor(254, 205, 211)),
        ("R2: Burnout Trap (Reinforcing)",
         "Firefighting (+) -> Developer Fatigue (+) -> Velocity (-) -> Pressure (- inverse). Pushes engineers to cognitive limits where they fear touching black-box code.",
         C_CORAL_RED, RGBColor(255, 241, 242), RGBColor(254, 205, 211)),
        ("B1: Debt Buffer (Balancing)",
         "Tech Debt (+) -> Sprint Token Capacity (+) -> Debt (-). Dedicated refactoring buffer stabilizes code quality and prevents compounding architectural debt.",
         C_TEAL_DEEP, RGBColor(240, 253, 250), RGBColor(153, 246, 228)),
        ("B2: Pushback Brake (Balancing)",
         "Fatigue (+) -> Scope Pushback (+) -> Pressure (-). High Psychological Safety enables pushback to de-escalate unrealistic deadlines before burnout occurs.",
         C_TEAL_DEEP, RGBColor(240, 253, 250), RGBColor(153, 246, 228))
    ]

    for idx, (ltitle, ldesc, lcol, lbg, lbord) in enumerate(cld_bottom_data):
        lx = left_x + idx * (cld_card_w + cld_gap)
        card = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, lx, bot_y, cld_card_w, bot_h)
        card.fill.solid()
        card.fill.fore_color.rgb = lbg
        card.line.color.rgb = lbord
        card.line.width = Pt(1.0)

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_left = ctf.margin_right = Inches(0.12)
        ctf.margin_top = Inches(0.08)

        p_t = ctf.paragraphs[0]
        r_t = p_t.add_run()
        r_t.text = f"{ltitle}\n"
        r_t.font.bold = True
        r_t.font.size = Pt(7.4)
        r_t.font.color.rgb = lcol
        disable_spellcheck(r_t)

        p_d = ctf.add_paragraph()
        r_d = p_d.add_run()
        r_d.text = ldesc
        r_d.font.size = Pt(6.2)
        r_d.font.color.rgb = C_TEXT_MAIN
        disable_spellcheck(r_d)

    # =========================================================================
    # SLIDE 5: PROJECT REVIEW & CLOSURE - Dim Watermark Pic 1 (Sword & Anvil)
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_slide_frame(s5, "Project Review, Governance & Closure",
                    "PROJECT REVIEW & CLOSURE", "icon_trophy.png", C_BG_S5,
                    "IIT Madras BS Degree Programme  •  BSGN3001 Team 114: Iterate")

    card_t = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_x, top_y, Inches(5.35), box_h)
    card_t.fill.solid()
    card_t.fill.fore_color.rgb = RGBColor(255, 255, 255)
    card_t.line.color.rgb = C_BORDER
    card_t.line.width = Pt(1.0)

    rt_x = Inches(6.9)
    rt_w = Inches(5.6)
    card_cont = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rt_x, top_y, rt_w, Inches(2.4))
    card_cont.fill.solid()
    card_cont.fill.fore_color.rgb = RGBColor(255, 255, 255)
    card_cont.line.color.rgb = C_BORDER
    card_cont.line.width = Pt(1.0)

    cb_y = top_y + Inches(2.55)
    cb_h = box_h - Inches(2.55)
    card_bp = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rt_x, cb_y, rt_w, cb_h)
    card_bp.fill.solid()
    card_bp.fill.fore_color.rgb = RGBColor(254, 252, 246)
    card_bp.line.color.rgb = RGBColor(253, 230, 138)
    card_bp.line.width = Pt(1.0)

    if os.path.exists("watermark_slide_5.png"):
        s5.shapes.add_picture("watermark_slide_5.png", Inches(3.6), Inches(1.8), Inches(6.2), Inches(4.6))

    ttf = card_t.text_frame
    ttf.word_wrap = True
    ttf.margin_left = ttf.margin_right = Inches(0.2)
    ttf.margin_top = Inches(0.18)

    tp0 = ttf.paragraphs[0]
    tr0 = tp0.add_run()
    tr0.text = "MEMBER TASK ATTRIBUTION & FIELDWORK OWNERSHIP\n"
    tr0.font.bold = True
    tr0.font.size = Pt(9.0)
    tr0.font.color.rgb = C_OCEAN_DARK
    disable_spellcheck(tr0)

    member_tasks = [
        ("Samyabrata Roy (22F2001443)", "Team Lead",
         "Fieldwork: Rounak Biswas (3.8 YoE, AI/ML R&D). Authored scope triage analysis, secondary systems literature review, and final consolidation.\nReflection: Observed that unmanaged backlog debt inevitably flips motivating deadline pressure into cognitive overload."),
        ("Abir Saha (23F3001436)", "Project Manager",
         "Fieldwork: Anunay Sinha (2.0 YoE, Deloitte Consulting). Synthesized legacy framework debt, microservices overhead, and managed milestone schedules.\nReflection: Enterprise legacy debt heavily burdens newer engineers; pre-QA mock isolation is vital for build stability."),
        ("Rishabh Barthwal (23F2004112)", "Research Lead",
         "Fieldwork: Suraj Sajeev (6.5 YoE, Apple Firmware). Transcribed and coded shared-variable race conditions, multi-ETA pushback rules, and verified timestamps.\nReflection: 8–10h firefighting stems from poorly isolated shared state; readable code is 'half of the work' in system maintainability."),
        ("Piyush Tilokchandani (21F1006739)", "Design Lead",
         "Fieldwork: Keshav Gupta (5.0+ YoE, Deel SaaS). Synthesized 18-item debt deferral, cognitive fatigue dynamics, recovery protocols, and led rubric audit.\nReflection: Technical debt is an organizational human systems failure; developer cognitive recovery is an essential engineering control."),
        ("Ramrup Satpati (24F3004027)", "Creative & Presentation Lead",
         "Fieldwork: Shubham Mishra (3.0 YoE, Siemens Automation). Modeled Causal Loop Diagram (CLD) archetypes, designed deck architecture, and compiled vector PDFs.\nReflection: API-handler shortcuts create team-wide 'black-box' code fear; formal sprint token capacity is mandatory for refactoring.")
    ]
    for mname, mrole, mdesc in member_tasks:
        p_m = ttf.add_paragraph()
        r_mn = p_m.add_run()
        r_mn.text = f"• {mname} — {mrole}\n  "
        r_mn.font.bold = True
        r_mn.font.size = Pt(7.2)
        r_mn.font.color.rgb = C_CORAL_RED
        disable_spellcheck(r_mn)

        r_md = p_m.add_run()
        r_md.text = mdesc
        r_md.font.size = Pt(6.5)
        r_md.font.color.rgb = C_TEXT_MAIN
        disable_spellcheck(r_md)
        p_m.space_after = Pt(2)

    p_tg = ttf.add_paragraph()
    r_tgh = p_tg.add_run()
    r_tgh.text = "\nTEAM COLLABORATION & GOVERNANCE MECHANISMS\n"
    r_tgh.font.bold = True
    r_tgh.font.size = Pt(8.2)
    r_tgh.font.color.rgb = C_TEAL_DEEP
    disable_spellcheck(r_tgh)

    team_gov = [
        ("Sync Cadence", "Bi-weekly sprint syncs, shared cloud repository for transcript audits, and collaborative peer-coding sessions."),
        ("Consensus Modeling", "Unanimous democratic consensus on archetype classifications (R1, R2, B1, B2) and qualitative interpretations."),
        ("Rubric Audit", "Dedicated pre-submission audit pass verifying all GP2 Deliverable 1.c and 1.a criteria, citations, and formatting benchmarks.")
    ]
    for gh, gd in team_gov:
        p_g = ttf.add_paragraph()
        r_gh = p_g.add_run()
        r_gh.text = f"• {gh}: "
        r_gh.font.bold = True
        r_gh.font.size = Pt(7.0)
        r_gh.font.color.rgb = C_OCEAN_DARK
        disable_spellcheck(r_gh)
        r_gd = p_g.add_run()
        r_gd.text = gd
        r_gd.font.size = Pt(6.4)
        r_gd.font.color.rgb = C_TEXT_MAIN
        disable_spellcheck(r_gd)
        p_g.space_after = Pt(1)

    ctf = card_cont.text_frame
    ctf.word_wrap = True
    ctf.margin_left = ctf.margin_right = Inches(0.2)
    ctf.margin_top = Inches(0.15)

    cp0 = ctf.paragraphs[0]
    cr0 = cp0.add_run()
    cr0.text = "COURSE CONTINUITY & INTERVIEWEE ROSTER CHANGES\n"
    cr0.font.bold = True
    cr0.font.size = Pt(8.8)
    cr0.font.color.rgb = C_BLUE_ROYAL
    disable_spellcheck(cr0)

    cp1 = ctf.add_paragraph()
    cr1 = cp1.add_run()
    cr1.text = (
        "• Course Continuity: 100% Active Retention. All 5 members completed their individual interviews, "
        "submitted interim reports, and actively contributed to this consolidated report. Zero opt-outs / dropouts.\n"
        "• Interviewee Roster Changes:\n"
        "   1. Participant 1 Change: Aakash Verma (GP1) was replaced by Rounak Biswas due to work scheduling unavailability "
        "(documented with email correspondence).\n"
        "   2. Participant 3 Change: Vikramaditya was replaced by Suraj Sajeev (6.5 YoE, Systems & Firmware) due to timeline conflicts.\n"
        "• Cohort Balance: 20.3 cumulative years of engineering practice across 5 distinct domains (SaaS, Embedded, AI, Consulting, and R&D)."
    )
    cr1.font.size = Pt(6.6)
    cr1.font.color.rgb = C_TEXT_MAIN
    disable_spellcheck(cr1)

    btf = card_bp.text_frame
    btf.word_wrap = True
    btf.margin_left = btf.margin_right = Inches(0.2)
    btf.margin_top = Inches(0.15)

    bp0 = btf.paragraphs[0]
    br0 = bp0.add_run()
    br0.text = "CHALLENGES, BEST PRACTICES & STRATEGIC ROADMAP\n"
    br0.font.bold = True
    br0.font.size = Pt(8.6)
    br0.font.color.rgb = C_AMBER_WARM
    disable_spellcheck(br0)

    bp1 = btf.add_paragraph()
    br1 = bp1.add_run()
    br1.text = (
        "• Methodological Challenges Overcome:\n"
        "   1. Cross-Domain Synthesis: Bridging embedded firmware lifecycles (Apple) with rapid-cadence SaaS architectures (Deel) via systems archetypes (R1/R2 loops).\n"
        "   2. Verbatim Auditing Rigor: Disentangling technical jargon, acronyms, and multi-track audio across 5 sessions using 3-pass verification.\n"
        "   3. Investigator Bias Mitigation: Structured peer debriefing and cross-coding among all team members to ensure objective qualitative interpretation.\n"
        "• Engineering Leadership Best Practices Institutionalized:\n"
        "   1. Dedicated Sprint Debt Allocation: Translating architectural debt into business risk terms (SLA penalties, customer churn) to secure refactoring buy-in.\n"
        "   2. Automated Non-Bypassable Gates: CI/CD quality pipelines decouple deployment velocity from defect injection, eliminating firefighting.\n"
        "   3. Psychological Safety for Pushback: Multi-stage phased ETAs (MVP vs. hardened architecture) empower engineers to challenge unrealistic deadlines.\n"
        "• Future Longitudinal Research Directions (GP3 Horizon):\n"
        "   Extend qualitative fieldwork into a large-scale quantitative survey instrument (N ≥ 100 engineering teams) to measure empirical causal coefficients linking debt age, test coverage, and voluntary developer attrition.\n"
        "• Final Team Review & Unanimous Sign-Off:\n"
        "   All 5 team members conducted an exhaustive joint audit, verified all qualitative attributions against video recordings, and unanimously approved this consolidated dossier on 17-Nov-2026."
    )
    br1.font.size = Pt(6.5)
    br1.font.color.rgb = C_TEXT_MAIN
    disable_spellcheck(br1)

    pptx_path = "Team_114_Iterate_Team_Proj_Report.pptx"
    prs.save(pptx_path)
    shutil.copyfile(pptx_path, "Team_114_SPG_GP2_Sep_2026.pptx")
    print(f"[*] Successfully generated PowerPoint: {pptx_path} (and copy Team_114_SPG_GP2_Sep_2026.pptx)")


# =============================================================================
# BUILD VECTOR PDF (ReportLab)
# =============================================================================
def build_pdf():
    pdf_path = "Team_114_Iterate_Team_Proj_Report.pdf"
    PAGE_WIDTH, PAGE_HEIGHT = landscape(letter)  # 792 x 612 pt
    c = canvas.Canvas(pdf_path, pagesize=(PAGE_WIDTH, PAGE_HEIGHT))

    def draw_top_down(flowable, x, top_y, w, max_h):
        _, used_h = flowable.wrap(w, max_h)
        flowable.drawOn(c, x, top_y - used_h)
        return used_h

    def draw_page_frame(title_text, category_text, icon_name="icon_rocket.png", bg_color=HEX_BG_S1, apa_text=None):
        c.setFillColor(bg_color)
        c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

        # Digital tech bubble top-left
        if os.path.exists(icon_name):
            c.drawImage(icon_name, 22, PAGE_HEIGHT - 65, width=48, height=48, mask='auto')

        # Top-right IITM Logo (Cleanly inside bounds)
        if os.path.exists("iitm_logo_clean.png"):
            c.drawImage("iitm_logo_clean.png", PAGE_WIDTH - 76, PAGE_HEIGHT - 66, width=54, height=54, mask='auto')

        # Category and Title
        c.setFillColor(HEX_CORAL_RED)
        c.setFont("Helvetica-Bold", 8.8)
        c.drawString(82, PAGE_HEIGHT - 32, category_text.upper())

        c.setFillColor(HEX_OCEAN_DARK)
        c.setFont("Helvetica-Bold", 15.5)
        c.drawString(82, PAGE_HEIGHT - 52, title_text)

        # Header underline
        c.setStrokeColor(HEX_CORAL_RED)
        c.setLineWidth(1.2)
        c.line(82, PAGE_HEIGHT - 62, PAGE_WIDTH - 82, PAGE_HEIGHT - 62)

        # Footer divider
        c.setStrokeColor(HexColor("#e2e8f0"))
        c.setLineWidth(0.8)
        c.line(82, 26, PAGE_WIDTH - 82, 26)

        # Left Footer
        c.setFillColor(HEX_TEXT_MUTED)
        c.setFont("Helvetica", 7.2)
        c.drawString(82, 14, "Team 114: Iterate  •  Beyond Quick Fixes: Technical Debt & Fatigue  •  GP2 Deliverable 1.c")

        # Right Footer (Citations)
        if apa_text:
            c.setFillColor(HEX_TEAL_DEEP)
            c.setFont("Helvetica-Bold", 6.8)
            c.drawRightString(PAGE_WIDTH - 82, 14, f"Citations: {apa_text}")

        # Page flip design at bottom right corner on every slide
        if os.path.exists("page_flip_corner.png"):
            c.drawImage("page_flip_corner.png", PAGE_WIDTH - 52, 0, width=52, height=75, mask='auto')

    # =========================================================================
    # PDF SLIDE 0: COVER SLIDE - 5 MEMBER PHOTO CARDS (Centered in Middle)
    # =========================================================================
    c.setFillColor(HEX_BG_S0)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    # Left Margin: Tech Icon Bubbles replacing flowers
    if os.path.exists("icon_rocket.png"):
        c.drawImage("icon_rocket.png", 24, PAGE_HEIGHT - 75, width=48, height=48, mask='auto')
    if os.path.exists("icon_gears.png"):
        c.drawImage("icon_gears.png", 42, PAGE_HEIGHT - 120, width=42, height=42, mask='auto')
    if os.path.exists("icon_trophy.png"):
        c.drawImage("icon_trophy.png", 22, PAGE_HEIGHT - 162, width=38, height=38, mask='auto')

    if os.path.exists("icon_dollar.png"):
        c.drawImage("icon_dollar.png", 22, 125, width=40, height=40, mask='auto')
    if os.path.exists("icon_search.png"):
        c.drawImage("icon_search.png", 44, 78, width=42, height=42, mask='auto')
    if os.path.exists("icon_bulb.png"):
        c.drawImage("icon_bulb.png", 20, 28, width=46, height=46, mask='auto')

    card_x = 95
    card_y = 35
    card_w = PAGE_WIDTH - 150  # 642 pt
    card_h = PAGE_HEIGHT - 70  # 542 pt

    c.setFillColor(HEX_CARD_BG)
    c.setStrokeColor(HEX_BORDER)
    c.setLineWidth(1.2)
    c.roundRect(card_x, card_y, card_w, card_h, 8, fill=1, stroke=1)

    # Restore Frontpage Watermark inside the card
    if os.path.exists("cover_watermark.png"):
        c.drawImage("cover_watermark.png", card_x + 2, card_y + 2, width=card_w - 4, height=card_h - 4, mask='auto')

    # Top-right IITM Logo inside the card (Fully visible, 100% unhidden!)
    if os.path.exists("iitm_logo_clean.png"):
        c.drawImage("iitm_logo_clean.png", card_x + card_w - 85, card_y + card_h - 85, width=72, height=72, mask='auto')

    c.setFillColor(HEX_CORAL_RED)
    c.setFont("Helvetica-Bold", 9.5)
    c.drawString(card_x + 30, card_y + card_h - 32, "IIT MADRAS BS DEGREE PROGRAMME")

    c.setFillColor(HEX_TEXT_MUTED)
    c.setFont("Helvetica-Bold", 8.2)
    c.drawString(card_x + 30, card_y + card_h - 48, "BSGN3001: STRATEGIES FOR PROFESSIONAL GROWTH  •  GROUP PROJECT 2 (GP2)")

    title_p = (
        "<b><font size='16' color='#0f2942'>"
        "Beyond Quick Fixes: Exploring Technical Debt &<br/>"
        "Developer Fatigue Through Systems Thinking"
        "</font></b>"
    )
    p_title = Paragraph(title_p, ParagraphStyle('CovTitle', fontName='Helvetica', leading=20))
    draw_top_down(p_title, card_x + 30, card_y + card_h - 60, card_w - 120, 60)

    c.setFillColor(HEX_TEAL_DEEP)
    c.setFont("Helvetica-Oblique", 9.2)
    c.drawString(card_x + 30, card_y + card_h - 110, "Linking Systems Thinking (Week 10) and Engineering Sense (Week 11)   |   TEAM 114: ITERATE")

    # 5 Member Profile Cards - POSITIONED UP TOWARDS THE MIDDLE
    members_roster = [
        ("Samyabrata Roy", "22F2001443", "Team Lead", "circle_samyabrata.png"),
        ("Abir Saha", "23F3001436", "Project Manager", "circle_abir.png"),
        ("Rishabh Barthwal", "23F2004112", "Research Lead", "circle_rishabh.png"),
        ("Piyush Tilokchandani", "21F1006739", "Design Lead", "circle_piyush.png"),
        ("Ramrup Satpati", "24F3004027", "Creative & Pres. Lead", "circle_ramrup.png"),
    ]

    mem_start_x = card_x + 22
    mem_w_pdf = 114
    mem_gap_pdf = (card_w - 44 - (5 * mem_w_pdf)) / 4  # exact even spacing
    mem_y_pdf = card_y + 125   # Vertically centered in the middle of the card
    mem_h_pdf = 238            # Taller card

    for idx, (mname, mroll, mrole, mavatar) in enumerate(members_roster):
        mx = mem_start_x + idx * (mem_w_pdf + mem_gap_pdf)
        c.setFillColor(HEX_CARD_BG)
        c.setStrokeColor(HEX_BORDER)
        c.setLineWidth(1.0)
        c.roundRect(mx, mem_y_pdf, mem_w_pdf, mem_h_pdf, 6, fill=1, stroke=1)

        # Bigger Circular Avatar Photo
        if os.path.exists(mavatar):
            photo_size = 98
            px = mx + (mem_w_pdf - photo_size) / 2
            py = mem_y_pdf + mem_h_pdf - photo_size - 14
            c.drawImage(mavatar, px, py, width=photo_size, height=photo_size, mask='auto')

        # Member details below photo
        c.setFillColor(HEX_OCEAN_DARK)
        c.setFont("Helvetica-Bold", 8.4)
        c.drawCentredString(mx + mem_w_pdf/2, mem_y_pdf + 92, mname)

        c.setFillColor(HEX_TEXT_MUTED)
        c.setFont("Helvetica", 7.2)
        c.drawCentredString(mx + mem_w_pdf/2, mem_y_pdf + 76, f"Roll: {mroll}")

        # Role pill
        c.setFillColor(HexColor("#fff1f2"))
        c.setStrokeColor(HexColor("#fecdd3"))
        c.setLineWidth(0.8)
        c.roundRect(mx + 8, mem_y_pdf + 14, mem_w_pdf - 16, 42, 4, fill=1, stroke=1)

        c.setFillColor(HEX_CORAL_RED)
        c.setFont("Helvetica-Bold", 7.0)
        if "Pres." in mrole:
            c.drawCentredString(mx + mem_w_pdf/2, mem_y_pdf + 35, "Creative &")
            c.drawCentredString(mx + mem_w_pdf/2, mem_y_pdf + 23, "Presentation Lead")
        else:
            c.drawCentredString(mx + mem_w_pdf/2, mem_y_pdf + 29, mrole)

    # Bottom overview pill
    bot_pill_y = card_y + 16
    bot_pill_h = 88
    c.setFillColor(HexColor("#f1f5f9"))
    c.setStrokeColor(HEX_BORDER)
    c.roundRect(card_x + 20, bot_pill_y, card_w - 40, bot_pill_h, 6, fill=1, stroke=1)

    c.setFillColor(HEX_OCEAN_DARK)
    c.setFont("Helvetica-Bold", 8.0)
    c.drawString(card_x + 30, bot_pill_y + bot_pill_h - 18, "Deliverable Overview & Alignment:")

    cov_desc = (
        "Consolidated synthesis of 5 primary practitioner interviews and secondary systems literature. "
        "Investigates the causal drivers of technical debt shortcuts, compounding friction, and developer burnout. "
        "Submitted for Evaluation | Term: September 2026."
    )
    p_cdesc = Paragraph(f"<font size='7.2' color='#1e293b'>{cov_desc}</font>",
                        ParagraphStyle('CovD', fontName='Helvetica', fontSize=7.2, leading=9.6))
    draw_top_down(p_cdesc, card_x + 30, bot_pill_y + bot_pill_h - 26, card_w - 60, 55)

    if os.path.exists("page_flip_corner.png"):
        c.drawImage("page_flip_corner.png", PAGE_WIDTH - 52, 0, width=52, height=75, mask='auto')

    c.showPage()

    # =========================================================================
    # PDF SLIDE 1: METHODOLOGY (5 MARKS) - Dim Watermark Pic 4 (VR)
    # =========================================================================
    draw_page_frame("How We Did the Study (Methodology)",
                    "RESEARCH METHODOLOGY (5 MARKS)", "icon_search.png", HEX_BG_S1,
                    "Edmondson (1999); Forsgren et al. (2018); Senge (1990); Waters Center (2020)")

    s_x = 82
    b_w = PAGE_WIDTH - 164
    b_y = 36
    b_h = PAGE_HEIGHT - 110

    p1_left_w = (b_w - 14) * 0.43
    p1_right_w = (b_w - 14) * 0.57
    p1_right_x = s_x + p1_left_w + 14

    # 1. Draw Card Backgrounds First
    c.setFillColor(HEX_CARD_BG)
    c.setStrokeColor(HEX_BORDER)
    c.roundRect(s_x, b_y, p1_left_w, b_h, 6, fill=1, stroke=1)

    p1_cohort_h = 275
    c.roundRect(p1_right_x, b_y + b_h - p1_cohort_h, p1_right_w, p1_cohort_h, 6, fill=1, stroke=1)

    p1_samp_h = b_h - p1_cohort_h - 10
    c.setFillColor(HexColor("#fefcf6"))
    c.setStrokeColor(HexColor("#fde68a"))
    c.roundRect(p1_right_x, b_y, p1_right_w, p1_samp_h, 6, fill=1, stroke=1)

    # 2. Draw Dim Watermark ON TOP of cards (subtle, clearly visible!)
    if os.path.exists("watermark_slide_1.png"):
        c.drawImage("watermark_slide_1.png", s_x + 50, b_y + 35, width=b_w - 100, height=b_h - 70, mask='auto')

    # 3. Draw Text ON TOP of watermark
    c.setFillColor(HEX_TEAL_DEEP)
    c.setFont("Helvetica-Bold", 9.4)
    c.drawString(s_x + 14, b_y + b_h - 18, "5-STAGE QUALITATIVE PROCESS FLOW")

    stages_text = [
        ("Stage 1: Study Design & Ethical Protocol Framing",
         "Anchored semi-structured qualitative interview questions in Peter Senge's (1990) Systems Thinking archetypes (Fixes that Fail, Shifting the Burden). Drafted formal institutional participant briefing sheets and secured written informed consent for recording and academic analysis."),
        ("Stage 2: Primary Fieldwork Data Collection (N=5)",
         "Conducted five 1-on-1 semi-structured virtual qualitative interviews (30–45 minutes each) across diverse industry paradigms. Enforced mandatory dual-camera recording per strict IITM assessment guidelines to observe behavioral nuance and verify participant authenticity."),
        ("Stage 3: Verbatim Transcription & Multi-Pass Audit",
         "Extracted high-fidelity multi-track audio streams. Generated full verbatim transcripts utilizing speech-to-text tooling, followed by rigorous multi-pass manual audits by team members to verify technical architecture terminology and eliminate transcription artifacts."),
        ("Stage 4: Qualitative Thematic Coding & Analysis",
         "Systematically coded interview transcripts across key systems archetypes: R1 (Quick-Fix Trap), R2 (Developer Burnout Trap), B1 (Architectural Refactoring Buffer), and B2 (Psychological Safety Pushback Brake). Synthesized cross-cutting patterns across different organizational scales."),
        ("Stage 5: Empirical Triangulation & Influence Modeling",
         "Cross-validated qualitative practitioner findings against DORA empirical delivery research benchmarks (Forsgren et al., 2018) to construct our formal systems influence architecture and actionable engineering governance recommendations.")
    ]
    py_cur = b_y + b_h - 26
    for st, sd in stages_text:
        p_st = Paragraph(
            f"<b><font size='8.0' color='#0f2942'>• {st}</font></b><br/>"
            f"<font size='7.3' color='#334155'>{sd}</font>",
            ParagraphStyle('Stg', fontName='Helvetica', fontSize=7.3, leading=9.6)
        )
        h_u = draw_top_down(p_st, s_x + 14, py_cur, p1_left_w - 28, 90)
        py_cur -= (h_u + 8)

    py_cur -= 4
    c.setFillColor(HEX_TEAL_DEEP)
    c.setFont("Helvetica-Bold", 9.0)
    c.drawString(s_x + 14, py_cur, "METHODOLOGICAL RIGOR & VALIDITY CONTROLS")
    py_cur -= 14

    safeguards_pdf = [
        ("Dual-Camera Engagement", "Active video participation & screen recording per IITM rubrics to verify authentic responses."),
        ("Multi-Pass Audit Trail", "Audio streams cross-audited across multiple passes to verify technical domain terminology."),
        ("Investigator Reflexivity", "Continuous peer debriefing & cross-coding among team members to prevent observer bias."),
        ("Ethical Compliance", "Informed consent captured prior to recording; full enterprise participant anonymization.")
    ]
    for sgh, sgd in safeguards_pdf:
        p_sg = Paragraph(
            f"<b><font size='7.6' color='#0f2942'>• {sgh}:</font></b> "
            f"<font size='7.1' color='#334155'>{sgd}</font>",
            ParagraphStyle('Sg', fontName='Helvetica', fontSize=7.1, leading=9.2)
        )
        h_sg = draw_top_down(p_sg, s_x + 14, py_cur, p1_left_w - 28, 70)
        py_cur -= (h_sg + 7)

    c.setFillColor(HEX_BLUE_ROYAL)
    c.setFont("Helvetica-Bold", 9.6)
    c.drawString(p1_right_x + 14, b_y + b_h - 18, "PRIMARY PRACTITIONER COHORT PROFILES (ANONYMIZED)")

    cohort_pdf = [
        ("Participant 1 (3.8 YoE)", "Software Developer | AI & Data Science R&D (Govt-Funded)", "Scope triage; motivating pressure dynamics; risk-based debt rules (B1 balancing loop). Dual-camera verified [03:50]."),
        ("Participant 2 (2.0 YoE)", "Software Developer | Enterprise Backend & Consulting (Deloitte)", "Inherited legacy frameworks; microservices architecture overhead; pre-QA mock DB isolation and automated contract testing."),
        ("Participant 3 (6.5 YoE)", "SDE-4 Systems & Firmware | Consumer Tech & Embedded (Apple)", "Urgent bugs taking 8–10h/day; multi-ETA pushback (B2); readable code as primary maintenance leverage [07:53, 08:14, 09:34]."),
        ("Participant 4 (5.0+ YoE)", "Software Engineer | HR-Tech & Global Payroll SaaS (Deel)", "18-item debt backlog deferred under launch velocity; developer cognitive depletion; recovery breaks as critical control [05:10]."),
        ("Participant 5 (3.0 YoE)", "CV & Full-Stack Engineer | Industrial AI & Automation (Siemens)", "API handler bypass; fear of touching legacy black-box code; formal sprint debt token capacity allocation [00:52].")
    ]
    cy_cur = b_y + b_h - 32
    for p_head, p_sub, p_foc in cohort_pdf:
        p_ch = Paragraph(
            f"<b><font size='8.0' color='#0f2942'>• {p_head} — {p_sub}</font></b><br/>"
            f"<font size='7.2' color='#334155'><i>Qualitative Contribution:</i> {p_foc}</font>",
            ParagraphStyle('CP', fontName='Helvetica', fontSize=7.2, leading=9.4)
        )
        h_c = draw_top_down(p_ch, p1_right_x + 14, cy_cur, p1_right_w - 28, 55)
        cy_cur -= (h_c + 8)

    c.setFillColor(HEX_AMBER_WARM)
    c.setFont("Helvetica-Bold", 9.0)
    c.drawString(p1_right_x + 14, b_y + p1_samp_h - 16, "SAMPLING STRATEGY & SECONDARY LITERATURE SOURCES")

    samp_p = (
        "<b>Purposive Sampling Criteria:</b> 4 practitioners with 3+ years of industry experience, plus 1 practitioner with 2 years "
        "in enterprise digital consulting (Deloitte). Encompasses diverse paradigms across Global SaaS, Embedded Firmware, Industrial AI, "
        "Enterprise Consulting, and Government R&D (20.3 cumulative years of engineering practice).<br/><br/>"
        "<b>Full Academic Literature Grounding (APA 7th Edition):</b><br/>"
        "• <b>Edmondson, A. (1999).</b> Psychological safety and learning behavior in work teams. <i>Adm. Sci. Q.</i>, 44(2), 350-383.<br/>"
        "• <b>Forsgren, N., Humble, J., & Kim, G. (2018).</b> <i>Accelerate: Science of lean software and DevOps</i>. IT Rev. Press.<br/>"
        "• <b>Senge, P. M. (1990).</b> <i>The fifth discipline: Art and practice of the learning organization</i>. Doubleday.<br/>"
        "• <b>Waters Center for Systems Thinking. (2020).</b> <i>Systems thinking in schools and organizations</i>. Waters Center."
    )
    p_samp = Paragraph(f"<font size='7.2' color='#1e293b'>{samp_p}</font>",
                       ParagraphStyle('Samp', fontName='Helvetica', fontSize=7.2, leading=9.8))
    draw_top_down(p_samp, p1_right_x + 14, b_y + p1_samp_h - 22, p1_right_w - 28, 180)

    c.showPage()

    # =========================================================================
    # PDF SLIDE 2: ANALYSIS & THEMATIC PATTERNS (5 MARKS) - Dim Watermark Pic 3 (Money)
    # =========================================================================
    draw_page_frame("Cross-Interview Thematic Patterns",
                    "EMPIRICAL ANALYSIS & THEMATIC FINDINGS (1 OF 2)", "icon_video.png", HEX_BG_S2,
                    "Edmondson (1999); Forsgren et al. (2018); Senge (1990); Waters Center (2020)")

    grid_w = (b_w - 14) / 2
    grid_h = (b_h - 14) / 2

    for gx, gy in [(s_x, b_y + grid_h + 14), (s_x + grid_w + 14, b_y + grid_h + 14),
                   (s_x, b_y), (s_x + grid_w + 14, b_y)]:
        c.setFillColor(HEX_CARD_BG)
        c.setStrokeColor(HEX_BORDER)
        c.roundRect(gx, gy, grid_w, grid_h, 6, fill=1, stroke=1)

    if os.path.exists("watermark_slide_2.png"):
        c.drawImage("watermark_slide_2.png", s_x + 100, b_y + 35, width=b_w - 200, height=b_h - 70, mask='auto')

    themes_pdf = [
        (s_x, b_y + grid_h + 14,
         "Pattern 1: The 'Fixes That Fail' Quick-Fix Trap",
         "Supported by 4 of 5 (Directly seen by 3; temporary patches by 1)",
         HEX_CORAL_RED,
         "Under market launches or demo pressures, teams bypass service layers or skip automated tests. While immediate symptomatic success is achieved, it seeds delayed technical liabilities.",
         "“Due to tight deadlines or business priorities, we choose quicker implementation... [01:36] ...sometimes this creates a whole kind of a mess.” [02:47] (Participant 4 — SaaS)<br/>“Instead of building a proper service layer, the team put business logic in API handlers... it worked, demo went well, and the shortcut felt like the right call.” [00:52] (Participant 5 — AI/CV)",
         "Secondary Finding: Senge's (1990) Fixes that Fail archetype. Part. 2 noted unclear requirements & legacy systems also trigger debt."),

        (s_x + grid_w + 14, b_y + grid_h + 14,
         "Pattern 2: The 'Next Sprint Never Comes' Dilemma",
         "Described directly by 2 of 5 (Participant 4 & Participant 5)",
         HEX_AMBER_WARM,
         "Debt is openly recognized and logged in retrospectives, but new feature requests consistently take precedence. Because debt is invisible to non-technical leaders, remediation is kicked to a 'next sprint' that never arrives.",
         "“...we already had 18 items in our backlog... we decided to take the backlog things first...” [07:05] (Participant 4 — SaaS)<br/>“The pressure to keep shipping does take over... cleanup kept happening to the next sprint, and the next sprint just never came.” [03:25] (Participant 5 — AI/CV)",
         "Secondary Finding: Waters Center (2020) on Shifting the Burden and compounding structural delays."),

        (s_x, b_y,
         "Pattern 3: Developer Fatigue & the Burnout Trap",
         "2 of 5 directly (P4, P5), plus heavy workload for 2 (P2, P3)",
         HEX_BLUE_ROYAL,
         "Unvalidated shortcuts degrade system stability, forcing intensive emergency firefighting. The cognitive strain and fear of touching black-box files directly deplete productivity.",
         "“It can become mentally exhausting... lots of miscommunication happens... even good engineers can become less productive.” [03:28-03:55] (Participant 4 — SaaS)<br/>“Couple of good developers were clearly burnt out... Over time people grew not to touch certain files, like a black box.” [02:44] (Participant 5 — AI/CV)\n“Maybe like eight to 10 hours a day to, like, in order to, like, fix that issue.” [07:53–07:58] (Participant 3 — Firmware)",
         "Secondary Finding: Forsgren et al. (2018) / DORA linking deployment pain and rework to developer burnout."),

        (s_x + grid_w + 14, b_y,
         "Pattern 4: Communication Gap & Reframing Debt",
         "Supported by 3 of 5 (Part. 1, 4, 3; business reframing by Part. 5)",
         HEX_TEAL_DEEP,
         "Engineering concerns framed solely as 'code hygiene' are deprioritized by leadership. Breaking the cycle requires psychological safety and translating technical risks into business metrics.",
         "“...high pressure does actually end up motivating me more to work on it.” [05:42] (Participant 1 — R&D)\n“...we kind of push engineers to take a break... [05:10] ...giving the engineers really good ownership... time is the key...” [05:47] (Participant 4 — SaaS)\n“Part of the problem was on our side... leadership cares about delivery speed, impact... and we were not speaking that language.” [04:12] (Participant 5 — AI/CV)",
         "Secondary Finding: Edmondson (1999) on psychological safety: teams can only push back when culture permits open voice.")
    ]

    for gx, gy, gt, gc_tag, gcol, gdesc, gquotes, gsec in themes_pdf:
        c.setFillColor(gcol)
        c.setFont("Helvetica-Bold", 8.2)
        c.drawString(gx + 12, gy + grid_h - 15, gt)

        c.setFillColor(HEX_OCEAN_DARK)
        c.setFont("Helvetica-Bold", 6.8)
        c.drawString(gx + 12, gy + grid_h - 26, f"Empirical Prevalence: {gc_tag}")

        p_gd = Paragraph(f"<font size='6.4' color='#1e293b'>{gdesc}</font>",
                         ParagraphStyle('GD', fontName='Helvetica', fontSize=6.4, leading=8.0))
        h_d = draw_top_down(p_gd, gx + 12, gy + grid_h - 30, grid_w - 24, 60)

        p_gq = Paragraph(f"<font size='5.8' color='#334155'><i>{gquotes}</i></font>",
                         ParagraphStyle('GQ', fontName='Helvetica', fontSize=5.8, leading=7.2))
        h_q = draw_top_down(p_gq, gx + 12, gy + grid_h - 34 - h_d, grid_w - 24, 110)

        p_gs = Paragraph(f"<b><font size='5.8' color='{gcol.hexval()}'>{gsec}</font></b>",
                         ParagraphStyle('GS', fontName='Helvetica', fontSize=5.8, leading=7.2))
        draw_top_down(p_gs, gx + 12, gy + grid_h - 38 - h_d - h_q, grid_w - 24, 30)

    c.showPage()

    # =========================================================================
    # PDF SLIDE 3: RECOMMENDATIONS (5 MARKS) - Dim Watermark Pic 2 (Fishing)
    # =========================================================================
    draw_page_frame("Actionable Engineering & Governance Recommendations",
                    "STRATEGIC RECOMMENDATIONS (2 OF 2)", "icon_bulb.png", HEX_BG_S3,
                    "Edmondson (1999); Forsgren et al. (2018); Waters Center (2020)")

    rec_w_pdf = (b_w - 24) / 3

    for idx in range(3):
        rx = s_x + idx * (rec_w_pdf + 12)
        c.setFillColor(HEX_CARD_BG)
        c.setStrokeColor(HEX_BORDER)
        c.roundRect(rx, b_y, rec_w_pdf, b_h, 6, fill=1, stroke=1)

    if os.path.exists("watermark_slide_3.png"):
        c.drawImage("watermark_slide_3.png", s_x + 80, b_y + 35, width=b_w - 160, height=b_h - 70, mask='auto')

    recs_pdf = [
        ("1. Debt Budget & Triage",
         "Sprint Token Allocation & Risk Rules",
         HEX_CORAL_RED,
         "Target Problem & Root Cause:",
         "The 'Next Sprint Never Comes' paradox (Waters Center, 2020). Engineering refactoring requests framed as abstract 'code quality' stall because business leadership prioritizes near-term feature delivery.",
         "Actionable Implementation Protocol:",
         "• <b>Formal Debt Budget:</b> Reserve a fixed share of each sprint's story points/tokens explicitly for architectural refactoring, pre-negotiated with Product Management (Participant 5).<br/>"
         "• <b>2-Tier Risk Triage Matrix:</b> Fix immediately if defect threatens cross-service contract stability or system scalability; apply temporary patch if localized and non-critical (Participant 1 [03:50], Participant 3 [02:59–03:06]).<br/>"
         "• <b>Business Translation:</b> Frame technical debt in commercial risk terms (SLA downtime penalty, user churn, cloud compute waste) rather than internal aesthetic code hygiene.",
         "Our suggested targets (not from interviews):",
         "• <b>Dedicated Sprint Debt Ratio:</b> Target 15–20% capacity allocated to debt tickets.<br/>"
         "• <b>Backlog Debt Age:</b> Max 45 days before compulsory review.<br/>"
         "• <b>Unplanned Work:</b> Firefighting < 10% sprint hours.",
         "Academic Grounding & Validation:",
         "Grounding: Senge (1990) 'Fixes that Fail'; Waters Center (2020) 'Shifting the Burden'. Supported by Participant 1 and Participant 5.",
         "Systemic Risk of Inaction:",
         "Unchecked quick fixes compound invisible architectural debt, transforming minor localized bugs into systemic outages and catastrophic multi-month system rewrites.",
         "Core Systemic Leverage & Outcome:",
         "Balances the R1 Quick-Fix Trap by formalizing a non-negotiable B1 refactoring buffer, preventing invisible architectural debt from compounding into catastrophic production outages."),

        ("2. Testing Safety Nets",
         "Automated Pipelines & Boy Scout Rule",
         HEX_BLUE_ROYAL,
         "Target Problem & Root Cause:",
         "The Quick-Fix Spiral (R1). Skipping test suites to meet urgent demo commitments creates hidden regression bugs, fragile shared state, and chronic weekend emergency firefighting.",
         "Actionable Implementation Protocol:",
         "• <b>Automated CI/CD Gates:</b> Mandate pre-merge automated linting, unit tests, and integration pipelines as non-bypassable deployment gates (Participant 3, Participant 5).<br/>"
         "• <b>Boy Scout Engineering Norm:</b> Institutionalize the standard of leaving every touched file cleaner, better tested, and better documented than found. Participant 3 noted readable code is 'half of the work' [09:34–09:39].<br/>"
         "• <b>Contract & Mock Isolation:</b> Build pre-release mock environments and automated contract tests (Participant 2) to prevent developer-QA environment mismatches and post-deploy failures.",
         "Our suggested targets (not from interviews):",
         "• <b>DORA Change Failure Rate:</b> Target < 5% of production releases.<br/>"
         "• <b>Automated Test Coverage:</b> ≥ 80% on core services.<br/>"
         "• <b>Recovery Time (MTTR):</b> Target < 1 hour to restore.",
         "Academic Grounding & Validation:",
         "Grounding: Forsgren et al. (2018) / DORA delivery research linking automated quality gates with reduced burnout. Supported by Participant 2, 3, and 5.",
         "Systemic Risk of Inaction:",
         "Manual testing bottlenecks and skipped regression tests cause post-deployment failures, eroding customer trust and triggering 8–10 hour emergency triage shifts.",
         "Core Systemic Leverage & Outcome:",
         "Decouples delivery velocity from error injection. Automated quality gates eliminate developer-QA friction and ensure high release cadence without regression firefighting."),

        ("3. Safe to Push Back",
         "Psychological Safety & Recovery",
         HEX_TEAL_DEEP,
         "Target Problem & Root Cause:",
         "The Developer Burnout Trap (R2). When teams lack psychological safety, engineers absorb uncommunicated scope creep, silently cut corners, and experience severe cognitive exhaustion.",
         "Actionable Implementation Protocol:",
         "• <b>Psychological Safety for Pushback:</b> Establish cultural norms empowering engineers to challenge unrealistic delivery deadlines without fear of negative evaluation (Edmondson, 1999).<br/>"
         "• <b>Multi-Stage Phased Delivery:</b> Replace binary yes/no commitments with transparent multi-stage ETAs (e.g., MVP release vs. fully hardened architecture), providing clear trade-off dialogues (Participant 3 [08:14–08:26]).<br/>"
         "• <b>Proactive Recovery Protocols:</b> Enforce recovery breaks after intensive delivery crunches, grant genuine technical ownership, and recognize that 'time is the key' (Participant 4 [05:10, 05:47]).<br/>"
         "• <b>Continuous Load Triage:</b> Institutionalize regular sprint retrospectives to inspect burnout indicators before technical debt cascades into team fatigue.",
         "Our suggested targets (not from interviews):",
         "• <b>Psychological Safety:</b> Edmondson (1999) scale ≥ 4.2 / 5.0.<br/>"
         "• <b>Overtime Burnout Ratio:</b> Max 1 crunch weekend/qtr.<br/>"
         "• <b>Retention Rate:</b> 0% voluntary burnout attrition.",
         "Academic Grounding & Validation:",
         "Grounding: Edmondson (1999) on team psychological safety; Senge (1990) personal mastery. Supported by Participant 1, 3, and 4.",
         "Systemic Risk of Inaction:",
         "Engineers absorb unchecked delivery stress in silence, triggering severe cynicism, intellectual depletion, and eventual voluntary departure of key talent.",
         "Core Systemic Leverage & Outcome:",
         "Activates the B2 Pushback Brake to halt runaway developer cognitive depletion. Replaces arbitrary crunch with phased delivery and institutionalized recovery.")
    ]

    for idx, (rt, rsub, rcol, rch, rc, racth, ract, rkh, rk, rgrdh, rgrd, roinh, roin, roth, rot) in enumerate(recs_pdf):
        rx = s_x + idx * (rec_w_pdf + 12)
        p_rt = Paragraph(
            f"<b><font size='10.0' color='{rcol.hexval()}'>{rt}</font></b><br/>"
            f"<b><font size='7.8' color='#0f2942'>Protocol: {rsub}</font></b>",
            ParagraphStyle('RTit', fontName='Helvetica', fontSize=9.5, leading=12.0)
        )
        h_head = draw_top_down(p_rt, rx + 12, b_y + b_h - 14, rec_w_pdf - 24, 60)

        cur_y = b_y + b_h - 14 - h_head - 14
        sections_p = [
            (rch, rc, '7.2', '#1e293b', 9.4),
            (racth, ract, '7.1', '#1e293b', 9.2),
            (rkh, rk, '7.1', '#0f2942', 9.2),
            (rgrdh, rgrd, '7.0', '#475569', 9.0),
            (roinh, roin, '7.0', '#991b1b', 9.0),
            (roth, rot, '7.0', '#0f766e', 9.0)
        ]
        for sh, sc, sz, scol, sld in sections_p:
            c.setFillColor(rcol)
            c.setFont("Helvetica-Bold", 7.6)
            c.drawString(rx + 12, cur_y, sh)
            cur_y -= 11
            p_sec = Paragraph(f"<font size='{sz}' color='{scol}'>{sc}</font>",
                              ParagraphStyle('RSec', fontName='Helvetica', fontSize=float(sz), leading=sld))
            h_used = draw_top_down(p_sec, rx + 12, cur_y, rec_w_pdf - 24, 220)
            cur_y -= (h_used + 8)

    c.showPage()

    # =========================================================================
    # PDF SLIDE 4: INFLUENCE MODEL (5 MARKS) - BIGGER, WIDER PICTURE + BOTTOM SUMMARY
    # =========================================================================
    draw_page_frame("Systems Thinking Influence Model: Causal Loop Analysis",
                    "SYSTEMS THINKING INFLUENCE MODEL (5 MARKS)", "icon_gears.png", HEX_BG_S4,
                    "Edmondson (1999); Forsgren et al. (2018); Senge (1990); Waters Center (2020)")

    cld_w_pdf = b_w
    cld_h_pdf = 345
    cld_y_pdf = b_y + b_h - cld_h_pdf
    if os.path.exists("influence_model_cld.png"):
        c.drawImage("influence_model_cld.png", s_x, cld_y_pdf, width=cld_w_pdf, height=cld_h_pdf, mask='auto')

    bot_y_pdf = b_y
    bot_h_pdf = cld_y_pdf - b_y - 8
    card_w_cld_pdf = (b_w - 24) / 4

    cld_bottom_pdf = [
        ("R1: Quick-Fix Spiral (Reinforcing)",
         "Pressure (+) -> Quick Fixes (+) -> Tech Debt (+) -> Complexity (+) -> Firefighting (+) -> Pressure (+). Fits Senge (1990) Fixes that Fail.",
         HEX_CORAL_RED, HexColor("#fff1f2"), HexColor("#fecdd3")),
        ("R2: Burnout Trap (Reinforcing)",
         "Firefighting (+) -> Developer Fatigue (+) -> Velocity (-) -> Pressure (- inverse). Pushes devs to cognitive limits where they fear touching legacy code.",
         HEX_CORAL_RED, HexColor("#fff1f2"), HexColor("#fecdd3")),
        ("B1: Debt Buffer (Balancing)",
         "Tech Debt (+) -> Sprint Token Capacity (+) -> Debt (-). Dedicated refactoring buffer stabilizes code quality and balances accumulated technical debt.",
         HEX_TEAL_DEEP, HexColor("#f0fdfa"), HexColor("#99f6e4")),
        ("B2: Pushback Brake (Balancing)",
         "Fatigue (+) -> Scope Pushback (+) -> Pressure (-). High Psychological Safety enables pushback to de-escalate unrealistic deadlines before burnout.",
         HEX_TEAL_DEEP, HexColor("#f0fdfa"), HexColor("#99f6e4"))
    ]

    for idx, (ltitle, ldesc, lcol, lbg, lbord) in enumerate(cld_bottom_pdf):
        lx = s_x + idx * (card_w_cld_pdf + 8)
        c.setFillColor(lbg)
        c.setStrokeColor(lbord)
        c.roundRect(lx, bot_y_pdf, card_w_cld_pdf, bot_h_pdf, 5, fill=1, stroke=1)

        c.setFillColor(lcol)
        c.setFont("Helvetica-Bold", 7.0)
        c.drawString(lx + 8, bot_y_pdf + bot_h_pdf - 14, ltitle)

        p_ld = Paragraph(f"<font size='5.8' color='#1e293b'>{ldesc}</font>",
                         ParagraphStyle('CLD_desc', fontName='Helvetica', fontSize=5.8, leading=7.2))
        draw_top_down(p_ld, lx + 8, bot_y_pdf + bot_h_pdf - 18, card_w_cld_pdf - 16, 75)

    c.showPage()

    # =========================================================================
    # PDF SLIDE 5: PROJECT REVIEW & CLOSURE - Dim Watermark Pic 1 (Sword & Anvil)
    # =========================================================================
    draw_page_frame("Project Review, Governance & Closure",
                    "PROJECT REVIEW & CLOSURE", "icon_trophy.png", HEX_BG_S5,
                    "IIT Madras BS Degree Programme  •  BSGN3001 Team 114: Iterate")

    p5_left_w = (b_w - 14) * 0.48
    p5_right_w = (b_w - 14) * 0.52
    p5_right_x = s_x + p5_left_w + 14

    c.setFillColor(HEX_CARD_BG)
    c.setStrokeColor(HEX_BORDER)
    c.roundRect(s_x, b_y, p5_left_w, b_h, 6, fill=1, stroke=1)

    p5_cont_h = 135
    c.roundRect(p5_right_x, b_y + b_h - p5_cont_h, p5_right_w, p5_cont_h, 6, fill=1, stroke=1)

    p5_bp_h = b_h - p5_cont_h - 10
    c.setFillColor(HexColor("#fefcf6"))
    c.setStrokeColor(HexColor("#fde68a"))
    c.roundRect(p5_right_x, b_y, p5_right_w, p5_bp_h, 6, fill=1, stroke=1)

    if os.path.exists("watermark_slide_5.png"):
        c.drawImage("watermark_slide_5.png", s_x + 100, b_y + 35, width=b_w - 200, height=b_h - 70, mask='auto')

    # 3. Draw Text ON TOP of watermark
    c.setFillColor(HEX_OCEAN_DARK)
    c.setFont("Helvetica-Bold", 9.4)
    c.drawString(s_x + 14, b_y + b_h - 18, "MEMBER TASK ATTRIBUTION & FIELDWORK OWNERSHIP")

    member_tasks_pdf = [
        ("Samyabrata Roy (22F2001443)", "Team Lead",
         "Fieldwork: Rounak Biswas (3.8 YoE, AI/ML R&D). Authored scope triage analysis, secondary systems literature review, and final consolidation.",
         "Learned that while deadline pressure can initially focus engineering effort, unmanaged backlog debt inevitably flips motivating pressure into cognitive overload."),

        ("Abir Saha (23F3001436)", "Project Manager",
         "Fieldwork: Anunay Sinha (2.0 YoE, Deloitte Consulting). Synthesized legacy framework debt, microservices overhead, and managed milestone schedules.",
         "Observed that enterprise legacy debt disproportionately burdens newer engineers; pre-QA mock isolation is vital to prevent multi-team deployment friction."),

        ("Rishabh Barthwal (23F2004112)", "Research Lead",
         "Fieldwork: Suraj Sajeev (6.5 YoE, Apple Firmware). Transcribed and coded shared-variable race conditions, multi-ETA pushback rules, and verified timestamps.",
         "Recognized that 8–10h emergency firefighting stems from poorly isolated shared state; writing readable code is 'half of the work' in long-term maintainability."),

        ("Piyush Tilokchandani (21F1006739)", "Design Lead",
         "Fieldwork: Keshav Gupta (5.0+ YoE, Deel SaaS). Synthesized 18-item debt deferral, cognitive fatigue dynamics, recovery protocols, and led rubric audit.",
         "Realized technical debt is fundamentally an organizational human systems failure; developer cognitive recovery breaks are an essential engineering control."),

        ("Ramrup Satpati (24F3004027)", "Creative & Presentation Lead",
         "Fieldwork: Shubham Mishra (3.0 YoE, Siemens Automation). Modeled Causal Loop Diagram (CLD) archetypes, designed deck architecture, and compiled vector PDFs.",
         "Discovered that shortcuts in API handlers create team-wide 'black-box' code fear, demonstrating that formal sprint token capacity is mandatory for refactoring.")
    ]
    my_cur = b_y + b_h - 26
    for mname, mrole, mfield, mrefl in member_tasks_pdf:
        p_m = Paragraph(
            f"<b><font size='7.5' color='#be123c'>• {mname} — {mrole}</font></b><br/>"
            f"<font size='7.0' color='#1e293b'><b>Contribution:</b> {mfield}</font><br/>"
            f"<font size='6.8' color='#475569'><i>Personal Reflection:</i> {mrefl}</font>",
            ParagraphStyle('MP', fontName='Helvetica', fontSize=7.0, leading=9.2)
        )
        h_m = draw_top_down(p_m, s_x + 14, my_cur, p5_left_w - 28, 120)
        my_cur -= (h_m + 8)

    my_cur -= 4
    c.setFillColor(HEX_TEAL_DEEP)
    c.setFont("Helvetica-Bold", 8.8)
    c.drawString(s_x + 14, my_cur, "TEAM COLLABORATION & GOVERNANCE MECHANISMS")
    my_cur -= 14

    team_gov_pdf = [
        ("Asynchronous & Synchronous Syncs", "Bi-weekly sprint syncs, shared cloud repository for transcript audit trails, and collaborative peer-coding sessions."),
        ("Consensus & Interpretive Rigor", "Unanimous democratic consensus on archetype classifications (R1, R2, B1, B2) and qualitative quote interpretations."),
        ("IITM Assessment Rubric Audit", "Dedicated pre-submission audit pass verifying all GP2 Deliverable 1.c and 1.a criteria, citations, and formatting benchmarks.")
    ]
    for gh, gd in team_gov_pdf:
        p_g = Paragraph(
            f"<b><font size='7.4' color='#0f2942'>• {gh}:</font></b> "
            f"<font size='7.0' color='#334155'>{gd}</font>",
            ParagraphStyle('GP', fontName='Helvetica', fontSize=7.0, leading=9.0)
        )
        h_g = draw_top_down(p_g, s_x + 14, my_cur, p5_left_w - 28, 60)
        my_cur -= (h_g + 6)

    c.setFillColor(HEX_BLUE_ROYAL)
    c.setFont("Helvetica-Bold", 9.0)
    c.drawString(p5_right_x + 14, b_y + b_h - 18, "COURSE CONTINUITY & INTERVIEWEE ROSTER CHANGES")

    cont_p = (
        "<b>• Course Continuity: 100% Active Retention.</b> All 5 members completed their individual interviews, "
        "submitted interim reports, and actively contributed to this consolidated report. Zero opt-outs / dropouts.<br/>"
        "<b>• Interviewee Roster Changes:</b><br/>"
        "&nbsp;&nbsp;1. <i>Participant 1 Change:</i> Aakash Verma (GP1) was replaced by Rounak Biswas due to work scheduling unavailability "
        "(documented with email correspondence).<br/>"
        "&nbsp;&nbsp;2. <i>Participant 3 Change:</i> Vikramaditya was replaced by Suraj Sajeev (6.5 YoE, Systems & Firmware) due to timeline conflicts.<br/>"
        "<b>• Cohort Balance:</b> 20.3 cumulative years of engineering practice across 5 distinct domains (SaaS, Embedded, AI, Consulting, and R&D)."
    )
    p_cont = Paragraph(f"<font size='7.0' color='#1e293b'>{cont_p}</font>",
                       ParagraphStyle('ContP', fontName='Helvetica', fontSize=7.0, leading=9.0))
    draw_top_down(p_cont, p5_right_x + 14, b_y + b_h - 24, p5_right_w - 28, 120)

    c.setFillColor(HEX_AMBER_WARM)
    c.setFont("Helvetica-Bold", 8.6)
    c.drawString(p5_right_x + 14, b_y + p5_bp_h - 16, "CHALLENGES, BEST PRACTICES & STRATEGIC ROADMAP")

    bp_sections_pdf = [
        ("Methodological Challenges Overcome",
         "• <b>Cross-Domain Synthesis:</b> Bridging embedded firmware lifecycles (Apple) with high-velocity SaaS releases (Deel) required abstracting findings into systems archetypes (R1/R2 loops).<br/>"
         "• <b>Verbatim Auditing Rigor:</b> Disentangling technical jargon, acronyms, and overlapping audio across 5 distinct recorded sessions required 3-pass verification against exact timestamps.<br/>"
         "• <b>Investigator Bias Mitigation:</b> Conducted structured peer debriefing and cross-coding among all team members to ensure balanced interpretation of qualitative statements."),

        ("Engineering Leadership Best Practices",
         "• <b>Dedicated Sprint Debt Allocation:</b> Translating architectural debt into business risk terms (SLA penalties, customer churn) secures executive buy-in for guaranteed refactoring.<br/>"
         "• <b>Automated Non-Bypassable Gates:</b> CI/CD pipelines decouple deployment velocity from defect injection, eliminating developer-QA friction and post-deploy firefighting.<br/>"
         "• <b>Psychological Safety for Pushback:</b> Multi-stage phased ETAs (MVP vs. hardened core) empower engineers to challenge unrealistic deadlines without fear of negative evaluation."),

        ("Future Longitudinal Research Directions (GP3 Horizon)",
         "Extend qualitative fieldwork into a large-scale quantitative survey instrument (<i>N</i> ≥ 100 engineering teams) to measure empirical causal coefficients linking debt age, test coverage, and voluntary developer attrition."),

        ("Final Team Review & Formal Sign-Off",
         "All 5 team members conducted an exhaustive joint audit, verified all qualitative attributions against video recordings, and unanimously approved this consolidated dossier on 17-Nov-2026.")
    ]

    py_bp_cur = b_y + p5_bp_h - 26
    for head, body in bp_sections_pdf:
        p_sec = Paragraph(
            f"<b><font size='8.0' color='#0f2942'>• {head}</font></b><br/>"
            f"<font size='7.2' color='#1e293b'>{body}</font>",
            ParagraphStyle('BP', fontName='Helvetica', fontSize=7.2, leading=9.6)
        )
        h_sec = draw_top_down(p_sec, p5_right_x + 14, py_bp_cur, p5_right_w - 28, 180)
        py_bp_cur -= (h_sec + 11)

    c.showPage()
    c.save()
    shutil.copyfile(pdf_path, "Team_114_SPG_GP2_Sep_2026.pdf")
    print(f"[*] Successfully generated Vector PDF: {pdf_path} (and copy Team_114_SPG_GP2_Sep_2026.pdf)")


if __name__ == "__main__":
    build_pptx()
    build_pdf()
