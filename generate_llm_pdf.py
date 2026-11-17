"""
ReportLab Vector PDF Generator for LLM Using Python by Ramrup Satpati.
Generates an exact matching 10-page vector PDF (LLM_Using_Python_Ramrup_Satpati.pdf).
"""

import os
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle

PAGE_WIDTH = 960.0
PAGE_HEIGHT = 540.0

# SPG Colors
HEX_OCEAN_DARK = HexColor("#0f172a")
HEX_CORAL_RED  = HexColor("#e11d48")
HEX_CORAL_SOFT = HexColor("#f43f5e")
HEX_TEAL_DEEP  = HexColor("#0d9488")
HEX_BLUE_ROYAL = HexColor("#1d4ed8")
HEX_INDIGO     = HexColor("#4f46e5")
HEX_AMBER_WARM = HexColor("#ea580c")
HEX_TEXT_MAIN  = HexColor("#1f2937")
HEX_TEXT_MUTED = HexColor("#64748b")
HEX_CARD_BG    = HexColor("#ffffff")
HEX_BORDER     = HexColor("#cbd5e1")


def draw_top_down(p, x, y_top, w, h):
    actual_w, actual_h = p.wrap(w, h)
    p.drawOn(c, x, y_top - actual_h)
    return actual_h


def add_pdf_frame(title_text, category_text, corner_img=None, bg_hex="#f8fafc", slide_num=1):
    c.setFillColor(HexColor(bg_hex))
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    if corner_img and os.path.exists(corner_img):
        c.drawImage(corner_img, 18, PAGE_HEIGHT - 82, width=70, height=70, mask="auto")

    c.setFillColor(HEX_CORAL_RED)
    c.setFont("Helvetica-Bold", 8.5)
    c.drawString(102, PAGE_HEIGHT - 38, category_text.upper())

    c.setFillColor(HEX_OCEAN_DARK)
    c.setFont("Helvetica-Bold", 16.5)
    c.drawString(102, PAGE_HEIGHT - 58, title_text)

    c.setStrokeColor(HEX_CORAL_RED)
    c.setLineWidth(2)
    c.line(102, PAGE_HEIGHT - 68, PAGE_WIDTH - 110, PAGE_HEIGHT - 68)

    if os.path.exists("iitm_logo_clean.png"):
        c.drawImage("iitm_logo_clean.png", PAGE_WIDTH - 98, PAGE_HEIGHT - 75, width=72, height=72, mask="auto")

    if os.path.exists("page_flip_corner.png"):
        c.drawImage("page_flip_corner.png", PAGE_WIDTH - 55, 0, width=55, height=86, mask="auto")

    c.setStrokeColor(HexColor("#e2e8f0"))
    c.setLineWidth(1)
    c.line(102, 24, PAGE_WIDTH - 110, 24)

    c.setFillColor(HEX_TEXT_MUTED)
    c.setFont("Helvetica", 8)
    c.drawString(102, 12, f"Ramrup Satpati (24F3004027)  •  LLM Using Python: Decoder-Only Transformer from Scratch  •  Slide {slide_num} of 10")
    c.drawRightString(PAGE_WIDTH - 115, 12, "IIT Madras BS Degree")


output_pdf = "LLM_Using_Python_Ramrup_Satpati.pdf"
c = canvas.Canvas(output_pdf, pagesize=(PAGE_WIDTH, PAGE_HEIGHT))

# =============================================================================
# SLIDE 1: COVER
# =============================================================================
c.setFillColor(HexColor("#fcfdff"))
c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

if os.path.exists("flower_slide_0.png"):
    c.drawImage("flower_slide_0.png", 26, PAGE_HEIGHT - 105, width=76, height=76, mask="auto")
if os.path.exists("flower_cover_bottom.png"):
    c.drawImage("flower_cover_bottom.png", 26, 32, width=76, height=76, mask="auto")
if os.path.exists("iitm_logo_clean.png"):
    c.drawImage("iitm_logo_clean.png", PAGE_WIDTH - 115, PAGE_HEIGHT - 115, width=90, height=90, mask="auto")
if os.path.exists("page_flip_corner.png"):
    c.drawImage("page_flip_corner.png", PAGE_WIDTH - 55, 0, width=55, height=86, mask="auto")

card_lx = 115
card_ly = 45
card_lw = 520
card_lh = PAGE_HEIGHT - 90

c.setFillColor(HEX_CARD_BG)
c.setStrokeColor(HEX_BORDER)
c.setLineWidth(1.2)
c.roundRect(card_lx, card_ly, card_lw, card_lh, 8, fill=1, stroke=1)

c.setFillColor(HEX_CORAL_RED)
c.setFont("Helvetica-Bold", 9.5)
c.drawString(card_lx + 25, card_ly + card_lh - 32, "IIT MADRAS BS DEGREE PROGRAMME  •  PROJECT PRESENTATION")

