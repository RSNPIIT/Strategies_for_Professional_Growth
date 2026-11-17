import os
import numpy as np
from scipy import ndimage
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

from PIL import Image, ImageDraw, ImageFont

from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph

def disable_spellcheck(run):
    rPr = run._r.get_or_add_rPr()
    rPr.set('noProof', '1')

def prepare_watermarks():
    # 1. Color Eagle Emblem (Page 5) - delicate low opacity (alpha max 20, ~7.8%)
    color_src = "/Users/ramrupsatpati/.gemini/antigravity/brain/58faa843-d2fc-401a-a000-1fd5f6e320d5/.user_uploaded/media_1793104183578_846a112f.png"
    if os.path.exists(color_src):
        im_src = Image.open(color_src).convert("RGBA")
        arr = np.array(im_src)
        h, w, _ = arr.shape
        cy, cx = h / 2.0, w / 2.0
        r = min(h, w) / 2.0 - 4
        y_grid, x_grid = np.ogrid[:h, :w]
        dist_from_center = np.sqrt((x_grid - cx)**2 + (y_grid - cy)**2)
        circle_mask = dist_from_center <= r
        alpha = np.zeros((h, w), dtype=np.uint8)
        is_non_white = (arr[:,:,0] < 240) | (arr[:,:,1] < 240) | (arr[:,:,2] < 240)
        mask = circle_mask & is_non_white
        alpha[mask] = 20
        edge_mask = (dist_from_center <= r) & (dist_from_center > r - 4) & is_non_white
        alpha[edge_mask] = (20 * (r - dist_from_center[edge_mask]) / 4.0).astype(np.uint8)
        arr[:,:,3] = alpha
        Image.fromarray(arr).save("eagle_watermark.png")

    # 2. Black Eagle Emblem (Page 7 / Last Slide) - delicate low opacity (alpha max 22, ~8.6%)
    black_src = "/Users/ramrupsatpati/.gemini/antigravity/brain/58faa843-d2fc-401a-a000-1fd5f6e320d5/.user_uploaded/media_1793105942752_56996bde.png"
    if os.path.exists(black_src):
        im_b = Image.open(black_src).convert("RGBA")
        arr_b = np.array(im_b)
        hb, wb, _ = arr_b.shape
        # Clean bottom-left search icon and outer border artifacts
        arr_b[450:, :150, :3] = 255
        arr_b[:3, :, :3] = 255
        arr_b[:, :3, :3] = 255
        arr_b[:, -3:, :3] = 255
        grey = arr_b[:,:,:3].mean(axis=2)
        alpha_b = np.zeros((hb, wb), dtype=np.uint8)
        dark_mask = grey < 200
        alpha_val = np.clip((200.0 - grey) / 200.0 * 22.0, 0, 22).astype(np.uint8)
        alpha_b[dark_mask] = alpha_val[dark_mask]
        out_b = np.zeros((hb, wb, 4), dtype=np.uint8)
        out_b[:,:,0] = 30
        out_b[:,:,1] = 41
        out_b[:,:,2] = 59  # Slate dark #1e293b
        out_b[:,:,3] = alpha_b
        Image.fromarray(out_b).save("black_eagle_watermark.png")

    # 3. Horse Emblem (Page 6 / Second Last Slide) - delicate low opacity (alpha max 20, ~7.8%)
    horse_src = "/Users/ramrupsatpati/.gemini/antigravity/brain/58faa843-d2fc-401a-a000-1fd5f6e320d5/.user_uploaded/media_1793108595388_1c89e7ff.png"
    if os.path.exists(horse_src):
        im_h = Image.open(horse_src).convert("RGB")
        arr_h = np.array(im_h)
        hh, wh, _ = arr_h.shape
        # Clean bottom-left search icon & outer border
        arr_h[620:, :110] = [240, 240, 240]
        arr_h[:3, :] = [240, 240, 240]
        arr_h[-3:, :] = [240, 240, 240]
        arr_h[:, :3] = [240, 240, 240]
        arr_h[:, -3:] = [240, 240, 240]
        rh, gh, bh = arr_h[:,:,0].astype(float), arr_h[:,:,1].astype(float), arr_h[:,:,2].astype(float)
        max_ch = np.maximum(np.maximum(rh, gh), bh)
        min_ch = np.minimum(np.minimum(rh, gh), bh)
        chroma_h = max_ch - min_ch
        is_checker = (max_ch > 200) & (chroma_h < 18)
        border_seed = np.zeros((hh, wh), dtype=bool)
        border_seed[0, :] = True
        border_seed[-1, :] = True
        border_seed[:, 0] = True
        border_seed[:, -1] = True
        bg_mask = ndimage.binary_propagation(border_seed, mask=is_checker)
        fg_mask = ~bg_mask
        fg_mask_clean = ndimage.binary_opening(fg_mask, structure=np.ones((2,2)))
        alpha_h = (fg_mask_clean * 20.0).astype(np.uint8)
        out_h = np.zeros((hh, wh, 4), dtype=np.uint8)
        out_h[:,:,:3] = arr_h
        out_h[:,:,3] = alpha_h
        Image.fromarray(out_h).save("horse_watermark.png")

    # 4. Wolf Watermark (Page 3 / Slide 2) - howling wolf and full moon (~7.8% opacity)
    wolf_src = "/Users/ramrupsatpati/.gemini/antigravity/brain/58faa843-d2fc-401a-a000-1fd5f6e320d5/.user_uploaded/media_1793110372651_5483dff6.png"
    if os.path.exists(wolf_src):
        im_w = Image.open(wolf_src).convert("RGB")
        arr_w = np.array(im_w)
        hw, ww, _ = arr_w.shape
        feather = 35
        y_ramp_w = np.ones(hw, dtype=float)
        y_ramp_w[:feather] = np.linspace(0, 1, feather)
        y_ramp_w[-feather:] = np.linspace(1, 0, feather)
        x_ramp_w = np.ones(ww, dtype=float)
        x_ramp_w[:feather] = np.linspace(0, 1, feather)
        x_ramp_w[-feather:] = np.linspace(1, 0, feather)
        edge_mask_w = np.outer(y_ramp_w, x_ramp_w)
        alpha_w = (edge_mask_w * 20.0).astype(np.uint8)
        out_w = np.zeros((hw, ww, 4), dtype=np.uint8)
        out_w[:,:,:3] = arr_w
        out_w[:,:,3] = alpha_w
        Image.fromarray(out_w).save("wolf_watermark.png")

    # 5. Chess Watermark (Page 4 / Slide 3) - chess pieces across strategy board (~7.0% opacity)
    chess_src = "/Users/ramrupsatpati/.gemini/antigravity/brain/58faa843-d2fc-401a-a000-1fd5f6e320d5/.user_uploaded/media_1793110287850_1170f8f8.png"
    if os.path.exists(chess_src):
        im_c = Image.open(chess_src).convert("RGB")
        arr_c = np.array(im_c)
        hc, wc, _ = arr_c.shape
        feather = 35
        y_ramp_c = np.ones(hc, dtype=float)
        y_ramp_c[:feather] = np.linspace(0, 1, feather)
        y_ramp_c[-feather:] = np.linspace(1, 0, feather)
        x_ramp_c = np.ones(wc, dtype=float)
        x_ramp_c[:feather] = np.linspace(0, 1, feather)
        x_ramp_c[-feather:] = np.linspace(1, 0, feather)
        edge_mask_c = np.outer(y_ramp_c, x_ramp_c)
        alpha_c = (edge_mask_c * 18.0).astype(np.uint8)
        out_c = np.zeros((hc, wc, 4), dtype=np.uint8)
        out_c[:,:,:3] = arr_c
        out_c[:,:,3] = alpha_c
        Image.fromarray(out_c).save("chess_watermark.png")

    # 6. Page Flip Corner (All Slides) - vibrant blue corner curl
    flip_src = "/Users/ramrupsatpati/.gemini/antigravity/brain/58faa843-d2fc-401a-a000-1fd5f6e320d5/.user_uploaded/media_1793111304157_3dbb70f1.png"
    if os.path.exists(flip_src):
        im_fl = Image.open(flip_src).convert("RGB")
        arr_fl = np.array(im_fl)
        # Paper corner is at x=285, y=292
        # Curl bounds: y from 57 to 292, x from 135 to 285
        crop_fl = arr_fl[57:293, 135:286]
        cfh, cfw, _ = crop_fl.shape
        diff_fl = np.abs(crop_fl.astype(float) - 245.0).max(axis=2)
        is_curl_fl = diff_fl > 4.0
        is_curl_fl = ndimage.binary_fill_holes(is_curl_fl)
        dist_in_fl = ndimage.distance_transform_edt(is_curl_fl)
        dist_out_fl = ndimage.distance_transform_edt(~is_curl_fl)
        alpha_fl = np.zeros((cfh, cfw), dtype=np.uint8)
        alpha_fl[is_curl_fl] = 255
        border_in = (dist_in_fl > 0) & (dist_in_fl < 1.5)
        alpha_fl[border_in] = np.clip(dist_in_fl[border_in] / 1.5 * 255, 100, 255).astype(np.uint8)
        border_out = (dist_out_fl > 0) & (dist_out_fl < 1.0) & (diff_fl > 1.5)
        alpha_fl[border_out] = np.clip((1.0 - dist_out_fl[border_out]) * 100, 0, 100).astype(np.uint8)
        out_fl = np.zeros((cfh, cfw, 4), dtype=np.uint8)
        out_fl[:,:,:3] = crop_fl
        out_fl[:,:,3] = alpha_fl
        Image.fromarray(out_fl).save("page_flip_corner.png")

# =============================================================================
# COLOR PALETTE (VIBRANT CORAL & OCEANIC ARCHITECTURE)
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

# Slide-specific background shades (PPTX)
C_BG_S0 = RGBColor(252, 253, 255)  # Cover: Pure Crisp Pearl
C_BG_S1 = RGBColor(248, 250, 252)  # Slide 1: Cool Slate Pearl
C_BG_S2 = RGBColor(250, 248, 245)  # Slide 2: Warm Sand / Ivory Mist
C_BG_S3 = RGBColor(248, 250, 252)  # Slide 3: Crisp Slate Mist
C_BG_S4 = RGBColor(250, 250, 249)  # Slide 4: Warm Stone
C_BG_S5 = RGBColor(246, 249, 250)  # Slide 5: Cool Mist Ocean
C_BG_S6 = RGBColor(248, 247, 252)  # Slide 6: Subtle Lavender Mist

# ReportLab Hex Colors
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
HEX_PILL_BG    = HexColor("#f1f5f9")     # Slate 100

# Slide-specific background shades (ReportLab)
HEX_BG_S0 = HexColor("#fcfdff")
HEX_BG_S1 = HexColor("#f8fafc")
HEX_BG_S2 = HexColor("#faf8f5")
HEX_BG_S3 = HexColor("#f8fafc")
HEX_BG_S4 = HexColor("#fafaf9")
HEX_BG_S5 = HexColor("#f6f9fa")
HEX_BG_S6 = HexColor("#f8f7fc")

# Themed Card Backgrounds & Borders
HEX_CARD_RISK    = HexColor("#fff7ed")   # Soft Warm Peach
HEX_BORDER_RISK  = HexColor("#fed7aa")
HEX_CARD_QA      = HexColor("#f0fdf4")   # Soft Cool Mint
HEX_BORDER_QA    = HexColor("#bbf7d0")

HEX_CARD_PROB    = HexColor("#fff1f2")   # Soft Rose Blush
HEX_BORDER_PROB  = HexColor("#fecdd3")
HEX_CARD_P1      = HexColor("#f0fdf4")   # Mint (Systems Thinking)
HEX_BORDER_P1    = HexColor("#a7f3d0")
HEX_CARD_P2      = HexColor("#eff6ff")   # Azure (Engineering Sense)
HEX_BORDER_P2    = HexColor("#bfdbfe")
HEX_CARD_P3      = HexColor("#fff7ed")   # Peach (Human Balancing Loops)
HEX_BORDER_P3    = HexColor("#ffedd5")

HEX_CARD_CLD     = HexColor("#f8fafc")   # Slate (CLD Architecture)
HEX_BORDER_CLD   = HexColor("#cbd5e1")
HEX_CARD_RES     = HexColor("#fffdf5")   # Warm Ivory (Literature)
HEX_BORDER_RES   = HexColor("#fef08a")

HEX_CARD_PROF    = HexColor("#f0fdfa")   # Teal Tint (Cohort & Strategy)
HEX_BORDER_PROF  = HexColor("#99f6e4")
HEX_CARD_Q       = HexColor("#faf5ff")   # Lavender Tint (Interview Protocol)
HEX_BORDER_Q     = HexColor("#e9d5ff")

