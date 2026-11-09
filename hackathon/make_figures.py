"""Three publication figures for the paper. Run: .venv/bin/python hackathon/make_figures.py
Data source: hackathon/sections/results-*.md (numbers hard-coded below, final and verified)."""
from math import sqrt
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = Path(__file__).resolve().parent / "figures"
OUT.mkdir(exist_ok=True)
BLUE, ORANGE, GREEN, GREY, INK = "#0072B2", "#E69F00", "#009E73", "#7F7F7F", "#1B2430"
plt.rcParams.update({
    "font.size": 10, "axes.labelsize": 10, "xtick.labelsize": 10, "ytick.labelsize": 10,
    "legend.fontsize": 10, "text.color": INK, "axes.labelcolor": INK, "xtick.color": INK,
    "ytick.color": INK, "figure.facecolor": "white", "savefig.facecolor": "white",
})


def wilson(k, n, z=1.96):
    """Wilson 95% interval for k of n, returned in percent (low, high)."""
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return 100 * max(0, c - h), 100 * min(1, c + h)


def style(ax):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.yaxis.grid(True, color="#E3E6EA", linewidth=0.8)
    ax.set_axisbelow(True)


def save(fig, name):
    fig.savefig(OUT / name, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- Figure 1
def fig1():
    W, H = 6.5, 3.5
    fig = plt.figure(figsize=(W, H))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")

    def box(x, y, w, h, text, fc="#F4F6F8", ec=INK):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.08",
                                    fc=fc, ec=ec, lw=1.2))
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=10, linespacing=1.15)

    def arrow(p, q, color=INK, ls="-", rad=0.0, lw=1.4):
        ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=12, color=color,
                                     lw=lw, ls=ls, connectionstyle=f"arc3,rad={rad}",
                                     shrinkA=0, shrinkB=0))

    by, bh, bw = 2.55, 0.9, 1.45
    xs = [0.05, 2.0, 3.95]
    box(xs[0], by, bw, bh, "Collector\n(script: the fault\nstarts here)", fc="#FBE9C2")
    box(xs[1], by, bw, bh, "Preparer\n(writes the draft)")
    box(xs[2], by, bw, bh, "Publisher\n(releases the\nrecord)")
    box(5.55, by, 0.9, bh, "System\ncheck\n(host)", fc="#CFE5F3", ec=BLUE)
    for i in range(2):
        arrow((xs[i] + bw + 0.03, by + bh / 2), (xs[i + 1] - 0.03, by + bh / 2))
        ax.text(xs[i] + bw + (xs[i + 1] - xs[i] - bw) / 2, by + bh / 2 + 0.08, "says:\ndone",
                ha="center", va="bottom", fontsize=10, linespacing=1.0)
    # database
    dy, dh = 0.95, 0.5
    box(0.05, dy, 6.4, dh, "Registry database (the actual state)", fc="#EEF0F3")
    # writes arrows
    for x in xs:
        cx = x + (1.1 if x == xs[2] else 0.35)
        arrow((cx, by - 0.03), (cx, dy + dh + 0.03))
        ax.text(cx + 0.07, dy + dh + 0.2, "writes", ha="left", va="center", fontsize=10)
    # checks (dashed) from Publisher
    px = xs[2]
    arrow((px + 0.6, by - 0.03), (xs[1] + 1.2, dy + dh + 0.03), ORANGE, "--", rad=0.0, lw=2)
    arrow((px + 0.25, by - 0.03), (xs[0] + 1.15, dy + dh + 0.03), GREEN, "--", rad=0.0, lw=2)
    arrow((6.0, by - 0.03), (6.0, dy + dh + 0.03), BLUE, "--", lw=2)
    handles = [
        Line2D([0], [0], color=ORANGE, ls="--", lw=2),
        Line2D([0], [0], color=GREEN, ls="--", lw=2),
        Line2D([0], [0], color=BLUE, ls="--", lw=2),
    ]
    labels = ["Check the last step: reads only the draft",
              "Check the whole chain: reads the draft and the source",
              "System check (host): compares every claim with the database"]
    ax.legend(handles, labels, loc="lower left", bbox_to_anchor=(0.0, 0.0), frameon=False,
              handlelength=2.6, borderaxespad=0.0, labelspacing=0.4)
    save(fig, "fig1_workflow.png")


# ---------------------------------------------------------------- Figure 2
def fig2():
    # source: hackathon/sections/results-*.md
    n = 120
    groups = ["No rule", "Rule: check\nthe last step", "Rule: check\nthe whole chain",
              "System check\n(by design)"]
    low = [112, 112, 27, 0]
    mid = [93, 120, 0, 0]
    fig, ax = plt.subplots(figsize=(6.5, 3.2))
    style(ax)
    bw = 0.4
    for series, off, color, lab in ((low, -bw / 2, ORANGE, "Three low-cost models"),
                                    (mid, bw / 2, BLUE, "Three mid-tier models")):
        for i, k in enumerate(series):
            pct = k / n * 100
            lo, hi = wilson(k, n)
            ax.bar(i + off, pct, bw, color=color, label=lab if i == 0 else None, zorder=2)
            ax.errorbar(i + off, pct, yerr=[[pct - lo], [hi - pct]], color=INK, capsize=3,
                        lw=1, capthick=1, zorder=3)
            ax.text(i + off + (0.11 if off > 0 else -0.11), hi + 1.5, f"{k}/{n}", ha="center", va="bottom", fontsize=10,
                    color=INK, zorder=4)
    ax.set_xticks(range(4)); ax.set_xticklabels(groups)
    ax.set_ylim(0, 100); ax.set_yticks(range(0, 101, 20)); ax.set_xlim(-0.6, 3.6)
    ax.set_ylabel("Workflows that released\nthe faulty record (%)")
    ax.tick_params(axis="x", length=0)
    ax.legend(loc="upper right", bbox_to_anchor=(1.0, 0.8), frameon=False)
    save(fig, "fig2_controls.png")


# ---------------------------------------------------------------- Figure 3
def fig3():
    # source: hackathon/sections/results-*.md
    n = 72
    xs = [0, 1, 2, 3]
    series = [
        ("No rule", GREY, "o", [7, 72, 72, 72], -0.07),
        ("Rule: check the last step", ORANGE, "s", [0, 72, 72, 72], 0.0),
        ("Rule: check the whole chain", GREEN, "^", [0, 3, 0, 0], 0.07),
    ]
    fig, ax = plt.subplots(figsize=(6.5, 3.2))
    style(ax)
    for lab, color, mk, ks, off in series:
        pct = [k / n * 100 for k in ks]
        ci = [wilson(k, n) for k in ks]
        yerr = [[p - c[0] for p, c in zip(pct, ci)], [c[1] - p for p, c in zip(pct, ci)]]
        ax.errorbar([x + off for x in xs], pct, yerr=yerr, color=color, marker=mk, ms=6,
                    lw=1.8, capsize=3, elinewidth=1.2, label=lab, zorder=3)
    ax.set_xlim(-0.35, 3.35); ax.set_ylim(-6, 106); ax.set_yticks(range(0, 101, 20))
    ax.set_xticks(xs)
    ax.set_xticklabels(["0\n(fault in the\nrecord it received)", "1", "2", "3"])
    ax.set_xlabel("Steps between the worker's input and the fault")
    ax.set_ylabel("Workflows where the worker\nbuilt on the fault (%)")
    ax.tick_params(axis="x", length=0)
    ax.legend(loc="center right", bbox_to_anchor=(1.0, 0.5), frameon=False)
    save(fig, "fig3_distance.png")


if __name__ == "__main__":
    fig1(); fig2(); fig3()
