import os
import matplotlib
os.environ['MPLCONFIGDIR'] = '/tmp/mpl_config'
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_cld():
    # Wider aspect ratio for prominence: 16.5 x 8.0 inches
    fig, ax = plt.subplots(figsize=(16.5, 8.0), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    c_coral = '#be123c'    # Reinforcing loops
    c_green = '#15803d'    # Balancing loops
    c_amber = '#c2410c'    # External input
    c_purple = '#6b21a8'   # Legacy input

    nodes = {
        'reqs': {
            'text': 'Unclear Client\nRequirements',
            'x': 8, 'y': 84, 'w': 13.5, 'h': 9.5,
            'bg': '#fff7ed', 'border': '#fdba74', 'tc': '#9a3412', 'tag': 'Exogenous Input (Part. 2)'
        },
        'press': {
            'text': 'Deadline Pressure\n(Market & Client SLAs)',
            'x': 30, 'y': 84, 'w': 18, 'h': 9.5,
            'bg': '#fef2f2', 'border': '#f87171', 'tc': '#991b1b', 'tag': 'Core System Driver'
        },
        'shortcuts': {
            'text': 'Propensity for\nQuick Fixes & Shortcuts',
            'x': 60, 'y': 84, 'w': 19, 'h': 9.5,
            'bg': '#fff1f2', 'border': '#fb7185', 'tc': '#9f1239', 'tag': 'Supported by 4 of 5'
        },
        'legacy': {
            'text': 'Inherited Legacy\nIncompatibilities',
            'x': 90, 'y': 84, 'w': 16.5, 'h': 9.5,
            'bg': '#f5f3ff', 'border': '#c4b5fd', 'tc': '#5b21b6', 'tag': 'Exogenous Input (Part. 2 & 3)'
        },
        'debt': {
            'text': 'Accumulated\nTechnical Debt',
            'x': 90, 'y': 55, 'w': 16.5, 'h': 9.5,
            'bg': '#fef2f2', 'border': '#e11d48', 'tc': '#881337', 'tag': 'Core Stock (Supported by 5/5)'
        },
        'bugs': {
            'text': 'Code Complexity,\nRework & Fragility',
            'x': 90, 'y': 26, 'w': 16.5, 'h': 9.5,
            'bg': '#f8fafc', 'border': '#94a3b8', 'tc': '#1e293b', 'tag': 'Delayed System Friction'
        },
        'fire': {
            'text': 'Production Firefighting\n& Emergency Rollbacks',
            'x': 60, 'y': 26, 'w': 19, 'h': 9.5,
            'bg': '#fff7ed', 'border': '#f97316', 'tc': '#c2410c', 'tag': 'Supported by 4 of 5'
        },
        'fatigue': {
            'text': 'Developer Fatigue\n& Burnout',
            'x': 30, 'y': 26, 'w': 18, 'h': 9.5,
            'bg': '#fff1f2', 'border': '#e11d48', 'tc': '#9f1239', 'tag': 'Supported by 4 of 5'
        },
        'velocity': {
            'text': 'Delivery Velocity\n& Productivity',
            'x': 30, 'y': 55, 'w': 18, 'h': 8.5,
            'bg': '#f0fdf4', 'border': '#86efac', 'tc': '#166534', 'tag': 'Systemic Throughput'
        },
        'b_capacity': {
            'text': 'Sprint Debt Capacity\n(Token Allocation)',
            'x': 60, 'y': 55, 'w': 19, 'h': 9.5,
            'bg': '#ecfdf5', 'border': '#10b981', 'tc': '#065f46', 'tag': 'B1: Dedicated Buffer'
        },
        # B2 Loop corrected: Pushback node on left, enabled by Psychological Safety
        'b_pushback': {
            'text': 'Upstream Scope\nPushback & Negotiation',
            'x': 8, 'y': 55, 'w': 14.5, 'h': 9.5,
            'bg': '#ecfdf5', 'border': '#10b981', 'tc': '#065f46', 'tag': 'B2: Balancing Action'
        },
        'b_safety': {
            'text': 'Psychological\nSafety Culture',
            'x': 8, 'y': 26, 'w': 14.0, 'h': 9.5,
            'bg': '#f0fdf4', 'border': '#86efac', 'tc': '#166534', 'tag': 'Enabling Condition (Edmondson)'
        }
    }

    # Draw nodes
    for k, n in nodes.items():
        box = patches.FancyBboxPatch(
            (n['x'] - n['w']/2, n['y'] - n['h']/2), n['w'], n['h'],
            boxstyle="round,pad=0.5,rounding_size=1.0",
            facecolor=n['bg'], edgecolor=n['border'], linewidth=1.4
        )
        ax.add_patch(box)
        ax.text(n['x'], n['y'] + 0.8, n['text'], ha='center', va='center',
                fontsize=8.0, fontweight='bold', color=n['tc'], linespacing=1.15)
        ax.text(n['x'], n['y'] - n['h']/2 + 1.2, n['tag'], ha='center', va='center',
                fontsize=6.2, fontweight='bold', color='#64748b', style='italic')

    # Sleek arrow drawing helper
    def draw_cld_link(x1, y1, x2, y2, pol='+', rad=0.0, color='#be123c', pol_pos=0.5, pol_offset=(0, 0)):
        ax.annotate(
            '', xy=(x2, y2), xytext=(x1, y1),
            arrowprops=dict(
                arrowstyle="-|>,head_length=0.45,head_width=0.22",
                connectionstyle=f"arc3,rad={rad}",
                color=color, lw=1.6
            )
        )
        mx = x1 + (x2 - x1) * pol_pos + pol_offset[0]
        my = y1 + (y2 - y1) * pol_pos + pol_offset[1]
        if pol:
            pol_bg = '#fee2e2' if pol == '+' else '#dcfce7'
            pol_col = '#991b1b' if pol == '+' else '#166534'
            ax.text(mx, my, f" {pol} ", ha='center', va='center', fontsize=7.2,
                    fontweight='bold', color=pol_col,
                    bbox=dict(boxstyle='circle,pad=0.15', facecolor=pol_bg, edgecolor=pol_col, lw=0.7))

    # 1. R1: Deadline Pressure -> Quick Fixes (+)
    draw_cld_link(39, 84, 50.5, 84, pol='+', rad=0.0, color=c_coral)
    # 2. R1: Quick Fixes -> Technical Debt (+)
    draw_cld_link(69.5, 84, 81.5, 59, pol='+', rad=0.1, color=c_coral)
    # 3. R1: Technical Debt -> Bugs & Complexity (+)
    draw_cld_link(90, 50.2, 90, 31, pol='+', rad=0.0, color=c_coral, pol_offset=(2.0, 0))
    # 4. R1: Bugs -> Firefighting (+)
    draw_cld_link(81.5, 26, 69.5, 26, pol='+', rad=0.0, color=c_coral)
    # 5. R1: Firefighting -> Deadline Pressure (+) (Loop closure)
    draw_cld_link(55, 31, 38, 79, pol='+', rad=-0.2, color=c_coral, pol_pos=0.45)

    # 6. R2: Firefighting -> Developer Fatigue (+)
    draw_cld_link(50.5, 26, 39, 26, pol='+', rad=0.0, color=c_coral)
    # 7. R2: Developer Fatigue -> Velocity (-)
    draw_cld_link(30, 31, 30, 50.5, pol='-', rad=0.0, color=c_coral, pol_offset=(-2.2, 0))
    # 8. R2: Velocity -> Deadline Pressure (-) [Drop in velocity increases pressure]
    draw_cld_link(30, 59.5, 30, 79, pol='-', rad=0.0, color=c_coral, pol_offset=(-2.2, 0))

    # Exogenous Inputs
    draw_cld_link(15, 84, 21, 84, pol='+', rad=0.0, color=c_amber)
    draw_cld_link(15, 80, 52, 31, pol='+', rad=0.25, color=c_amber, pol_pos=0.3)
    draw_cld_link(90, 79, 90, 60, pol='+', rad=0.0, color=c_purple, pol_offset=(2.0, 0))

    # Balancing Loop B1: Debt -> Sprint Debt Capacity (+) -> Debt (-)
    draw_cld_link(81.5, 55, 69.5, 55, pol='+', rad=0.0, color=c_green)
    draw_cld_link(65, 60, 81.5, 57, pol='-', rad=-0.35, color=c_green, pol_pos=0.5, pol_offset=(0, 1.8))

    # Balancing Loop B2 (FIXED LOGIC):
    # Fatigue increases the necessity/impulse to push back on scope (+)
    draw_cld_link(21, 26, 12, 50, pol='+', rad=-0.15, color=c_green, pol_pos=0.45)
    # Psychological Safety enables open pushback (+)
    draw_cld_link(8, 31, 8, 50, pol='+', rad=0.0, color=c_green, pol_offset=(2.0, 0))
    # Scope Pushback directly reduces Deadline Pressure (-)
    draw_cld_link(8, 60, 21, 82, pol='-', rad=-0.25, color=c_green, pol_pos=0.5, pol_offset=(-1.8, 0))

    # Center Loop Emblems
    ax.text(67, 70, "R1: Quick-Fix\nDebt Spiral\n(Reinforcing)", ha='center', va='center',
            fontsize=8.5, fontweight='bold', color=c_coral,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#fff1f2', edgecolor=c_coral, lw=1.2))
    ax.text(46, 43, "R2: Developer\nBurnout Trap\n(Reinforcing)", ha='center', va='center',
            fontsize=8.5, fontweight='bold', color=c_coral,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#fff1f2', edgecolor=c_coral, lw=1.2))
    ax.text(76, 44, "B1: Refactoring\nBuffer\n(Balancing)", ha='center', va='center',
            fontsize=8.0, fontweight='bold', color=c_green,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#ecfdf5', edgecolor=c_green, lw=1.2))
    ax.text(17, 43, "B2: Safety &\nPushback Brake\n(Balancing)", ha='center', va='center',
            fontsize=8.0, fontweight='bold', color=c_green,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#ecfdf5', edgecolor=c_green, lw=1.2))

    # Polarity Legend at bottom
    leg_box = patches.FancyBboxPatch(
        (10, 3.5), 80, 6.5, boxstyle="round,pad=0.4,rounding_size=0.8",
        facecolor='#f8fafc', edgecolor='#cbd5e1', linewidth=1.0
    )
    ax.add_patch(leg_box)
    ax.text(50, 7.0,
            "Causal Polarity: (+) Same direction change (increase causes increase)  |  (-) Opposite direction change (increase causes decrease)",
            ha='center', va='center', fontsize=6.8, fontweight='bold', color='#334155')
    ax.text(50, 4.8,
            "Loops: R1 = Quick-Fix Spiral  |  R2 = Burnout Trap  |  B1 = Sprint Debt Token Allocation  |  B2 = Scope Pushback (enabled by Psychological Safety)",
            ha='center', va='center', fontsize=6.5, color='#64748b')

    plt.tight_layout()
    plt.savefig('influence_model_cld.png', dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print('[*] Successfully regenerated clean, wider influence_model_cld.png with corrected B2 logic')

if __name__ == '__main__':
    draw_cld()
