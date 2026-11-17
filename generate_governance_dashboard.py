import os
from PIL import Image, ImageDraw, ImageFont

def generate_governance_dashboard(output_path="governance_dashboard.png"):
    # Canvas dimensions: 1020 x 1110 (crisp resolution for 5.1 in x 5.55 in)
    w, h = 1020, 1110
    img = Image.new("RGBA", (w, h), (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Fonts
    font_arial = "/System/Library/Fonts/Supplemental/Arial.ttf"
    font_bold = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
    if not os.path.exists(font_bold):
        font_bold = font_arial

    f_title = ImageFont.truetype(font_bold, 22)
    f_sub = ImageFont.truetype(font_arial, 14)
    f_sec = ImageFont.truetype(font_bold, 16)
    f_label_b = ImageFont.truetype(font_bold, 13)
    f_label = ImageFont.truetype(font_arial, 12)
    f_num_big = ImageFont.truetype(font_bold, 26)
    f_badge = ImageFont.truetype(font_bold, 11)
    f_axis = ImageFont.truetype(font_arial, 12)

    # Background card with subtle rounded border
    draw.rounded_rectangle([2, 2, w - 3, h - 3], radius=16, fill=(255, 255, 255), outline=(203, 213, 225), width=2)

    # Top Header Banner
    draw.rounded_rectangle([2, 2, w - 3, 76], radius=16, fill=(240, 253, 244))
    draw.rectangle([2, 50, w - 3, 76], fill=(240, 253, 244))
    draw.line([(2, 76), (w - 3, 76)], fill=(187, 247, 208), width=2)

    draw.text((28, 16), "Quality Assurance & Milestone Progress Tracker", font=f_title, fill=(15, 23, 42))
    draw.text((28, 48), "Visual tracking of deliverable progress, audit compliance, and team communication SLAs", font=f_sub, fill=(13, 148, 136))

    # SECTION 1: SPRINT MILESTONE PROGRESS (HORIZONTAL BARS)
    draw.text((28, 92), "1. DELIVERABLE PROGRESS & SPRINT STATUS", font=f_sec, fill=(15, 23, 42))

    milestones = [
        ("Phase 1: Team Inception & Contract", "100%", 1.0, (16, 185, 129), "Verified (Deliverables 1.a-1.c)"),
        ("Phase 2: GP1 Pitch Deck Submission", "100%", 1.0, (225, 29, 72), "Pitch Deck & Methodology Ready"),
        ("Phase 3: Video Interviews (N=5)", "40%", 0.40, (13, 148, 136), "2 of 5 Recorded (Both Cameras On)"),
        ("Phase 4: Thematic Analysis & CLD", "20%", 0.20, (29, 78, 216), "Coding Matrix & CLD Protocol Ready"),
        ("Phase 5: GP2 Project Report (Nov 14)", "Scheduled", 0.04, (234, 88, 12), "48-Hour Buffer (Internal Lock Nov 12)"),
        ("Phase 6: Live Defense Presentation", "Scheduled", 0.04, (124, 58, 237), "Deck Design & Mock Defense (Nov 30)")
    ]

    bar_start_y = 124
    bar_h = 24
    bar_max_w = 440
    bar_x = 285

    for i, (m_title, pct_lbl, pct_val, col, note) in enumerate(milestones):
        cy = bar_start_y + i * 49

        # Title
        draw.text((28, cy + 3), m_title, font=f_label_b, fill=(30, 41, 59))

        # Progress bar track
        draw.rounded_rectangle([bar_x, cy, bar_x + bar_max_w, cy + bar_h], radius=6, fill=(241, 245, 249), outline=(226, 232, 240), width=1)

        # Progress bar fill
        filled_w = max(int(bar_max_w * pct_val), 18)
        draw.rounded_rectangle([bar_x, cy, bar_x + filled_w, cy + bar_h], radius=6, fill=col)

        # Value text inside or beside bar
        if pct_val >= 0.2:
            draw.text((bar_x + 12, cy + 5), pct_lbl, font=f_badge, fill=(255, 255, 255))
        else:
            draw.text((bar_x + filled_w + 8, cy + 5), pct_lbl, font=f_badge, fill=col)

        # Status note
        draw.text((bar_x + bar_max_w + 16, cy + 5), note, font=f_label, fill=(71, 85, 105))

    # SECTION 2: OPERATIONAL QUALITY METRIC CARDS (2x2 GRID)
    draw.line([(28, 436), (w - 28, 436)], fill=(226, 232, 240), width=1)
    draw.text((28, 452), "2. QUALITY ASSURANCE CONTROLS & AUDIT STANDARDS", font=f_sec, fill=(15, 23, 42))

    cards = [
        {
            "num": "100%",
            "title": "Dual-Camera & Consent Audit",
            "desc": "Written email consent secured before calls; video recorded with both cameras on per rubric.",
            "color": (16, 185, 129),
            "bg": (240, 253, 244),
            "border": (187, 247, 208)
        },
        {
            "num": "< 12 hrs",
            "title": "Escalation SLA & Checkpoints",
            "desc": "Mandatory 12h blocker response on WhatsApp; bi-weekly syncs (Wed & Sun 9 PM IST).",
            "color": (29, 78, 216),
            "bg": (239, 246, 255),
            "border": (191, 219, 254)
        },
        {
            "num": "3-Pass",
            "title": "Editorial & Rubric Verification",
            "desc": "Multi-pass review by Ramrup Satpati; APA 7th citation formatting and strict rubric audit.",
            "color": (225, 29, 72),
            "bg": (255, 241, 242),
            "border": (254, 205, 211)
        },
        {
            "num": "48 Hours",
            "title": "Internal Safety Margin Buffer",
            "desc": "GP2 drafts finalized by Nov 12 to absorb corporate release crunches before official Nov 14 portal deadline.",
            "color": (234, 88, 12),
            "bg": (255, 247, 237),
            "border": (254, 215, 170)
        }
    ]

    card_y = 486
    card_w = 468
    card_h = 104

    for idx, c_info in enumerate(cards):
        col_idx = idx % 2
        row_idx = idx // 2
        cx = 28 + col_idx * (card_w + 26)
        cy = card_y + row_idx * (card_h + 16)

        draw.rounded_rectangle([cx, cy, cx + card_w, cy + card_h], radius=10, fill=c_info["bg"], outline=c_info["border"], width=1)

        # Big KPI value
        draw.text((cx + 18, cy + 14), c_info["num"], font=f_num_big, fill=c_info["color"])

        # Title
        draw.text((cx + 18, cy + 50), c_info["title"], font=f_label_b, fill=(15, 23, 42))

        # Description wrapped
        desc_words = c_info["desc"].split()
        lines = []
        cur_line = []
        for word in desc_words:
            cur_line.append(word)
            if len(" ".join(cur_line)) > 52:
                cur_line.pop()
                lines.append(" ".join(cur_line))
                cur_line = [word]
        if cur_line:
            lines.append(" ".join(cur_line))

        for li, line_text in enumerate(lines[:2]):
            draw.text((cx + 18, cy + 68 + li * 16), line_text, font=f_label, fill=(71, 85, 105))

    # SECTION 3: SPRINT VELOCITY & EFFORT LINE GRAPH (VISUAL TREND)
    draw.line([(28, 730), (w - 28, 730)], fill=(226, 232, 240), width=1)
    draw.text((28, 746), "3. PLANNED VS. ACTUAL SPRINT VELOCITY (LINE GRAPH)", font=f_sec, fill=(15, 23, 42))

    # Legend at top right of section 3
    leg_x = w - 380
    leg_y = 748
    draw.line([(leg_x, leg_y + 8), (leg_x + 24, leg_y + 8)], fill=(148, 163, 184), width=2)
    draw.text((leg_x + 30, leg_y), "Planned Velocity", font=f_axis, fill=(100, 116, 139))

    draw.line([(leg_x + 160, leg_y + 8), (leg_x + 184, leg_y + 8)], fill=(13, 148, 136), width=3)
    draw.ellipse([leg_x + 168, leg_y + 4, leg_x + 176, leg_y + 12], fill=(13, 148, 136))
    draw.text((leg_x + 192, leg_y), "Actual Track (Ahead)", font=f_axis, fill=(13, 148, 136))

    gx_left = 80
    gx_right = w - 60
    gy_bottom = 1040
    gy_top = 800

    # Grid lines and Y axis
    y_ticks = [(100, "100%"), (75, "75%"), (50, "50%"), (25, "25%"), (0, "0%")]
    for val, lbl in y_ticks:
        y_pos = gy_bottom - int((val / 100) * (gy_bottom - gy_top))
        draw.line([(gx_left, y_pos), (gx_right, y_pos)], fill=(241, 245, 249), width=1)
        draw.text((gx_left - 48, y_pos - 8), lbl, font=f_axis, fill=(148, 163, 184))

    # X axis points
    time_points = [
        (0.00, "Oct 10\nKickoff"),
        (0.18, "Oct 18\nContract"),
        (0.30, "Oct 24\nGP1 Pitch"),
        (0.50, "Nov 04\nInterviews"),
        (0.72, "Nov 14\nGP2 Report"),
        (1.00, "Nov 30\nLive Defense")
    ]

    for ratio, label in time_points:
        x_pos = gx_left + int(ratio * (gx_right - gx_left))
        draw.line([(x_pos, gy_bottom), (x_pos, gy_bottom + 6)], fill=(148, 163, 184), width=1)
        lines = label.split("\n")
        draw.text((x_pos - 24, gy_bottom + 10), lines[0], font=f_axis, fill=(30, 41, 59))
        draw.text((x_pos - 24, gy_bottom + 26), lines[1], font=f_axis, fill=(100, 116, 139))

    # Planned Line (Dashed Slate line)
    plan_pts = [
        (0.00, 0),
        (0.18, 15),
        (0.30, 27),
        (0.50, 52),
        (0.72, 76),
        (1.00, 100)
    ]
    px_coords = []
    for ratio, val in plan_pts:
        x_pt = gx_left + int(ratio * (gx_right - gx_left))
        y_pt = gy_bottom - int((val / 100) * (gy_bottom - gy_top))
        px_coords.append((x_pt, y_pt))

    for i in range(len(px_coords) - 1):
        x1, y1 = px_coords[i]
        x2, y2 = px_coords[i + 1]
        steps = 15
        for s in range(steps):
            if s % 2 == 0:
                sx1 = x1 + (x2 - x1) * (s / steps)
                sy1 = y1 + (y2 - y1) * (s / steps)
                sx2 = x1 + (x2 - x1) * ((s + 0.8) / steps)
                sy2 = y1 + (y2 - y1) * ((s + 0.8) / steps)
                draw.line([(sx1, sy1), (sx2, sy2)], fill=(148, 163, 184), width=2)

    # Actual Progress Line (Solid Teal line up to Oct 27)
    act_pts = [
        (0.00, 0),
        (0.18, 18),
        (0.30, 32),
        (0.36, 42)
    ]
    ax_coords = []
    for ratio, val in act_pts:
        x_pt = gx_left + int(ratio * (gx_right - gx_left))
        y_pt = gy_bottom - int((val / 100) * (gy_bottom - gy_top))
        ax_coords.append((x_pt, y_pt))

    for i in range(len(ax_coords) - 1):
        draw.line([ax_coords[i], ax_coords[i + 1]], fill=(13, 148, 136), width=4)

    for pt_x, pt_y in ax_coords:
        draw.ellipse([pt_x - 5, pt_y - 5, pt_x + 5, pt_y + 5], fill=(13, 148, 136), outline=(255, 255, 255), width=2)

    # Current Day Callout badge on graph
    curr_x, curr_y = ax_coords[-1]
    callout_w = 175
    draw.rounded_rectangle([curr_x + 8, curr_y - 32, curr_x + 8 + callout_w, curr_y - 6], radius=4, fill=(13, 148, 136))
    draw.text((curr_x + 16, curr_y - 27), "Oct 27: Ahead of Plan", font=f_badge, fill=(255, 255, 255))
    draw.polygon([(curr_x + 12, curr_y - 6), (curr_x + 22, curr_y - 6), (curr_x + 6, curr_y)], fill=(13, 148, 136))

    img.save(output_path, "PNG")
    print(f"[*] Generated user-friendly Governance Dashboard: {output_path} ({w}x{h})")

if __name__ == "__main__":
    generate_governance_dashboard()
