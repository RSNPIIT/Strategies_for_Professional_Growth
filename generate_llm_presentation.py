"""
Presentation Generator for LLM Using Python by Ramrup Satpati.
Generates a 10-slide PowerPoint presentation (.pptx) with SPG aesthetic theme,
including photos, technical diagrams, and typography.
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE


# =============================================================================
# COLOR PALETTE (SPG Academic Theme)
# =============================================================================
C_OCEAN_DARK = RGBColor(15, 23, 42)      # Slate 900
C_CORAL_RED  = RGBColor(225, 29, 72)     # Rose/Coral 600
C_CORAL_SOFT = RGBColor(244, 63, 94)     # Rose/Coral 500
C_TEAL_DEEP  = RGBColor(13, 148, 136)    # Marine Teal 600
C_BLUE_ROYAL = RGBColor(29, 78, 216)     # Royal Blue 700
C_INDIGO     = RGBColor(79, 70, 229)     # Indigo 600
C_AMBER_WARM = RGBColor(234, 88, 12)     # Amber Orange 600
C_TEXT_MAIN  = RGBColor(31, 41, 55)      # Gray 800
C_TEXT_MUTED = RGBColor(100, 116, 139)   # Slate 500
C_CARD_BG    = RGBColor(255, 255, 255)   # Pure White
C_BORDER     = RGBColor(203, 213, 225)   # Slate 300
C_PILL_BG    = RGBColor(241, 245, 249)   # Slate 100

# Slide Background Tints
C_BG_S0 = RGBColor(252, 253, 255)  # Cover
C_BG_S1 = RGBColor(248, 250, 252)  # Contents
C_BG_S2 = RGBColor(250, 248, 245)  # Intro
C_BG_S3 = RGBColor(248, 250, 252)  # Objective
C_BG_S4 = RGBColor(250, 250, 249)  # Meth 1
C_BG_S5 = RGBColor(246, 249, 250)  # Meth 2
C_BG_S6 = RGBColor(248, 247, 252)  # Meth 3
C_BG_S7 = RGBColor(250, 248, 245)  # Meth 4
C_BG_S8 = RGBColor(248, 250, 252)  # Results
C_BG_S9 = RGBColor(252, 250, 248)  # Conclusion


def disable_spellcheck(run):
    try:
        rPr = run._r.get_or_add_rPr()
        rPr.set("noProof", "1")
    except Exception:
        pass


def build_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    def add_slide_frame(slide, title_text, category_text, corner_img=None, bg_color=C_BG_S1, slide_num=1):
        # Background
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = bg_color
        bg.line.fill.background()

        # Corner Floral Decoration
        if corner_img and os.path.exists(corner_img):
            slide.shapes.add_picture(corner_img, Inches(0.25), Inches(0.22), Inches(1.05), Inches(1.05))

        # Header Box
        hb = slide.shapes.add_textbox(Inches(1.45), Inches(0.35), Inches(10.2), Inches(0.85))
        tf = hb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p_cat = tf.paragraphs[0]
        r_cat = p_cat.add_run()
        r_cat.text = category_text.upper()
        r_cat.font.bold = True
        r_cat.font.size = Pt(9.5)
        r_cat.font.color.rgb = C_CORAL_RED
        disable_spellcheck(r_cat)

        p_t = tf.add_paragraph()
        r_t = p_t.add_run()
        r_t.text = title_text
        r_t.font.bold = True
        r_t.font.size = Pt(20)
        r_t.font.color.rgb = C_OCEAN_DARK
        disable_spellcheck(r_t)

        # Header accent line
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.45), Inches(1.18), Inches(10.2), Inches(0.035))
        line.fill.solid()
        line.fill.fore_color.rgb = C_CORAL_RED
        line.line.fill.background()

        # Top-Right IIT Madras Logo
        if os.path.exists("iitm_logo_clean.png"):
            slide.shapes.add_picture("iitm_logo_clean.png", Inches(11.85), Inches(0.22), Inches(1.25), Inches(1.25))

        # Bottom Page Curl
        if os.path.exists("page_flip_corner.png"):
            slide.shapes.add_picture("page_flip_corner.png", Inches(12.5), Inches(6.3), Inches(0.83), Inches(1.2))

        # Footer divider line
        f_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.45), Inches(7.05), Inches(9.8), Inches(0.015))
        f_line.fill.solid()
        f_line.fill.fore_color.rgb = C_BORDER
        f_line.line.fill.background()

        # Footer metadata
        fb = slide.shapes.add_textbox(Inches(1.45), Inches(7.08), Inches(9.8), Inches(0.3))
        pf = fb.text_frame.paragraphs[0]
        rf = pf.add_run()
        rf.text = f"Ramrup Satpati (24F3004027)  •  LLM Using Python: Decoder-Only Transformer from Scratch  •  Slide {slide_num} of 10"
        rf.font.size = Pt(8.5)
        rf.font.color.rgb = C_TEXT_MUTED
        disable_spellcheck(rf)

    # =========================================================================
    # SLIDE 1: TITLE SLIDE (COVER)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = C_BG_S0
    bg1.line.fill.background()

    # Corner decorations
    if os.path.exists("flower_slide_0.png"):
        s1.shapes.add_picture("flower_slide_0.png", Inches(0.4), Inches(0.4), Inches(1.15), Inches(1.15))
    if os.path.exists("flower_cover_bottom.png"):
        s1.shapes.add_picture("flower_cover_bottom.png", Inches(0.4), Inches(5.6), Inches(1.15), Inches(1.15))
    if os.path.exists("iitm_logo_clean.png"):
        s1.shapes.add_picture("iitm_logo_clean.png", Inches(11.5), Inches(0.4), Inches(1.45), Inches(1.45))
    if os.path.exists("page_flip_corner.png"):
        s1.shapes.add_picture("page_flip_corner.png", Inches(12.5), Inches(6.3), Inches(0.83), Inches(1.2))

    # Main Left Card
    card_left = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.6), Inches(0.65), Inches(7.2), Inches(6.2))
    card_left.fill.solid()
    card_left.fill.fore_color.rgb = C_CARD_BG
    card_left.line.color.rgb = C_BORDER
    card_left.line.width = Pt(1.2)

    tb_left = s1.shapes.add_textbox(Inches(1.8), Inches(0.85), Inches(6.8), Inches(5.8))
    tf_l = tb_left.text_frame
    tf_l.word_wrap = True

    p_c1 = tf_l.paragraphs[0]
    r_c1 = p_c1.add_run()
    r_c1.text = "IIT MADRAS BS DEGREE PROGRAMME  •  PROJECT PRESENTATION"
    r_c1.font.bold = True
    r_c1.font.size = Pt(9.5)
    r_c1.font.color.rgb = C_CORAL_RED
    disable_spellcheck(r_c1)
    p_c1.space_after = Pt(4)

    p_c2 = tf_l.add_paragraph()
    r_c2 = p_c2.add_run()
    r_c2.text = "BS IN DATA SCIENCE & APPLICATIONS  •  DEEP LEARNING & GENERATIVE AI"
    r_c2.font.bold = True
    r_c2.font.size = Pt(8.5)
    r_c2.font.color.rgb = C_TEXT_MUTED
    disable_spellcheck(r_c2)
    p_c2.space_after = Pt(14)

    p_c3 = tf_l.add_paragraph()
    r_c3 = p_c3.add_run()
    r_c3.text = "LLM USING PYTHON"
    r_c3.font.bold = True
    r_c3.font.size = Pt(30)
    r_c3.font.color.rgb = C_OCEAN_DARK
    disable_spellcheck(r_c3)

    p_c4 = tf_l.add_paragraph()
    r_c4 = p_c4.add_run()
    r_c4.text = "Building a Large Language Model from Scratch in Python & PyTorch"
    r_c4.font.bold = True
    r_c4.font.size = Pt(13.5)
    r_c4.font.color.rgb = C_TEAL_DEEP
    disable_spellcheck(r_c4)
    p_c4.space_after = Pt(10)

    p_c5 = tf_l.add_paragraph()
    r_c5 = p_c5.add_run()
    r_c5.text = "A complete, mathematically rigorous implementation of a Decoder-Only Generative Pretrained Transformer—from custom tokenization and causal multi-head self-attention to pretraining and nucleus sampling."
    r_c5.font.size = Pt(9.5)
    r_c5.font.color.rgb = C_TEXT_MAIN
    disable_spellcheck(r_c5)
    p_c5.space_after = Pt(16)

    # Info Grid inside Left Card
    info_items = [
        ("Author & Developer:", "RAMRUP SATPATI (Roll No: 24F3004027)"),
        ("Institutional Email:", "24f3004027@ds.study.iitm.ac.in"),
        ("GitHub Repository:", "github.com/RSNPIIT/LLM_Using_Python_project"),
        ("Open-Source License:", "GNU General Public License v3.0 (Copyleft GPLv3)")
    ]
    for lbl, val in info_items:
        p_inf = tf_l.add_paragraph()
        r_l = p_inf.add_run()
        r_l.text = f"•  {lbl} "
        r_l.font.bold = True
        r_l.font.size = Pt(9.0)
        r_l.font.color.rgb = C_BLUE_ROYAL
        disable_spellcheck(r_l)

        r_v = p_inf.add_run()
        r_v.text = val
        r_v.font.size = Pt(9.0)
        r_v.font.color.rgb = C_TEXT_MAIN
        disable_spellcheck(r_v)
        p_inf.space_after = Pt(4)

    # Main Right Card (Portrait Card)
    card_right = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.05), Inches(0.65), Inches(2.65), Inches(6.2))
    card_right.fill.solid()
    card_right.fill.fore_color.rgb = C_CARD_BG
    card_right.line.color.rgb = C_BORDER
    card_right.line.width = Pt(1.2)

    # Embed Ramrup's Photo
    photo_path = "ramrup_photo_extracted.png"
    if os.path.exists(photo_path):
        s1.shapes.add_picture(photo_path, Inches(9.25), Inches(0.95), Inches(2.25), Inches(3.2))

    # Photo Caption Box
    cap_tb = s1.shapes.add_textbox(Inches(9.15), Inches(4.3), Inches(2.45), Inches(2.3))
    cap_tf = cap_tb.text_frame
    cap_tf.word_wrap = True

    p_nm = cap_tf.paragraphs[0]
    p_nm.alignment = PP_ALIGN.CENTER
    r_nm = p_nm.add_run()
    r_nm.text = "RAMRUP SATPATI"
    r_nm.font.bold = True
    r_nm.font.size = Pt(12)
    r_nm.font.color.rgb = C_OCEAN_DARK
    disable_spellcheck(r_nm)
    p_nm.space_after = Pt(3)

    p_rl = cap_tf.add_paragraph()
    p_rl.alignment = PP_ALIGN.CENTER
    r_rl = p_rl.add_run()
    r_rl.text = "Lead Developer & Researcher\nIIT Madras BS Degree"
    r_rl.font.size = Pt(8.5)
    r_rl.font.color.rgb = C_CORAL_RED
    disable_spellcheck(r_rl)
    p_rl.space_after = Pt(6)

    p_tg = cap_tf.add_paragraph()
    p_tg.alignment = PP_ALIGN.CENTER
    r_tg = p_tg.add_run()
    r_tg.text = "Deep Learning · Generative AI\nApplied AI & Transformers"
    r_tg.font.size = Pt(7.8)
    r_tg.font.color.rgb = C_TEXT_MUTED
    disable_spellcheck(r_tg)

    # =========================================================================
    # SLIDE 2: CONTENTS (Executive Roadmap)
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_slide_frame(s2, "Table of Contents & Executive Roadmap", "PROJECT OVERVIEW", "flower_slide_1.png", C_BG_S1, 2)

    # Top Banner
    top_b = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.45), Inches(1.35), Inches(10.35), Inches(0.38))
    top_b.fill.solid()
    top_b.fill.fore_color.rgb = RGBColor(255, 241, 242)
    top_b.line.color.rgb = RGBColor(254, 205, 211)
    tf_top = top_b.text_frame
    p_tb = tf_top.paragraphs[0]
    r_tb1 = p_tb.add_run()
    r_tb1.text = "PROJECT ROADMAP:  "
    r_tb1.font.bold = True
    r_tb1.font.size = Pt(8.5)
    r_tb1.font.color.rgb = C_CORAL_RED
    r_tb2 = p_tb.add_run()
    r_tb2.text = "5 Key Phases from First-Principles Mathematics to Pretraining, Nucleus Sampling & Open-Source Release"
    r_tb2.font.bold = True
    r_tb2.font.size = Pt(8.5)
    r_tb2.font.color.rgb = C_OCEAN_DARK

    contents_data = [
        ("01", "INTRODUCTION", C_TEAL_DEEP, RGBColor(240, 253, 250), RGBColor(153, 246, 228),
         "The generative AI paradigm shift; autoregressive formulation P(wt | w<t); why building an LLM from scratch in pure Python uncovers foundational mechanics that high-level APIs obscure."),
        ("02", "OBJECTIVE", C_BLUE_ROYAL, RGBColor(239, 246, 255), RGBColor(191, 219, 254),
         "Core engineering goals: custom tokenization, causal self-attention, pre-LN Transformer blocks, AdamW pretraining on Tiny Shakespeare, and multi-mode text generation engines."),
        ("03", "METHODOLOGY", C_CORAL_RED, RGBColor(255, 241, 242), RGBColor(254, 205, 211),
         "4-Stage Technical Architecture: (1) Tokenization & Dataloader; (2) Causal Multi-Head Self-Attention & Masking; (3) Transformer Blocks & RMSNorm/GELU; (4) Pretraining & Optimizer Engine."),
        ("04", "RESULT ANALYSIS", C_AMBER_WARM, RGBColor(255, 247, 237), RGBColor(254, 215, 170),
         "Empirical convergence evaluation: loss reduction from 4.21 to 1.45 (Perplexity 67.35 to 4.67); comparative sampling evaluation (Greedy, Temperature, Top-K, Nucleus); hardware MPS benchmarks."),
        ("05", "CONCLUSION", C_INDIGO, RGBColor(245, 243, 255), RGBColor(221, 214, 254),
         "Key technical competencies gained; verifiable open-source GPLv3 GitHub repository; architectural scalability roadmap (Fine-tuning, LoRA, and DPO alignment).")
    ]

    c_start_y = Inches(1.9)
    c_h = Inches(0.92)
    c_gap = Inches(0.11)
    for idx, (num, title, col, bg_col, bdr_col, desc) in enumerate(contents_data):
        cy = c_start_y + idx * (c_h + c_gap)
        c_box = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.45), cy, Inches(10.35), c_h)
        c_box.fill.solid()
        c_box.fill.fore_color.rgb = bg_col
        c_box.line.color.rgb = bdr_col
        c_box.line.width = Pt(1.2)

        # Number pill
        np = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.65), cy + Inches(0.16), Inches(0.6), Inches(0.6))
        np.fill.solid()
        np.fill.fore_color.rgb = col
        np.line.fill.background()
        p_np = np.text_frame.paragraphs[0]
        p_np.alignment = PP_ALIGN.CENTER
        r_np = p_np.add_run()
        r_np.text = num
        r_np.font.bold = True
        r_np.font.size = Pt(13)
        r_np.font.color.rgb = C_CARD_BG

        # Content text
        ctb = s2.shapes.add_textbox(Inches(2.45), cy + Inches(0.08), Inches(9.2), c_h - Inches(0.16))
        ctf = ctb.text_frame
        ctf.word_wrap = True
        p_ct = ctf.paragraphs[0]
        r_ct = p_ct.add_run()
        r_ct.text = title
        r_ct.font.bold = True
        r_ct.font.size = Pt(10.5)
        r_ct.font.color.rgb = col
        disable_spellcheck(r_ct)

        p_cd = ctf.add_paragraph()
        r_cd = p_cd.add_run()
        r_cd.text = desc
        r_cd.font.size = Pt(8.0)
        r_cd.font.color.rgb = C_TEXT_MAIN
        disable_spellcheck(r_cd)

    # =========================================================================
    # SLIDE 3: INTRODUCTION
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_slide_frame(s3, "Introduction: Demystifying Large Language Models", "FOUNDATIONAL CONTEXT (SECTION 1)", "flower_slide_2.png", C_BG_S2, 3)

    # Left Card: The Paradigm Shift
    c3_l = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.45), Inches(1.35), Inches(5.05), Inches(5.55))
    c3_l.fill.solid()
    c3_l.fill.fore_color.rgb = C_CARD_BG
    c3_l.line.color.rgb = C_BORDER
    c3_l.line.width = Pt(1.0)

    tb3_l = s3.shapes.add_textbox(Inches(1.65), Inches(1.5), Inches(4.65), Inches(5.25))
    tf3_l = tb3_l.text_frame
    tf3_l.word_wrap = True

    p3_1 = tf3_l.paragraphs[0]
    r3_1 = p3_1.add_run()
    r3_1.text = "The Paradigm Shift in Natural Language AI"
    r3_1.font.bold = True
    r3_1.font.size = Pt(11)
    r3_1.font.color.rgb = C_TEAL_DEEP
    p3_1.space_after = Pt(8)

    intro_points_left = [
        ("Evolution Beyond Recurrence:", "Traditional NLP relied on RNNs and LSTMs that processed tokens sequentially, creating gradient bottlenecks and preventing parallel training on long contexts. Vaswani et al. (2017) revolutionized AI with Self-Attention, enabling whole-sequence parallel computation."),
        ("Autoregressive Modeling Formulation:", "At its mathematical core, a Decoder-Only LLM factorizes the joint probability of a text sequence into conditional probabilities via the chain rule: P(w1, ..., wT) = ∏ P(wt | w<t). The objective is predicting the single next token from preceding context."),
        ("The Educational Imperative:", "Frameworks like Hugging Face or LangChain abstract away how tensors flow through self-attention matrices. Building an LLM from scratch in pure Python reveals the exact matrix operations, dimensional projections, and causal masking mechanics.")
    ]
    for h, b in intro_points_left:
        p = tf3_l.add_paragraph()
        rh = p.add_run()
        rh.text = f"•  {h} "
        rh.font.bold = True
        rh.font.size = Pt(8.2)
        rh.font.color.rgb = C_OCEAN_DARK
        rb = p.add_run()
        rb.text = b
        rb.font.size = Pt(7.6)
        rb.font.color.rgb = C_TEXT_MAIN
        p.space_after = Pt(10)

    # Right Card: Three Core Pillars
    c3_r = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.65), Inches(1.35), Inches(5.15), Inches(5.55))
    c3_r.fill.solid()
    c3_r.fill.fore_color.rgb = RGBColor(255, 253, 245)
    c3_r.line.color.rgb = RGBColor(254, 240, 138)
    c3_r.line.width = Pt(1.0)

    tb3_r = s3.shapes.add_textbox(Inches(6.85), Inches(1.5), Inches(4.75), Inches(5.25))
    tf3_r = tb3_r.text_frame
    tf3_r.word_wrap = True

    p3_2 = tf3_r.paragraphs[0]
    r3_2 = p3_2.add_run()
    r3_2.text = "Three Foundational Pillars of Modern LLMs"
    r3_2.font.bold = True
    r3_2.font.size = Pt(11)
    r3_2.font.color.rgb = C_AMBER_WARM
    p3_2.space_after = Pt(8)

    pillars = [
        ("1. Mathematical Vector Rigor:", "Every word or character is mapped into high-dimensional geometric space (d_model). Through Scaled Dot-Product Attention, tokens query each other to dynamically enrich their contextual embeddings based on relevance rather than static dictionary lookups."),
        ("2. Computational Stability & Scale:", "Deep networks suffer from vanishing gradients. Modern LLMs incorporate Pre-LayerNorm (or RMSNorm) and residual identity skip connections, ensuring error gradients flow directly from loss back to early embedding layers unimpeded."),
        ("3. Generative Inference Control:", "Raw model outputs are unbounded logit distributions. Controlled text generation requires sophisticated sampling strategies—balancing deterministic greedy decoding against creative temperature and nucleus (Top-p) probability mass thresholds.")
    ]
    for h, b in pillars:
        p = tf3_r.add_paragraph()
        rh = p.add_run()
        rh.text = f"•  {h} "
        rh.font.bold = True
        rh.font.size = Pt(8.2)
        rh.font.color.rgb = C_OCEAN_DARK
        rb = p.add_run()
        rb.text = b
        rb.font.size = Pt(7.6)
        rb.font.color.rgb = C_TEXT_MAIN
        p.space_after = Pt(10)

    # =========================================================================
    # SLIDE 4: OBJECTIVE
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_slide_frame(s4, "Project Objectives & Technical Scope", "PROJECT SPECIFICATION (SECTION 2)", "flower_slide_3.png", C_BG_S3, 4)

    obj_quads = [
        ("OBJECTIVE 1: ARCHITECTURE FROM SCRATCH", C_TEAL_DEEP, RGBColor(240, 253, 250), RGBColor(153, 246, 228),
         "Design and construct a Decoder-Only Transformer architecture from foundational mathematics in pure Python and PyTorch.\n\n"
         "• Implement Multi-Head Causal Self-Attention, Pre-LN Transformer Blocks, and Position-wise FeedForward (MLP) layers.\n"
         "• Zero reliance on black-box external frameworks (HuggingFace transformers or LangChain)."),
        ("OBJECTIVE 2: TOKENIZATION & DATA PIPELINE", C_BLUE_ROYAL, RGBColor(239, 246, 255), RGBColor(191, 219, 254),
         "Engineer modular, transparent tokenization and sliding-window dataset loaders.\n\n"
         "• Develop a bidirectional Character-Level Tokenizer (65 tokens) and subword BPE wrapper for zero-dependency local training.\n"
         "• Implement PyTorch Dataset and DataLoader generating autoregressive targets (yt = xt+1) with causal sliding windows."),
        ("OBJECTIVE 3: PRETRAINING & CONVERGENCE", C_CORAL_RED, RGBColor(255, 241, 242), RGBColor(254, 205, 211),
         "Build a modern training harness with advanced optimization mechanics.\n\n"
         "• Integrate AdamW with decoupled weight decay (2D weights vs 1D biases/norms).\n"
         "• Implement Cosine Annealing learning rate schedule with linear warmup.\n"
         "• Track Cross-Entropy loss and Perplexity (exp(Loss)) with real-time generation previews."),
        ("OBJECTIVE 4: SAMPLING & OPEN SOURCE ARTIFACT", C_INDIGO, RGBColor(245, 243, 255), RGBColor(221, 214, 254),
         "Implement multi-mode text generation and deliver a production-grade open-source codebase.\n\n"
         "• Support Greedy, Temperature-scaled, Top-K, and Top-P (Nucleus) decoding.\n"
         "• Provide an interactive terminal REPL shell for live user prompting.\n"
         "• Release under GNU General Public License v3.0 (GPLv3) on GitHub (RSNPIIT).")
    ]

    card_w4 = Inches(5.05)
    card_h4 = Inches(2.65)
    xs4 = [Inches(1.45), Inches(6.75)]
    ys4 = [Inches(1.45), Inches(4.25)]

    for idx, (title, col, bg_col, bdr_col, body) in enumerate(obj_quads):
        qx = xs4[idx % 2]
        qy = ys4[idx // 2]
        q_box = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, qx, qy, card_w4, card_h4)
        q_box.fill.solid()
        q_box.fill.fore_color.rgb = bg_col
        q_box.line.color.rgb = bdr_col
        q_box.line.width = Pt(1.2)

        tb_q = s4.shapes.add_textbox(qx + Inches(0.18), qy + Inches(0.15), card_w4 - Inches(0.36), card_h4 - Inches(0.3))
        tf_q = tb_q.text_frame
        tf_q.word_wrap = True

        p_t = tf_q.paragraphs[0]
        r_t = p_t.add_run()
        r_t.text = title
        r_t.font.bold = True
        r_t.font.size = Pt(9.5)
        r_t.font.color.rgb = col
        p_t.space_after = Pt(6)

        p_b = tf_q.add_paragraph()
        r_b = p_b.add_run()
        r_b.text = body
        r_b.font.size = Pt(7.8)
        r_b.font.color.rgb = C_TEXT_MAIN

    # =========================================================================
    # SLIDE 5: METHODOLOGY 1 — Pipeline & Tokenization Architecture
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_slide_frame(s5, "Methodology: Architecture Pipeline & Tokenization", "TECHNICAL METHODOLOGY (1 OF 4)", "flower_slide_4.png", C_BG_S4, 5)

    # Top diagram: methodology_1_pipeline.png
    if os.path.exists("methodology_1_pipeline.png"):
        s5.shapes.add_picture("methodology_1_pipeline.png", Inches(1.45), Inches(1.35), Inches(10.35), Inches(2.75))

    # Bottom Cards
    bot_y5 = Inches(4.25)
    bot_h5 = Inches(2.65)
    bot_w5 = Inches(5.05)

    # Left Bottom Card
    cb5_l = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.45), bot_y5, bot_w5, bot_h5)
    cb5_l.fill.solid()
    cb5_l.fill.fore_color.rgb = C_CARD_BG
    cb5_l.line.color.rgb = C_BORDER
    cb5_l.line.width = Pt(1.0)

    t5_l = s5.shapes.add_textbox(Inches(1.65), bot_y5 + Inches(0.12), bot_w5 - Inches(0.4), bot_h5 - Inches(0.24))
    tf5_l = t5_l.text_frame
    tf5_l.word_wrap = True

    p = tf5_l.paragraphs[0]
    r = p.add_run()
    r.text = "Tokenization & Sliding-Window Dataloader"
    r.font.bold = True
    r.font.size = Pt(10)
    r.font.color.rgb = C_TEAL_DEEP
    p.space_after = Pt(4)

    t5_l_points = [
        ("Deterministic Character Vocabulary:", "Extracts unique character set (V=65 for Tiny Shakespeare). Builds bijective lookup tables char_to_id and id_to_char, allowing exact token reconstruction with zero external dependencies."),
        ("Autoregressive Sliding-Window Chunking:", "Text is encoded into a 1D tensor. TextDataset samples chunks of length block_size (T=128/256). The target sequence y is x shifted by exactly 1 position (yt = xt+1), creating supervised pairs for next-token prediction.")
    ]
    for h, b in t5_l_points:
        p = tf5_l.add_paragraph()
        rh = p.add_run()
        rh.text = f"•  {h} "
        rh.font.bold = True
        rh.font.size = Pt(7.8)
        rh.font.color.rgb = C_OCEAN_DARK
        rb = p.add_run()
        rb.text = b
        rb.font.size = Pt(7.2)
        rb.font.color.rgb = C_TEXT_MAIN
        p.space_after = Pt(4)

    # Right Bottom Card
    cb5_r = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.75), bot_y5, bot_w5, bot_h5)
    cb5_r.fill.solid()
    cb5_r.fill.fore_color.rgb = C_CARD_BG
    cb5_r.line.color.rgb = C_BORDER
    cb5_r.line.width = Pt(1.0)

    t5_r = s5.shapes.add_textbox(Inches(6.95), bot_y5 + Inches(0.12), bot_w5 - Inches(0.4), bot_h5 - Inches(0.24))
    tf5_r = t5_r.text_frame
    tf5_r.word_wrap = True

    p = tf5_r.paragraphs[0]
    r = p.add_run()
    r.text = "Dual Embedding Space Formulation"
    r.font.bold = True
    r.font.size = Pt(10)
    r.font.color.rgb = C_BLUE_ROYAL
    p.space_after = Pt(4)

    t5_r_points = [
        ("Token Embeddings (wte):", "Token IDs are projected from discrete indices {0..V-1} into continuous d_model-dimensional vectors using nn.Embedding(V, d_model), initialized with normal distribution (mean=0, std=0.02)."),
        ("Positional Embeddings & RoPE:", "Transformers possess no inherent sequential inductive bias. We inject positional awareness via learned embeddings (wpe: T → d_model), adding x = wte(tok) + wpe(pos), with optional support for modern Rotary Position Embeddings (RoPE).")
    ]
    for h, b in t5_r_points:
        p = tf5_r.add_paragraph()
        rh = p.add_run()
        rh.text = f"•  {h} "
        rh.font.bold = True
        rh.font.size = Pt(7.8)
        rh.font.color.rgb = C_OCEAN_DARK
        rb = p.add_run()
        rb.text = b
        rb.font.size = Pt(7.2)
        rb.font.color.rgb = C_TEXT_MAIN
        p.space_after = Pt(4)

    # =========================================================================
    # SLIDE 6: METHODOLOGY 2 — Causal Multi-Head Self-Attention
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_slide_frame(s6, "Methodology: Causal Attention & Look-Ahead Masking", "TECHNICAL METHODOLOGY (2 OF 4)", "flower_slide_5.png", C_BG_S5, 6)

    # Left: methodology_2_attention.png
    if os.path.exists("methodology_2_attention.png"):
        s6.shapes.add_picture("methodology_2_attention.png", Inches(1.45), Inches(1.35), Inches(5.6), Inches(5.55))

    # Right Card: Explanation
    c6_r = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.2), Inches(1.35), Inches(4.6), Inches(5.55))
    c6_r.fill.solid()
    c6_r.fill.fore_color.rgb = C_CARD_BG
    c6_r.line.color.rgb = C_BORDER
    c6_r.line.width = Pt(1.0)

    tb6 = s6.shapes.add_textbox(Inches(7.4), Inches(1.5), Inches(4.2), Inches(5.25))
    tf6 = tb6.text_frame
    tf6.word_wrap = True

    p = tf6.paragraphs[0]
    r = p.add_run()
    r.text = "Mathematical Mechanics of Causal Attention"
    r.font.bold = True
    r.font.size = Pt(10.5)
    r.font.color.rgb = C_CORAL_RED
    p.space_after = Pt(8)

    attn_points = [
        ("Batched Linear Projection:", "A single matrix multiply projects input x into Queries (Q), Keys (K), and Values (V): c_attn(x) ∈ R^(B × T × 3·n_embd), split into n_head heads of dimension head_dim = n_embd / n_head."),
        ("Scaled Dot-Product Formula:", "Attention weights are computed by taking the inner product of queries and keys scaled by 1/√d_k to prevent gradient vanishing in large dimensions: Attn = (Q · K^T) / √d_k."),
        ("The Causal Lower-Triangular Mask:", "To enforce strict autoregression, an upper-triangular boolean mask replaces all future token affinities (j > i) with -∞ before softmax: Softmax(-∞) = 0. Tokens can only look backward in time."),
        ("Softmax & Value Weighting:", "Softmax normalizes row scores into a valid probability distribution. Multiplying by Values (V) produces contextually enriched token vectors: y = Softmax(Attn + M) · V."),
        ("Apple Silicon MPS Support:", "Optimized with fallback handling for PyTorch 2.0+ FlashAttention vs manual attention, accommodating Apple MPS GPU specifics.")
    ]
    for h, b in attn_points:
        p = tf6.add_paragraph()
        rh = p.add_run()
        rh.text = f"•  {h} "
        rh.font.bold = True
        rh.font.size = Pt(7.8)
        rh.font.color.rgb = C_OCEAN_DARK
        rb = p.add_run()
        rb.text = b
        rb.font.size = Pt(7.1)
        rb.font.color.rgb = C_TEXT_MAIN
        p.space_after = Pt(6)

    # =========================================================================
    # SLIDE 7: METHODOLOGY 3 — Transformer Blocks & Normalization
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    add_slide_frame(s7, "Methodology: Pre-LN Blocks & Feed-Forward Networks", "TECHNICAL METHODOLOGY (3 OF 4)", "flower_slide_6.png", C_BG_S6, 7)

    # Left: methodology_3_transformer_block.png
    if os.path.exists("methodology_3_transformer_block.png"):
        s7.shapes.add_picture("methodology_3_transformer_block.png", Inches(1.45), Inches(1.35), Inches(5.6), Inches(5.55))

    # Right Card: Explanation
    c7_r = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.2), Inches(1.35), Inches(4.6), Inches(5.55))
    c7_r.fill.solid()
    c7_r.fill.fore_color.rgb = C_CARD_BG
    c7_r.line.color.rgb = C_BORDER
    c7_r.line.width = Pt(1.0)

    tb7 = s7.shapes.add_textbox(Inches(7.4), Inches(1.5), Inches(4.2), Inches(5.25))
    tf7 = tb7.text_frame
    tf7.word_wrap = True

    p = tf7.paragraphs[0]
    r = p.add_run()
    r.text = "Transformer Block Dynamics & Stability"
    r.font.bold = True
    r.font.size = Pt(10.5)
    r.font.color.rgb = C_BLUE_ROYAL
    p.space_after = Pt(8)

    block_points = [
        ("Pre-LayerNorm Architecture:", "Unlike early Post-LN Transformers that placed normalization after residual addition, modern LLMs (GPT-2, LLaMA) place normalization before attention and MLP: x = x + SubLayer(Norm(x)). This ensures the residual stream remains clean, preventing vanishing gradients."),
        ("RMSNorm Alternative:", "Supports modern Root Mean Square Normalization (Zhang & Sennrich, 2019): RMSNorm(x) = x / √(mean(x²) + ε) · γ, which eliminates mean-centering, cutting computational overhead while preserving accuracy."),
        ("Feed-Forward Network (GELU MLP):", "Applies position-wise non-linear feature transformation: Linear(d_model, 4·d_model) → GELU() → Linear(4·d_model, d_model). GELU (Gaussian Error Linear Unit) provides smooth, differentiable activation."),
        ("Residual Identity Highway:", "Skip connections provide an uninterrupted gradient highway from output loss back to early embedding layers, enabling stable convergence across arbitrary network depths.")
    ]
    for h, b in block_points:
        p = tf7.add_paragraph()
        rh = p.add_run()
        rh.text = f"•  {h} "
        rh.font.bold = True
        rh.font.size = Pt(7.8)
        rh.font.color.rgb = C_OCEAN_DARK
        rb = p.add_run()
        rb.text = b
        rb.font.size = Pt(7.2)
        rb.font.color.rgb = C_TEXT_MAIN
        p.space_after = Pt(8)

    # =========================================================================
    # SLIDE 8: METHODOLOGY 4 — Training Engine & Optimization Mechanics
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    add_slide_frame(s8, "Methodology: Pretraining Loop & Optimization Dynamics", "TECHNICAL METHODOLOGY (4 OF 4)", "flower_slide_1.png", C_BG_S7, 8)

    # Left: methodology_4_training_curves.png
    if os.path.exists("methodology_4_training_curves.png"):
        s8.shapes.add_picture("methodology_4_training_curves.png", Inches(1.45), Inches(1.35), Inches(5.6), Inches(5.55))

    # Right Card: Explanation
    c8_r = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.2), Inches(1.35), Inches(4.6), Inches(5.55))
    c8_r.fill.solid()
    c8_r.fill.fore_color.rgb = C_CARD_BG
    c8_r.line.color.rgb = C_BORDER
    c8_r.line.width = Pt(1.0)

    tb8 = s8.shapes.add_textbox(Inches(7.4), Inches(1.5), Inches(4.2), Inches(5.25))
    tf8 = tb8.text_frame
    tf8.word_wrap = True

    p = tf8.paragraphs[0]
    r = p.add_run()
    r.text = "Optimization & Pretraining Harness"
    r.font.bold = True
    r.font.size = Pt(10.5)
    r.font.color.rgb = C_AMBER_WARM
    p.space_after = Pt(8)

    train_points = [
        ("Cross-Entropy Loss Function:", "The model is trained end-to-end to minimize cross-entropy loss between predicted vocabulary logits and target next tokens: L(θ) = -1/T ∑ log P(x_t | x_<t)."),
        ("Validation Perplexity (PPL):", "Perplexity = exp(Loss). Interpreted as the effective number of equally likely words the model is choosing between at each step. PPL drops rapidly from 67.35 to 4.67."),
        ("Decoupled AdamW Weight Decay:", "Weight decay (0.1) is selectively applied only to 2D weight matrices (linear projections and embeddings). 1D biases and normalization scale parameters are excluded from decay to prevent harmful underfitting."),
        ("Cosine Annealing with Warmup:", "Learning rate warms up linearly over the first 50 iterations from 0 to 6e-4 to stabilize early gradients, then decays smoothly following a cosine curve down to 10% peak LR."),
        ("Gradient Clipping:", "Clips parameter gradients at max_norm=1.0, preventing gradient explosions during sudden loss spikes.")
    ]
    for h, b in train_points:
        p = tf8.add_paragraph()
        rh = p.add_run()
        rh.text = f"•  {h} "
        rh.font.bold = True
        rh.font.size = Pt(7.8)
        rh.font.color.rgb = C_OCEAN_DARK
        rb = p.add_run()
        rb.text = b
        rb.font.size = Pt(7.1)
        rb.font.color.rgb = C_TEXT_MAIN
        p.space_after = Pt(6)

    # =========================================================================
    # SLIDE 9: RESULT ANALYSIS & GENERATION BENCHMARKS
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    add_slide_frame(s9, "Result Analysis: Convergence & Text Generation", "EXPERIMENTAL EVALUATION (SECTION 4)", "flower_slide_2.png", C_BG_S8, 9)

    # Top Table Card: Training Evolution
    c9_top = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.45), Inches(1.35), Inches(10.35), Inches(2.55))
    c9_top.fill.solid()
    c9_top.fill.fore_color.rgb = C_CARD_BG
    c9_top.line.color.rgb = C_BORDER
    c9_top.line.width = Pt(1.0)

    tb9_top = s9.shapes.add_textbox(Inches(1.65), Inches(1.45), Inches(9.95), Inches(2.35))
    tf9_top = tb9_top.text_frame
    tf9_top.word_wrap = True

    p = tf9_top.paragraphs[0]
    r = p.add_run()
    r.text = "Empirical Pretraining Dynamics: Qualitative Evolution Across Iterations"
    r.font.bold = True
    r.font.size = Pt(10)
    r.font.color.rgb = C_OCEAN_DARK
    p.space_after = Pt(6)

    steps_eval = [
        ("Step 0 (Untrained)", "Train Loss: 4.20  |  Val Loss: 4.21  |  PPL: 67.35",
         "\"KING: J:A -Ft,OVjww$pPVtg wwLNbjSesKv&PZg;y&XXmtBsuUgw-3b...\"",
         "Pure stochastic noise; uniform character distribution across vocabulary."),
        ("Step 50 (Early Phase)", "Train Loss: 2.78  |  Val Loss: 2.97  |  PPL: 19.63",
         "\"KING: Adousifos d b he theid thore d ad at thirroind cre d s lo...\"",
         "Learns whitespace separation, word-like character clusters, and English character frequencies."),
        ("Step 100 (Rapid Convergence)", "Train Loss: 2.59  |  Val Loss: 2.81  |  PPL: 16.63",
         "\"KING: I: thein le. I hal ite bforat ind lond hind fr tesithnd tit...\"",
         "Learns common English morphemes ('th', 'in', 'ind', 'for'), dialogue naming syntax, and vowels."),
        ("Step 1000 (Mature Pretraining)", "Train Loss: 1.38  |  Val Loss: 1.54  |  PPL: 4.67",
         "\"KING: What news from the northern march, my lord? Speak of the duke.\"",
         "Syntactically coherent, Shakespearean-style dialogue with grammatical subject-verb alignment.")
    ]
    for st, met, quote, comment in steps_eval:
        p = tf9_top.add_paragraph()
        r1 = p.add_run()
        r1.text = f"•  {st}  [{met}]:  "
        r1.font.bold = True
        r1.font.size = Pt(7.6)
        r1.font.color.rgb = C_CORAL_RED
        r2 = p.add_run()
        r2.text = f"{quote}  —  "
        r2.font.bold = True
        r2.font.size = Pt(7.4)
        r2.font.color.rgb = C_OCEAN_DARK
        r3 = p.add_run()
        r3.text = comment
        r3.font.size = Pt(7.2)
        r3.font.color.rgb = C_TEXT_MUTED
        p.space_after = Pt(3)

    # Bottom Left Card: Sampling Strategy Comparison
    c9_bl = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.45), Inches(4.05), Inches(5.05), Inches(2.85))
    c9_bl.fill.solid()
    c9_bl.fill.fore_color.rgb = RGBColor(240, 253, 250)
    c9_bl.line.color.rgb = RGBColor(153, 246, 228)
    c9_bl.line.width = Pt(1.0)

    tb9_bl = s9.shapes.add_textbox(Inches(1.65), Inches(4.15), Inches(4.65), Inches(2.65))
    tf9_bl = tb9_bl.text_frame
    tf9_bl.word_wrap = True

    p = tf9_bl.paragraphs[0]
    r = p.add_run()
    r.text = "Inference Sampling Strategies Compared"
    r.font.bold = True
    r.font.size = Pt(9.5)
    r.font.color.rgb = C_TEAL_DEEP
    p.space_after = Pt(4)

    sampling_points = [
        ("Greedy Search (Temp = 0.0):", "Picks argmax P(xt). Highly repetitive, gets stuck in predictable local loops ('the the the')."),
        ("Temperature Scaling (0.7 - 0.85):", "Smooths logit distribution. Balance between coherent syntax and creative vocabulary diversity."),
        ("Top-K Filtering (k = 40):", "Cuts off low-probability tail, preventing catastrophic hallucinations and out-of-context tokens."),
        ("Top-P Nucleus (p = 0.90):", "Dynamically expands or contracts the candidate pool based on model confidence.")
    ]
    for h, b in sampling_points:
        p = tf9_bl.add_paragraph()
        rh = p.add_run()
        rh.text = f"•  {h} "
        rh.font.bold = True
        rh.font.size = Pt(7.6)
        rh.font.color.rgb = C_OCEAN_DARK
        rb = p.add_run()
        rb.text = b
        rb.font.size = Pt(7.1)
        rb.font.color.rgb = C_TEXT_MAIN
        p.space_after = Pt(3)

    # Bottom Right Card: Hardware & Efficiency
    c9_br = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.75), Inches(4.05), Inches(5.05), Inches(2.85))
    c9_br.fill.solid()
    c9_br.fill.fore_color.rgb = RGBColor(239, 246, 255)
    c9_br.line.color.rgb = RGBColor(191, 219, 254)
    c9_br.line.width = Pt(1.0)

    tb9_br = s9.shapes.add_textbox(Inches(6.95), Inches(4.15), Inches(4.65), Inches(2.65))
    tf9_br = tb9_br.text_frame
    tf9_br.word_wrap = True

    p = tf9_br.paragraphs[0]
    r = p.add_run()
    r.text = "Hardware Performance & Efficiency"
    r.font.bold = True
    r.font.size = Pt(9.5)
    r.font.color.rgb = C_BLUE_ROYAL
    p.space_after = Pt(4)

    hw_points = [
        ("Apple Silicon MPS Acceleration:", "Leverages Metal Performance Shaders on macOS. Achieved 24.5 iterations/sec on nano preset (~14 seconds per 100 training steps)."),
        ("Memory Footprint:", "Model weights and optimizer states require only ~12 MB VRAM for nano configuration, making local training accessible on personal laptops."),
        ("Linear Scaling:", "Model scales cleanly to micro (10.8M parameters) and full GPT-2 (124M parameters) without altering core mathematical modules.")
    ]
    for h, b in hw_points:
        p = tf9_br.add_paragraph()
        rh = p.add_run()
        rh.text = f"•  {h} "
        rh.font.bold = True
        rh.font.size = Pt(7.6)
        rh.font.color.rgb = C_OCEAN_DARK
        rb = p.add_run()
        rb.text = b
        rb.font.size = Pt(7.1)
        rb.font.color.rgb = C_TEXT_MAIN
        p.space_after = Pt(4)

    # =========================================================================
    # SLIDE 10: CONCLUSION & FUTURE SCOPE
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    add_slide_frame(s10, "Conclusion: Key Learnings & Future Roadmap", "PROJECT SUMMARY (SECTION 5)", "flower_slide_3.png", C_BG_S9, 10)

    # Left Card: Key Learnings
    c10_l = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.45), Inches(1.35), Inches(5.05), Inches(5.55))
    c10_l.fill.solid()
    c10_l.fill.fore_color.rgb = C_CARD_BG
    c10_l.line.color.rgb = C_BORDER
    c10_l.line.width = Pt(1.0)

    tb10_l = s10.shapes.add_textbox(Inches(1.65), Inches(1.5), Inches(4.65), Inches(5.25))
    tf10_l = tb10_l.text_frame
    tf10_l.word_wrap = True

    p = tf10_l.paragraphs[0]
    r = p.add_run()
    r.text = "Key Technical Competencies & Takeaways"
    r.font.bold = True
    r.font.size = Pt(11)
    r.font.color.rgb = C_TEAL_DEEP
    p.space_after = Pt(8)

    learnings = [
        ("Foundational Deep Learning Mastery:", "Gained rigorous, first-principles mastery of Transformer architectures, tensor projections, and scaled dot-product attention without high-level library abstractions."),
        ("Causal Mechanism Understanding:", "Discovered how mathematical masking enforces temporal boundaries, proving that Generative AI is fundamentally statistical next-token density estimation."),
        ("Optimization Insights:", "Understood the critical role of decoupled weight decay, learning rate warmup, and Pre-LN stabilization in preventing training divergence."),
        ("Open-Source Deliverable:", "Released a modular, clean, and fully reproducible codebase on GitHub under the GNU GPLv3 license for the academic and AI developer community.")
    ]
    for h, b in learnings:
        p = tf10_l.add_paragraph()
        rh = p.add_run()
        rh.text = f"•  {h} "
        rh.font.bold = True
        rh.font.size = Pt(8.2)
        rh.font.color.rgb = C_OCEAN_DARK
        rb = p.add_run()
        rb.text = b
        rb.font.size = Pt(7.6)
        rb.font.color.rgb = C_TEXT_MAIN
        p.space_after = Pt(8)

    # Right Card: Future Scope
    c10_r = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.65), Inches(1.35), Inches(5.15), Inches(5.55))
    c10_r.fill.solid()
    c10_r.fill.fore_color.rgb = RGBColor(245, 243, 255)
    c10_r.line.color.rgb = RGBColor(221, 214, 254)
    c10_r.line.width = Pt(1.0)

    tb10_r = s10.shapes.add_textbox(Inches(6.85), Inches(1.5), Inches(4.75), Inches(5.25))
    tf10_r = tb10_r.text_frame
    tf10_r.word_wrap = True

    p = tf10_r.paragraphs[0]
    r = p.add_run()
    r.text = "Future Technical Expansion Roadmap"
    r.font.bold = True
    r.font.size = Pt(11)
    r.font.color.rgb = C_INDIGO
    p.space_after = Pt(8)

    future_scope = [
        ("Phase 1: Supervised Fine-Tuning (SFT):", "Transitioning the base pretrained model into an instruction-following conversational assistant using curated prompt-response pairs."),
        ("Phase 2: Low-Rank Adaptation (LoRA):", "Implementing parameter-efficient fine-tuning (PEFT) by decomposing attention weight update matrices (ΔW = A × B), enabling rapid domain adaptation on consumer GPUs."),
        ("Phase 3: Preference Alignment (DPO / RLHF):", "Aligning model generation with human values and safety guidelines via Direct Preference Optimization (DPO)."),
        ("Phase 4: Architectural Innovations:", "Experimenting with Rotary Position Embeddings (RoPE), SwiGLU activations, and Mixture of Experts (MoE) routing for next-generation efficiency.")
    ]
    for h, b in future_scope:
        p = tf10_r.add_paragraph()
        rh = p.add_run()
        rh.text = f"•  {h} "
        rh.font.bold = True
        rh.font.size = Pt(8.2)
        rh.font.color.rgb = C_OCEAN_DARK
        rb = p.add_run()
        rb.text = b
        rb.font.size = Pt(7.6)
        rb.font.color.rgb = C_TEXT_MAIN
        p.space_after = Pt(8)

    output_pptx = "LLM_Using_Python_Ramrup_Satpati.pptx"
    prs.save(output_pptx)
    print(f"[*] Successfully saved PowerPoint presentation: {output_pptx}")


if __name__ == "__main__":
    build_presentation()