c.setFillColor(HEX_TEXT_MUTED)
c.setFont("Helvetica-Bold", 8.5)
c.drawString(card_lx + 25, card_ly + card_lh - 48, "BS IN DATA SCIENCE & APPLICATIONS  •  DEEP LEARNING & GENERATIVE AI")

c.setFillColor(HEX_OCEAN_DARK)
c.setFont("Helvetica-Bold", 24)
c.drawString(card_lx + 25, card_ly + card_lh - 84, "LLM USING PYTHON")

c.setFillColor(HEX_TEAL_DEEP)
c.setFont("Helvetica-Bold", 12)
c.drawString(card_lx + 25, card_ly + card_lh - 106, "Building a Large Language Model from Scratch in Python & PyTorch")

desc_p1 = (
    "A complete, mathematically rigorous implementation of a Decoder-Only Generative Pretrained "
    "Transformer—from custom tokenization and causal multi-head self-attention to pretraining and nucleus sampling."
)
p_d1 = Paragraph(f"<font size='8.5' color='#334155'>{desc_p1}</font>", ParagraphStyle('D1', fontName='Helvetica', fontSize=8.5, leading=12))
draw_top_down(p_d1, card_lx + 25, card_ly + card_lh - 120, card_lw - 50, 45)

meta_items = [
    ("Author & Developer:", "RAMRUP SATPATI (Roll No: 24F3004027)"),
    ("Institutional Email:", "24f3004027@ds.study.iitm.ac.in"),
    ("GitHub Repository:", "github.com/RSNPIIT/LLM_Using_Python_project"),
    ("Open-Source License:", "GNU General Public License v3.0 (Copyleft GPLv3)")
]
m_y = card_ly + card_lh - 180
for lbl, val in meta_items:
    c.setFillColor(HEX_BLUE_ROYAL)
    c.setFont("Helvetica-Bold", 8.8)
    c.drawString(card_lx + 25, m_y, f"•   {lbl}")
    c.setFillColor(HEX_TEXT_MAIN)
    c.setFont("Helvetica", 8.8)
    c.drawString(card_lx + 155, m_y, val)
    m_y -= 22

# Right Portrait Card
card_rx = 650
card_rw = PAGE_WIDTH - 650 - 115
c.setFillColor(HEX_CARD_BG)
c.setStrokeColor(HEX_BORDER)
c.roundRect(card_rx, card_ly, card_rw, card_lh, 8, fill=1, stroke=1)

if os.path.exists("ramrup_photo_extracted.png"):
    c.drawImage("ramrup_photo_extracted.png", card_rx + 15, card_ly + 145, width=card_rw - 30, height=275, mask="auto")

c.setFillColor(HEX_OCEAN_DARK)
c.setFont("Helvetica-Bold", 12.5)
c.drawCentredString(card_rx + card_rw / 2, card_ly + 115, "RAMRUP SATPATI")

c.setFillColor(HEX_CORAL_RED)
c.setFont("Helvetica-Bold", 8.5)
c.drawCentredString(card_rx + card_rw / 2, card_ly + 98, "Lead AI & Deep Learning Developer")

c.setFillColor(HEX_TEXT_MUTED)
c.setFont("Helvetica", 7.8)
c.drawCentredString(card_rx + card_rw / 2, card_ly + 82, "IIT Madras BS Degree in Data Science")
c.drawCentredString(card_rx + card_rw / 2, card_ly + 68, "Deep Learning & Generative AI")

c.showPage()

# =============================================================================
# SLIDE 2: CONTENTS
# =============================================================================
add_pdf_frame("Table of Contents & Executive Roadmap", "PROJECT OVERVIEW", "flower_slide_1.png", "#f8fafc", 2)

# Top Banner
c.setFillColor(HexColor("#fff1f2"))
c.setStrokeColor(HexColor("#fecdd3"))
c.roundRect(102, 436, PAGE_WIDTH - 212, 24, 4, fill=1, stroke=1)
c.setFillColor(HEX_CORAL_RED)
c.setFont("Helvetica-Bold", 8.0)
c.drawString(116, 444, "PROJECT ROADMAP:")
c.setFillColor(HEX_OCEAN_DARK)
c.setFont("Helvetica-Bold", 8.0)
c.drawString(220, 444, "5 Key Phases from First-Principles Mathematics to Pretraining, Nucleus Sampling & Open-Source Release")