# =============================================================================
# GANTT & PIE CHART GENERATOR (PIL, OCT 10 - NOV 30)
# =============================================================================
def build_gantt_chart():
    w, h = 1800, 480
    img = Image.new('RGBA', (w, h), (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    C_DARK = (15, 23, 42, 255)
    C_MUTED = (100, 116, 139, 255)
    C_BORDER_LINE = (203, 213, 225, 255)

    C_P1 = (16, 185, 129, 255)   # Phase 1: Emerald Green (Completed)
    C_P2 = (244, 63, 94, 255)    # Phase 2: Coral Rose (Current GP1)
    C_P3 = (13, 148, 136, 255)   # Phase 3: Deep Teal (Interviews)
    C_P4 = (2, 132, 199, 255)    # Phase 4: Sky Blue (Thematic Analysis)
    C_P5 = (234, 88, 12, 255)    # Phase 5: Amber Orange (GP2 Report Due Nov 14)
    C_P6 = (124, 58, 237, 255)   # Phase 6: Violet Indigo (GP2 Live Presentation Nov 30)

    try:
        font_bold = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 18)
        font_bar = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 13)
        font_small = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 12)
        font_header = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 13)
        font_pie_title = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 16)
        font_legend = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 12)
    except:
        font_bold = font_bar = font_small = font_header = font_pie_title = font_legend = ImageFont.load_default()

    # LEFT SIDE: EXECUTION GANTT (x = 0 to 1240)
    grid_left = 360
    grid_right = 1190
    total_days = 52 # Oct 10 to Nov 30

    def day_to_x(month, day):
        d_offset = (day - 10) if month == 10 else (21 + day)
        return grid_left + int(d_offset * (grid_right - grid_left) / total_days)

    key_dates = [
        (10, 10, 'Oct 10'), (10, 18, 'Oct 18'), (10, 24, 'Oct 24'),
        (10, 31, 'Oct 31'), (11, 7, 'Nov 07'), (11, 14, 'Nov 14'),
        (11, 21, 'Nov 21'), (11, 30, 'Nov 30')
    ]

    for m, d, label in key_dates:
        x = day_to_x(m, d)
        is_d1 = (m == 10 and d == 24)
        is_d2 = (m == 11 and d == 14)
        is_d3 = (m == 11 and d == 30)

        if is_d1:
            line_col = (244, 63, 94, 220)
            line_w = 2
        elif is_d2:
            line_col = (234, 88, 12, 240)
            line_w = 2
        elif is_d3:
            line_col = (124, 58, 237, 240)
            line_w = 2
        else:
            line_col = (226, 232, 240, 255)
            line_w = 1

        draw.line([(x, 48), (x, h - 18)], fill=line_col, width=line_w)
        draw.text((x - 18, 26), label, fill=C_DARK if (is_d1 or is_d2 or is_d3) else C_MUTED, font=font_small)

    # Milestones
    x_d1 = day_to_x(10, 24)
    draw.text((x_d1 - 55, 8), 'GP1 Cutoff (Oct 24)', fill=C_P2, font=font_header)

    x_d2 = day_to_x(11, 14)
    draw.text((x_d2 - 65, 8), 'GP2 Report (Nov 14)', fill=C_P5, font=font_header)

    x_d3 = day_to_x(11, 30)
    draw.text((x_d3 - 95, 8), 'Presentation (Nov 30)', fill=C_P6, font=font_header)

    tasks = [
        ('Phase 1: Inception & Contract', 10, 10, 10, 18, C_P1, 'Del 1.a-1.c'),
        ('Phase 2: GP1 Pitch Deck', 10, 19, 10, 24, C_P2, 'GP1 Deck'),
        ('Phase 3: Field Interviews (N=5)', 10, 25, 11, 4, C_P3, '5 Interviews (30-45m)'),
        ('Phase 4: Thematic Analysis', 11, 5, 11, 9, C_P4, 'Synthesis & CLD'),
        ('Phase 5: GP2 Project Report', 11, 10, 11, 14, C_P5, 'Del 1.c Upload'),
        ('Phase 6: Live Presentation Prep', 11, 15, 11, 30, C_P6, 'Del 2 Defense (Nov 30)')
    ]

    bar_y_start = 54
    bar_height = 34
    bar_spacing = 68

    for idx, (t_name, sm, sd, em, ed, bar_col, st_lbl) in enumerate(tasks):
        y = bar_y_start + idx * bar_spacing
        draw.text((20, y + 8), t_name, fill=C_DARK, font=font_bold)

        bx1 = day_to_x(sm, sd)
        bx2 = day_to_x(em, ed) + 6
        draw.rounded_rectangle([(bx1, y), (bx2, y + bar_height)], radius=5, fill=bar_col)

        bbox = font_bar.getbbox(st_lbl)
        tw = bbox[2] - bbox[0]
        bar_w = bx2 - bx1
        if tw <= bar_w - 10:
            tx = bx1 + (bar_w - tw) // 2
            draw.text((tx, y + 8), st_lbl, fill=(255, 255, 255, 255), font=font_bar)
        else:
            draw.text((bx2 + 6, y + 8), st_lbl, fill=bar_col, font=font_bar)

    # VERTICAL SEPARATOR (x = 1240)
    draw.line([(1240, 20), (1240, h - 20)], fill=(226, 232, 240, 255), width=2)

    # RIGHT SIDE: EFFORT DISTRIBUTION DONUT CHART
    p_title = 'Phase Workload & Effort'
    bbox_t = font_pie_title.getbbox(p_title)
    tw_t = bbox_t[2] - bbox_t[0]
    draw.text((1240 + (560 - tw_t) // 2, 14), p_title, fill=C_DARK, font=font_pie_title)

    slices = [
        ('P1: Inception', 15, C_P1),
        ('P2: GP1 Deck', 12, C_P2),
        ('P3: Interviews (N=5)', 25, C_P3),
        ('P4: Synthesis & CLD', 12, C_P4),
        ('P5: GP2 Report', 12, C_P5),
        ('P6: Live Defense', 24, C_P6)
    ]

    cx, cy = 1520, 160
    r_out = 92
    r_in = 54

    scale = 4
    large_size = (r_out * 2 * scale + 40, r_out * 2 * scale + 40)
    pie_img = Image.new('RGBA', large_size, (0, 0, 0, 0))
    pie_draw = ImageDraw.Draw(pie_img)
    pcx, pcy = large_size[0] // 2, large_size[1] // 2

    start_angle = -90
    for name, pct, col in slices:
        angle_extent = pct * 3.6
        pie_draw.pieslice(
            [(pcx - r_out * scale, pcy - r_out * scale), (pcx + r_out * scale, pcy + r_out * scale)],
            start=start_angle, end=start_angle + angle_extent, fill=col
        )
        start_angle += angle_extent

    pie_draw.ellipse(
        [(pcx - r_in * scale, pcy - r_in * scale), (pcx + r_in * scale, pcy + r_in * scale)],
        fill=(255, 255, 255, 255)
    )

    pie_thumb = pie_img.resize((r_out * 2 + 10, r_out * 2 + 10), Image.Resampling.LANCZOS)
    img.paste(pie_thumb, (cx - r_out - 5, cy - r_out - 5), mask=pie_thumb)

    draw.text((cx - 26, cy - 14), 'TOTAL', fill=C_MUTED, font=font_small)
    draw.text((cx - 32, cy + 2), '52 Days', fill=C_DARK, font=font_bold)

    leg_y = 278
    for i, (name, pct, col) in enumerate(slices):
        col_idx = i % 2
        row_idx = i // 2
        lx = 1275 + col_idx * 265
        ly = leg_y + row_idx * 34

        draw.rounded_rectangle([(lx, ly + 2), (lx + 14, ly + 16)], radius=3, fill=col)
        draw.text((lx + 22, ly), f'{pct}%  {name}', fill=C_DARK, font=font_legend)

    draw.rounded_rectangle([(0, 0), (w - 1, h - 1)], radius=10, outline=C_BORDER_LINE, width=2)
    img.save('gantt_chart.png')
    print('Generated gantt_chart.png (Oct 10 - Nov 30 with Donut Chart)')


def ensure_flower_assets():
    req_flowers = [f"flower_slide_{i}.png" for i in range(7)] + ["flower_cover_bottom.png"]
    if all(os.path.exists(f) for f in req_flowers):
        return
    flower_src = None
    for cand in [
        "flower_sheet.png",
        "/Users/ramrupsatpati/.gemini/antigravity/brain/58faa843-d2fc-401a-a000-1fd5f6e320d5/.user_uploaded/media_1793113982089_225376e9.png"
    ]:
        if os.path.exists(cand):
            flower_src = cand
            break
    if not flower_src:
        return

    import numpy as np
    import scipy.ndimage as ndi
    from collections import deque
    img = Image.open(flower_src).convert("RGB")
    arr = np.array(img)[0:838, 6:478]
    H, W, _ = arr.shape
    bg_ref = np.array([229, 229, 229], dtype=float)
    diff = np.sqrt(np.sum((arr.astype(float) - bg_ref)**2, axis=2))
    is_bg = diff < 16
    visited = np.zeros((H, W), dtype=bool)
    queue = deque()
    for r in range(H):
        if is_bg[r, 0]: queue.append((r, 0)); visited[r, 0] = True
        if is_bg[r, W-1]: queue.append((r, W-1)); visited[r, W-1] = True
    for c in range(W):
        if is_bg[0, c] and not visited[0, c]: queue.append((0, c)); visited[0, c] = True
        if is_bg[H-1, c] and not visited[H-1, c]: queue.append((H-1, c)); visited[H-1, c] = True
    while queue:
        r, c = queue.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < H and 0 <= nc < W:
                if not visited[nr, nc] and is_bg[nr, nc]:
                    visited[nr, nc] = True
                    queue.append((nr, nc))
    fg_mask = ~visited
    dist = ndi.distance_transform_edt(fg_mask)
    alpha_full = np.clip((dist - 0.7) / 1.3, 0.0, 1.0) * 255.0

    row_splits = [0, 165, 325, 485, 650, 838]
    col_splits = [0, 155, 315, 472]
    selection = {
        "flower_slide_0.png": (0, 0),
        "flower_cover_bottom.png": (1, 1),
        "flower_slide_1.png": (0, 2),
        "flower_slide_2.png": (1, 2),
        "flower_slide_3.png": (3, 2),
        "flower_slide_4.png": (2, 2),
        "flower_slide_5.png": (2, 1),
        "flower_slide_6.png": (4, 2),
    }
    for out_name, (ri, ci) in selection.items():
        r_start, r_end = row_splits[ri], row_splits[ri+1]
        c_start, c_end = col_splits[ci], col_splits[ci+1]
        cell_fg = fg_mask[r_start:r_end, c_start:c_end]
        ys, xs = np.where(cell_fg)
        ymin, ymax = ys.min(), ys.max() + 1
        xmin, xmax = xs.min(), xs.max() + 1
        y0 = max(0, r_start + ymin - 2)
        y1 = min(H, r_start + ymax + 2)
        x0 = max(0, c_start + xmin - 2)
        x1 = min(W, c_start + xmax + 2)
        crop_rgb = arr[y0:y1, x0:x1].copy()
        crop_alpha = alpha_full[y0:y1, x0:x1].astype(np.uint8)
        rgba = np.dstack([crop_rgb, crop_alpha])
        labeled, num_features = ndi.label(rgba[:, :, 3] > 0)
        if num_features > 1:
            sizes = [np.sum(labeled == i) for i in range(1, num_features + 1)]
            main_label = np.argmax(sizes) + 1
            rgba[labeled != main_label, 3] = 0
            ys_c, xs_c = np.where(rgba[:, :, 3] > 0)
            rgba = rgba[ys_c.min():ys_c.max()+1, xs_c.min():xs_c.max()+1]
        Image.fromarray(rgba, "RGBA").save(out_name)
    print("Extracted individual slide flower decorations.")


# =============================================================================
# 1. PPTX BUILDER (Team_114_SPG_GP1_Sep_2026.pptx)
# =============================================================================
def build_pptx():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    def add_coral_frame(slide, title_text, category_text="BSGN3001: STRATEGIES FOR PROFESSIONAL GROWTH", coral_corner="flower_slide_1.png", bg_color=C_BG_S1):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = bg_color
        bg.line.fill.background()

        if os.path.exists(coral_corner):
            slide.shapes.add_picture(coral_corner, Inches(0.25), Inches(0.22), Inches(1.05), Inches(1.05))

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

        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.45), Inches(1.18), Inches(10.2), Inches(0.035))
        line.fill.solid()
        line.fill.fore_color.rgb = C_CORAL_RED
        line.line.fill.background()

        if os.path.exists("iitm_logo_clean.png"):
            slide.shapes.add_picture("iitm_logo_clean.png", Inches(11.85), Inches(0.22), Inches(1.25), Inches(1.25))

        f_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.45), Inches(7.05), Inches(9.8), Inches(0.015))
        f_line.fill.solid()
        f_line.fill.fore_color.rgb = C_BORDER
        f_line.line.fill.background()

        fb = slide.shapes.add_textbox(Inches(1.45), Inches(7.08), Inches(9.8), Inches(0.3))
        pf = fb.text_frame.paragraphs[0]
        rf = pf.add_run()
        rf.text = "Team 114: Iterate  •  Beyond Quick Fixes: Exploring Tech Debt & Developer Fatigue  •  GP1 Deliverable 2"
        rf.font.size = Pt(8.5)
        rf.font.color.rgb = C_TEXT_MUTED
        disable_spellcheck(rf)

    def add_slide_decorations(slide, slide_idx):
        tree_path = f"tree_slide_{slide_idx}.png"
        if os.path.exists(tree_path):
            slide.shapes.add_picture(tree_path, Inches(11.85), Inches(5.15), Inches(1.05), Inches(1.45))
        if os.path.exists("page_flip_corner.png"):
            slide.shapes.add_picture("page_flip_corner.png", Inches(12.56), Inches(6.30), Inches(0.77), Inches(1.20))

    # --- SLIDE 0: COVER SLIDE ---
    s0 = prs.slides.add_slide(blank_layout)
    bg0 = s0.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg0.fill.solid()
    bg0.fill.fore_color.rgb = C_BG_S0
    bg0.line.fill.background()

    if os.path.exists("iitm_logo_clean.png"):
        s0.shapes.add_picture("iitm_logo_clean.png", Inches(11.5), Inches(0.4), Inches(1.45), Inches(1.45))
    if os.path.exists("flower_slide_0.png"):
        s0.shapes.add_picture("flower_slide_0.png", Inches(0.4), Inches(0.4), Inches(1.15), Inches(1.15))
    if os.path.exists("flower_cover_bottom.png"):
        s0.shapes.add_picture("flower_cover_bottom.png", Inches(0.4), Inches(5.6), Inches(1.15), Inches(1.15))

    card0 = s0.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.6), Inches(0.65), Inches(10.1), Inches(6.2))
    card0.fill.solid()
    card0.fill.fore_color.rgb = C_CARD_BG
    card0.line.color.rgb = C_BORDER
    card0.line.width = Pt(1.2)

    if os.path.exists("cover_watermark.png"):
        s0.shapes.add_picture("cover_watermark.png", Inches(1.65), Inches(0.7), Inches(10.0), Inches(6.1))

    tb0 = s0.shapes.add_textbox(Inches(1.6), Inches(0.65), Inches(10.1), Inches(6.2))
    tf0 = tb0.text_frame
    tf0.word_wrap = True
    tf0.margin_left = tf0.margin_right = Inches(0.4)
    tf0.margin_top = Inches(0.35)

    p0 = tf0.paragraphs[0]
    r = p0.add_run()
    r.text = "IIT MADRAS BS DEGREE PROGRAMME\n"
    r.font.bold = True
    r.font.size = Pt(11)
    r.font.color.rgb = C_CORAL_RED
    disable_spellcheck(r)

    r_sub = p0.add_run()
    r_sub.text = "BSGN3001: STRATEGIES FOR PROFESSIONAL GROWTH  •  GROUP PROJECT 1 (GP1)\n\n"
    r_sub.font.bold = True
    r_sub.font.size = Pt(9.5)
    r_sub.font.color.rgb = C_TEXT_MUTED
    disable_spellcheck(r_sub)

    r_title = p0.add_run()
    r_title.text = "Beyond Quick Fixes: Exploring Technical Debt & Developer Fatigue\nThrough Systems Thinking\n\n"
    r_title.font.bold = True
    r_title.font.size = Pt(21)
    r_title.font.color.rgb = C_OCEAN_DARK
    disable_spellcheck(r_title)

    r_theme = p0.add_run()
    r_theme.text = "Linking Systems Thinking (Week 10) and Engineering Sense (Week 11)\n\n"
    r_theme.font.italic = True
    r_theme.font.size = Pt(11.5)
    r_theme.font.color.rgb = C_TEAL_DEEP
    disable_spellcheck(r_theme)

    p_badge = tf0.add_paragraph()
    r_badge = p_badge.add_run()
    r_badge.text = "TEAM 114: ITERATE  |  PITCH DECK DELIVERABLE 2 (OCTOBER 2026)\n"
    r_badge.font.bold = True
    r_badge.font.size = Pt(11)
    r_badge.font.color.rgb = C_CORAL_RED
    disable_spellcheck(r_badge)
    p_badge.space_after = Pt(6)

    roster = [
        ("Samyabrata Roy", "22F2001443", "Team Lead", "22F2001443@ds.study.iitm.ac.in"),
        ("Abir Saha", "23F3001436", "Project Manager", "23F3001436@ds.study.iitm.ac.in"),
        ("Rishabh Barthwal", "23F2004112", "Research Lead", "23F2004112@ds.study.iitm.ac.in"),
        ("Piyush Tilokchandani", "21F1006739", "Slides / Design Lead", "21F1006739@ds.study.iitm.ac.in"),
        ("Ramrup Satpati", "24F3004027", "Editor / Creative & Presentation Lead", "24F3004027@ds.study.iitm.ac.in")
    ]
    for name, roll, role, email in roster:
        p_m = tf0.add_paragraph()
        r_dot = p_m.add_run()
        r_dot.text = "•   "
        r_dot.font.bold = True
        r_dot.font.color.rgb = C_CORAL_RED

        r_m = p_m.add_run()
        r_m.text = f"{name:24} "
        r_m.font.bold = True
        r_m.font.size = Pt(11)
        r_m.font.color.rgb = C_OCEAN_DARK
        disable_spellcheck(r_m)

        r_det = p_m.add_run()
        r_det.text = f"({roll}  |  {email})           "
        r_det.font.size = Pt(9.5)
        r_det.font.color.rgb = C_TEXT_MUTED
        disable_spellcheck(r_det)

        r_r = p_m.add_run()
        r_r.text = f"—   {role}"
        r_r.font.bold = True
        r_r.font.size = Pt(10)
        r_r.font.color.rgb = C_CORAL_RED
        disable_spellcheck(r_r)
        p_m.space_after = Pt(2)

    p_f = tf0.add_paragraph()
    p_f.space_before = Pt(6)
    rf = p_f.add_run()
    rf.text = "Deliverable Overview & Alignment: "
    rf.font.bold = True
    rf.font.size = Pt(8.5)
    rf.font.color.rgb = C_OCEAN_DARK

    rf_desc = p_f.add_run()
    rf_desc.text = "This 6-slide pitch deck details Team Iterate's Project Management Plan, Team Profile, Conceptual Causal Loop Diagram (CLD), secondary resource identification, and qualitative discussion protocol for GP1 Deliverable 2 submission.\n"
    rf_desc.font.size = Pt(8.0)
    rf_desc.font.color.rgb = C_TEXT_MAIN

    r_op_h = p_f.add_run()
    r_op_h.text = "Note on Operational Roles: "
    r_op_h.font.bold = True
    r_op_h.font.size = Pt(8.2)
    r_op_h.font.color.rgb = C_CORAL_RED
    disable_spellcheck(r_op_h)

    r_op_b = p_f.add_run()
    r_op_b.text = "Defined roles serve as primary administrative touchpoints for accountability and submission requirements. In practice, responsibilities remain fluid; all members actively cross-collaborate across research, interview execution, and development, ensuring ultimate ownership of the work belongs to the whole team."
    r_op_b.font.size = Pt(7.8)
    r_op_b.font.color.rgb = C_TEXT_MUTED
    disable_spellcheck(r_op_b)

    add_slide_decorations(s0, 0)

    # --- SLIDE 1: TEAM PROFILE ---
    s1 = prs.slides.add_slide(blank_layout)
    add_coral_frame(s1, "Team Profile: Complementary Capabilities & Governance", "TEAM PROFILE (1 SLIDE)", "flower_slide_1.png", bg_color=C_BG_S1)

    card_y = Inches(1.35)
    card_w = Inches(1.95)
    card_h = Inches(4.55)
    start_x = Inches(1.45)
    spacing = Inches(2.1)

    members_data = [
        ("Samyabrata Roy", "22F2001443", "Team Lead",
         "BS Data Science · MSc Stats (CU) · Assoc. SWE",
         "Core Coordination",
         "Oversees holistic delivery, academic milestone compliance, and portal submissions.",
         "Strategic Planning, Milestone Integrity", "portrait_samyabrata.png", C_OCEAN_DARK),
        ("Abir Saha", "23F3001436", "Project Manager",
         "BS Data Science · Full-Stack & Process Eng",
         "Sprint Governance",
         "Maintains project timeline, task tracking, meeting cadences, and blocker resolution.",
         "Process Architecture, Sprint Schedules", "portrait_abir.png", C_CORAL_RED),
        ("Rishabh Barthwal", "23F2004112", "Research Lead",
         "BS Data Science · Applied AI & Systems Researcher",
         "Theory & Synthesis",
         "Heads theoretical modeling around Peter Senge archetypes and interview protocol.",
         "ENTJ-A, Analytical Inquiry, Literature", "portrait_rishabh.png", C_TEAL_DEEP),
        ("Piyush Tilokchandani", "21F1006739", "Design Lead",
         "BS Data Science\nSoftware Dev at Piramal Finance",
         "Visual Architecture",
         "Curates deck visual aesthetics, data diagrams, typography, and presentation layout.",
         "Information Architecture, Visual Systems", "portrait_piyush.png", C_INDIGO),
        ("Ramrup Satpati", "24F3004027", "Creative & Pres. Lead",
         "BS Data Science · Deep Learning & Applied AI Eng",
         "Narrative & Synthesis",
         "Directs content synthesis, editorial rigor, human-loop integration, and final deck delivery.",
         "ENFJ-A, Qualitative Synthesis, AI Systems", "portrait_ramrup.png", C_CORAL_RED)
    ]

    for idx, (m_name, m_roll, m_role, m_bg, m_focus, m_desc, m_traits, m_portrait, m_color) in enumerate(members_data):
        cx = start_x + idx * spacing
        mc = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, card_y, card_w, card_h)
        mc.fill.solid()
        mc.fill.fore_color.rgb = C_CARD_BG
        mc.line.color.rgb = RGBColor(148, 163, 184) # Crisp Slate 400
        mc.line.width = Pt(1.75)

        # Top Accent Header Bar
        bar = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, card_y, card_w, Inches(0.08))
        bar.fill.solid()
        bar.fill.fore_color.rgb = m_color
        bar.line.fill.background()

        # Portrait at top (1.5 in x 1.68 in)
        if os.path.exists(m_portrait):
            s1.shapes.add_picture(m_portrait, cx + Inches(0.225), card_y + Inches(0.12), Inches(1.5), Inches(1.68))

        tf_m = mc.text_frame
        tf_m.word_wrap = True
        tf_m.margin_left = tf_m.margin_right = Inches(0.06)
        tf_m.margin_top = Inches(1.84)

        p_name = tf_m.paragraphs[0]
        r_n = p_name.add_run()
        r_n.text = m_name
        r_n.font.bold = True
        r_n.font.size = Pt(10.0)
        r_n.font.color.rgb = C_OCEAN_DARK
        disable_spellcheck(r_n)
        p_name.alignment = PP_ALIGN.CENTER

        p_role = tf_m.add_paragraph()
        r_r = p_role.add_run()
        r_r.text = m_role
        r_r.font.bold = True
        r_r.font.size = Pt(8.8)
        r_r.font.color.rgb = m_color
        disable_spellcheck(r_r)
        p_role.alignment = PP_ALIGN.CENTER

        p_roll = tf_m.add_paragraph()
        r_ro = p_roll.add_run()
        r_ro.text = f"({m_roll})"
        r_ro.font.size = Pt(7.5)
        r_ro.font.color.rgb = C_TEXT_MUTED
        disable_spellcheck(r_ro)
        p_roll.alignment = PP_ALIGN.CENTER

        # Education & Background Line
        p_bg_p = tf_m.add_paragraph()
        r_bg = p_bg_p.add_run()
        r_bg.text = m_bg
        r_bg.font.bold = True
        r_bg.font.size = Pt(7.0)
        r_bg.font.color.rgb = C_TEAL_DEEP
        disable_spellcheck(r_bg)
        p_bg_p.alignment = PP_ALIGN.CENTER
        p_bg_p.space_after = Pt(2)

        # Scope Tag Pill
        p_pill = tf_m.add_paragraph()
        r_pl = p_pill.add_run()
        r_pl.text = f"Scope: {m_focus}"
        r_pl.font.bold = True
        r_pl.font.size = Pt(7.2)
        r_pl.font.color.rgb = C_OCEAN_DARK
        disable_spellcheck(r_pl)
        p_pill.alignment = PP_ALIGN.CENTER
        p_pill.space_after = Pt(2)

        p_desc = tf_m.add_paragraph()
        r_d = p_desc.add_run()
        r_d.text = m_desc
        r_d.font.size = Pt(7.0)
        r_d.font.color.rgb = C_TEXT_MAIN
        disable_spellcheck(r_d)
        p_desc.alignment = PP_ALIGN.CENTER
        p_desc.space_after = Pt(4)

        p_tr = tf_m.add_paragraph()
        r_tr = p_tr.add_run()
        r_tr.text = f"Traits: {m_traits}"
        r_tr.font.italic = True
        r_tr.font.size = Pt(6.8)
        r_tr.font.color.rgb = C_TEXT_MUTED
        disable_spellcheck(r_tr)
        p_tr.alignment = PP_ALIGN.CENTER

    # BOTTOM CONTAINERS: Left Diversity Card + Right SWOT 4-Box Matrix
    div_box = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.45), Inches(6.00), Inches(3.40), Inches(0.98))
    div_box.fill.solid()
    div_box.fill.fore_color.rgb = RGBColor(239, 246, 255) # Ice Blue tint
    div_box.line.color.rgb = RGBColor(191, 219, 254)
    div_box.line.width = Pt(1.0)

    tf_d = div_box.text_frame
    tf_d.word_wrap = True
    tf_d.margin_left = tf_d.margin_right = Inches(0.14)
    tf_d.margin_top = Inches(0.08)

    pd1 = tf_d.paragraphs[0]
    rd1 = pd1.add_run()
    rd1.text = "Team Diversity & Operating Cadence:\n"
    rd1.font.bold = True
    rd1.font.size = Pt(8.8)
    rd1.font.color.rgb = C_OCEAN_DARK
    disable_spellcheck(rd1)

    pd2 = tf_d.add_paragraph()
    rd2 = pd2.add_run()
    rd2.text = "• 5 BS Data Science (IITM) · FinTech SWE, MSc Stats & AI\n"
    rd2.font.bold = True
    rd2.font.size = Pt(7.5)
    rd2.font.color.rgb = C_CORAL_RED
    disable_spellcheck(rd2)

    rd3 = pd2.add_run()
    rd3.text = "• Cohort: 2021–2024 batches · 2 Working Pros · Ages 21–26 · Multi-City (BLR, CCU, DEL)"
    rd3.font.size = Pt(7.0)
    rd3.font.color.rgb = C_TEXT_MAIN
    disable_spellcheck(rd3)

    # Right Container: 4-Box SWOT Matrix
    swot_outer = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.95), Inches(6.00), Inches(6.85), Inches(0.98))
    swot_outer.fill.solid()
    swot_outer.fill.fore_color.rgb = RGBColor(255, 255, 255)
    swot_outer.line.color.rgb = RGBColor(203, 213, 225)
    swot_outer.line.width = Pt(1.0)

    swot_quads = [
        ("STRENGTHS (S)", C_TEAL_DEEP, RGBColor(240, 253, 244),
         "5 of 5 in BS Data Science; cross-industry blend of FinTech SWE, MSc Stats & AI."),
        ("WEAKNESSES (W)", C_AMBER_WARM, RGBColor(255, 247, 237),
         "Balancing full-time software jobs, term courses, and asynchronous time zones."),
        ("OPPORTUNITIES (O)", C_BLUE_ROYAL, RGBColor(239, 246, 255),
         "Direct Tier-1 tech & R&D network access (IDEAS-TIH, Deloitte, Deel, Siemens)."),
        ("THREATS (T)", C_CORAL_RED, RGBColor(255, 241, 242),
         "Interviewee cancellations, corporate release crunches, and academic exam conflicts.")
    ]

    for q_idx, (q_title, q_col, q_bg, q_desc) in enumerate(swot_quads):
        qx = Inches(5.02) + q_idx * Inches(1.68)
        q_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, qx, Inches(6.06), Inches(1.62), Inches(0.86))
        q_card.fill.solid()
        q_card.fill.fore_color.rgb = q_bg
        q_card.line.color.rgb = RGBColor(226, 232, 240)
        q_card.line.width = Pt(0.75)

        tf_q = q_card.text_frame
        tf_q.word_wrap = True
        tf_q.margin_left = tf_q.margin_right = Inches(0.06)
        tf_q.margin_top = Inches(0.05)

        pq = tf_q.paragraphs[0]
        rq_t = pq.add_run()
        rq_t.text = q_title + "\n"
        rq_t.font.bold = True
        rq_t.font.size = Pt(7.2)
        rq_t.font.color.rgb = q_col
        disable_spellcheck(rq_t)

        rq_d = pq.add_run()
        rq_d.text = q_desc
        rq_d.font.size = Pt(6.3)
        rq_d.font.color.rgb = C_TEXT_MAIN
        disable_spellcheck(rq_d)

    add_slide_decorations(s1, 1)

    # --- SLIDE 2: PROJECT MANAGEMENT PLAN (Slide 1 of PMP) ---
    s2 = prs.slides.add_slide(blank_layout)
    add_coral_frame(s2, "Project Management Plan: Execution Gantt & WBS Matrix", "PROJECT MANAGEMENT PLAN (SLIDE 1 OF 2)", "flower_slide_2.png", bg_color=C_BG_S2)

    # Project Goal Banner at top
    goal_box = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.45), Inches(1.24), Inches(10.35), Inches(0.34))
    goal_box.fill.solid()
    goal_box.fill.fore_color.rgb = RGBColor(255, 241, 242) # Rose Blush Tint
    goal_box.line.color.rgb = RGBColor(254, 205, 211)
    goal_box.line.width = Pt(1.0)
    tf_gb = goal_box.text_frame
    tf_gb.word_wrap = True
    tf_gb.margin_left = tf_gb.margin_right = Inches(0.18)
    tf_gb.margin_top = Inches(0.04)
    pg = tf_gb.paragraphs[0]
    rg_icon = pg.add_run()
    rg_icon.text = "🎯 Project Goal: "
    rg_icon.font.bold = True
    rg_icon.font.size = Pt(9.0)
    rg_icon.font.color.rgb = C_CORAL_RED
    disable_spellcheck(rg_icon)
    rg_txt = pg.add_run()
    rg_txt.text = "Use 5 engineers' real stories to show how quick fixes create tech debt and tire developers, and find what breaks the cycle."
    rg_txt.font.bold = True
    rg_txt.font.size = Pt(9.0)
    rg_txt.font.color.rgb = C_OCEAN_DARK
    disable_spellcheck(rg_txt)

    if os.path.exists("gantt_chart.png"):
        s2.shapes.add_picture("gantt_chart.png", Inches(1.45), Inches(1.64), Inches(10.35), Inches(2.40))

    wbs_box = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.45), Inches(4.12), Inches(10.35), Inches(2.80))
    wbs_box.fill.solid()
    wbs_box.fill.fore_color.rgb = RGBColor(255, 253, 247) # Warm Creme Tint
    wbs_box.line.color.rgb = C_BORDER
    wbs_box.line.width = Pt(1.0)

    # Watermark layer on top of card fills, behind text
    if os.path.exists("wolf_watermark.png"):
        s2.shapes.add_picture("wolf_watermark.png", Inches(4.82), Inches(4.20), Inches(3.6), Inches(2.65))

    tb_wbs = s2.shapes.add_textbox(Inches(1.45), Inches(4.12), Inches(10.35), Inches(2.80))
    tf_wbs = tb_wbs.text_frame
    tf_wbs.word_wrap = True
    tf_wbs.margin_left = tf_wbs.margin_right = Inches(0.22)
    tf_wbs.margin_top = Inches(0.08)

    p = tf_wbs.paragraphs[0]
    r = p.add_run()
    r.text = "Work Breakdown Structure (WBS) & Deliverable Ownership Matrix"
    r.font.bold = True
    r.font.size = Pt(10.5)
    r.font.color.rgb = C_OCEAN_DARK
    disable_spellcheck(r)
    p.space_after = Pt(2)

    wbs_items = [
        ("WBS 1.0: Literature & Archetype Modeling", "Rishabh Barthwal (Lead), Ramrup Satpati",
         "Curate Peter Senge (1990) archetypes, Waters Center habits, and DORA research.", C_TEAL_DEEP),
        ("WBS 2.0: Interviewee Sourcing & Scheduling", "All 5 Members (1 candidate each), Abir Saha (PM)",
         "Identify 5 practitioners across SaaS, FinTech, and cloud platforms; schedule calls.", C_BLUE_ROYAL),
        ("WBS 3.0: Interview Execution & Transcription", "All 5 Members (Equal Ownership)",
         "Conduct 30–45 min semi-structured interviews; record video, both cameras on, after written consent by email; generate verbatim transcripts.", C_TEAL_DEEP),
        ("WBS 4.0: Cross-Case Thematic Analysis", "Ramrup Satpati (Lead), Rishabh Barthwal",
         "Synthesize recurring themes across transcripts; validate reinforcing debt loops and human balancing loops.", C_BLUE_ROYAL),
        ("WBS 5.0: GP2 Team Project Report [Deliverable 1.c]", "Samyabrata Roy (Lead), All Members",
         "Each member: 5–10 min video clip + 1-page interim report (14 Nov); consolidate team project report under 'Deliverable 1.C.' within portal.", C_AMBER_WARM),
        ("WBS 6.0: GP2 Live Presentation & Deck [Deliverable 2]", "Piyush Tilokchandani (Design), Ramrup Satpati (Lead)",
         "Design slide deck, conduct mock defense sessions, and deliver live team presentation by November 30.", C_INDIGO)
    ]
    for w_t, w_o, w_d, w_col in wbs_items:
        pw = tf_wbs.add_paragraph()
        rw1 = pw.add_run()
        rw1.text = f"•  {w_t} "
        rw1.font.bold = True
        rw1.font.size = Pt(7.8)
        rw1.font.color.rgb = C_OCEAN_DARK
        disable_spellcheck(rw1)

        rw2 = pw.add_run()
        rw2.text = f"[{w_o}]: "
        rw2.font.bold = True
        rw2.font.size = Pt(7.6)
        rw2.font.color.rgb = w_col
        disable_spellcheck(rw2)

        rw3 = pw.add_run()
        rw3.text = w_d
        rw3.font.size = Pt(7.3)
        rw3.font.color.rgb = C_TEXT_MAIN
        disable_spellcheck(rw3)
        pw.space_after = Pt(2)

    add_slide_decorations(s2, 2)

    # --- SLIDE 3: RISK & QUALITY CONTROLS (Slide 2 of PMP) ---
    s3 = prs.slides.add_slide(blank_layout)
    add_coral_frame(s3, "Project Management Plan: Risk Management & Quality Controls", "PROJECT MANAGEMENT PLAN (SLIDE 2 OF 2)", "flower_slide_3.png", bg_color=C_BG_S3)

    # Left Card: Proactive Risk Matrix
    risk_box = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.45), Inches(1.35), Inches(5.1), Inches(5.55))
    risk_box.fill.solid()
    risk_box.fill.fore_color.rgb = RGBColor(255, 247, 237) # Warm Peach Tint
    risk_box.line.color.rgb = RGBColor(254, 215, 170)
    risk_box.line.width = Pt(1.0)

    # Right Side: Visual Quality Assurance & Milestone Progress Dashboard
    if os.path.exists("governance_dashboard.png"):
        s3.shapes.add_picture("governance_dashboard.png", Inches(6.7), Inches(1.35), Inches(5.1), Inches(5.55))

    # Watermark layer on top of card fills, behind text
    if os.path.exists("chess_watermark.png"):
        s3.shapes.add_picture("chess_watermark.png", Inches(1.87), Inches(2.42), Inches(9.5), Inches(3.5))

    tb_rk = s3.shapes.add_textbox(Inches(1.45), Inches(1.35), Inches(5.1), Inches(5.55))
    tf_rk = tb_rk.text_frame
    tf_rk.word_wrap = True
    tf_rk.margin_left = tf_rk.margin_right = Inches(0.22)
    tf_rk.margin_top = Inches(0.14)

    p = tf_rk.paragraphs[0]
    r = p.add_run()
    r.text = "Proactive Risk Matrix & Mitigation"
    r.font.bold = True
    r.font.size = Pt(11.5)
    r.font.color.rgb = C_AMBER_WARM
    disable_spellcheck(r)
    p.space_after = Pt(6)

    risks = [
        ("Risk 1: Interviewee Scheduling Delays", "Severity: High | Likelihood: Medium",
         "Mitigation: Each member secures 1 primary candidate and 1 fallback professional by Oct 28. If primary cancels, switch to the backup interviewee, keep the email proof (as live video is mandatory)."),
        ("Risk 2: Interview Data Fragmentation", "Severity: Medium | Likelihood: Medium",
         "Mitigation: Standardized 5-question interview guide and shared Notion transcript template ensure uniform qualitative analysis across all 5 interviews."),
        ("Risk 3: Theoretical Scope Creep", "Severity: Medium | Likelihood: Low",
         "Mitigation: Strictly anchor research to the single core feedback cycle ('Quick Fixes -> Technical Debt -> Developer Fatigue') rather than broader software engineering topics."),
        ("Risk 4: Deadline Crunch & Academic Clashes", "Severity: High | Likelihood: Low",
         "Mitigation: Strict internal deadline buffer: GP2 drafts finalized by Nov 12, giving a 48-hour buffer before the official November 14 portal deadline.")
    ]
    for r_t, r_m, r_d in risks:
        pr = tf_rk.add_paragraph()
        rr1 = pr.add_run()
        rr1.text = f"{r_t}\n"
        rr1.font.bold = True
        rr1.font.size = Pt(8.2)
        rr1.font.color.rgb = C_OCEAN_DARK
        disable_spellcheck(rr1)
        rr2 = pr.add_run()
        rr2.text = f"{r_m}\n"
        rr2.font.bold = True
        rr2.font.size = Pt(7.2)
        rr2.font.color.rgb = C_TEAL_DEEP
        disable_spellcheck(rr2)
        rr3 = pr.add_run()
        rr3.text = r_d
        rr3.font.size = Pt(7.5)
        rr3.font.color.rgb = C_TEXT_MAIN
        disable_spellcheck(rr3)
        pr.space_after = Pt(5)

    add_slide_decorations(s3, 3)

    # --- SLIDE 4: TOPIC SELECTION & FOUNDATIONS (Slide 1 of Topic) ---
    s4 = prs.slides.add_slide(blank_layout)
    add_coral_frame(s4, "Topic Selection: Core Problem & Theoretical Foundations", "TOPIC SELECTION & RESOURCES (SLIDE 1 OF 2)", "flower_slide_4.png", bg_color=C_BG_S4)

    prob_box = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.45), Inches(1.35), Inches(10.35), Inches(1.8))
    prob_box.fill.solid()
    prob_box.fill.fore_color.rgb = RGBColor(255, 241, 242) # Rose Blush Tint
    prob_box.line.color.rgb = RGBColor(254, 205, 211)
    prob_box.line.width = Pt(1.0)

    tp_w = Inches(3.32)
    tp_h = Inches(3.65)
    tp_y = Inches(3.25)

    pillars = [
        ("SPG Week 10: Systems Thinking", C_TEAL_DEEP, RGBColor(240, 253, 244), RGBColor(167, 243, 208),
         "• Feedback Loops: Analyzing how reinforcing loops (R) accelerate technical debt, while balancing loops (B) stabilize delivery.\n"
         "• Waters Center Habits: 'Observes how elements change over time', 'Considers short-term, long-term and unintended consequences of actions', and 'Considers how mental models affect reality.'\n"
         "• Peter Senge (1990) Archetypes:\n"
         "  - 'Fixes that Fail': Quick patches create delayed blowbacks.\n"
         "  - 'Shifting the Burden': Symptomatic solutions erode long-term architectural capacity."),
        ("SPG Week 11: Engineering Sense", C_BLUE_ROYAL, RGBColor(239, 246, 255), RGBColor(191, 219, 254),
         "• Pragmatic Trade-off Analysis: Balancing immediate business delivery against long-term architectural maintainability.\n"
         "• Empirical Root-Cause Diagnosis: Distinguishing superficial software bugs from foundational design deficiencies.\n"
         "• High-Leverage Debt Remediation: Knowing when to refactor vs. when to build new features within real-world time and budget constraints."),
        ("Human Balancing Loops (Core Skills 2030)", C_CORAL_RED, RGBColor(255, 247, 237), RGBColor(254, 215, 170),
         "• Resilience, Flexibility & Agility (WEF, 2025): Managing developer cognitive fatigue under constant release pressure.\n"
         "• Psychological Safety (Amy Edmondson, 1999): Psychologically safe teams speak up and learn more, empowering developers to openly voice concerns and renegotiate scope.\n"
         "• Breaking the Fatigue Loop: Exploring whether developer well-being and open communication act as balancing forces.")
    ]

    for idx, (p_title, p_color, p_bg, p_border, p_content) in enumerate(pillars):
        px = Inches(1.45) + idx * Inches(3.51)
        p_card = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, px, tp_y, tp_w, tp_h)
        p_card.fill.solid()
        p_card.fill.fore_color.rgb = p_bg
        p_card.line.color.rgb = p_border
        p_card.line.width = Pt(1.0)

    # Watermark layer on top of card fills, behind text
    if os.path.exists("eagle_watermark.png"):
        s4.shapes.add_picture("eagle_watermark.png", Inches(4.56), Inches(1.65), Inches(4.2), Inches(4.2))

    # Text layer on top of watermark
    tb_pb = s4.shapes.add_textbox(Inches(1.45), Inches(1.35), Inches(10.35), Inches(1.8))
    tf_pb = tb_pb.text_frame
    tf_pb.word_wrap = True
    tf_pb.margin_left = tf_pb.margin_right = Inches(0.25)
    tf_pb.margin_top = Inches(0.12)

    p = tf_pb.paragraphs[0]
    r = p.add_run()
    r.text = "The Core Problem: The Vicious Cycle of Quick Fixes and Developer Fatigue"
    r.font.bold = True
    r.font.size = Pt(11.5)
    r.font.color.rgb = C_CORAL_RED
    disable_spellcheck(r)
    p.space_after = Pt(4)

    p_pd = tf_pb.add_paragraph()
    r = p_pd.add_run()
    r.text = (
        "In modern software engineering, market pressure and tight deadlines frequently force teams to bypass robust architectural "
        "standards in favor of tactical shortcuts ('quick fixes'). While shortcuts provide immediate symptomatic relief, they leave "
        "hidden architectural liabilities—Technical Debt. As debt accumulates, code complexity grows, regression bugs proliferate, "
        "and feature delivery slows down. Teams respond by taking more shortcuts to meet original targets, trapping developers in a "
        "constant cycle of firefighting, cognitive exhaustion, and developer fatigue."
    )
    r.font.size = Pt(8.2)
    r.font.color.rgb = C_TEXT_MAIN
    disable_spellcheck(r)

    for idx, (p_title, p_color, p_bg, p_border, p_content) in enumerate(pillars):
        px = Inches(1.45) + idx * Inches(3.51)
        tb_p = s4.shapes.add_textbox(px, tp_y, tp_w, tp_h)
        tf_p = tb_p.text_frame
        tf_p.word_wrap = True
        tf_p.margin_left = tf_p.margin_right = Inches(0.18)
        tf_p.margin_top = Inches(0.14)

        p = tf_p.paragraphs[0]
        r = p.add_run()
        r.text = p_title
        r.font.bold = True
        r.font.size = Pt(10.0)
        r.font.color.rgb = p_color
        disable_spellcheck(r)
        p.space_after = Pt(5)

        p_c = tf_p.add_paragraph()
        r_c = p_c.add_run()
        r_c.text = p_content
        r_c.font.size = Pt(7.6)
        r_c.font.color.rgb = C_TEXT_MAIN
        disable_spellcheck(r_c)

    add_slide_decorations(s4, 4)

    # --- SLIDE 5: TOPIC SELECTION: PRIMARY & SECONDARY RESOURCE IDENTIFICATION ---
    s5 = prs.slides.add_slide(blank_layout)
    add_coral_frame(s5, "Topic Selection: Primary & Secondary Resource Identification", "TOPIC SELECTION & RESOURCES (SLIDE 2 OF 2)", "flower_slide_5.png", bg_color=C_BG_S5)

    s5_left_w = Inches(6.05)
    s5_right_w = Inches(4.15)
    s5_gap = Inches(0.15)
    s5_left_x = Inches(1.45)
    s5_right_x = s5_left_x + s5_left_w + s5_gap
    s5_box_y = Inches(1.35)
    s5_box_h = Inches(5.55)

    prim_box = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, s5_left_x, s5_box_y, s5_left_w, s5_box_h)
    prim_box.fill.solid()
    prim_box.fill.fore_color.rgb = RGBColor(248, 250, 252) # Soft Slate Pearl
    prim_box.line.color.rgb = C_BORDER
    prim_box.line.width = Pt(1.0)

    # Right Card shape: Secondary Literature & Theoretical Frameworks
    res_box = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, s5_right_x, s5_box_y, s5_right_w, s5_box_h)
    res_box.fill.solid()
    res_box.fill.fore_color.rgb = RGBColor(255, 253, 245) # Soft Warm Ivory Tint
    res_box.line.color.rgb = RGBColor(254, 240, 138)
    res_box.line.width = Pt(1.0)

    card_h = Inches(0.91)
    card_gap = Inches(0.07)
    cards_start_y = s5_box_y + Inches(0.56)

    interviewees_data = [
        {
            "name": "Rounak Biswas",
            "role": "Software Developer",
            "exp": "3.8 Yrs Exp",
            "color": C_CORAL_RED,
            "interviewer": "Samyabrata Roy (Team Lead)",
            "domain": "Data Science & AI R&D (IDEAS-TIH)",
            "relevance": "Navigates rapid prototyping and model deployment shortcuts in AI research pipelines; balances project milestones against long-term code debt and developer fatigue."
        },
        {
            "name": "Anunay Sinha",
            "role": "Software Engineer",
            "exp": "3+ Yrs Exp",
            "color": C_TEAL_DEEP,
            "interviewer": "Abir Saha (Project Manager)",
            "domain": "Backend APIs & Reliability (Deloitte USI)",
            "relevance": "Explores how deadline-driven backend shortcuts contribute to technical debt, degrade system reliability and monitoring, and increase developer workload."
        },
        {
            "name": "Suraj Sajeev",
            "role": "SDE-4 Systems (FW)",
            "exp": "6.5 YoE",
            "color": C_BLUE_ROYAL,
            "interviewer": "Rishabh Barthwal (Research Lead)",
            "domain": "FW, Embedded Systems",
            "relevance": "Provides critical systems engineering insights into low-level firmware shortcuts, hardware-software abstraction debt, and how relentless deadline pressures impact embedded reliability and workload."
        },
        {
            "name": "Keshav Gupta",
            "role": "Software Engineer",
            "exp": "5 Yrs Exp",
            "color": C_AMBER_WARM,
            "interviewer": "Piyush Tilokchandani (Design Lead)",
            "domain": "HR Tech & Global Payroll SaaS (Deel)",
            "relevance": "Navigates staged release freezes and feature flags where urgent hotfixes are cherry-picked—exposing how deadline-driven quick fixes enter code and compound debt."
        },
        {
            "name": "Shubham Mishra",
            "role": "Computer Vision & Full-Stack Engineer",
            "exp": "3 Yrs Exp",
            "color": C_INDIGO,
            "interviewer": "Ramrup Satpati (Creative & Pres. Lead)",
            "domain": "Applied AI & Computer Vision Systems (Siemens)",
            "relevance": "Bridges deep learning vision pipelines with full-stack APIs; direct exposure to heuristic shortcuts and unoptimized inference patches to hit latency SLAs under tight sprints."
        }
    ]

    # Draw card background rectangles first
    for idx, inv in enumerate(interviewees_data):
        cy = cards_start_y + idx * (card_h + card_gap)
        c_shape = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, s5_left_x + Inches(0.12), cy, s5_left_w - Inches(0.24), card_h)
        c_shape.fill.solid()
        c_shape.fill.fore_color.rgb = RGBColor(255, 255, 255)
        c_shape.line.color.rgb = RGBColor(226, 232, 240)
        c_shape.line.width = Pt(0.75)

        # Color accent strip on left
        strip = s5.shapes.add_shape(MSO_SHAPE.RECTANGLE, s5_left_x + Inches(0.12), cy, Inches(0.06), card_h)
        strip.fill.solid()
        strip.fill.fore_color.rgb = inv["color"]
        strip.line.fill.background()

    # Watermark layer on top of card fills, behind text
    if os.path.exists("horse_watermark.png"):
        s5.shapes.add_picture("horse_watermark.png", Inches(4.28), Inches(2.12), Inches(4.68), Inches(4.0))

    # Header for Primary Resources inside left card
    hdr_box = s5.shapes.add_textbox(s5_left_x + Inches(0.15), s5_box_y + Inches(0.08), s5_left_w - Inches(0.3), Inches(0.48))
    tf_hdr = hdr_box.text_frame
    tf_hdr.word_wrap = True
    tf_hdr.margin_left = tf_hdr.margin_right = tf_hdr.margin_top = tf_hdr.margin_bottom = 0
    p_h = tf_hdr.paragraphs[0]
    r_h1 = p_h.add_run()
    r_h1.text = "Primary Resources: Planned Practitioner Cohort (N = 5)"
    r_h1.font.bold = True
    r_h1.font.size = Pt(11.0)
    r_h1.font.color.rgb = C_OCEAN_DARK
    disable_spellcheck(r_h1)

    p_hsub = tf_hdr.add_paragraph()
    r_hsub = p_hsub.add_run()
    r_hsub.text = "Empirical qualitative inquiry: 1 semi-structured interview per member with industry software engineers (≥3 Yrs Exp)"
    r_hsub.font.size = Pt(7.0)
    r_hsub.font.color.rgb = C_TEXT_MUTED
    disable_spellcheck(r_hsub)

    # Text for interviewee cards
    for idx, inv in enumerate(interviewees_data):
        cy = cards_start_y + idx * (card_h + card_gap)
        tb_c = s5.shapes.add_textbox(s5_left_x + Inches(0.12), cy, s5_left_w - Inches(0.24), card_h)
        tf_c = tb_c.text_frame
        tf_c.word_wrap = True
        tf_c.margin_left = Inches(0.14)
        tf_c.margin_right = Inches(0.12)
        tf_c.margin_top = Inches(0.04)
        tf_c.margin_bottom = Inches(0.04)

        # Line 1: Name + Exp Pill on left; Interviewer on right
        p1 = tf_c.paragraphs[0]
        r_nm = p1.add_run()
        r_nm.text = inv["name"]
        r_nm.font.bold = True
        r_nm.font.size = Pt(8.2)
        r_nm.font.color.rgb = C_OCEAN_DARK
        disable_spellcheck(r_nm)

        r_xp = p1.add_run()
        r_xp.text = f"  •  {inv['exp']}"
        r_xp.font.bold = True
        r_xp.font.size = Pt(7.2)
        r_xp.font.color.rgb = inv["color"]
        disable_spellcheck(r_xp)

        r_sp = p1.add_run()
        r_sp.text = "   |   "
        r_sp.font.size = Pt(7.2)
        r_sp.font.color.rgb = C_TEXT_MUTED
        disable_spellcheck(r_sp)

        r_int_lbl = p1.add_run()
        r_int_lbl.text = "Interviewer: "
        r_int_lbl.font.size = Pt(7.0)
        r_int_lbl.font.color.rgb = C_TEXT_MUTED
        disable_spellcheck(r_int_lbl)

        r_int = p1.add_run()
        r_int.text = inv["interviewer"]
        r_int.font.bold = True
        r_int.font.size = Pt(7.0)
        r_int.font.color.rgb = C_OCEAN_DARK
        disable_spellcheck(r_int)
        p1.space_after = Pt(1)

        # Line 2: Role & Domain
        p2 = tf_c.add_paragraph()
        r_rd_lbl = p2.add_run()
        r_rd_lbl.text = "ROLE & DOMAIN: "
        r_rd_lbl.font.bold = True
        r_rd_lbl.font.size = Pt(6.8)
        r_rd_lbl.font.color.rgb = C_TEXT_MUTED
        disable_spellcheck(r_rd_lbl)

        r_rd = p2.add_run()
        r_rd.text = f"{inv['role']}  —  {inv['domain']}"
        r_rd.font.bold = True
        r_rd.font.size = Pt(6.8)
        r_rd.font.color.rgb = C_TEXT_MAIN
        disable_spellcheck(r_rd)
        p2.space_after = Pt(1)

        # Line 3: Relevance
        p3 = tf_c.add_paragraph()
        r_rel_lbl = p3.add_run()
        r_rel_lbl.text = "RELEVANCE: "
        r_rel_lbl.font.bold = True
        r_rel_lbl.font.size = Pt(6.8)
        r_rel_lbl.font.color.rgb = C_TEXT_MUTED
        disable_spellcheck(r_rel_lbl)

        r_rel = p3.add_run()
        r_rel.text = inv["relevance"]
        r_rel.font.size = Pt(6.8)
        r_rel.font.color.rgb = C_TEXT_MAIN
        disable_spellcheck(r_rel)

    # Text for Right Card: Secondary Literature & Theoretical Frameworks
    tb_res = s5.shapes.add_textbox(s5_right_x, s5_box_y, s5_right_w, s5_box_h)
    tf_res = tb_res.text_frame
    tf_res.word_wrap = True
    tf_res.margin_left = tf_res.margin_right = Inches(0.20)
    tf_res.margin_top = Inches(0.12)

    p = tf_res.paragraphs[0]
    r = p.add_run()
    r.text = "Secondary Literature & Theoretical Frameworks"
    r.font.bold = True
    r.font.size = Pt(11.0)
    r.font.color.rgb = C_OCEAN_DARK
    disable_spellcheck(r)

    p_sub = tf_res.add_paragraph()
    r_sub = p_sub.add_run()
    r_sub.text = "Academic foundations grounding system dynamics & human resilience"
    r_sub.font.size = Pt(7.0)
    r_sub.font.color.rgb = C_TEXT_MUTED
    disable_spellcheck(r_sub)
    p_sub.space_after = Pt(6)

    resources = [
        ("Peter M. Senge (1990) -> The Fifth Discipline",
         "Source of systems archetypes ('Fixes that Fail', 'Shifting the Burden'). Establishes how delayed feedback and local optimizations impair organizational capacity."),
        ("Waters Center for Systems Thinking (2020) -> Habits of a Systems Thinker",
         "Core cognitive habits: observing how system dynamics change over time, anticipating unintended consequences, and pinpointing high-leverage intervention points."),
        ("Forsgren, Humble, & Kim (2018) -> Accelerate (DORA Research)",
         "Empirical research on software delivery performance, automated testing rigor, and architectural decoupling linked to lower burnout (Forsgren et al., 2018)."),
        ("Amy Edmondson (1999) -> Psychological Safety & Team Learning",
         "Foundational framework demonstrating that psychologically safe teams speak up and learn more; essential for openly voicing architectural risks."),
        ("World Economic Forum (2025) -> Future of Jobs Report 2025",
         "Highlights systems thinking; resilience, flexibility and agility (WEF, 2025) as top core skills for navigating modern technological disruption.")
    ]
    for r_t, r_d in resources:
        pr = tf_res.add_paragraph()
        rr1 = pr.add_run()
        rr1.text = f"•  {r_t}\n"
        rr1.font.bold = True
        rr1.font.size = Pt(7.8)
        rr1.font.color.rgb = C_OCEAN_DARK
        disable_spellcheck(rr1)
        rr2 = pr.add_run()
        rr2.text = r_d
        rr2.font.size = Pt(7.1)
        rr2.font.color.rgb = C_TEXT_MAIN
        disable_spellcheck(rr2)
        pr.space_after = Pt(4)

    add_slide_decorations(s5, 5)

    # --- SLIDE 6: DISCUSSION PLAN & INTERVIEW PROTOCOL ---
    s6 = prs.slides.add_slide(blank_layout)
    add_coral_frame(s6, "Discussion Plan: Interview Strategy & Draft Questions", "DISCUSSION PLAN & DRAFT QUESTIONS (1 SLIDE)", "flower_slide_6.png", bg_color=C_BG_S6)

    s6_left_w = Inches(4.35)
    s6_right_w = Inches(5.85)
    s6_gap = Inches(0.15)
    s6_left_x = Inches(1.45)
    s6_right_x = s6_left_x + s6_left_w + s6_gap
    s6_box_y = Inches(1.35)
    s6_box_h = Inches(5.55)

    prof_box = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, s6_left_x, s6_box_y, s6_left_w, s6_box_h)
    prof_box.fill.solid()
    prof_box.fill.fore_color.rgb = RGBColor(240, 253, 250) # Soft Teal Tint
    prof_box.line.color.rgb = RGBColor(153, 246, 228)
    prof_box.line.width = Pt(1.0)

    # Right Card: Draft Semi-Structured Interview Protocol
    q_box = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, s6_right_x, s6_box_y, s6_right_w, s6_box_h)
    q_box.fill.solid()
    q_box.fill.fore_color.rgb = RGBColor(250, 245, 255) # Soft Lavender Tint
    q_box.line.color.rgb = RGBColor(233, 213, 255)
    q_box.line.width = Pt(1.0)

    # Watermark layer on top of card fills, behind text
    if os.path.exists("black_eagle_watermark.png"):
        s6.shapes.add_picture("black_eagle_watermark.png", Inches(3.62), Inches(2.12), Inches(6.0), Inches(4.0))

    # Text layer for Left Card
    tb_pf = s6.shapes.add_textbox(s6_left_x, s6_box_y, s6_left_w, s6_box_h)
    tf_pf = tb_pf.text_frame
    tf_pf.word_wrap = True
    tf_pf.margin_left = tf_pf.margin_right = Inches(0.18)
    tf_pf.margin_top = Inches(0.12)

    p = tf_pf.paragraphs[0]
    r = p.add_run()
    r.text = "Interview Strategy & CLD Synthesis"
    r.font.bold = True
    r.font.size = Pt(11)
    r.font.color.rgb = C_TEAL_DEEP
    disable_spellcheck(r)
    p.space_after = Pt(4)

    p_sec1 = tf_pf.add_paragraph()
    r_sec1 = p_sec1.add_run()
    r_sec1.text = "QUALITATIVE EXECUTION PROTOCOL:"
    r_sec1.font.bold = True
    r_sec1.font.size = Pt(7.6)
    r_sec1.font.color.rgb = C_OCEAN_DARK
    disable_spellcheck(r_sec1)
    p_sec1.space_after = Pt(2)

    proto_items = [
        ("Format & Scope:", "N = 5 semi-structured 30–45 min video calls (both cameras on, written consent by email) via Google Meet / Zoom."),
        ("Ethics & Capture:", "Informed consent recorded; verbatim transcript generation via automated tooling."),
        ("Thematic Coding:", "Collaborative thematic synthesis to map patterns to systems archetypes.")
    ]
    for pt, pd in proto_items:
        pp = tf_pf.add_paragraph()
        rp1 = pp.add_run()
        rp1.text = f"• {pt} "
        rp1.font.bold = True
        rp1.font.size = Pt(7.2)
        rp1.font.color.rgb = C_TEXT_MUTED
        disable_spellcheck(rp1)
        rp2 = pp.add_run()
        rp2.text = pd
        rp2.font.size = Pt(7.0)
        rp2.font.color.rgb = C_TEXT_MAIN
        disable_spellcheck(rp2)
        pp.space_after = Pt(2)

    p_sec2 = tf_pf.add_paragraph()
    r_sec2 = p_sec2.add_run()
    r_sec2.text = "\nCONCEPTUAL CLD FEEDBACK LOOPS:"
    r_sec2.font.bold = True
    r_sec2.font.size = Pt(7.6)
    r_sec2.font.color.rgb = C_OCEAN_DARK
    disable_spellcheck(r_sec2)
    p_sec2.space_after = Pt(2)

    cld_loops_s6 = [
        ("R1 (The Quick Fix Spiral):", C_CORAL_RED,
         "Deadline Pressure (+) -> Shortcuts (+) -> Compounding Technical Debt (+) -> Delays (+) -> Deadline Pressure. (Vicious Reinforcing Cycle)"),
        ("R2 (Fatigue & Firefighting Trap):", C_AMBER_WARM,
         "Technical Debt (+) -> Firefighting & Outages (+) -> Developer Fatigue (+) -> Attrition (+) -> Team Deficit (+) -> Pressure for Shortcuts."),
        ("B1 (Engineering Sense Refactoring):", C_TEAL_DEEP,
         "Technical Debt (+) -> Root-Cause Diagnostic (+) -> Refactoring Sprints (+) -> System Modularity & Health (-) -> Debt. (Stabilizer)"),
        ("B2 (Psychological Safety Pushback):", C_BLUE_ROYAL,
         "Fatigue (+) -> Concerns voiced (+) -> Scope renegotiation (+) -> less Deadline pressure (-). (Human Balancing Loop)")
    ]
    for lt, l_col, ld in cld_loops_s6:
        pl = tf_pf.add_paragraph()
        rl1 = pl.add_run()
        rl1.text = f"{lt}\n"
        rl1.font.bold = True
        rl1.font.size = Pt(7.2)
        rl1.font.color.rgb = l_col
        disable_spellcheck(rl1)
        rl2 = pl.add_run()
        rl2.text = ld
        rl2.font.size = Pt(6.8)
        rl2.font.color.rgb = C_TEXT_MAIN
        disable_spellcheck(rl2)
        pl.space_after = Pt(3)

    # Text layer for Right Card
    tb_q = s6.shapes.add_textbox(s6_right_x, s6_box_y, s6_right_w, s6_box_h)
    tf_q = tb_q.text_frame
    tf_q.word_wrap = True
    tf_q.margin_left = tf_q.margin_right = Inches(0.22)
    tf_q.margin_top = Inches(0.12)

    p = tf_q.paragraphs[0]
    r = p.add_run()
    r.text = "Draft Semi-Structured Interview Protocol (5 Core Questions)"
    r.font.bold = True
    r.font.size = Pt(11.5)
    r.font.color.rgb = C_INDIGO
    disable_spellcheck(r)
    p.space_after = Pt(6)

    draft_questions = [
        ("Q1 (Shortcuts & Immediate Payoffs):", C_TEAL_DEEP,
         "Can you describe a specific project where your team implemented a 'quick fix' or technical shortcut to meet a tight deadline? What was the immediate operational payoff?"),
        ("Q2 (Subsequent Evolution & Delayed Effects):", C_BLUE_ROYAL,
         "Tell me about what happened in the months following that release. How did the codebase evolve, and how did your team manage subsequent feature delivery?"),
        ("Q3 (Production Maintenance & Daily Workload):", C_AMBER_WARM,
         "Tell me about a time when your team had to maintain, debug, or support that system in production. What was the day-to-day engineering experience and workload like for you and your teammates?"),
        ("Q4 (Team Dynamics & Raising Concerns):", C_INDIGO,
         "Tell me about a situation where someone on your team raised concerns about deadlines, code quality, or architectural debt. How did the team, peers, and leadership respond?"),
        ("Q5 (High-Leverage Interventions & Sustainable Velocity):", C_CORAL_RED,
         "Looking back, what practical engineering practices or cultural interventions have you seen work best to break the cycle of quick fixes and restore sustainable team velocity?")
    ]
    for q_t, q_col, q_d in draft_questions:
        pq = tf_q.add_paragraph()
        rq1 = pq.add_run()
        rq1.text = f"{q_t}\n"
        rq1.font.bold = True
        rq1.font.size = Pt(8.2)
        rq1.font.color.rgb = q_col
        disable_spellcheck(rq1)
        rq2 = pq.add_run()
        rq2.text = q_d
        rq2.font.size = Pt(7.6)
        rq2.font.color.rgb = C_TEXT_MAIN
        disable_spellcheck(rq2)
        pq.space_after = Pt(5)

    add_slide_decorations(s6, 6)

    prs.save("Team_114_SPG_GP1_Sep_2026.pptx")
    print("[*] Successfully generated PowerPoint: Team_114_SPG_GP1_Sep_2026.pptx")


