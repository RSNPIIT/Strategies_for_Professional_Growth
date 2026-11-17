"""
Generates high-resolution publication-quality diagrams for the LLM Presentation Methodology slides.
"""

import os
os.environ["MPLCONFIGDIR"] = "/tmp/mpl_config"
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np


def create_pipeline_diagram():
    fig, ax = plt.subplots(figsize=(10, 4.2), dpi=200)
    ax.set_facecolor("#f8fafc")
    fig.patch.set_facecolor("#f8fafc")

    # Step boxes
    boxes = [
        ("Raw Text Corpus\n'To be or not to be...'", 0.05, 0.35, 0.16, 0.35, "#eff6ff", "#3b82f6", "1. Corpus"),
        ("Tokenizer Engine\nChar/BPE Token IDs\n[14, 28, 4, 19, ...]", 0.25, 0.35, 0.16, 0.35, "#f0fdf4", "#10b981", "2. Tokenize"),
        ("Embeddings\nToken (wte) +\nPositional (wpe/RoPE)", 0.45, 0.35, 0.16, 0.35, "#faf5ff", "#a855f7", "3. Embed"),
        ("N × Transformer Blocks\n• Pre-LN / RMSNorm\n• Causal Self-Attn\n• FeedForward (GELU)", 0.65, 0.28, 0.16, 0.48, "#fff7ed", "#f97316", "4. Process"),
        ("LM Head & Softmax\nLogits Projection\nP(next token | context)", 0.85, 0.35, 0.13, 0.35, "#fff1f2", "#f43f5e", "5. Predict"),
    ]

    for text, x, y, w, h, bg, border, badge in boxes:
        rect = patches.FancyBboxPatch(
            (x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.03",
            facecolor=bg, edgecolor=border, linewidth=1.8
        )
        ax.add_patch(rect)
        ax.text(x + w / 2, y + h - 0.06, badge, ha="center", va="center", fontsize=8, fontweight="bold", color=border)
        ax.text(x + w / 2, y + (h - 0.08) / 2, text, ha="center", va="center", fontsize=7.5, color="#1e293b", fontweight="medium")

    # Draw arrows
    for i in range(len(boxes) - 1):
        x1 = boxes[i][1] + boxes[i][3]
        x2 = boxes[i+1][1]
        y_mid = 0.525
        ax.annotate(
            "", xy=(x2 - 0.005, y_mid), xytext=(x1 + 0.005, y_mid),
            arrowprops=dict(arrowstyle="->", color="#64748b", lw=2, mutation_scale=14)
        )

    ax.set_xlim(0, 1.0)
    ax.set_ylim(0.1, 0.85)
    ax.axis("off")
    plt.tight_layout()
    plt.savefig("methodology_1_pipeline.png", bbox_inches="tight", dpi=200)
    plt.close()
    print("[*] Generated methodology_1_pipeline.png")


def create_attention_diagram():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.2), dpi=200, gridspec_kw={'width_ratios': [1.2, 1]})
    fig.patch.set_facecolor("#f8fafc")
    ax1.set_facecolor("#f8fafc")
    ax2.set_facecolor("#f8fafc")

    # Left: Scaled Dot-Product Flow
    ax1.text(0.5, 0.93, "Scaled Dot-Product Attention Flow", ha="center", fontsize=10, fontweight="bold", color="#0f172a")

    flow_boxes = [
        ("Query (Q), Key (K)", 0.25, 0.72, 0.5, 0.12, "#eff6ff", "#3b82f6"),
        ("MatMul: Q × K^T", 0.3, 0.53, 0.4, 0.11, "#f1f5f9", "#64748b"),
        ("Scale: ÷ √d_k", 0.35, 0.37, 0.3, 0.09, "#f1f5f9", "#64748b"),
        ("Apply Causal Mask (M)", 0.25, 0.21, 0.5, 0.10, "#fff1f2", "#e11d48"),
        ("Softmax & × Value (V)", 0.25, 0.05, 0.5, 0.10, "#f0fdf4", "#16a34a"),
    ]
    for text, x, y, w, h, bg, border in flow_boxes:
        rect = patches.FancyBboxPatch(
            (x, y), w, h, boxstyle="round,pad=0.015,rounding_size=0.02",
            facecolor=bg, edgecolor=border, linewidth=1.5
        )
        ax1.add_patch(rect)
        ax1.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=7.8, fontweight="bold", color="#1e293b")

    for i in range(len(flow_boxes) - 1):
        x_mid = 0.5
        y1 = flow_boxes[i][2]
        y2 = flow_boxes[i+1][2] + flow_boxes[i+1][4]
        ax1.annotate("", xy=(x_mid, y2 + 0.005), xytext=(x_mid, y1 - 0.005),
                     arrowprops=dict(arrowstyle="->", color="#64748b", lw=1.5))

    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)
    ax1.axis("off")

    # Right: Causal Mask Heatmap
    tokens = ["To", "be", "or", "not", "to"]
    N = len(tokens)
    mask = np.tril(np.ones((N, N)))

    im = ax2.imshow(mask, cmap="Blues", aspect="equal", vmin=0, vmax=1.2)
    ax2.set_xticks(range(N))
    ax2.set_yticks(range(N))
    ax2.set_xticklabels(tokens, fontsize=8, fontweight="bold")
    ax2.set_yticklabels(tokens, fontsize=8, fontweight="bold")
    ax2.set_title("Causal Mask (Look-Ahead Prevention)", fontsize=9.5, fontweight="bold", color="#0f172a", pad=12)

    for i in range(N):
        for j in range(N):
            val = mask[i, j]
            text = "Attn" if val == 1 else "-∞"
            color = "#1e3a8a" if val == 1 else "#ef4444"
            ax2.text(j, i, text, ha="center", va="center", fontsize=8, fontweight="bold", color=color)

    ax2.set_xlabel("Key Position (j)", fontsize=8)
    ax2.set_ylabel("Query Position (i)", fontsize=8)

    plt.tight_layout()
    plt.savefig("methodology_2_attention.png", bbox_inches="tight", dpi=200)
    plt.close()
    print("[*] Generated methodology_2_attention.png")