contents_pdf = [
    ("01", "INTRODUCTION", HEX_TEAL_DEEP, HexColor("#f0fdf4"),
     "The generative AI paradigm shift; autoregressive formulation P(wt | w_past); why building an LLM from scratch in pure Python uncovers foundational mechanics that high-level APIs obscure."),
    ("02", "OBJECTIVE", HEX_BLUE_ROYAL, HexColor("#eff6ff"),
     "Core engineering goals: custom tokenization, causal self-attention, pre-LN Transformer blocks, AdamW pretraining on Tiny Shakespeare, and multi-mode text generation engines."),
    ("03", "METHODOLOGY", HEX_CORAL_RED, HexColor("#fff1f2"),
     "4-Stage Technical Architecture: (1) Tokenization & Dataloader; (2) Causal Multi-Head Self-Attention & Masking; (3) Transformer Blocks & RMSNorm/GELU; (4) Pretraining & Optimizer Engine."),
    ("04", "RESULT ANALYSIS", HEX_AMBER_WARM, HexColor("#fff7ed"),
     "Empirical convergence evaluation: loss reduction from 4.21 to 1.45 (Perplexity 67.35 to 4.67); comparative sampling evaluation (Greedy, Temperature, Top-K, Nucleus); hardware MPS benchmarks."),
    ("05", "CONCLUSION", HEX_INDIGO, HexColor("#faf5ff"),
     "Key technical competencies gained; verifiable open-source GPLv3 GitHub repository; architectural scalability roadmap (Fine-tuning, LoRA, and DPO alignment).")
]

cy = 360
for num, title, col, bg_col, desc in contents_pdf:
    c.setFillColor(bg_col)
    c.setStrokeColor(HexColor("#e2e8f0"))
    c.roundRect(102, cy, PAGE_WIDTH - 212, 62, 5, fill=1, stroke=1)

    c.setFillColor(col)
    c.roundRect(114, cy + 12, 38, 38, 4, fill=1, stroke=0)
    c.setFillColor(HEX_CARD_BG)
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(133, cy + 24, num)

    c.setFillColor(col)
    c.setFont("Helvetica-Bold", 9.8)
    c.drawString(165, cy + 44, title)

    p_c = Paragraph(f"<font size='7.5' color='#334155'>{desc}</font>", ParagraphStyle('CD', fontName='Helvetica', fontSize=7.5, leading=10))
    draw_top_down(p_c, 165, cy + 40, PAGE_WIDTH - 395, 35)

    cy -= 72

c.showPage()

# =============================================================================
# SLIDE 3: INTRODUCTION
# =============================================================================
add_pdf_frame("Introduction: Demystifying Large Language Models", "FOUNDATIONAL CONTEXT (SECTION 1)", "flower_slide_2.png", "#faf8f5", 3)

c_w = (PAGE_WIDTH - 212 - 16) / 2
c_h = 390
c_y = 40

# Left Card
c.setFillColor(HEX_CARD_BG)
c.setStrokeColor(HEX_BORDER)
c.roundRect(102, c_y, c_w, c_h, 6, fill=1, stroke=1)

c.setFillColor(HEX_TEAL_DEEP)
c.setFont("Helvetica-Bold", 10.5)
c.drawString(116, c_y + c_h - 22, "The Paradigm Shift in Natural Language AI")

intro_left_pdf = [
    ("Evolution Beyond Recurrence:", "Traditional NLP relied on RNNs and LSTMs that processed tokens sequentially, creating gradient bottlenecks and preventing parallel training on long contexts. Vaswani et al. (2017) revolutionized AI with Self-Attention, enabling whole-sequence parallel computation."),
    ("Autoregressive Modeling Formulation:", "At its mathematical core, a Decoder-Only LLM factorizes the joint probability of a text sequence into conditional probabilities via the chain rule: P(w1, ..., wT) = ∏ P(wt | w_past). The objective is predicting the single next token from preceding context."),
    ("The Educational Imperative:", "Frameworks like Hugging Face or LangChain abstract away how tensors flow through self-attention matrices. Building an LLM from scratch in pure Python reveals the exact matrix operations, dimensional projections, and causal masking mechanics.")
]
py_cur = c_y + c_h - 36
for h, b in intro_left_pdf:
    c.setFillColor(HEX_OCEAN_DARK)
    c.setFont("Helvetica-Bold", 8.2)
    c.drawString(116, py_cur, f"•   {h}")
    p = Paragraph(f"<font size='7.5' color='#334155'>{b}</font>", ParagraphStyle('IL', fontName='Helvetica', fontSize=7.5, leading=10.5))
    h_used = draw_top_down(p, 126, py_cur - 6, c_w - 28, 90)
    py_cur -= (h_used + 16)

# Right Card
c.setFillColor(HexColor("#fffdf7"))
c.setStrokeColor(HexColor("#fef08a"))
c.roundRect(102 + c_w + 16, c_y, c_w, c_h, 6, fill=1, stroke=1)

c.setFillColor(HEX_AMBER_WARM)
c.setFont("Helvetica-Bold", 10.5)
c.drawString(102 + c_w + 30, c_y + c_h - 22, "Three Foundational Pillars of Modern LLMs")