# =============================================================================
# 2. REPORTLAB PDF BUILDER (Team_114_SPG_GP1_Sep_2026.pdf)
# =============================================================================
def build_pdf():
    PAGE_WIDTH = 960
    PAGE_HEIGHT = 540
    c = canvas.Canvas("Team_114_SPG_GP1_Sep_2026.pdf", pagesize=(PAGE_WIDTH, PAGE_HEIGHT))

    def draw_top_down(p, x, y_top, w, h):
        actual_w, actual_h = p.wrap(w, h)
        p.drawOn(c, x, y_top - actual_h)
        return actual_h

    def draw_coral_page_frame(title_text, category_text="BSGN3001: STRATEGIES FOR PROFESSIONAL GROWTH", coral_corner="flower_slide_1.png", bg_color=HEX_BG_S1):
        c.setFillColor(bg_color)
        c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

        if os.path.exists(coral_corner):
            c.drawImage(coral_corner, 18, PAGE_HEIGHT - 82, width=70, height=70, mask='auto')

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
            c.drawImage("iitm_logo_clean.png", PAGE_WIDTH - 98, PAGE_HEIGHT - 75, width=72, height=72, mask='auto')

        c.setStrokeColor(HexColor("#e2e8f0"))
        c.setLineWidth(1)
        c.line(102, 24, PAGE_WIDTH - 110, 24)

        c.setFillColor(HEX_TEXT_MUTED)
        c.setFont("Helvetica", 8)
        c.drawString(102, 12, "Team 114: Iterate  •  Beyond Quick Fixes: Exploring Tech Debt & Developer Fatigue  •  GP1 Deliverable 2")
        c.drawRightString(PAGE_WIDTH - 115, 12, "IIT Madras BS Degree")

    def draw_slide_decorations(slide_idx):
        tree_path = f"tree_slide_{slide_idx}.png"
        if os.path.exists(tree_path):
            c.drawImage(tree_path, PAGE_WIDTH - 105, 16, width=48, height=72, mask='auto')
        if os.path.exists("page_flip_corner.png"):
            c.drawImage("page_flip_corner.png", PAGE_WIDTH - 55, 0, width=55, height=86, mask='auto')

    # --- PDF SLIDE 0: COVER SLIDE ---
    c.setFillColor(HEX_BG_S0)
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    if os.path.exists("flower_slide_0.png"):
        c.drawImage("flower_slide_0.png", 26, PAGE_HEIGHT - 105, width=76, height=76, mask='auto')
    if os.path.exists("flower_cover_bottom.png"):
        c.drawImage("flower_cover_bottom.png", 26, 32, width=76, height=76, mask='auto')
    if os.path.exists("iitm_logo_clean.png"):
        c.drawImage("iitm_logo_clean.png", PAGE_WIDTH - 115, PAGE_HEIGHT - 115, width=90, height=90, mask='auto')

    card_x = 115
    card_y = 45
    card_w = PAGE_WIDTH - 230
    card_h = PAGE_HEIGHT - 90
    c.setFillColor(HEX_CARD_BG)
    c.setStrokeColor(HEX_BORDER)
    c.setLineWidth(1.2)
    c.roundRect(card_x, card_y, card_w, card_h, 8, fill=1, stroke=1)

    if os.path.exists("cover_watermark.png"):
        c.drawImage("cover_watermark.png", card_x + 2, card_y + 2, width=card_w - 4, height=card_h - 4, mask='auto')

    c.setFillColor(HEX_CORAL_RED)
    c.setFont("Helvetica-Bold", 9.5)
    c.drawString(card_x + 30, card_y + card_h - 32, "IIT MADRAS BS DEGREE PROGRAMME")

    c.setFillColor(HEX_TEXT_MUTED)
    c.setFont("Helvetica-Bold", 8.5)
    c.drawString(card_x + 30, card_y + card_h - 48, "BSGN3001: STRATEGIES FOR PROFESSIONAL GROWTH  •  GROUP PROJECT 1 (GP1)")

    c.setFillColor(HEX_OCEAN_DARK)
    c.setFont("Helvetica-Bold", 17)
    c.drawString(card_x + 30, card_y + card_h - 78, "Beyond Quick Fixes: Exploring Technical Debt & Developer Fatigue")
    c.drawString(card_x + 30, card_y + card_h - 100, "Through Systems Thinking")

    c.setFillColor(HEX_TEAL_DEEP)
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(card_x + 30, card_y + card_h - 122, "Linking Systems Thinking (Week 10) and Engineering Sense (Week 11)")

    c.setFillColor(HEX_CORAL_RED)
    c.setFont("Helvetica-Bold", 9.5)
    c.drawString(card_x + 30, card_y + card_h - 152, "TEAM 114: ITERATE  |  PITCH DECK DELIVERABLE 2 (OCTOBER 2026)")

    roster = [
        ("Samyabrata Roy", "22F2001443", "Team Lead", "22F2001443@ds.study.iitm.ac.in"),
        ("Abir Saha", "23F3001436", "Project Manager", "23F3001436@ds.study.iitm.ac.in"),
        ("Rishabh Barthwal", "23F2004112", "Research Lead", "23F2004112@ds.study.iitm.ac.in"),
        ("Piyush Tilokchandani", "21F1006739", "Slides / Design Lead", "21F1006739@ds.study.iitm.ac.in"),
        ("Ramrup Satpati", "24F3004027", "Editor / Creative & Presentation Lead", "24F3004027@ds.study.iitm.ac.in")
    ]
    ry = card_y + card_h - 180
    for name, roll, role, email in roster:
        c.setFillColor(HEX_OCEAN_DARK)
        c.setFont("Helvetica-Bold", 10.5)
        c.drawString(card_x + 35, ry, f"•   {name}")

        c.setFillColor(HEX_TEXT_MUTED)
        c.setFont("Helvetica", 9)
        c.drawString(card_x + 205, ry, f"({roll}  |  {email})")

        c.setFillColor(HEX_CORAL_RED)
        c.setFont("Helvetica-Bold", 9.5)
        c.drawString(card_x + 475, ry, f"—   {role}")
        ry -= 26

    bot_pill_y = card_y + 12
    bot_pill_h = 60
    c.setFillColor(HEX_PILL_BG)
    c.setStrokeColor(HEX_BORDER)
    c.roundRect(card_x + 30, bot_pill_y, card_w - 60, bot_pill_h, 6, fill=1, stroke=1)

    c.setFillColor(HEX_OCEAN_DARK)
    c.setFont("Helvetica-Bold", 8.0)
    c.drawString(card_x + 42, bot_pill_y + 44, "Deliverable Overview & Alignment:")
    c.setFillColor(HEX_TEXT_MAIN)
    c.setFont("Helvetica", 7.2)
    c.drawString(card_x + 185, bot_pill_y + 44, "This 6-slide pitch deck details Team Iterate's Project Management Plan, Team Profile, Conceptual CLD, secondary")
    c.drawString(card_x + 42, bot_pill_y + 33, "literature frameworks, and qualitative interview protocol for GP1 Deliverable 2 submission.")

    c.setFillColor(HEX_CORAL_RED)
    c.setFont("Helvetica-Bold", 7.5)
    c.drawString(card_x + 42, bot_pill_y + 19, "Note on Operational Roles:")
    c.setFillColor(HEX_TEXT_MUTED)
    c.setFont("Helvetica", 6.8)
    c.drawString(card_x + 155, bot_pill_y + 19, "Defined roles serve as primary administrative touchpoints for accountability and submission requirements. In practice,")
    c.drawString(card_x + 42, bot_pill_y + 8, "responsibilities remain fluid; all members actively cross-collaborate across research, interview execution, and development.")

    draw_slide_decorations(0)
    c.showPage()

    # --- PDF SLIDE 1: TEAM PROFILE ---
    draw_coral_page_frame("Team Profile: Complementary Capabilities & Governance", "TEAM PROFILE (1 SLIDE)", "flower_slide_1.png", bg_color=HEX_BG_S1)

    c_w = 142
    c_h = 315
    c_y = 120
    s_x = 102
    sp_x = 153

    members_data_pdf = [
        ("Samyabrata Roy", "22F2001443", "Team Lead",
         "BS Data Science · MSc Stats (CU) · Assoc. SWE",
         "Core Coordination",
         "Oversees holistic delivery, academic milestone compliance, and portal submissions.",
         "Strategic Alignment, Milestone Integrity", "portrait_samyabrata.png", HEX_OCEAN_DARK),
        ("Abir Saha", "23F3001436", "Project Manager",
         "BS Data Science · Full-Stack & Process Eng",
         "Sprint Governance",
         "Maintains project timeline, task tracking, meeting cadences, and blocker resolution.",
         "Process Architecture, Sprint Schedules", "portrait_abir.png", HEX_CORAL_RED),
        ("Rishabh Barthwal", "23F2004112", "Research Lead",
         "BS Data Science · Applied AI & Systems",
         "Theory & Synthesis",
         "Heads theoretical modeling around Peter Senge archetypes and interview protocol.",
         "ENTJ-A, Analytical Inquiry, Literature", "portrait_rishabh.png", HEX_TEAL_DEEP),
        ("Piyush Tilokchandani", "21F1006739", "Design Lead",
         "BS Data Science\nSoftware Dev at Piramal Finance",
         "Visual Architecture",
         "Curates deck visual aesthetics, data diagrams, typography, and presentation layout.",
         "Information Architecture, Visual Systems", "portrait_piyush.png", HEX_INDIGO),
        ("Ramrup Satpati", "24F3004027", "Creative & Pres. Lead",
         "BS Data Science · Deep Learning & AI Eng",
         "Narrative & Synthesis",
         "Directs content synthesis, editorial rigor, human-loop integration, and final presentation.",
         "ENFJ-A, Qualitative Synthesis, AI Systems", "portrait_ramrup.png", HEX_CORAL_RED)
    ]

    for idx, (m_name, m_roll, m_role, m_bg, m_focus, m_desc, m_traits, m_portrait, m_color) in enumerate(members_data_pdf):
        cur_x = s_x + idx * sp_x
        c.setFillColor(HEX_CARD_BG)
        c.setStrokeColor(HexColor("#94a3b8")) # Crisp Slate 400
        c.setLineWidth(1.6)
        c.roundRect(cur_x, c_y, c_w, c_h, 8, fill=1, stroke=1)

        # Top Accent Header Bar
        c.setFillColor(m_color)
        c.roundRect(cur_x, c_y + c_h - 6, c_w, 6, 3, fill=1, stroke=0)

        # Large Portrait (104 x 116 pt)
        port_w = 104
        port_h = 116
        port_x = cur_x + (c_w - port_w) / 2
        port_y = c_y + c_h - 128
        if os.path.exists(m_portrait):
            c.drawImage(m_portrait, port_x, port_y, width=port_w, height=port_h, mask='auto')

        # Name
        c.setFillColor(HEX_OCEAN_DARK)
        c.setFont("Helvetica-Bold", 9.2)
        c.drawCentredString(cur_x + c_w/2, c_y + c_h - 140, m_name)

        # Role Badge
        c.setFillColor(m_color)
        c.setFont("Helvetica-Bold", 7.8)
        c.drawCentredString(cur_x + c_w/2, c_y + c_h - 151, m_role)

        # Roll Number
        c.setFillColor(HEX_TEXT_MUTED)
        c.setFont("Helvetica", 7.0)
        c.drawCentredString(cur_x + c_w/2, c_y + c_h - 160, f"({m_roll})")

        # Background Line
        c.setFillColor(HEX_TEAL_DEEP)
        c.setFont("Helvetica-Bold", 6.0)
        if "\n" in m_bg:
            b_line1, b_line2 = m_bg.split("\n", 1)
            c.drawCentredString(cur_x + c_w/2, c_y + c_h - 167, b_line1)
            c.drawCentredString(cur_x + c_w/2, c_y + c_h - 175, b_line2)
        else:
            c.drawCentredString(cur_x + c_w/2, c_y + c_h - 170, m_bg)

        # Scope Tag Pill
        c.setFillColor(HEX_PILL_BG)
        c.roundRect(cur_x + 8, c_y + c_h - 190, c_w - 16, 13, 3, fill=1, stroke=0)
        c.setFillColor(HEX_OCEAN_DARK)
        c.setFont("Helvetica-Bold", 6.8)
        c.drawCentredString(cur_x + c_w/2, c_y + c_h - 186, f"Scope: {m_focus}")

        # Description
        desc_p = Paragraph(f"<font size='6.5' color='#334155'>{m_desc}</font>",
                           ParagraphStyle('D', fontName='Helvetica', fontSize=6.5, leading=8.6, alignment=1))
        draw_top_down(desc_p, cur_x + 8, c_y + c_h - 192, c_w - 16, 55)

        # Traits Tag
        tr_p = Paragraph(f"<font size='6.0' color='#64748b'><i>Traits:</i> {m_traits}</font>",
                         ParagraphStyle('T', fontName='Helvetica-Oblique', fontSize=6.0, leading=7.8, alignment=1))
        draw_top_down(tr_p, cur_x + 8, c_y + 32, c_w - 16, 28)

    # Footer Area: Left Diversity Card + Right SWOT 4-Box Matrix
    f_y = 32
    f_h = 76
    b_w = PAGE_WIDTH - 204

    # Left Diversity Card
    div_w = 250
    c.setFillColor(HexColor("#eff6ff")) # Soft Ice Blue
    c.setStrokeColor(HexColor("#bfdbfe"))
    c.roundRect(s_x, f_y, div_w, f_h, 6, fill=1, stroke=1)

    c.setFillColor(HEX_OCEAN_DARK)
    c.setFont("Helvetica-Bold", 8.2)
    c.drawString(s_x + 10, f_y + f_h - 16, "Team Diversity & Operating Cadence:")

    c.setFillColor(HEX_CORAL_RED)
    c.setFont("Helvetica-Bold", 7.2)
    c.drawString(s_x + 10, f_y + f_h - 28, "• 5 BS Data Science · FinTech SWE, Stats & AI")

    c.setFillColor(HEX_TEXT_MAIN)
    c.setFont("Helvetica", 6.8)
    p_div = Paragraph("<font size='6.8' color='#1e293b'>• Cohort: 2021–2024 batches · 2 Working Pros · Ages 21–26 · Multi-City (BLR, CCU, DEL) · Shared ownership (1 interview each).</font>",
                      ParagraphStyle('DivP', fontName='Helvetica', fontSize=6.8, leading=8.8))
    draw_top_down(p_div, s_x + 10, f_y + f_h - 32, div_w - 18, 40)

    # Right Container: 4-Box SWOT Matrix
    swot_x = s_x + div_w + 10
    swot_w = b_w - div_w - 10
    c.setFillColor(HexColor("#ffffff"))
    c.setStrokeColor(HEX_BORDER)
    c.roundRect(swot_x, f_y, swot_w, f_h, 6, fill=1, stroke=1)

    swot_quads_pdf = [
        ("STRENGTHS (S)", HEX_TEAL_DEEP, HexColor("#f0fdf4"),
         "5 of 5 in BS Data Science; cross-industry blend of FinTech SWE, MSc Stats & AI."),
        ("WEAKNESSES (W)", HEX_AMBER_WARM, HexColor("#fff7ed"),
         "Balancing full-time software jobs, term courses, and asynchronous time zones."),
        ("OPPORTUNITIES (O)", HEX_BLUE_ROYAL, HexColor("#eff6ff"),
         "Direct Tier-1 tech & R&D network access (IDEAS-TIH, Deloitte, Deel, Siemens)."),
        ("THREATS (T)", HEX_CORAL_RED, HexColor("#fff1f2"),
         "Interviewee cancellations, corporate release crunches, and exam conflicts.")
    ]

    q_w = (swot_w - 20) / 4
    for qi, (qt, qc, qb, qd) in enumerate(swot_quads_pdf):
        qx = swot_x + 5 + qi * (q_w + 3.5)
        c.setFillColor(qb)
        c.setStrokeColor(HexColor("#e2e8f0"))
        c.roundRect(qx, f_y + 4, q_w, f_h - 8, 4, fill=1, stroke=1)

        c.setFillColor(qc)
        c.setFont("Helvetica-Bold", 6.8)
        c.drawString(qx + 5, f_y + f_h - 16, qt)

        p_qd = Paragraph(f"<font size='6.0' color='#1e293b'>{qd}</font>",
                         ParagraphStyle('SwotD', fontName='Helvetica', fontSize=6.0, leading=7.8))
        draw_top_down(p_qd, qx + 5, f_y + f_h - 20, q_w - 10, 50)

    draw_slide_decorations(1)
    c.showPage()

    # --- PDF SLIDE 2: EXECUTION GANTT & WBS (Slide 1 of PMP) ---
    draw_coral_page_frame("Project Management Plan: Execution Gantt & WBS Matrix", "PROJECT MANAGEMENT PLAN (SLIDE 1 OF 2)", "flower_slide_2.png", bg_color=HEX_BG_S2)

    # Goal Banner at top
    c.setFillColor(HexColor("#fff1f2")) # Rose blush
    c.setStrokeColor(HexColor("#fecdd3"))
    c.roundRect(s_x, 436, b_w, 22, 4, fill=1, stroke=1)
    c.setFillColor(HEX_CORAL_RED)
    c.setFont("Helvetica-Bold", 8.0)
    c.drawString(s_x + 12, 443, "PROJECT GOAL:")
    c.setFillColor(HEX_OCEAN_DARK)
    c.setFont("Helvetica-Bold", 8.0)
    c.drawString(s_x + 88, 443, "Use 5 engineers' real stories to show how quick fixes create tech debt and tire developers, and find what breaks the cycle.")

    if os.path.exists("gantt_chart.png"):
        c.drawImage("gantt_chart.png", s_x, 260, width=b_w, height=168, mask='auto')

    w_y = 32
    w_h = 222
    c.setFillColor(HexColor("#fffdf7")) # Warm Creme Tint
    c.setStrokeColor(HEX_BORDER)
    c.setLineWidth(1.0)
    c.roundRect(s_x, w_y, b_w, w_h, 6, fill=1, stroke=1)

    # Watermark layer on top of card fills, behind text
    if os.path.exists("wolf_watermark.png"):
        c.drawImage("wolf_watermark.png", 480 - 140, w_y + w_h / 2.0 - 103, width=280, height=206, mask='auto')

    c.setFillColor(HEX_OCEAN_DARK)
    c.setFont("Helvetica-Bold", 9.5)
    c.drawString(s_x + 15, w_y + w_h - 17, "Work Breakdown Structure (WBS) & Deliverable Ownership Matrix")

    wbs_items_pdf = [
        ("WBS 1.0: Literature & Archetype Modeling", "Rishabh Barthwal (Lead), Ramrup Satpati",
         "Curate Peter Senge (1990) archetypes, Waters Center habits, and DORA research.", HEX_TEAL_DEEP),
        ("WBS 2.0: Interviewee Sourcing & Scheduling", "All 5 Members (1 candidate each), Abir Saha (PM)",
         "Identify 5 practitioners across SaaS, FinTech, and cloud platforms; schedule calls.", HEX_BLUE_ROYAL),
        ("WBS 3.0: Interview Execution & Transcription", "All 5 Members (Equal Ownership)",
         "Conduct 30–45 min semi-structured interviews; record video, both cameras on, after written consent by email; generate verbatim transcripts.", HEX_TEAL_DEEP),
        ("WBS 4.0: Cross-Case Thematic Analysis", "Ramrup Satpati (Lead), Rishabh Barthwal",
         "Synthesize recurring themes across transcripts; validate reinforcing debt loops and human balancing loops.", HEX_BLUE_ROYAL),
        ("WBS 5.0: GP2 Team Project Report [Deliverable 1.c]", "Samyabrata Roy (Lead), All Members",
         "Each member: 5–10 min video clip + 1-page interim report (14 Nov); consolidate team project report under 'Deliverable 1.C.' within portal.", HEX_AMBER_WARM),
        ("WBS 6.0: GP2 Live Presentation & Deck [Deliverable 2]", "Piyush Tilokchandani (Design), Ramrup Satpati (Lead)",
         "Design slide deck, conduct mock defense sessions, and deliver live team presentation by November 30.", HEX_INDIGO)
    ]
    wy_cur = w_y + w_h - 32
    for w_t, w_o, w_d, w_col in wbs_items_pdf:
        c.setFillColor(HEX_OCEAN_DARK)
        c.setFont("Helvetica-Bold", 7.6)
        c.drawString(s_x + 18, wy_cur, f"•   {w_t}")
        c.setFillColor(w_col)
        c.setFont("Helvetica-Bold", 7.3)
        c.drawString(s_x + 235, wy_cur, f"[{w_o}]")
        c.setFillColor(HEX_TEXT_MAIN)
        c.setFont("Helvetica", 7.0)
        c.drawString(s_x + 18, wy_cur - 10, f"    {w_d}")
        wy_cur -= 28

    draw_slide_decorations(2)
    c.showPage()

    # --- PDF SLIDE 3: RISK & QUALITY CONTROLS (Slide 2 of PMP) ---
    draw_coral_page_frame("Project Management Plan: Risk Management & Quality Controls", "PROJECT MANAGEMENT PLAN (SLIDE 2 OF 2)", "flower_slide_3.png", bg_color=HEX_BG_S3)

    h_w = (PAGE_WIDTH - 204 - 15) / 2
    b_h = PAGE_HEIGHT - 125
    b_y = 35

    # Left Card: Proactive Risk Matrix
    c.setFillColor(HEX_CARD_RISK) # Soft Warm Peach
    c.setStrokeColor(HEX_BORDER_RISK)
    c.roundRect(s_x, b_y, h_w, b_h, 6, fill=1, stroke=1)

    # Right Side: Visual Quality Assurance & Milestone Progress Dashboard
    qa_x = s_x + h_w + 15
    if os.path.exists("governance_dashboard.png"):
        c.drawImage("governance_dashboard.png", qa_x, b_y, width=h_w, height=b_h, mask='auto')

    # Watermark layer on top of card fills, behind text
    if os.path.exists("chess_watermark.png"):
        c.drawImage("chess_watermark.png", 480 - 340, b_y + b_h / 2.0 - 126, width=680, height=252, mask='auto')

    c.setFillColor(HEX_AMBER_WARM)
    c.setFont("Helvetica-Bold", 10.5)
    c.drawString(s_x + 15, b_y + b_h - 20, "Proactive Risk Matrix & Mitigation")

    risks_pdf = [
        ("Risk 1: Interviewee Scheduling Delays", "Severity: High | Likelihood: Medium",
         "Each member secures 1 primary candidate and 1 fallback professional by Oct 28. If primary cancels, switch to the backup interviewee, keep the email proof (as live video is mandatory)."),
        ("Risk 2: Interview Data Fragmentation", "Severity: Medium | Likelihood: Medium",
         "Standardized 5-question interview guide and shared Notion transcript template ensure uniform qualitative analysis across all 5 interviews."),
        ("Risk 3: Theoretical Scope Creep", "Severity: Medium | Likelihood: Low",
         "Strictly anchor research to the single core feedback cycle ('Quick Fixes -> Technical Debt -> Developer Fatigue') rather than broader software engineering topics."),
        ("Risk 4: Deadline Crunch & Academic Clashes", "Severity: High | Likelihood: Low",
         "Strict internal deadline buffer: GP2 drafts finalized by Nov 12, giving a 48-hour buffer before the official November 14 portal deadline.")
    ]
    ry_cur = b_y + b_h - 40
    for rt, rm, rd in risks_pdf:
        c.setFillColor(HEX_OCEAN_DARK)
        c.setFont("Helvetica-Bold", 8.0)
        c.drawString(s_x + 15, ry_cur, rt)
        c.setFillColor(HEX_TEAL_DEEP)
        c.setFont("Helvetica-Bold", 7.0)
        c.drawString(s_x + 15, ry_cur - 10, rm)
        p_rd = Paragraph(f"<font size='7.0' color='#334155'><b>Mitigation:</b> {rd}</font>",
                         ParagraphStyle('R', fontName='Helvetica', fontSize=7.0, leading=9.2))
        draw_top_down(p_rd, s_x + 15, ry_cur - 16, h_w - 30, 48)
        ry_cur -= 84

    draw_slide_decorations(3)
    c.showPage()

    # --- PDF SLIDE 4: CORE PROBLEM & 3 PILLARS (Slide 1 of Topic) ---
    draw_coral_page_frame("Topic Selection: Core Problem & Theoretical Foundations", "TOPIC SELECTION & RESOURCES (SLIDE 1 OF 2)", "flower_slide_4.png", bg_color=HEX_BG_S4)

    pr_h = 100
    pr_y = PAGE_HEIGHT - 78 - pr_h
    c.setFillColor(HEX_CARD_PROB) # Rose Blush Tint
    c.setStrokeColor(HEX_BORDER_PROB)
    c.roundRect(s_x, pr_y, b_w, pr_h, 6, fill=1, stroke=1)

    pil_w = (b_w - 20) / 3
    pil_h = 245
    pil_y = 35

    pillars_pdf = [
        ("SPG Week 10: Systems Thinking", HEX_TEAL_DEEP, HEX_CARD_P1, HEX_BORDER_P1, [
            ("Feedback Loops:", "Analyzing how reinforcing loops (R) accelerate technical debt, while balancing loops (B) stabilize delivery."),
            ("Waters Center Habits:", "'Observes how elements change over time', 'Considers short-term, long-term and unintended consequences of actions', and 'Considers mental models.'"),
            ("Peter Senge (1990) Archetypes:", "• 'Fixes that Fail': Quick patches create delayed blowbacks.<br/>• 'Shifting the Burden': Symptomatic workarounds erode long-term architectural health.")
        ]),
        ("SPG Week 11: Engineering Sense", HEX_BLUE_ROYAL, HEX_CARD_P2, HEX_BORDER_P2, [
            ("Pragmatic Trade-off Analysis:", "Balancing immediate delivery velocity against long-term code maintainability."),
            ("Root-Cause Diagnosis:", "Distinguishing superficial software bugs from foundational design deficiencies."),
            ("High-Leverage Debt Remediation:", "Knowing when to refactor vs. when to build new features within real-world time and budget constraints.")
        ]),
        ("Human Balancing Loops (Core 2030)", HEX_CORAL_RED, HEX_CARD_P3, HEX_BORDER_P3, [
            ("Resilience, Flexibility & Agility:", "Managing developer cognitive fatigue under constant release pressure (WEF, 2025)."),
            ("Psychological Safety (Amy Edmondson):", "Psychologically safe teams speak up and learn more (Edmondson, 1999); empowering engineers to voice concerns."),
            ("Breaking the Fatigue Loop:", "Exploring whether developer well-being and open communication act as balancing forces.")
        ])
    ]

    # Draw pillar card backgrounds
    for idx, (p_t, p_col, p_bg, p_bord, p_items) in enumerate(pillars_pdf):
        px = s_x + idx * (pil_w + 10)
        c.setFillColor(p_bg)
        c.setStrokeColor(p_bord)
        c.roundRect(px, pil_y, pil_w, pil_h, 6, fill=1, stroke=1)

    # Watermark layer on top of card fills, behind text
    if os.path.exists("eagle_watermark.png"):
        c.drawImage("eagle_watermark.png", PAGE_WIDTH / 2.0 - 150, PAGE_HEIGHT / 2.0 - 155, width=300, height=300, mask='auto')

    # Draw problem box text
    c.setFillColor(HEX_CORAL_RED)
    c.setFont("Helvetica-Bold", 10.5)
    c.drawString(s_x + 15, pr_y + pr_h - 18, "The Core Problem: The Vicious Cycle of Quick Fixes and Developer Fatigue")

    prob_desc = (
        "In modern software engineering, market pressure and tight deadlines frequently force teams to bypass robust architectural "
        "standards in favor of tactical shortcuts ('quick fixes'). While shortcuts provide immediate symptomatic relief, they leave "
        "hidden architectural liabilities—Technical Debt. As debt accumulates, code complexity grows, regression bugs proliferate, "
        "and feature delivery slows down. Teams respond by taking more shortcuts to meet original targets, trapping developers in a "
        "constant cycle of firefighting, cognitive exhaustion, and developer fatigue."
    )
    p_pr = Paragraph(f"<font size='7.5' color='#334155'>{prob_desc}</font>",
                     ParagraphStyle('Prob', fontName='Helvetica', fontSize=7.5, leading=10.5))
    draw_top_down(p_pr, s_x + 15, pr_y + pr_h - 26, b_w - 30, 65)

    # Draw pillar text
    for idx, (p_t, p_col, p_bg, p_bord, p_items) in enumerate(pillars_pdf):
        px = s_x + idx * (pil_w + 10)
        c.setFillColor(p_col)
        c.setFont("Helvetica-Bold", 9.2)
        c.drawString(px + 12, pil_y + pil_h - 18, p_t)

        pi_y = pil_y + pil_h - 30
        for it_h, it_b in p_items:
            c.setFillColor(HEX_OCEAN_DARK)
            c.setFont("Helvetica-Bold", 7.5)
            c.drawString(px + 12, pi_y, it_h)
            p_it = Paragraph(f"<font size='7.0' color='#334155'>{it_b}</font>",
                             ParagraphStyle('PI', fontName='Helvetica', fontSize=7.0, leading=9.2))
            h_used = draw_top_down(p_it, px + 12, pi_y - 6, pil_w - 24, 60)
            pi_y -= (h_used + 14)

    draw_slide_decorations(4)
    c.showPage()

    # --- PDF SLIDE 5: TOPIC SELECTION: PRIMARY & SECONDARY RESOURCE IDENTIFICATION ---
    draw_coral_page_frame("Topic Selection: Primary & Secondary Resource Identification", "TOPIC SELECTION & RESOURCES (SLIDE 2 OF 2)", "flower_slide_5.png", bg_color=HEX_BG_S5)

    left_w = (b_w - 14) * 0.58
    right_w = (b_w - 14) * 0.42
    right_x = s_x + left_w + 14

    # Left Card: Primary Resources (Planned Practitioner Cohort N=5)
    c.setFillColor(HexColor("#f8fafc"))
    c.setStrokeColor(HexColor("#cbd5e1"))
    c.roundRect(s_x, b_y, left_w, b_h, 6, fill=1, stroke=1)

    # Right Card: Secondary Literature
    c.setFillColor(HEX_CARD_RES)
    c.setStrokeColor(HEX_BORDER_RES)
    c.roundRect(right_x, b_y, right_w, b_h, 6, fill=1, stroke=1)

    card_gap = 6
    card_h = (b_h - 44 - (4 * card_gap)) / 5

    interviewees_pdf = [
        {
            "name": "Rounak Biswas",
            "role": "Software Developer",
            "exp": "3.8 Yrs Exp",
            "color": HEX_CORAL_RED,
            "interviewer": "Samyabrata Roy (Team Lead)",
            "domain": "Data Science & AI R&D (IDEAS-TIH)",
            "relevance": "Navigates rapid prototyping and model deployment shortcuts in AI research pipelines; balances project milestones against long-term code debt and developer fatigue."
        },
        {
            "name": "Anunay Sinha",
            "role": "Software Engineer",
            "exp": "3+ Yrs Exp",
            "color": HEX_TEAL_DEEP,
            "interviewer": "Abir Saha (Project Manager)",
            "domain": "Backend APIs & Reliability (Deloitte USI)",
            "relevance": "Explores how deadline-driven backend shortcuts contribute to technical debt, degrade system reliability and monitoring, and increase developer workload."
        },
        {
            "name": "Suraj Sajeev",
            "role": "SDE-4 Systems (FW)",
            "exp": "6.5 YoE",
            "color": HEX_BLUE_ROYAL,
            "interviewer": "Rishabh Barthwal (Research Lead)",
            "domain": "FW, Embedded Systems",
            "relevance": "Provides critical systems engineering insights into low-level firmware shortcuts, hardware-software abstraction debt, and how relentless deadline pressures impact embedded reliability and workload."
        },
        {
            "name": "Keshav Gupta",
            "role": "Software Engineer",
            "exp": "5 Yrs Exp",
            "color": HEX_AMBER_WARM,
            "interviewer": "Piyush Tilokchandani (Design Lead)",
            "domain": "HR Tech & Global Payroll SaaS (Deel)",
            "relevance": "Navigates staged release freezes and feature flags where urgent hotfixes are cherry-picked—exposing how deadline-driven quick fixes enter code and compound debt."
        },
        {
            "name": "Shubham Mishra",
            "role": "Computer Vision & Full-Stack Engineer",
            "exp": "3 Yrs Exp",
            "color": HEX_INDIGO,
            "interviewer": "Ramrup Satpati (Creative & Pres. Lead)",
            "domain": "Applied AI & Computer Vision Systems (Siemens)",
            "relevance": "Bridges deep learning vision pipelines with full-stack APIs; direct exposure to heuristic shortcuts and unoptimized inference patches to hit latency SLAs under tight sprints."
        }
    ]

    # Draw interviewee card shapes first
    for i, inv in enumerate(interviewees_pdf):
        cy = b_y + b_h - 40 - (i + 1) * card_h - (i * card_gap) + card_gap
        c.setFillColor(HexColor("#ffffff"))
        c.setStrokeColor(HexColor("#e2e8f0"))
        c.roundRect(s_x + 8, cy, left_w - 16, card_h, 4, fill=1, stroke=1)

        # Accent tab
        c.setFillColor(inv["color"])
        c.roundRect(s_x + 8, cy, 3.5, card_h, 2, fill=1, stroke=0)

    # Watermark layer on top of card fills, behind text
    if os.path.exists("horse_watermark.png"):
        c.drawImage("horse_watermark.png", 480 - 180, 248 - 155, width=360, height=310, mask='auto')

    # Draw left card header text
    c.setFillColor(HEX_OCEAN_DARK)
    c.setFont("Helvetica-Bold", 10.5)
    c.drawString(s_x + 14, b_y + b_h - 20, "Primary Resources: Planned Practitioner Cohort (N = 5)")

    c.setFillColor(HEX_TEXT_MUTED)
    c.setFont("Helvetica", 7.0)
    c.drawString(s_x + 14, b_y + b_h - 32, "Empirical qualitative inquiry: 1 interview per member with practicing software engineers (≥3 Yrs Exp)")

    # Draw interviewee card text
    for i, inv in enumerate(interviewees_pdf):
        cy = b_y + b_h - 40 - (i + 1) * card_h - (i * card_gap) + card_gap

        # Line 1: Candidate Name + Exp Pill on left; Interviewer on right
        c.setFillColor(HEX_OCEAN_DARK)
        c.setFont("Helvetica-Bold", 8.2)
        c.drawString(s_x + 18, cy + card_h - 13, inv['name'])
        
        w_name = c.stringWidth(inv['name'] + " ", "Helvetica-Bold", 8.2)
        c.setFont("Helvetica-Bold", 7.2)
        c.setFillColor(inv["color"])
        c.drawString(s_x + 18 + w_name, cy + card_h - 13, f"•  {inv['exp']}")

        c.setFont("Helvetica", 7.0)
        c.setFillColor(HEX_TEXT_MUTED)
        w_int = c.stringWidth(f"Interviewer: {inv['interviewer']}", "Helvetica-Bold", 7.0)
        c.drawString(s_x + left_w - 16 - w_int, cy + card_h - 13, "Interviewer: ")
        c.setFont("Helvetica-Bold", 7.0)
        c.setFillColor(HEX_OCEAN_DARK)
        w_lbl = c.stringWidth("Interviewer: ", "Helvetica", 7.0)
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
        draw_top_down(p_rel, s_x + 88, cy + card_h - 27, left_w - 104, 26)

    # Right Card text
    c.setFillColor(HEX_OCEAN_DARK)
    c.setFont("Helvetica-Bold", 10.5)
    c.drawString(right_x + 14, b_y + b_h - 20, "Secondary Literature & Theoretical Frameworks")

    c.setFillColor(HEX_TEXT_MUTED)
    c.setFont("Helvetica", 7.0)
    c.drawString(right_x + 14, b_y + b_h - 32, "Academic foundations grounding system dynamics & human resilience")

    res_pdf = [
        ("Peter M. Senge (1990) -> The Fifth Discipline",
         "Source of systems archetypes ('Fixes that Fail', 'Shifting the Burden'). Establishes how delayed feedback and local optimizations impair organizational capacity."),
        ("Waters Center for Systems Thinking (2020) -> Habits of a Systems Thinker",
         "Core cognitive habits: observing how system dynamics change over time, anticipating unintended consequences, and pinpointing high-leverage intervention points."),
        ("Forsgren, Humble, & Kim (2018) -> Accelerate (DORA Research)",
         "Empirical research on software delivery performance, automated testing rigor, and architectural decoupling linked to lower burnout (Forsgren et al., 2018)."),
        ("Amy Edmondson (1999) -> Psychological Safety & Team Learning",
         "Foundational framework demonstrating that psychologically safe teams speak up and learn more; essential for openly voicing architectural risks."),
        ("World Economic Forum (2025) -> Future of Jobs Report 2025",
         "Highlights systems thinking; resilience, flexibility and agility (WEF, 2025) as top core skills for navigating modern technological disruption.")
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

    draw_slide_decorations(5)
    c.showPage()

    # --- PDF SLIDE 6: DISCUSSION PLAN & INTERVIEW PROTOCOL ---
    draw_coral_page_frame("Discussion Plan: Interview Strategy & Draft Questions", "DISCUSSION PLAN & DRAFT QUESTIONS (1 SLIDE)", "flower_slide_6.png", bg_color=HEX_BG_S6)

    left_w6 = (b_w - 14) * 0.42
    right_w6 = (b_w - 14) * 0.58
    right_x6 = s_x + left_w6 + 14

    # Left Card: Interview Methodology & CLD Loop Synthesis
    c.setFillColor(HexColor("#f0fdfa"))
    c.setStrokeColor(HexColor("#99f6e4"))
    c.roundRect(s_x, b_y, left_w6, b_h, 6, fill=1, stroke=1)

    # Right Card: Draft Semi-Structured Interview Protocol
    c.setFillColor(HEX_CARD_Q) # Soft Lavender Tint
    c.setStrokeColor(HEX_BORDER_Q)
    c.roundRect(right_x6, b_y, right_w6, b_h, 6, fill=1, stroke=1)

    # Watermark layer on top of card fills, behind text
    if os.path.exists("black_eagle_watermark.png"):
        c.drawImage("black_eagle_watermark.png", 480 - 225, 248 - 150, width=450, height=300, mask='auto')

    c.setFillColor(HEX_TEAL_DEEP)
    c.setFont("Helvetica-Bold", 10.5)
    c.drawString(s_x + 14, b_y + b_h - 20, "Interview Strategy & CLD Synthesis")

    # Section 1: Methodology Protocol
    c.setFillColor(HEX_OCEAN_DARK)
    c.setFont("Helvetica-Bold", 7.6)
    c.drawString(s_x + 14, b_y + b_h - 36, "QUALITATIVE EXECUTION PROTOCOL:")

    proto_items = [
        ("Format & Scope:", "N = 5 semi-structured 30–45 min video calls (both cameras on, written consent by email) via Google Meet / Zoom."),
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
        ("R2 (Fatigue & Firefighting Trap):", HEX_AMBER_WARM,
         "Technical Debt (+) -> Firefighting & Outages (+) -> Developer Fatigue (+) -> Attrition (+) -> Team Deficit (+) -> Pressure for Shortcuts."),
        ("B1 (Engineering Sense Refactoring):", HEX_TEAL_DEEP,
         "Technical Debt (+) -> Root-Cause Diagnostic (+) -> Refactoring Sprints (+) -> System Modularity & Health (-) -> Debt. (Stabilizer)"),
        ("B2 (Psychological Safety Pushback):", HEX_BLUE_ROYAL,
         "Fatigue (+) -> Concerns voiced (+) -> Scope renegotiation (+) -> less Deadline pressure (-). (Human Balancing Loop)")
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

    # Right Card text
    c.setFillColor(HEX_INDIGO)
    c.setFont("Helvetica-Bold", 10.5)
    c.drawString(right_x6 + 14, b_y + b_h - 20, "Draft Semi-Structured Interview Protocol (5 Core Questions)")

    draft_questions_pdf = [
        ("Q1 (Shortcuts & Immediate Payoffs):", HEX_TEAL_DEEP,
         "Can you describe a specific project where your team implemented a 'quick fix' or technical shortcut to meet a tight deadline? What was the immediate operational payoff?"),
        ("Q2 (Subsequent Evolution & Delayed Effects):", HEX_BLUE_ROYAL,
         "Tell me about what happened in the months following that release. How did the codebase evolve, and how did your team manage subsequent feature delivery?"),
        ("Q3 (Production Maintenance & Daily Workload):", HEX_AMBER_WARM,
         "Tell me about a time when your team had to maintain, debug, or support that system in production. What was the day-to-day engineering experience and workload like for you and your teammates?"),
        ("Q4 (Team Dynamics & Raising Concerns):", HEX_INDIGO,
         "Tell me about a situation where someone on your team raised concerns about deadlines, code quality, or architectural debt. How did the team, peers, and leadership respond?"),
        ("Q5 (High-Leverage Interventions & Sustainable Velocity):", HEX_CORAL_RED,
         "Looking back, what practical engineering practices or cultural interventions have you seen work best to break the cycle of quick fixes and restore sustainable team velocity?")
    ]

    qy_cur = b_y + b_h - 44
    for qt, qc, qd in draft_questions_pdf:
        c.setFillColor(qc)
        c.setFont("Helvetica-Bold", 8.0)
        c.drawString(right_x6 + 14, qy_cur, qt)
        p_qd = Paragraph(f"<font size='7.2' color='#334155'>{qd}</font>",
                         ParagraphStyle('QD', fontName='Helvetica', fontSize=7.2, leading=9.5))
        draw_top_down(p_qd, right_x6 + 20, qy_cur - 8, right_w6 - 36, 45)
        qy_cur -= 66

    draw_slide_decorations(6)
    c.showPage()
    c.save()
    print("[*] Successfully generated ReportLab Vector PDF: Team_114_SPG_GP1_Sep_2026.pdf")


if __name__ == "__main__":
    from generate_governance_dashboard import generate_governance_dashboard
    prepare_watermarks()
    ensure_flower_assets()
    generate_governance_dashboard()
    build_gantt_chart()
    build_pptx()
    build_pdf()
