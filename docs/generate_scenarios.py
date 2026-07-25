"""
Generate example pitch-calling prediction charts for the README.

Three worked scenarios. For each, we:
  1. Define the game state (pitcher averages, matchup, count, last pitch, timing).
  2. Score every available pitch using a deterministic model derived from the
     README rules (timing exploitation, count leverage, platoon, tunneling/
     movement separation, same-pitch repeat penalty).
  3. Render a figure: (left) top-5 recommendation bar chart, (right) 5x5 zone
     grid with the last pitch + recommended locations.

Charts are saved as PNGs in docs/scenarios/ and embedded in the README.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

# ---------- pitch reference (from README quick-reference table) ----------
REF = {
    # name: (velo, ivb, horz_armside_positive, spin, family)
    "4 Seam":  (94, +19, +8,  2300, "fastball"),
    "Sinker":  (92, +7,  +12, 2050, "fastball"),
    "Cutter":  (89, +11, -4,  2450, "fastball"),
    "Gyro":    (86, -4,  -6,  2550, "breaking"),
    "Sweeper": (84, +2,  -20, 2850, "breaking"),
    "Curve":   (78, -14, -9,  2550, "breaking"),
    "Split":   (87, +5,  +2,  1550, "offspeed"),
    "Change":  (84, +10, +13, 1650, "offspeed"),
}
PITCHES = list(REF.keys())

# location names on the 5x5 grid (col, row), catcher's view, row 0 = top
# inner 3x3 = cols/rows 1..3 (heart). outer ring = shadow/chase.
# "arm side" / "glove side" depend on pitcher hand; we map per-scenario.
def loc_name(col, row, batter_hand):
    # mirror horizontally for batter hand so "in/away" is from hitter perspective
    # col 0 = catcher's left, col 4 = catcher's right.
    # For RHH: away = catcher's left (col 0-1), in = catcher's right (col 3-4)
    # For LHH: away = catcher's right (col 3-4), in = catcher's left (col 0-1)
    h = batter_hand
    v = "Up" if row <= 1 else ("Down" if row >= 3 else "Mid")
    if h == "R":
        s = "In" if col >= 3 else ("Away" if col <= 1 else "Mid")
    else:
        s = "In" if col <= 1 else ("Away" if col >= 3 else "Mid")
    if v == "Mid" and s == "Mid":
        return "Middle Middle"
    if s == "Mid":
        return f"{v} & Middle"
    if v == "Mid":
        return f"Middle & {s}"
    return f"{v} & {s}"

def cell_intent(col, row):
    # in-zone (heart) => strike-eligible; ring => chase-eligible
    return "strike" if (1 <= col <= 3 and 1 <= row <= 3) else "chase"

# ---------- deterministic scoring model ----------
def score_pitch(pitch, avg, state):
    """Return (score, recommended_col, recommended_row, intent, reason)."""
    pvelo, pivb, phorz_as, pspin, fam = REF[pitch]
    a = avg.get(pitch, {})
    # use pitcher's entered avg if present, else reference defaults
    velo = a.get("velo") or pvelo
    ivb  = a.get("vert") if a.get("vert") is not None else pivb
    horz_as = a.get("horz") if a.get("horz") is not None else phorz_as  # arm-side positive

    balls, strikes = state["balls"], state["strikes"]
    pitcher_hand = state["pitcher_hand"]
    batter_hand  = state["batter_hand"]
    timing       = state["timing"]
    last_type    = state["last_type"]
    last_loc     = state["last_loc"]  # (col, row) or None

    score = 50.0  # baseline
    reasons = []

    # --- 1. count leverage: strike vs chase mix ---
    # pitcher's counts (0-2,1-2,0-1): favor chase (breaking/offspeed, ring)
    # hitter's counts (2-0,3-0,2-1,3-1,3-2): favor strike (in-zone, commanded)
    # neutral (0-0,1-1,2-2): best pitch, best loc
    is_pitchers_count = (strikes > balls) and (strikes >= 2 or (strikes == 1 and balls == 0))
    is_hitters_count  = balls > strikes or balls == 3
    if is_pitchers_count:
        if fam in ("breaking", "offspeed"):
            score += 8; reasons.append("chase pitch in pitcher's count")
        # expand location to ring (chase)
        chase_loc = True
    elif is_hitters_count:
        score += 5 if fam == "fastball" else 3
        reasons.append("must-throw-strike count")
        chase_loc = False  # need a strike
    else:
        chase_loc = None  # flexible

    # --- 2. timing exploitation ---
    # Early = cheating to velo -> slower same-tunnel (change/split/curve) or high FB
    # Late  = sitting soft -> harder elevated (4-seam up) or cutter hands
    # On Time -> change tunnel AND speed (opposite family)
    if timing == "early":
        if fam == "offspeed":
            score += 18; reasons.append("hitter early: offspeed in tunnel freezes them out front")
        elif pitch == "Curve":
            score += 14; reasons.append("hitter early: curve for timing freeze")
        elif pitch == "4 Seam":
            score += 8; reasons.append("hitter early: high FB makes them roll over / swing under")
        elif fam == "breaking":
            score += 4
    elif timing == "late":
        if pitch == "4 Seam":
            score += 18; reasons.append("hitter late: heater up blows by them")
        elif pitch == "Cutter":
            score += 12; reasons.append("hitter late: cutter on hands freezes/jams")
        elif fam == "offspeed":
            score -= 8; reasons.append("hitter late: avoid offspeed (they're sitting soft)")
    elif timing == "ontime":
        # must change family AND tunnel from last pitch
        if last_type:
            last_fam = REF[last_type][4]
            if fam != last_fam:
                score += 14; reasons.append("hitter on time: switch pitch family to reset tunnel")
            else:
                score -= 10; reasons.append("on time: same family is predictable")
        score -= 4  # they're locked in, be careful
    # unknown -> no timing adjustment

    # --- 3. platoon logic ---
    same_hand = (pitcher_hand == batter_hand)
    if same_hand:
        # breaking balls away/back-foot are great vs same-handed
        if fam == "breaking":
            score += 10; reasons.append("same-handed: breaker breaks away / back-foot (chase)")
        if pitch == "Change":
            score -= 4; reasons.append("same-handed: changeup less ideal")
    else:
        # opposite-handed: changeup (fade away), cutter (jam), sinker (front hip)
        if pitch == "Change":
            score += 10; reasons.append("opposite-handed: changeup fades off barrel")
        if pitch == "Cutter":
            score += 8; reasons.append("opposite-handed: cutter jams the hands")
        if pitch == "Sinker":
            score += 6; reasons.append("opposite-handed: sinker runs in on front hip")
        if fam == "breaking" and pitch not in ("Sweeper",):
            score -= 3; reasons.append("opposite-handed: breaker breaks into barrel")

    # --- 4. tunneling / movement separation from last pitch ---
    if last_type and last_type != pitch:
        lvelo, livb, lhorz, _, _ = REF[last_type]
        sep = np.hypot(ivb - livb, horz_as - lhorz)
        if sep > 25:
            score += 8; reasons.append(f"strong movement separation ({sep:.0f} in) vs last pitch")
        elif sep > 15:
            score += 4; reasons.append(f"good separation ({sep:.0f} in)")
        # velocity separation
        vsep = abs(velo - lvelo)
        if vsep > 10:
            score += 5; reasons.append(f"big velo gap ({vsep:.0f} mph)")
    elif last_type == pitch:
        # same-pitch repeat penalty unless hitter rolled over (we approximate: late on FB = ok repeat)
        if timing == "late" and pitch == "4 Seam":
            score += 6; reasons.append("repeat heater: hitter can't catch up, go back up")
        elif timing == "early" and fam in ("breaking", "offspeed"):
            score -= 10; reasons.append("repeat offspeed: hitter already sitting soft")
        else:
            score -= 6; reasons.append("same-pitch repeat: predictability cost")

    # --- 5. choose recommended location ---
    # default target logic by pitch family + count + platoon
    rec_col, rec_row = 2, 2  # fallback middle
    if pitch == "4 Seam":
        rec_col, rec_row = 2, 0  # up & middle (high IVB lives up)
    elif pitch == "Sinker":
        rec_col, rec_row = (1 if batter_hand == "R" else 3), 4  # down & arm-side
    elif pitch == "Cutter":
        rec_col, rec_row = (3 if batter_hand == "R" else 1), 2  # on the hands (in)
    elif pitch == "Gyro":
        # back-foot to same-handed; below zone to opposite
        if same_hand:
            rec_col, rec_row = (3 if batter_hand == "R" else 1), 4
        else:
            rec_col, rec_row = 2, 4
    elif pitch == "Sweeper":
        if same_hand:
            rec_col, rec_row = (1 if batter_hand == "R" else 3), 3  # off corner away / back foot
        else:
            rec_col, rec_row = (3 if batter_hand == "R" else 1), 3  # back door
    elif pitch == "Curve":
        rec_col, rec_row = 2, 4  # down, below zone for chase
    elif pitch == "Split":
        rec_col, rec_row = 2, 3  # knees, drops below
    elif pitch == "Change":
        rec_col, rec_row = (1 if batter_hand == "R" else 3), 4  # down & arm-side (fade away)

    # if hitter's count, pull location toward in-zone (strike)
    if is_hitters_count:
        rec_col = max(1, min(3, rec_col))
        rec_row = max(1, min(3, rec_row))
    # if pitcher's count, push to ring (chase) for breaking/offspeed
    if is_pitchers_count and fam in ("breaking", "offspeed"):
        rec_row = max(rec_row, 4)  # push down off zone

    intent = cell_intent(rec_col, rec_row)
    if is_pitchers_count and fam in ("breaking", "offspeed"):
        intent = "chase"
    if is_hitters_count:
        intent = "strike"

    locname = loc_name(rec_col, rec_row, batter_hand)
    return score, rec_col, rec_row, intent, locname, "; ".join(reasons) or "default"

def recommend(avg, state, top_n=5):
    out = []
    for p in PITCHES:
        if p not in avg or avg[p].get("velo") is None:
            # skip pitches the pitcher doesn't throw (sparse table)
            continue
        score, c, r, intent, locname, reason = score_pitch(p, avg, state)
        out.append({"type": p, "score": score, "col": c, "row": r,
                    "intent": intent, "locationName": locname, "reason": reason})
    out.sort(key=lambda x: -x["score"])
    return out[:top_n]

# ---------- chart rendering ----------
def render_scenario(state, avg, recs, title, outfile):
    fig = plt.figure(figsize=(13, 5.2))
    fig.patch.set_facecolor("#0d1117")
    gs = fig.add_gridspec(1, 2, width_ratios=[1.15, 1.0], wspace=0.28)

    # ---- left: recommendation bar chart ----
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.set_facecolor("#0d1117")
    names = [f"{r['type']}\n{r['locationName']}" for r in recs]
    scores = [r["score"] for r in recs]
    colors = ["#b6f09c" if r["intent"] == "strike" else "#f0b95c" for r in recs]
    y = np.arange(len(recs))[::-1]
    bars = ax1.barh(y, scores, color=colors, edgecolor="#2a3542", height=0.62)
    ax1.set_yticks(y)
    ax1.set_yticklabels(names, color="#e6edf3", fontsize=9)
    ax1.set_xlim(40, max(scores) + 18)
    ax1.set_xlabel("Recommendation score", color="#8b98a5", fontsize=10)
    ax1.tick_params(colors="#8b98a5")
    for sp in ax1.spines.values():
        sp.set_color("#2a3542")
    ax1.set_title(title, color="#e6edf3", fontsize=12, fontweight="bold", loc="left", pad=12)
    # score labels + tag
    for bar, r in zip(bars, recs):
        ax1.text(bar.get_width() + 1.2, bar.get_y() + bar.get_height()/2,
                 f"{r['score']:.0f}  [{r['intent'].upper()}]",
                 va="center", color=("#b6f09c" if r["intent"]=="strike" else "#f0b95c"),
                 fontsize=8.5, fontweight="bold")
    # legend
    ax1.text(0.99, 0.04, "STRIKE = in-zone  |  CHASE = off-zone",
             transform=ax1.transAxes, ha="right", color="#8b98a5", fontsize=8)

    # ---- right: zone grid with last pitch + recs ----
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.set_facecolor("#121922")
    ax2.set_xlim(-0.5, 4.5); ax2.set_ylim(-0.5, 4.5)
    ax2.set_aspect("equal")
    ax2.set_xticks([]); ax2.set_yticks([])
    for sp in ax2.spines.values():
        sp.set_color("#2a3542")
    # draw 5x5 cells
    for col in range(5):
        for row in range(5):
            inzone = (1 <= col <= 3 and 1 <= row <= 3)
            rect = patches.Rectangle((col-0.5, row-0.5), 1, 1,
                                     facecolor=("#1c242f" if inzone else "#161d26"),
                                     edgecolor=("#3b4a5c" if inzone else "#2a3542"),
                                     linewidth=1.4)
            ax2.add_patch(rect)
    # last pitch
    if state["last_loc"]:
        lc, lr = state["last_loc"]
        ax2.scatter([lc], [lr], s=240, marker="o", facecolor="#f5c451",
                    edgecolor="#0d1117", linewidth=1.5, zorder=5)
        ax2.text(lc, lr - 0.34, "LAST", ha="center", color="#f5c451", fontsize=7, fontweight="bold")
    # recommended locations (numbered)
    for i, r in enumerate(recs):
        ax2.scatter([r["col"]], [r["row"]], s=300, marker="o",
                    facecolor=("#b6f09c" if r["intent"]=="strike" else "#f0b95c"),
                    edgecolor="#0d1117", linewidth=1.5, zorder=6, alpha=0.92)
        ax2.text(r["col"], r["row"], str(i+1), ha="center", va="center",
                 color="#0d1117", fontsize=11, fontweight="bold", zorder=7)
    ax2.set_title("Last pitch (gold) + ranked recommendations",
                  color="#e6edf3", fontsize=10.5, fontweight="bold", loc="left", pad=12)
    # state annotation
    stxt = (f"{state['pitcher_hand']}HP vs {state['batter_hand']}HH  |  "
            f"Count {state['balls']}-{state['strikes']}  |  "
            f"Last: {state['last_type'] or '-'}  |  Timing: {state['timing'].title()}")
    fig.text(0.5, 0.965, stxt, ha="center", color="#8b98a5", fontsize=9)

    plt.subplots_adjust(top=0.88, bottom=0.10, left=0.16, right=0.97)
    fig.savefig(outfile, dpi=150, facecolor=fig.get_facecolor(), bbox_inches="tight")
    plt.close(fig)

# ---------- three example scenarios ----------
def main():
    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scenarios")
    os.makedirs(outdir, exist_ok=True)

    # Scenario 1: RHP vs LHH, 0-1, last 4-seam up-and-away, timing EARLY
    avg1 = {
        "4 Seam":  {"velo": 94, "vert": 19, "horz":  8},
        "Curve":   {"velo": 79, "vert": -20, "horz": -9},
        "Cutter":  {"velo": 85, "vert":  3, "horz": -3},
        "Sweeper": {"velo": 83, "vert": -3, "horz": -20},
        "Change":  {"velo": 84, "vert": 10, "horz": 13},
    }
    state1 = {"pitcher_hand":"R","batter_hand":"L","balls":0,"strikes":1,
              "last_type":"4 Seam","last_loc":(1,0),"timing":"early"}
    recs1 = recommend(avg1, state1)
    render_scenario(state1, avg1, recs1,
                    "Scenario 1: Hitter EARLY on a fastball up-and-away",
                    os.path.join(outdir, "scenario1.png"))
    print("Scenario 1 (RHP vs LHH, 0-1, early):")
    for r in recs1: print(f"  {r['type']:8s} {r['locationName']:16s} {r['intent']:6s} {r['score']:.0f}  [{r['reason']}]")

    # Scenario 2: LHP vs RHH, 2-1, last changeup down, timing ON TIME
    avg2 = {
        "4 Seam":  {"velo": 95, "vert": 18, "horz": -7},
        "Sinker":  {"velo": 92, "vert": 6,  "horz": -13},
        "Sweeper": {"velo": 82, "vert": 1,  "horz": 18},
        "Curve":   {"velo": 76, "vert": -15,"horz": 8},
        "Change":  {"velo": 84, "vert": 9,  "horz": -13},
        "Split":   {"velo": 86, "vert": 4,  "horz": -2},
    }
    state2 = {"pitcher_hand":"L","batter_hand":"R","balls":2,"strikes":1,
              "last_type":"Change","last_loc":(3,4),"timing":"ontime"}
    recs2 = recommend(avg2, state2)
    render_scenario(state2, avg2, recs2,
                    "Scenario 2: Hitter ON TIME on a changeup (locked in)",
                    os.path.join(outdir, "scenario2.png"))
    print("\nScenario 2 (LHP vs RHH, 2-1, on time):")
    for r in recs2: print(f"  {r['type']:8s} {r['locationName']:16s} {r['intent']:6s} {r['score']:.0f}  [{r['reason']}]")

    # Scenario 3: RHP vs RHH, 1-2, last sweeper back-foot, timing LATE
    avg3 = {
        "4 Seam":  {"velo": 97, "vert": 20, "horz": 7},
        "Sweeper": {"velo": 84, "vert": 2,  "horz": -19},
        "Gyro":    {"velo": 87, "vert": -3, "horz": -6},
        "Split":   {"velo": 88, "vert": 5,  "horz": 2},
        "Curve":   {"velo": 80, "vert": -13,"horz": -8},
    }
    state3 = {"pitcher_hand":"R","batter_hand":"R","balls":1,"strikes":2,
              "last_type":"Sweeper","last_loc":(3,4),"timing":"late"}
    recs3 = recommend(avg3, state3)
    render_scenario(state3, avg3, recs3,
                    "Scenario 3: Hitter LATE on a sweeper back-foot (sitting soft)",
                    os.path.join(outdir, "scenario3.png"))
    print("\nScenario 3 (RHP vs RHH, 1-2, late):")
    for r in recs3: print(f"  {r['type']:8s} {r['locationName']:16s} {r['intent']:6s} {r['score']:.0f}  [{r['reason']}]")

    print("\nCharts saved to docs/scenarios/")

if __name__ == "__main__":
    main()