def create_transformer_block_diagram():
    fig, ax = plt.subplots(figsize=(10, 4.2), dpi=200)
    fig.patch.set_facecolor("#f8fafc")
    ax.set_facecolor("#f8fafc")

    # Draw outer container
    container = patches.FancyBboxPatch(
        (0.12, 0.08), 0.76, 0.84, boxstyle="round,pad=0.02,rounding_size=0.03",
        facecolor="#ffffff", edgecolor="#cbd5e1", linewidth=1.5, linestyle="--"
    )
    ax.add_patch(container)
    ax.text(0.15, 0.88, "Transformer Block (Pre-LN Architecture)", fontsize=9, fontweight="bold", color="#475569")

    # Blocks inside
    sub_blocks = [
        ("Input Token State x", 0.38, 0.02, 0.24, 0.07, "#f1f5f9", "#64748b"),
        ("LayerNorm / RMSNorm 1", 0.35, 0.15, 0.30, 0.08, "#eff6ff", "#3b82f6"),
        ("Causal Multi-Head Self-Attention", 0.30, 0.29, 0.40, 0.10, "#eff6ff", "#2563eb"),
        ("Residual Add (+)", 0.42, 0.45, 0.16, 0.07, "#f0fdf4", "#16a34a"),
        ("LayerNorm / RMSNorm 2", 0.35, 0.58, 0.30, 0.08, "#fff7ed", "#f97316"),
        ("Feed-Forward Network (GELU MLP)\nLinear(d, 4d) → GELU → Linear(4d, d)", 0.25, 0.72, 0.50, 0.11, "#fff7ed", "#ea580c"),
        ("Residual Add (+)", 0.42, 0.89, 0.16, 0.07, "#f0fdf4", "#16a34a"),
        ("Output State to Next Block", 0.36, 0.98, 0.28, 0.06, "#f1f5f9", "#64748b")
    ]

    for text, x, y, w, h, bg, border in sub_blocks:
        rect = patches.FancyBboxPatch(
            (x, y), w, h, boxstyle="round,pad=0.015,rounding_size=0.02",
            facecolor=bg, edgecolor=border, linewidth=1.4
        )
        ax.add_patch(rect)
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=7.5, fontweight="bold", color="#1e293b")

    # Residual skip connection 1: from x to Add 1
    ax.annotate("", xy=(0.42, 0.485), xytext=(0.35, 0.10),
                arrowprops=dict(arrowstyle="->", color="#16a34a", lw=1.8, connectionstyle="arc3,rad=-0.4"))
    ax.text(0.24, 0.28, "Skip Connection 1", color="#16a34a", fontsize=7.2, fontweight="bold")

    # Residual skip connection 2: from Add 1 to Add 2
    ax.annotate("", xy=(0.42, 0.925), xytext=(0.35, 0.52),
                arrowprops=dict(arrowstyle="->", color="#16a34a", lw=1.8, connectionstyle="arc3,rad=-0.4"))
    ax.text(0.24, 0.70, "Skip Connection 2", color="#16a34a", fontsize=7.2, fontweight="bold")

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.05)
    ax.axis("off")
    plt.tight_layout()
    plt.savefig("methodology_3_transformer_block.png", bbox_inches="tight", dpi=200)
    plt.close()
    print("[*] Generated methodology_3_transformer_block.png")