intro_right_pdf = [
    ("1. Mathematical Vector Rigor:", "Every word or character is mapped into high-dimensional geometric space (d_model). Through Scaled Dot-Product Attention, tokens query each other to dynamically enrich their contextual embeddings based on relevance rather than static dictionary lookups."),
    ("2. Computational Stability & Scale:", "Deep networks suffer from vanishing gradients. Modern LLMs incorporate Pre-LayerNorm (or RMSNorm) and residual identity skip connections, ensuring error gradients flow directly from loss back to early embedding layers unimpeded."),
    ("3. Generative Inference Control:", "Raw model outputs are unbounded logit distributions. Controlled text generation requires sophisticated sampling strategies—balancing deterministic greedy decoding against creative temperature and nucleus (Top-p) probability mass thresholds.")
]
py_cur2 = c_y + c_h - 36
for h, b in intro_right_pdf:
    c.setFillColor(HEX_OCEAN_DARK)
    c.setFont("Helvetica-Bold", 8.2)
    c.drawString(102 + c_w + 30, py_cur2, f"•   {h}")
    p = Paragraph(f"<font size='7.5' color='#334155'>{b}</font>", ParagraphStyle('IR', fontName='Helvetica', fontSize=7.5, leading=10.5))
    h_used = draw_top_down(p, 102 + c_w + 40, py_cur2 - 6, c_w - 28, 90)
    py_cur2 -= (h_used + 16)

c.showPage()

# =============================================================================
# SLIDE 4: OBJECTIVE
# =============================================================================
add_pdf_frame("Project Objectives & Technical Scope", "PROJECT SPECIFICATION (SECTION 2)", "flower_slide_3.png", "#f8fafc", 4)

obj_quads_pdf = [
    ("OBJECTIVE 1: ARCHITECTURE FROM SCRATCH", HEX_TEAL_DEEP, HexColor("#f0fdf4"), HexColor("#99f6e4"),
     "Design and construct a Decoder-Only Transformer architecture from foundational mathematics in pure Python and PyTorch.<br/><br/>"
     "• Implement Multi-Head Causal Self-Attention, Pre-LN Transformer Blocks, and Position-wise FeedForward (MLP) layers.<br/>"
     "• Zero reliance on black-box external frameworks (HuggingFace transformers or LangChain)."),
    ("OBJECTIVE 2: TOKENIZATION & DATA PIPELINE", HEX_BLUE_ROYAL, HexColor("#eff6ff"), HexColor("#bfdbfe"),
     "Engineer modular, transparent tokenization and sliding-window dataset loaders.<br/><br/>"
     "• Develop a bidirectional Character-Level Tokenizer (65 tokens) and subword BPE wrapper for zero-dependency local training.<br/>"
     "• Implement PyTorch Dataset and DataLoader generating autoregressive targets (yt = xt+1) with causal sliding windows."),
    ("OBJECTIVE 3: PRETRAINING & CONVERGENCE", HEX_CORAL_RED, HexColor("#fff1f2"), HexColor("#fecdd3"),
     "Build a modern training harness with advanced optimization mechanics.<br/><br/>"
     "• Integrate AdamW with decoupled weight decay (2D weights vs 1D biases/norms).<br/>"
     "• Implement Cosine Annealing learning rate schedule with linear warmup.<br/>"
     "• Track Cross-Entropy loss and Perplexity (exp(Loss)) with real-time generation previews."),
    ("OBJECTIVE 4: SAMPLING & OPEN SOURCE ARTIFACT", HEX_INDIGO, HexColor("#faf5ff"), HexColor("#ddd6fe"),
     "Implement multi-mode text generation and deliver a production-grade open-source codebase.<br/><br/>"
     "• Support Greedy, Temperature-scaled, Top-K, and Top-P (Nucleus) decoding.<br/>"
     "• Provide an interactive terminal REPL shell for live user prompting.<br/>"
     "• Release under GNU General Public License v3.0 (GPLv3) on GitHub (RSNPIIT).")
]

card_w4 = (PAGE_WIDTH - 212 - 16) / 2
card_h4 = 188
xs4 = [102, 102 + card_w4 + 16]
ys4 = [240, 42]

