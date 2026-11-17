import os
from PIL import Image, ImageDraw, ImageFont

def generate_notion_tracker(output_path="notion_tracker.png"):
    w, h = 960, 440
    img = Image.new("RGBA", (w, h), (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Fonts
    font_arial = "/System/Library/Fonts/Supplemental/Arial.ttf"
    font_bold = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
    if not os.path.exists(font_bold):
        font_bold = font_arial

    f_title = ImageFont.truetype(font_bold, 15)
    f_header = ImageFont.truetype(font_bold, 12)
    f_sub = ImageFont.truetype(font_arial, 11)
    f_card_t = ImageFont.truetype(font_bold, 11)
    f_card_b = ImageFont.truetype(font_arial, 10)
    f_badge = ImageFont.truetype(font_bold, 9)

    # Background
    draw.rectangle([0, 0, w, h], fill=(250, 250, 250))

    # Top Navigation Bar (Notion Style)
    draw.rectangle([0, 0, w, 44], fill=(255, 255, 255))
    draw.line([(0, 44), (w, 44)], fill=(229, 231, 235), width=1)

    # Breadcrumb & Board Title
    draw.text((16, 14), "Team 114: Iterate", font=f_header, fill=(30, 41, 59))
    draw.text((135, 14), "/", font=f_sub, fill=(156, 163, 175))
    draw.text((150, 14), "GP1 & GP2 Sprint Board Tracker", font=f_header, fill=(225, 29, 72))

    # Right side filter / search badges
    draw.rounded_rectangle([w - 225, 10, w - 120, 34], radius=4, fill=(243, 244, 246), outline=(229, 231, 235), width=1)
    draw.text((w - 215, 15), "FILTER: ACTIVE", font=f_badge, fill=(75, 85, 99))
    draw.rounded_rectangle([w - 110, 10, w - 16, 34], radius=4, fill=(243, 244, 246), outline=(229, 231, 235), width=1)
    draw.text((w - 102, 15), "ALL MEMBERS", font=f_badge, fill=(75, 85, 99))

    # Columns Setup
    col_w = 296
    col_gap = 16
    start_x = 16
    start_y = 56

    cols = [
        {
            "name": "IN PROGRESS",
            "count": "3",
            "badge_bg": (219, 234, 254),
            "badge_fg": (30, 64, 175),
            "cards": [
                {
                    "title": "WBS 3.0: Semi-Structured Interviews",
                    "sub": "30-45 min video calls (both cameras on)",
                    "tags": [("Oct 28", (254, 243, 199), (180, 83, 9)), ("All 5", (224, 231, 255), (67, 56, 202))],
                    "progress": "2 / 5 Recorded"
                },
                {
                    "title": "WBS 4.0: Conceptual CLD Synthesis",
                    "sub": "Map R1, R2, B1, B2 feedback dynamics",
                    "tags": [("Oct 27", (254, 226, 226), (185, 28, 28)), ("Rishabh, RS", (243, 232, 255), (126, 34, 206))],
                    "progress": "Synthesis v2 ready"
                },
                {
                    "title": "WBS 2.0: Backup Candidate Outreach",
                    "sub": "Secure written consent & fallback contacts",
                    "tags": [("Oct 26", (254, 243, 199), (180, 83, 9)), ("Abir (PM)", (209, 250, 229), (6, 95, 70))],
                    "progress": "5 Backups Aligned"
                }
            ]
        },
        {
            "name": "TO DO (UPCOMING)",
            "count": "3",
            "badge_bg": (243, 244, 246),
            "badge_fg": (75, 85, 99),
            "cards": [
                {
                    "title": "WBS 5.0: Individual Interim Reports",
                    "sub": "5-10 min video clip + 1-page report each",
                    "tags": [("Nov 14", (254, 226, 226), (185, 28, 28)), ("All 5", (224, 231, 255), (67, 56, 202))],
                    "progress": "Templates shared"
                },
                {
                    "title": "Cross-Transcript Thematic Analysis",
                    "sub": "Affinity diagramming across 5 verbatim texts",
                    "tags": [("Nov 05", (243, 244, 246), (55, 65, 81)), ("Ramrup, RB", (243, 232, 255), (126, 34, 206))],
                    "progress": "Pending calls"
                },
                {
                    "title": "WBS 6.0: GP2 Presentation Deck",
                    "sub": "Live mock defense & 7-slide final deck",
                    "tags": [("Nov 30", (243, 244, 246), (55, 65, 81)), ("Piyush, RS", (224, 231, 255), (67, 56, 202))],
                    "progress": "Outline staged"
                }
            ]
        },
        {
            "name": "DONE / VERIFIED",
            "count": "4",
            "badge_bg": (220, 252, 231),
            "badge_fg": (22, 101, 52),
            "cards": [
                {
                    "title": "WBS 1.0: Theoretical Literature Review",
                    "sub": "Peter Senge archetypes & WEF (2025)",
                    "tags": [("Verified", (220, 252, 231), (22, 101, 52)), ("Rishabh", (243, 232, 255), (126, 34, 206))],
                    "progress": "Completed"
                },
                {
                    "title": "Interview Guide & 5 Core Questions",
                    "sub": "Neutral 'Tell me about a time...' format",
                    "tags": [("Verified", (220, 252, 231), (22, 101, 52)), ("Ramrup", (254, 243, 199), (180, 83, 9))],
                    "progress": "Rubric aligned"
                },
                {
                    "title": "GP1 Pitch Deck (Deliverable 2)",
                    "sub": "PMP, SWOT, Gantt, and CLD protocol",
                    "tags": [("Verified", (220, 252, 231), (22, 101, 52)), ("All 5", (224, 231, 255), (67, 56, 202))],
                    "progress": "Ready to submit"
                }
            ]
        }
    ]

    for col_idx, col in enumerate(cols):
        cx = start_x + col_idx * (col_w + col_gap)
        
        # Column Header Pill
        draw.rounded_rectangle([cx, start_y, cx + 115, start_y + 22], radius=4, fill=col["badge_bg"])
        draw.text((cx + 8, start_y + 5), col["name"], font=f_badge, fill=col["badge_fg"])
        draw.text((cx + 102, start_y + 5), col["count"], font=f_badge, fill=col["badge_fg"])

        # Cards in column
        card_y = start_y + 32
        for card in col["cards"]:
            card_h = 104
            # White card with crisp border
            draw.rounded_rectangle([cx, card_y, cx + col_w, card_y + card_h], radius=6, fill=(255, 255, 255), outline=(226, 232, 240), width=1)

            # Left accent notch
            draw.rounded_rectangle([cx, card_y + 6, cx + 3, card_y + card_h - 6], radius=2, fill=col["badge_fg"])

            # Card Title
            draw.text((cx + 12, card_y + 10), card["title"], font=f_card_t, fill=(15, 23, 42))

            # Card Subtitle
            draw.text((cx + 12, card_y + 28), card["sub"], font=f_card_b, fill=(100, 116, 139))

            # Tags
            tag_x = cx + 12
            for tag_text, tag_bg, tag_fg in card["tags"]:
                tag_w = draw.textlength(tag_text, font=f_badge) + 12
                draw.rounded_rectangle([tag_x, card_y + 54, tag_x + tag_w, card_y + 72], radius=3, fill=tag_bg)
                draw.text((tag_x + 6, card_y + 58), tag_text, font=f_badge, fill=tag_fg)
                tag_x += tag_w + 6

            # Bottom info bar: Progress
            draw.line([(cx + 12, card_y + 80), (cx + col_w - 12, card_y + 80)], fill=(241, 245, 249), width=1)
            draw.text((cx + 12, card_y + 86), "Status: " + card["progress"], font=f_badge, fill=(71, 85, 105))

            card_y += card_h + 10

    # Subtle outer border
    draw.rectangle([0, 0, w - 1, h - 1], outline=(203, 213, 225), width=1)

    img.save(output_path, "PNG")
    print(f"[*] Generated Notion board mockup: {output_path} ({w}x{h})")

if __name__ == "__main__":
    generate_notion_tracker()