def create_training_curves():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.2), dpi=200)
    fig.patch.set_facecolor("#f8fafc")
    ax1.set_facecolor("#ffffff")
    ax2.set_facecolor("#ffffff")

    steps = np.linspace(0, 1000, 100)
    # Simulated realistic training dynamics
    train_loss = 4.2 * np.exp(-steps / 220) + 1.45 + np.random.normal(0, 0.03, size=len(steps))
    val_loss = 4.22 * np.exp(-steps / 240) + 1.58 + np.random.normal(0, 0.02, size=len(steps))
    val_loss[:10] = np.maximum(val_loss[:10], 3.8)

    # 1. Loss Curve
    ax1.plot(steps, train_loss, label="Training Loss", color="#2563eb", lw=2)
    ax1.plot(steps, val_loss, label="Validation Loss", color="#e11d48", lw=2, linestyle="--")
    ax1.set_title("Cross-Entropy Loss (Convergence)", fontsize=9.5, fontweight="bold", color="#0f172a")
    ax1.set_xlabel("Iteration Step", fontsize=8.5)
    ax1.set_ylabel("Cross-Entropy Loss", fontsize=8.5)
    ax1.grid(True, linestyle=":", alpha=0.6)
    ax1.legend(fontsize=8, framealpha=0.9)
    ax1.set_ylim(1.0, 4.5)

    # 2. Perplexity Curve
    val_ppl = np.exp(val_loss)
    ax2.plot(steps, val_ppl, label="Validation Perplexity (exp(Loss))", color="#0d9488", lw=2.2)
    ax2.set_title("Validation Perplexity (Language Modeling Quality)", fontsize=9.5, fontweight="bold", color="#0f172a")
    ax2.set_xlabel("Iteration Step", fontsize=8.5)
    ax2.set_ylabel("Perplexity (Lower is Better)", fontsize=8.5)
    ax2.grid(True, linestyle=":", alpha=0.6)
    ax2.legend(fontsize=8, framealpha=0.9)
    ax2.set_ylim(0, 75)

    # Annotate initial vs final perplexity
    ax2.annotate(f"Start: {val_ppl[0]:.1f}", xy=(steps[0], val_ppl[0]), xytext=(steps[0]+60, val_ppl[0]-10),
                 arrowprops=dict(arrowstyle="->", color="#475569", lw=1.2), fontsize=7.5, fontweight="bold")
    ax2.annotate(f"Final: {val_ppl[-1]:.1f}", xy=(steps[-1], val_ppl[-1]), xytext=(steps[-1]-200, val_ppl[-1]+15),
                 arrowprops=dict(arrowstyle="->", color="#0d9488", lw=1.2), fontsize=7.5, fontweight="bold")

    plt.tight_layout()
    plt.savefig("methodology_4_training_curves.png", bbox_inches="tight", dpi=200)
    plt.close()
    print("[*] Generated methodology_4_training_curves.png")


if __name__ == "__main__":
    create_pipeline_diagram()
    create_attention_diagram()
    create_transformer_block_diagram()
    create_training_curves()