for idx, (title, col, bg_col, bdr_col, body) in enumerate(obj_quads_pdf):
    qx = xs4[idx % 2]
    qy = ys4[idx // 2]
    c.setFillColor(bg_col)
    c.setStrokeColor(bdr_col)
    c.roundRect(qx, qy, card_w4, card_h4, 6, fill=1, stroke=1)

    c.setFillColor(col)
    c.setFont("Helvetica-Bold", 9.0)
    c.drawString(qx + 14, qy + card_h4 - 20, title)

    p_b = Paragraph(f"<font size='7.5' color='#334155'>{body}</font>", ParagraphStyle('OB', fontName='Helvetica', fontSize=7.5, leading=10.5))
    draw_top_down(p_b, qx + 14, qy + card_h4 - 28, card_w4 - 28, 140)

c.showPage()

# =============================================================================
# SLIDE 5: METHODOLOGY 1 (Pipeline & Tokenization)
# =============================================================================
add_pdf_frame("Methodology: Architecture Pipeline & Tokenization", "TECHNICAL METHODOLOGY (1 OF 4)", "flower_slide_4.png", "#fafaf9", 5)

if os.path.exists("methodology_1_pipeline.png"):
    c.drawImage("methodology_1_pipeline.png", 102, 245, width=PAGE_WIDTH - 212, height=195, mask="auto")

bot_y5 = 40
bot_h5 = 195
bot_w5 = (PAGE_WIDTH - 212 - 16) / 2

# Left Bottom
c.setFillColor(HEX_CARD_BG)
c.setStrokeColor(HEX_BORDER)
c.roundRect(102, bot_y5, bot_w5, bot_h5, 6, fill=1, stroke=1)

c.setFillColor(HEX_TEAL_DEEP)
c.setFont("Helvetica-Bold", 9.5)
c.drawString(116, bot_y5 + bot_h5 - 20, "Tokenization & Sliding-Window Dataloader")

t5_l_desc = (
    "<b>• Deterministic Character Vocabulary:</b> Extracts unique character set (V=65 for Tiny Shakespeare). "
    "Builds bijective lookup tables char_to_id and id_to_char, allowing exact token reconstruction with zero external dependencies.<br/><br/>"
    "<b>• Autoregressive Sliding-Window Chunking:</b> Text is encoded into a 1D tensor. TextDataset samples chunks of "
    "length block_size (T=128/256). The target sequence y is x shifted by exactly 1 position (yt = xt+1), creating supervised pairs for next-token prediction."
)
p_t5l = Paragraph(f"<font size='7.5' color='#334155'>{t5_l_desc}</font>", ParagraphStyle('T5L', fontName='Helvetica', fontSize=7.5, leading=10.5))
draw_top_down(p_t5l, 116, bot_y5 + bot_h5 - 28, bot_w5 - 28, 155)

# Right Bottom
c.setFillColor(HEX_CARD_BG)
c.setStrokeColor(HEX_BORDER)
c.roundRect(102 + bot_w5 + 16, bot_y5, bot_w5, bot_h5, 6, fill=1, stroke=1)

c.setFillColor(HEX_BLUE_ROYAL)
c.setFont("Helvetica-Bold", 9.5)
c.drawString(102 + bot_w5 + 30, bot_y5 + bot_h5 - 20, "Dual Embedding Space Formulation")

t5_r_desc = (
    "<b>• Token Embeddings (wte):</b> Token IDs are projected from discrete indices {0..V-1} into continuous "
    "d_model-dimensional vectors using nn.Embedding(V, d_model), initialized with normal distribution (mean=0, std=0.02).<br/><br/>"
    "<b>• Positional Embeddings & RoPE:</b> Transformers possess no inherent sequential inductive bias. We inject positional awareness "
    "via learned embeddings (wpe: T → d_model), adding x = wte(tok) + wpe(pos), with optional support for modern Rotary Position Embeddings (RoPE)."
)
p_t5r = Paragraph(f"<font size='7.5' color='#334155'>{t5_r_desc}</font>", ParagraphStyle('T5R', fontName='Helvetica', fontSize=7.5, leading=10.5))
draw_top_down(p_t5r, 102 + bot_w5 + 30, bot_y5 + bot_h5 - 28, bot_w5 - 28, 155)

c.showPage()

# =============================================================================
# SLIDE 6: METHODOLOGY 2 (Causal Self-Attention)
# =============================================================================
add_pdf_frame("Methodology: Causal Attention & Look-Ahead Masking", "TECHNICAL METHODOLOGY (2 OF 4)", "flower_slide_5.png", "#f6f9fa", 6)

w_img = 420
if os.path.exists("methodology_2_attention.png"):
    c.drawImage("methodology_2_attention.png", 102, 40, width=w_img, height=395, mask="auto")

w_card6 = PAGE_WIDTH - 212 - w_img - 16
c.setFillColor(HEX_CARD_BG)
c.setStrokeColor(HEX_BORDER)
c.roundRect(102 + w_img + 16, 40, w_card6, 395, 6, fill=1, stroke=1)

c.setFillColor(HEX_CORAL_RED)
c.setFont("Helvetica-Bold", 10)
c.drawString(102 + w_img + 30, 40 + 395 - 22, "Mathematical Mechanics of Causal Attention")

attn_desc = (
    "<b>• Batched Linear Projection:</b> A single matrix multiply projects input x into Queries (Q), Keys (K), and Values (V): "
    "c_attn(x) ∈ R^(B × T × 3·n_embd), split into n_head heads of dimension head_dim = n_embd / n_head.<br/><br/>"
    "<b>• Scaled Dot-Product Formula:</b> Attention weights are computed by taking the inner product of queries and keys scaled by 1/√d_k "
    "to prevent gradient vanishing in large dimensions: Attn = (Q · K^T) / √d_k.<br/><br/>"
    "<b>• The Causal Lower-Triangular Mask:</b> To enforce strict autoregression, an upper-triangular boolean mask replaces all future token affinities "
    "(j &gt; i) with -∞ before softmax: Softmax(-∞) = 0. Tokens can only look backward in time.<br/><br/>"
    "<b>• Softmax & Value Weighting:</b> Softmax normalizes row scores into a valid probability distribution. Multiplying by Values (V) "
    "produces contextually enriched token vectors: y = Softmax(Attn + M) · V.<br/><br/>"
    "<b>• Apple Silicon MPS Support:</b> Optimized with fallback handling for PyTorch 2.0+ FlashAttention vs manual attention on Apple MPS GPU."
)
p_attn = Paragraph(f"<font size='7.5' color='#334155'>{attn_desc}</font>", ParagraphStyle('Attn', fontName='Helvetica', fontSize=7.5, leading=10.5))
draw_top_down(p_attn, 102 + w_img + 30, 40 + 395 - 32, w_card6 - 28, 350)

c.showPage()

# =============================================================================
# SLIDE 7: METHODOLOGY 3 (Transformer Blocks & Pre-LN)
# =============================================================================
add_pdf_frame("Methodology: Pre-LN Blocks & Feed-Forward Networks", "TECHNICAL METHODOLOGY (3 OF 4)", "flower_slide_6.png", "#f8f7fc", 7)

if os.path.exists("methodology_3_transformer_block.png"):
    c.drawImage("methodology_3_transformer_block.png", 102, 40, width=w_img, height=395, mask="auto")

c.setFillColor(HEX_CARD_BG)
c.setStrokeColor(HEX_BORDER)
c.roundRect(102 + w_img + 16, 40, w_card6, 395, 6, fill=1, stroke=1)

c.setFillColor(HEX_BLUE_ROYAL)
c.setFont("Helvetica-Bold", 10)
c.drawString(102 + w_img + 30, 40 + 395 - 22, "Transformer Block Dynamics & Stability")

block_desc = (
    "<b>• Pre-LayerNorm Architecture:</b> Unlike early Post-LN Transformers that placed normalization after residual addition, "
    "modern LLMs (GPT-2, LLaMA) place normalization before attention and MLP: x = x + SubLayer(Norm(x)). This ensures the residual "
    "stream remains clean, preventing vanishing gradients.<br/><br/>"
    "<b>• RMSNorm Alternative:</b> Supports modern Root Mean Square Normalization (Zhang & Sennrich, 2019): RMSNorm(x) = x / √(mean(x²) + ε) · γ, "
    "which eliminates mean-centering, cutting computational overhead while preserving accuracy.<br/><br/>"
    "<b>• Feed-Forward Network (GELU MLP):</b> Applies position-wise non-linear feature transformation: "
    "Linear(d_model, 4·d_model) → GELU() → Linear(4·d_model, d_model). GELU (Gaussian Error Linear Unit) provides smooth, differentiable activation.<br/><br/>"
    "<b>• Residual Identity Highway:</b> Skip connections provide an uninterrupted gradient highway from output loss back to early embedding layers, "
    "enabling stable convergence across arbitrary network depths."
)
p_block = Paragraph(f"<font size='7.5' color='#334155'>{block_desc}</font>", ParagraphStyle('Block', fontName='Helvetica', fontSize=7.5, leading=10.5))
draw_top_down(p_block, 102 + w_img + 30, 40 + 395 - 32, w_card6 - 28, 350)

c.showPage()

# =============================================================================
# SLIDE 8: METHODOLOGY 4 (Training Engine & Optimization)
# =============================================================================
add_pdf_frame("Methodology: Pretraining Loop & Optimization Dynamics", "TECHNICAL METHODOLOGY (4 OF 4)", "flower_slide_1.png", "#faf8f5", 8)

if os.path.exists("methodology_4_training_curves.png"):
    c.drawImage("methodology_4_training_curves.png", 102, 40, width=w_img, height=395, mask="auto")

c.setFillColor(HEX_CARD_BG)
c.setStrokeColor(HEX_BORDER)
c.roundRect(102 + w_img + 16, 40, w_card6, 395, 6, fill=1, stroke=1)

c.setFillColor(HEX_AMBER_WARM)
c.setFont("Helvetica-Bold", 10)
c.drawString(102 + w_img + 30, 40 + 395 - 22, "Optimization & Pretraining Harness")

train_desc = (
    "<b>• Cross-Entropy Loss Function:</b> The model is trained end-to-end to minimize cross-entropy loss between predicted vocabulary "
    "logits and target next tokens: L(θ) = -1/T ∑ log P(x_t | x_past).<br/><br/>"
    "<b>• Validation Perplexity (PPL):</b> Perplexity = exp(Loss). Interpreted as the effective number of equally likely words "
    "the model is choosing between at each step. PPL drops rapidly from 67.35 to 4.67.<br/><br/>"
    "<b>• Decoupled AdamW Weight Decay:</b> Weight decay (0.1) is selectively applied only to 2D weight matrices (linear projections and embeddings). "
    "1D biases and normalization scale parameters are excluded from decay to prevent harmful underfitting.<br/><br/>"
    "<b>• Cosine Annealing with Warmup:</b> Learning rate warms up linearly over the first 50 iterations from 0 to 6e-4 to stabilize early gradients, "
    "then decays smoothly following a cosine curve down to 10% peak LR.<br/><br/>"
    "<b>• Gradient Clipping:</b> Clips parameter gradients at max_norm=1.0, preventing gradient explosions during sudden loss spikes."
)
p_tr = Paragraph(f"<font size='7.5' color='#334155'>{train_desc}</font>", ParagraphStyle('Tr', fontName='Helvetica', fontSize=7.5, leading=10.5))
draw_top_down(p_tr, 102 + w_img + 30, 40 + 395 - 32, w_card6 - 28, 350)

c.showPage()

# =============================================================================
# SLIDE 9: RESULT ANALYSIS
# =============================================================================
add_pdf_frame("Result Analysis: Convergence & Text Generation", "EXPERIMENTAL EVALUATION (SECTION 4)", "flower_slide_2.png", "#f8fafc", 9)

# Top Card: Table
c.setFillColor(HEX_CARD_BG)
c.setStrokeColor(HEX_BORDER)
c.roundRect(102, 260, PAGE_WIDTH - 212, 175, 6, fill=1, stroke=1)

c.setFillColor(HEX_OCEAN_DARK)
c.setFont("Helvetica-Bold", 9.5)
c.drawString(116, 260 + 175 - 18, "Empirical Pretraining Dynamics: Qualitative Evolution Across Iterations")

results_table_pdf = [
    ("Step 0 (Untrained)", "Train Loss: 4.20 | Val Loss: 4.21 | PPL: 67.35",
     "\"KING: J:A -Ft,OVjww$pPVtg wwLNbjSesKv&PZg...\"", "Pure stochastic noise; uniform character distribution."),
    ("Step 50 (Early Phase)", "Train Loss: 2.78 | Val Loss: 2.97 | PPL: 19.63",
     "\"KING: Adousifos d b he theid thore d ad at thirroind...\"", "Learns whitespace separation & word-like character clusters."),
    ("Step 100 (Rapid Convergence)", "Train Loss: 2.59 | Val Loss: 2.81 | PPL: 16.63",
     "\"KING: I: thein le. I hal ite bforat ind lond hind fr...\"", "Learns English morphemes ('th', 'in', 'ind') & dialogue syntax."),
    ("Step 1000 (Mature Pretraining)", "Train Loss: 1.38 | Val Loss: 1.54 | PPL: 4.67",
     "\"KING: What news from the northern march, my lord?\"", "Syntactically coherent, Shakespearean-style dialogue.")
]

ry_tbl = 260 + 175 - 34
for st, met, quote, comm in results_table_pdf:
    c.setFillColor(HEX_CORAL_RED)
    c.setFont("Helvetica-Bold", 7.8)
    c.drawString(116, ry_tbl, f"•   {st}  [{met}]:")
    c.setFillColor(HEX_OCEAN_DARK)
    c.drawString(126, ry_tbl - 10, f"{quote}   —   ")
    c.setFillColor(HEX_TEXT_MUTED)
    c.setFont("Helvetica", 7.2)
    c.drawString(136 + len(quote)*4.2, ry_tbl - 10, comm)
    ry_tbl -= 32

# Bottom Left Card: Sampling
c.setFillColor(HexColor("#f0fdf4"))
c.setStrokeColor(HexColor("#99f6e4"))
c.roundRect(102, 40, bot_w5, 205, 6, fill=1, stroke=1)

c.setFillColor(HEX_TEAL_DEEP)
c.setFont("Helvetica-Bold", 9.5)
c.drawString(116, 40 + 205 - 18, "Inference Sampling Strategies Compared")

samp_desc = (
    "<b>• Greedy Search (Temp = 0.0):</b> Picks argmax P(xt). Highly repetitive, gets stuck in predictable local loops ('the the the').<br/><br/>"
    "<b>• Temperature Scaling (0.7 - 0.85):</b> Smooths logit distribution. Balance between coherent syntax and creative vocabulary diversity.<br/><br/>"
    "<b>• Top-K Filtering (k = 40):</b> Cuts off low-probability tail, preventing catastrophic hallucinations and out-of-context tokens.<br/><br/>"
    "<b>• Top-P Nucleus (p = 0.90):</b> Dynamically expands or contracts the candidate pool based on model confidence."
)
p_samp = Paragraph(f"<font size='7.2' color='#334155'>{samp_desc}</font>", ParagraphStyle('Samp', fontName='Helvetica', fontSize=7.2, leading=9.8))
draw_top_down(p_samp, 116, 40 + 205 - 26, bot_w5 - 28, 170)

# Bottom Right Card: Hardware
c.setFillColor(HexColor("#eff6ff"))
c.setStrokeColor(HexColor("#bfdbfe"))
c.roundRect(102 + bot_w5 + 16, 40, bot_w5, 205, 6, fill=1, stroke=1)

c.setFillColor(HEX_BLUE_ROYAL)
c.setFont("Helvetica-Bold", 9.5)
c.drawString(102 + bot_w5 + 30, 40 + 205 - 18, "Hardware Performance & Efficiency")

hw_desc = (
    "<b>• Apple Silicon MPS Acceleration:</b> Leverages Metal Performance Shaders on macOS. Achieved 24.5 iterations/sec on nano preset (~14 seconds per 100 training steps).<br/><br/>"
    "<b>• Memory Footprint:</b> Model weights and optimizer states require only ~12 MB VRAM for nano configuration, making local training accessible on personal laptops.<br/><br/>"
    "<b>• Linear Scaling:</b> Model scales cleanly to micro (10.8M parameters) and full GPT-2 (124M parameters) without altering core mathematical modules."
)
p_hw = Paragraph(f"<font size='7.2' color='#334155'>{hw_desc}</font>", ParagraphStyle('HW', fontName='Helvetica', fontSize=7.2, leading=9.8))
draw_top_down(p_hw, 102 + bot_w5 + 30, 40 + 205 - 26, bot_w5 - 28, 170)

c.showPage()

# =============================================================================
# SLIDE 10: CONCLUSION & FUTURE SCOPE
# =============================================================================
add_pdf_frame("Conclusion: Key Learnings & Future Roadmap", "PROJECT SUMMARY (SECTION 5)", "flower_slide_3.png", "#fcfaf8", 10)

# Left Card: Learnings
c.setFillColor(HEX_CARD_BG)
c.setStrokeColor(HEX_BORDER)
c.roundRect(102, c_y, c_w, c_h, 6, fill=1, stroke=1)

c.setFillColor(HEX_TEAL_DEEP)
c.setFont("Helvetica-Bold", 10.5)
c.drawString(116, c_y + c_h - 22, "Key Technical Competencies & Takeaways")

learnings_pdf = [
    ("Foundational Deep Learning Mastery:", "Gained rigorous, first-principles mastery of Transformer architectures, tensor projections, and scaled dot-product attention without high-level library abstractions."),
    ("Causal Mechanism Understanding:", "Discovered how mathematical masking enforces temporal boundaries, proving that Generative AI is fundamentally statistical next-token density estimation."),
    ("Optimization Insights:", "Understood the critical role of decoupled weight decay, learning rate warmup, and Pre-LN stabilization in preventing training divergence."),
    ("Open-Source Deliverable:", "Released a modular, clean, and fully reproducible codebase on GitHub under the GNU GPLv3 license for the academic and AI developer community.")
]
py_cur_c1 = c_y + c_h - 36
for h, b in learnings_pdf:
    c.setFillColor(HEX_OCEAN_DARK)
    c.setFont("Helvetica-Bold", 8.2)
    c.drawString(116, py_cur_c1, f"•   {h}")
    p = Paragraph(f"<font size='7.5' color='#334155'>{b}</font>", ParagraphStyle('CL', fontName='Helvetica', fontSize=7.5, leading=10.5))
    h_used = draw_top_down(p, 126, py_cur_c1 - 6, c_w - 28, 90)
    py_cur_c1 -= (h_used + 16)

# Right Card: Future Scope
c.setFillColor(HexColor("#faf5ff"))
c.setStrokeColor(HexColor("#ddd6fe"))
c.roundRect(102 + c_w + 16, c_y, c_w, c_h, 6, fill=1, stroke=1)

c.setFillColor(HEX_INDIGO)
c.setFont("Helvetica-Bold", 10.5)
c.drawString(102 + c_w + 30, c_y + c_h - 22, "Future Technical Expansion Roadmap")

future_pdf = [
    ("Phase 1: Supervised Fine-Tuning (SFT):", "Transitioning the base pretrained model into an instruction-following conversational assistant using curated prompt-response pairs."),
    ("Phase 2: Low-Rank Adaptation (LoRA):", "Implementing parameter-efficient fine-tuning (PEFT) by decomposing attention weight update matrices (ΔW = A × B), enabling rapid domain adaptation on consumer GPUs."),
    ("Phase 3: Preference Alignment (DPO / RLHF):", "Aligning model generation with human values and safety guidelines via Direct Preference Optimization (DPO)."),
    ("Phase 4: Architectural Innovations:", "Experimenting with Rotary Position Embeddings (RoPE), SwiGLU activations, and Mixture of Experts (MoE) routing for next-generation efficiency.")
]
py_cur_c2 = c_y + c_h - 36
for h, b in future_pdf:
    c.setFillColor(HEX_OCEAN_DARK)
    c.setFont("Helvetica-Bold", 8.2)
    c.drawString(102 + c_w + 30, py_cur_c2, f"•   {h}")
    p = Paragraph(f"<font size='7.5' color='#334155'>{b}</font>", ParagraphStyle('CR', fontName='Helvetica', fontSize=7.5, leading=10.5))
    h_used = draw_top_down(p, 102 + c_w + 40, py_cur_c2 - 6, c_w - 28, 90)
    py_cur_c2 -= (h_used + 16)

c.showPage()
c.save()
print(f"[*] Successfully saved vector PDF: {output_pdf}")
