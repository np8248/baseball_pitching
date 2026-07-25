# Baseball Pitching Reference

A research-backed guide to baseball pitching, pitch calling, and player data. Covers the 8 pitch types in modern arsenals, hitter timing and how to exploit it, count leverage, platoon splits, the strike zone and chase regions, pitch sequencing and tunneling, and the Statcast/metric vocabulary used to evaluate pitchers and hitters.

Movement and velocity values are MLB averages synthesized from Statcast/Baseball Savant, Rapsodo, Trackman/Hawk-Eye, FanGraphs, Baseball Prospectus, Driveline, and pitch-design literature (2025-2026).

---

## Table of Contents

1. [How movement is measured](#how-movement-is-measured)
2. [The 8 pitches](#the-8-pitches)
3. [Quick reference table](#quick-reference-the-8-pitches)
4. [Hitter timing: early, late, on time, and how to exploit it](#hitter-timing-early-late-on-time-and-how-to-exploit-it)
5. [Count leverage: what to throw in every count](#count-leverage-what-to-throw-in-every-count)
6. [Platoon splits: handedness matchups](#platoon-splits-handedness-matchups)
7. [The strike zone and chase regions](#the-strike-zone-and-chase-regions)
8. [Pitch sequencing and tunneling](#pitch-sequencing-and-tunneling)
9. [Player data: Statcast metrics explained](#player-data-statcast-metrics-explained)
10. [Pitcher evaluation metrics: Stuff+, Location+, Pitching+](#pitcher-evaluation-metrics-stuff-location-pitching)
11. [Sources](#sources)

---

## How movement is measured

Two numbers define a pitch's shape, both in **inches**:

- **Vert (Induced Vertical Break, IVB)** - how much the pitch resists gravity versus a spinless ball. Positive = "rise" (falls less than expected, like a 4-seam). Negative = extra drop (like a curveball). Gravity is removed, so this is pure spin effect. League-average 4-seam IVB is ~15-16 in; elite is 19-21 in.
- **Horz (Horizontal Break)** - side-to-side movement. **Sign convention:** positive = arm-side run, negative = glove-side break, from the catcher's view. For a RHP, arm-side is to the catcher's right; for a LHP, arm-side is to the catcher's left. A RHP's 4-seam (Horz +8) runs arm-side; a RHP's sweeper (Horz -20) breaks glove-side. The sign flips with pitcher handedness for the same physical movement.

> Coaches entering numbers from Rapsodo / Trackman / Hawk-Eye are entering IVB (not raw drop) and Horz in this arm-side-positive convention.

**Vertical Approach Angle (VAA)** is a third, related metric: the angle at which the pitch enters the zone. MLB average 4-seam VAA is ~-4.4 degrees. Flatter (closer to -3.7) is elite for fastballs at the top of the zone; steeper is better for breaking balls below the zone. VAA is driven by release height and extension.

### Plain-English glossary (the jargon, explained simply)

| Term | What it actually means |
| --- | --- |
| **IVB / Vert** | "How much the spin fights gravity." A high positive number = the ball looks like it rises (really: falls less than expected). A negative number = the ball drops extra. Measured in inches. |
| **Horz** | "How much the ball moves sideways." Positive = toward the pitcher's throwing-arm side. Negative = toward the glove side. Measured in inches. |
| **VAA** | "The angle the ball comes in at." Flat (close to 0) = comes in level, hard to hit at the top. Steep (more negative) = comes in diving down, hard to hit at the bottom. |
| **Arm side** | The side of the pitcher's throwing arm (a righty's arm side is to the catcher's right). |
| **Glove side** | The side of the pitcher's glove (a righty's glove side is to the catcher's left). |
| **Spin rate (rpm)** | How fast the ball spins, in revolutions per minute. More spin usually = more movement, but only if the spin is the right kind. |
| **Spin axis** | The direction the ball is spinning around. Like a clock face: 12:00 = pure backspin (fastball), 6:00 = pure topspin (curveball), 3:00/9:00 = pure sidespin (sweeper). |
| **Spin efficiency** | How much of the spin actually creates movement vs. being "wasted." 100% = all spin moves the ball. Near 0% = bullet spin (gyro slider), barely moves from spin. |
| **Magnus force** | The force that makes a spinning ball curve through the air. Backspin pushes it up (fights gravity), topspin pushes it down, sidespin pushes it sideways. |
| **Backspin** | Spinning backward (top of the ball moving away from the throw). Creates upward Magnus force - the "rise" of a fastball. |
| **Topspin** | Spinning forward (top of the ball moving toward the throw). Creates downward Magnus force - the drop of a curveball. |
| **Sidespin** | Spinning sideways. Creates horizontal break - the sweep of a sweeper or run of a sinker. |
| **Gyro / bullet spin** | Spinning like a football spiral (point-first). Almost no Magnus force, so almost no movement from spin - the pitch moves from seam effects instead. |
| **Seam-shifted wake** | The seams on the ball push air unevenly, creating extra movement the spin alone wouldn't predict. Why some sinkers/sliders "jump" late. |
| **Tunnel / tunneling** | Two pitches that look identical out of the hand and share the same flight path until late, then diverge. The hitter can't tell which is which until it's too late to adjust. |
| **Extension** | How far toward home plate the pitcher releases the ball. More extension = less distance for the hitter = effectively faster. |
| **Chase** | Getting the hitter to swing at a pitch outside the strike zone. |
| **Whiff** | A swing-and-miss. |
| **Platoon** | A handedness matchup (LHP vs RHH, etc.). "Platoon advantage" = hitter facing an opposite-handed pitcher. |

---

## The 8 pitches

### 1. Four-Seam Fastball (4 Seam)

| Metric | Typical MLB Range |
| --- | --- |
| Velocity | 92-101 mph (avg ~94) |
| Vert (IVB) | +15 to +21 in (avg 15-16, elite 19-21) |
| Horz | +2 to +8 in arm-side |
| Spin Rate | 2200+ rpm |
| Spin axis | Pure backspin (12:00-2:00 for RHP, 10:00-12:00 for LHP), high spin efficiency |

**How it works:** Backspin generates an upward Magnus force that fights gravity. The ball does not literally rise - it falls *less* than the hitter's brain predicts from the early flight path, so it arrives higher than expected. Elite IVB (19+) at the top of the zone generates swing-and-miss because hitters swing underneath it.

**In plain English:** This is the basic straight fastball - the fastest pitch, thrown as hard as you can with backspin so it cuts through the air. It doesn't actually rise (nothing can, physics says so), but because it's spinning backward it fights gravity and "falls less" than the hitter expects, so it looks like it jumps up at the last second. The harder the spin and the higher you throw it, the more hitters swing under it.

**Where to throw it:** Top of the zone, at the letters. The higher the IVB, the higher you can live. Avoid the middle-bottom of the zone where the "rise" advantage disappears. Best tunnel partner is a curveball (vertical contrast) or changeup (timing disruption).

---

### 2. Sinker / Two-Seam Fastball (Sinker)

| Metric | Typical MLB Range |
| --- | --- |
| Velocity | 90-97 mph (avg ~93) |
| Vert (IVB) | +4 to +10 in |
| Horz | +8 to +14 in arm-side run |
| Spin Rate | 2000+ rpm |
| Spin axis | Sidespin/topspin, lower efficiency than 4-seam |

**How it works:** Fingers aligned along the two seams generate sidespin, producing both downward and arm-side horizontal movement. The pitch arrives lower and further to the arm side than a 4-seam from the same release. The best sinkers add **seam-shifted wake** (asymmetric airflow from seam orientation), adding 6-9 in of extra drop beyond what spin predicts - the "heavy" feel.

**In plain English:** A slower, "heavier" fastball that drops and runs to one side instead of staying straight. You grip it along two seams instead of four, so it spins sideways and sinks down + sideways as it reaches the plate. Hitters hit it into the ground (ground balls) instead of hitting it in the air - that's the whole point. It's not a strikeout pitch, it's a "get me a weak grounder for a double play" pitch.

**Where to throw it:** Down and to the arm side, especially on the corners. The goal is ground balls, not whiffs. Aim at the front hip of an opposite-handed hitter to jam them, or just off the plate arm-side to induce weak rollover contact. Pairs with a slider/sweeper for arm-side/glove-side contrast.

---

### 3. Cutter / Cut Fastball (Cutter)

| Metric | Typical MLB Range |
| --- | --- |
| Velocity | 88-95 mph (2-5 mph below the 4-seam) |
| Vert (IVB) | +8 to +14 in |
| Horz | -2 to -6 in glove-side |
| Spin Rate | 2400+ rpm |
| Spin axis | Slight gyro shift off a 4-seam, mostly backspin with a touch of sidespin |

**How it works:** Slight off-center fingertip pressure shifts the spin axis just enough to move the pitch glove-side with less IVB than a 4-seam. It looks like a fastball out of the hand, then cuts late across the plate. Mariano Rivera made it the most dominant single pitch in history; Corbin Burnes built a Cy Young arsenal around it.

**In plain English:** A fastball that veers slightly to the side (toward the pitcher's glove) instead of going straight. It's halfway between a fastball and a slider - fast enough to look like a fastball out of your hand, but it darts a few inches sideways just before the plate, jamming hitters and breaking bats. Not as fast as a 4-seam, not as slow/breaky as a slider - the "in between" pitch.

**Where to throw it:** On the hands of opposite-handed hitters (a RHP's cutter runs into a LHH's hands, breaking bats and producing weak contact). Also effective on the outside corner to same-handed hitters for called strikes. Pairs with the 4-seam (same tunnel, different late movement).

---

### 4. Gyro Slider (Gyro)

| Metric | Typical MLB Range |
| --- | --- |
| Velocity | 83-89 mph |
| Vert (IVB) | -2 to -6 in (slight drop) |
| Horz | -3 to -8 in glove-side |
| Spin Rate | 2400-2700 rpm |
| Spin axis | Bullet/gyro spin (spin axis nearly aligned with flight direction), very low spin efficiency |

**How it works:** A gyro slider (sometimes called a "bullet spin" slider) has its spin axis pointing almost directly at the target, so the Magnus force is minimal and the ball moves very little from spin. Its deception comes from **seam-shifted wake**: the asymmetric seam orientation creates pressure differential late in flight, producing a sharp, late, shorter break than a sweeper. It tunnels exceptionally well off a fastball because the early flight path is nearly identical. Near-zero spin efficiency is the defining trait (vs. a sweeper's high-efficiency side spin).

**In plain English:** A slider that barely spins usefully - the ball spins like a bullet flying forward (point-first), so the spin doesn't really push it anywhere. Instead, the seams on the ball catch the air unevenly late in flight, making it dart sharply at the last second. It looks just like a fastball for most of its path, then jumps a few inches. It's the "sneaky late break" slider - shorter and sharper than a sweeper, great for fooling hitters who already committed to a fastball.

**Where to throw it:** Back-foot to same-handed hitters (a RHP's gyro slider ends at a RHH's back foot) for chase, or just below the zone for swing-and-miss. The late, compact break makes it hard to identify and square up. Pairs with a high-IVB 4-seam for tunnel + late divergence.

---

### 5. Sweeper (Sweeper)

| Metric | Typical MLB Range |
| --- | --- |
| Velocity | 80-88 mph |
| Vert (IVB) | 0 to +4 in (minimal) |
| Horz | -16 to -22 in glove-side (elite up to -24) |
| Spin Rate | 2800+ rpm |
| Spin axis | Nearly pure gyroscopic/side spin, high spin efficiency |

**How it works:** The signature pitch of the 2020s. Nearly pure side spin produces extreme horizontal movement with minimal vertical drop - it sweeps across the zone from arm side to glove side. Popularized by the Dodgers and Yankees; Adam Ottavino, Shohei Ohtani, Yu Darvish, and Nestor Cortes are the prominent practitioners. Against same-sided hitters it exits the zone entirely for chase; against opposite-handed hitters it breaks across the plate as a strike.

**In plain English:** A slider that moves SIDEWAYS a lot instead of down. Think of it as a "wide slider" - it breaks 16-22 inches to the pitcher's glove side, sweeping across the plate like a broom. To a same-handed hitter it starts over the plate then sweeps off the outside corner (they chase it and miss); to an opposite-handed hitter it sweeps back over the corner for a strike. It's the trendiest pitch in baseball because it gets swings-and-misses on pitches outside the zone.

**Where to throw it:** Off the outside corner to same-handed hitters (the pitch chases them out of the zone), or back-foot for swing-and-miss. Against opposite-handed hitters, the back door or back foot. Pairs with a 4-seam for horizontal contrast - hitters must defend the full width of the zone on every pitch.

---

### 6. Curveball (Curve)

| Metric | Typical MLB Range |
| --- | --- |
| Velocity | 73-84 mph |
| Vert (IVB) | -10 to -16 in (sharp drop) |
| Horz | -6 to -12 in glove-side |
| Spin Rate | 2500+ rpm |
| Spin axis | Topspin (12-to-6 for a 12-6 curve), high efficiency |

**How it works:** The oldest breaking ball. 12-to-6 topspin generates a sharp downward Magnus force, so the ball drops well below where a spinless pitch would land. A good curve from a high release can drop 14-16 in. The big arc gives hitters more time to identify it, so release-point consistency and tunnel quality separate elite from hittable curves.

**In plain English:** The classic "drop off the table" pitch. You spin it forward (topspin) so it dives straight down - imagine the ball dropping from 12 o'clock to 6 o'clock on a clock face. It's much slower than a fastball (often 15+ mph slower), with a big looping arc that drops sharply at the end. Hitters swing over the top of it. It's slower and "loopier" than a slider, so hitters have more time to see it coming - that's why it has to be thrown with the exact same arm motion as your fastball or they'll know it's coming.

**Where to throw it:** Below the zone for swing-and-miss (the "get me over" version is middle-middle for a called strike early in the count). The 0-0 or 1-0 get-ahead curve is a staple. Back-foot to same-handed hitters for chase. Pairs with a high-IVB 4-seam for the maximum vertical contrast (19 in up vs. -16 in down).

---

### 7. Splitter / Split-Finger Fastball (Split)

| Metric | Typical MLB Range |
| --- | --- |
| Velocity | 85-91 mph (8-12 mph below the 4-seam) |
| Vert (IVB) | +2 to +8 in (but 6-10 in more drop than a 4-seam from same release) |
| Horz | minimal, slight arm-side |
| Spin Rate | 1400-1700 rpm (low) |
| Spin axis | Reduced backspin, near-zero efficiency |

**How it works:** Fingers spread wide on either side of the ball strip away backspin. The pitch starts on a fastball plane (same arm speed, same release) then drops sharply below the zone - 6-10 in more than a 4-seam from the same release. The late drop after the tunnel point is the primary weapon. Paul Skenes's "splinker" (splitter-sinker hybrid) is the modern benchmark. Long a NPB staple, it swept MLB in the 2020s.

**In plain English:** A pitch that looks exactly like a fastball out of your hand but suddenly drops straight down right before the plate. You grip it with your fingers split wide apart on the sides of the ball, which kills the spin, so gravity takes over and it "falls off a cliff." Hitters swing where they think the fastball is going to be, and the ball drops under their bat. It's slower than a fastball but faster than a changeup, and the whole trick is the late downward drop.

**Where to throw it:** Just below the zone, starting at the knees. The hitter commits to a fastball path and swings over the top of it. Effective in pitcher's counts (0-2, 1-2) for chase, and as a surprise first-pitch strike. Pairs with a 4-seam for the fastball/splitter tunnel.

---

### 8. Changeup (Change)

| Metric | Typical MLB Range |
| --- | --- |
| Velocity | 82-90 mph (8-12 mph below the 4-seam) |
| Vert (IVB) | +6 to +14 in (fades, less IVB than a 4-seam) |
| Horz | +10 to +16 in arm-side fade |
| Spin Rate | 1500-1800 rpm |
| Spin axis | Reduced backspin vs. fastball, some sidespin |

**How it works:** The most tunnel-dependent pitch in baseball. Thrown with fastball arm speed but a grip that reduces backspin (ball deeper in the hand), it arrives 8-12 mph slower. The hitter commits to a fastball-speed prediction and the bat arrives early. Late arm-side fade adds a second deception layer. Three main grips: **circle change** (max arm-side fade/depth), **palmball** (lower spin, similar fade), **vulcan** (split middle/ring fingers for tumbling action).

**In plain English:** A "slow fastball" - you throw it with the exact same arm motion as your fastball, but a special grip (usually the circle change, making an "OK" sign with your thumb and index finger) makes the ball come out 8-12 mph slower. The hitter sees fastball arm speed and swings as if it's a fastball, but the ball is late, so they swing way out in front of it. It also drifts slightly to the side (arm-side fade). The whole point is fooling their TIMING, not their eyes - it only works if it looks identical to your fastball coming out of your hand.

**Where to throw it:** Down and arm-side, mirroring the 4-seam tunnel. Best counts: 1-0, 2-1, 3-2 (especially after a missed fastball), and any hitter's count where the hitter is timing the heater. Against opposite-handed hitters it fades away from the barrel. Useless without a convincing fastball tunnel - a changeup with no tunnel is just a slow pitch.

---

## Quick reference: the 8 pitches

| Pitch | Velo (mph) | Vert/IVB (in) | Horz (in) | Spin (rpm) | Primary goal |
| --- | --- | --- | --- | --- | --- |
| 4 Seam | 92-101 | +15 to +21 | +2 to +8 (AS) | 2200+ | Whiffs at top of zone |
| Sinker | 90-97 | +4 to +10 | +8 to +14 (AS) | 2000+ | Ground balls |
| Cutter | 88-95 | +8 to +14 | -2 to -6 (GS) | 2400+ | Weak contact / jams |
| Gyro | 83-89 | -2 to -6 | -3 to -8 (GS) | 2400-2700 | Late compact chase |
| Sweeper | 80-88 | 0 to +4 | -16 to -22 (GS) | 2800+ | Horizontal chase |
| Curve | 73-84 | -10 to -16 | -6 to -12 (GS) | 2500+ | Vertical drop whiffs |
| Split | 85-91 | +2 to +8 | minimal | 1400-1700 | Late drop tunnel |
| Change | 82-90 | +6 to +14 | +10 to +16 (AS) | 1500-1800 | Timing disruption |

*AS = arm-side, GS = glove-side. Horz sign is from the catcher's view, positive = arm-side.*

---

## Hitter timing: early, late, on time, and how to exploit it

Hitters don't *react* to a pitch at contact - they **commit** ~175 ms after release, about 23.8 ft from the plate. The brain takes release height, arm angle, spin direction, and early trajectory, builds a prediction of where the ball will cross the plate and *when*, and launches the swing to intersect that prediction. The hitter is locked in before the ball is halfway home. Pitchers win when the ball ends up somewhere different than the prediction.

This is the foundation of the PitchCall timing input (Early / Late / On Time / Unknown). Timing tells you *what kind of prediction error the hitter just made*, which tells you what to exploit next.

### What each timing signal means

- **Early** - the hitter's bat arrived ahead of the pitch. They read it as faster than it was, or as a fastball when it was offspeed. They are *cheating* to velocity or jumping on the first thing they see. Their swing plane is too flat/steep for the actual pitch, producing weak contact or whiffs out in front.
- **Late** - the hitter's bat arrived behind the pitch. They read it as slower than it was, or as offspeed when it was a fastball. They are *sitting soft* or their bat speed / reaction is a half-step slow. They make contact deeper, often hooking the ball or topping it.
- **On Time** - the hitter's prediction matched. They squared it up. This is the *worst* outcome for the pitcher; the hitter has your timing. You must disrupt it on the next pitch.
- **Unknown** - no swing, or a take. No timing signal. Default to count-based logic.

### The exploitation logic (what to throw next)

| Last pitch timing | Hitter is... | Best next move | Why |
| --- | --- | --- | --- |
| **Early** | cheating to velo / out in front | **Slower, same tunnel.** Changeup, splitter, curveball. Or repeat the heater up to make them roll over. | Their brain is calibrated fast. Anything slower, on a fastball tunnel, makes them swing way out in front. A high-IVB fastball up also works - they'll swing under it. |
| **Late** | sitting soft / bat behind | **Harder, elevated, or opposite tunnel.** 4-seam up, or a hard gyro/cutter on the hands. | Their brain is calibrated slow. A fastball (especially up) will blow by them. A cutter on the hands freezes or breaks their bat. Avoid another offspeed - they're already waiting for it. |
| **On Time** | locked in | **Change the tunnel and the speed.** Go opposite family (fastball to breaking, or breaking to fastball) and change the elevation. Avoid the middle of the zone. | They have your timing and your tunnel. You must reset both. A pitch from a different movement family at a different height forces a new prediction. |
| **Unknown** | took the pitch | **Count-based.** If ahead, expand for chase. If behind, attack the zone. | No timing info, so default to leverage. |

### The physics of the timing error

A league-average fastball travels from release to mitt in ~400 ms; the swing takes ~100 ms. The decision window is ~50 ms. A changeup that's 10 mph slower than the fastball adds roughly **30-40 ms** of flight time - enough that a hitter committed to the fastball speed swings ~6-8 in *in front of* where the ball actually is. That's why the changeup's value is almost entirely in the fastball tunnel, not the raw movement.

**Attack Angle** (Statcast bat tracking, 2024+) measures the upward angle of the swing path. Hitters match their attack angle to the pitch's descent. A high-IVB fastball with a flat VAA (-3.7 degrees) arrives on a plane the hitter's slightly-upward attack angle can't intersect cleanly at the top of the zone - they swing underneath. A curveball with a steep VAA (-9 degrees) arrives on a plane their flat attack angle can't intersect at the bottom - they swing over it. Timing errors and attack-angle mismatches compound: being early on a high fastball means the bat is both too far in front *and* too low.

---

## Count leverage: what to throw in every count

The count is the single most important pitch-selection input. Every added ball helps the hitter; every added strike helps the pitcher. The effect is large and measurable:

- **AVG by count:** batters hit ~.166 after falling behind 0-2 and ~.289 after going ahead 2-0 (Statcast, 2017). Adding a ball, for a fixed strike count, raises AVG by ~17-18 points.
- **Run value:** 0-0 is neutral (0). 0-2 is about -0.13 runs (huge pitcher edge). 3-0 is about +0.11 runs (huge hitter edge). The leverage of a count = the difference between the run value if the next pitch is a strike vs. a ball. 2-0 has the highest leverage (~0.16); 0-0 is lowest (~0.07).
- **HR rate on balls in play** rises with each added ball and falls with each added strike.

### Pitcher's counts vs. hitter's counts

| Count | Type | Run value (approx) | Intent |
| --- | --- | --- | --- |
| 0-2 | Pitcher | -0.13 | Expand; chase pitch below/away. No fastballs middle. |
| 1-2 | Pitcher | -0.11 | Expand; put-away breaker. Fastball up to open the zone. |
| 0-1 | Pitcher | -0.10 | Get-ahead; can expand slightly. Any pitch with zone contact risk OK. |
| 2-2 | Neutral/slight pitcher | -0.12 | Best pitch in best location. High whiff pitch. |
| 1-1 | Neutral | -0.06 | The "swing count." Sets the tone for the rest of the AB. |
| 0-0 | Neutral | 0.00 | Establish. Get-ahead pitch (often fastball or get-over curve). |
| 2-1 | Hitter | -0.02 | Must throw strike; hitter looking to damage. Use your best pitch. |
| 3-2 | Hitter | +0.03 | Must throw strike; hitter can't sit soft only. Fastball or tunnel split/change. |
| 2-0 | Hitter | +0.00 | Hitter locked in; pitcher must throw strike. Avoid middle. |
| 1-0 | Hitter | -0.04 | Hitter ahead; be careful but don't fall further behind. |
| 3-1 | Hitter | +0.15 | Hitter's count; fastball expected but offspeed usage rising. |
| 3-0 | Hitter | +0.11 | Take likely; if green light, hitter is teeing off. Must be a strike. |

### Modern usage shifts (2020s)

The old "fastball in hitter's counts" rule is dying. From 2015 to 2021, fastball usage fell from 57.7% to 50.9% league-wide, and **offspeed usage in hitter's counts climbed steadily**. In high-leverage spots, pitchers now throw offspeed in 2-1 and 3-1 counts far more than they did a decade ago. Ryan Zimmerman's quote captures it: "There's no such thing as a fastball count now." The principle: if you can command your secondary, *be unpredictable in the counts the hitter expects a heater*. The cost of predictability is higher than the cost of a missed breaker.

### Practical rules of thumb

- **0-0:** Establish the fastball or a get-over curve. First-pitch strikes are worth ~0.10 runs.
- **0-1 / 0-2 / 1-2:** Expand. Chase pitches (sweeper back-foot, splitter below, curve in the dirt). Avoid the heart of the zone - a 0-2 fastball middle is a mistake.
- **1-1:** The true swing count. Whatever wins this count shapes the rest of the AB. Throw your best pitch.
- **2-0 / 2-1 / 3-0 / 3-1 / 3-2:** Must-throw-strike counts. Use your most-commanded pitch for a strike, ideally at the edges. In 3-ball counts, a tunnel split or changeup is effective because the hitter can't afford to take but is calibrated to the fastball.
- **Even counts (1-1, 2-2):** Best pitch, best location. No free passes.

---

## Platoon splits: handedness matchups

Platoon splits are the most persistent and predictive splits in baseball. The rule: **hitters perform better against opposite-handed pitchers** (RHH vs LHP, LHH vs RHP). The effect is larger for left-handed hitters (the "lefty-lefty" penalty is famously steep).

2025 wRC+ reference (league):
- LHB vs LHP: ~86 (big penalty)
- LHB vs RHP: ~108 (advantage)
- RHB vs LHP: ~104 (mild advantage)
- RHB vs RHP: ~99 (near neutral)

### Why it happens

1. **Visual angle:** a same-handed pitcher's release is on the same side as the hitter's open stance, making the ball harder to pick up early.
2. **Movement direction:** breaking balls from a same-handed pitcher break *away* from the hitter (harder to chase productively and harder to pull) OR, for back-foot sliders/sweepers, break *into* the hitter's back foot (chase-inducing). Breaking balls from an opposite-handed pitcher break *into* the hitter's barrel path (easier to pull, more damage).
3. **Platoon advantage compounds with pitch type:** sweepers/sliders are devastating against same-handed hitters (chase); changeups are devastating against opposite-handed hitters (fade away from barrel).

### Pitch-by-matchup guide

| Pitcher | Hitter | Best pitches | Why |
| --- | --- | --- | --- |
| RHP | LHH | Changeup (fade away), cutter (jams), sinker (front hip), sweeper back-door | Changeup fades away from LHH barrel; cutter runs into hands; sinker jams. Avoid sweepers middle (LHH pulls them). |
| RHP | RHH | Sweeper/gyro back-foot, curveball down, 4-seam up | Breaking balls break away from RHH (chase) or into back foot. High-IVB fastball up is a swing-under pitch. |
| LHP | RHH | Changeup (fade), sinker (front hip), sweeper back-foot (LHP sweepers break into RHH) | Mirror of RHP/LHH. Changeup is the workhorse offspeed. |
| LHP | LHH | Sweeper/gyro back-foot, curveball down, 4-seam up | Same-handed: use the chase breaking ball away and the high fastball. The lefty-lefty penalty helps you. |

**General platoon rules:**
- **Fastballs** are roughly platoon-neutral; their value doesn't swing much with handedness.
- **Breaking balls (sweeper, gyro, slider, curve)** are best against **same-handed** hitters (chase, back-foot).
- **Changeups** are best against **opposite-handed** hitters (fade away from barrel).
- **Cutters** are great against **opposite-handed** hitters (jams them, weak contact).
- **Splitters** are roughly platoon-neutral (the drop, not the horizontal, is the weapon).

---

## The strike zone and chase regions

### Rulebook zone

- **Plate width:** 17 inches. Ball diameter ~2.86-2.94 in. A pitch is a strike if any part of the ball crosses any part of the plate's horizontal projection, so the effective width is ~17 + ~2.9 = **~20 in (1.67 ft)**.
- **Vertical zone:** top = the midpoint between the batter's shoulders and the top of the uniform pants; bottom = the hollow beneath the kneecap (per the official rule). Typical MLB zone: ~1.5 ft (bottom, hollow beneath kneecap) to ~3.5 ft (top) for an average hitter. **Scales with hitter height** - tall hitters have a taller zone.
- **MLB umpire zone has tightened** over the Statcast era (smaller, more rulebook-accurate), per FanGraphs tracking.

### Statcast's 4 Attack Regions (the modern zone model)

Baseball Savant splits the area around the plate into four regions for the Swing/Take metric:

| Region | Location | Run value |
| --- | --- | --- |
| **Heart** | Middle of the zone (roughly the inner 3x3) | Highest run value for hitters if taken; pitchers must avoid |
| **Shadow** | The edges - 1 ball width around the heart (the "chase" ring) | Where the pitcher-hitter duel is actually decided; called-strike and swing-and-miss rates peak here |
| **Chase** | Further off the plate (1-2 ball widths out) | Hitters should take; pitchers want swings here |
| **Waste** | Way off the plate | Auto-take; any swing is a pitcher win |

### Why the Shadow is where the game is won

The Shadow region (just off the edges) is where:
- **Called-strike probability** is highest for pitches that *look* like strikes but barely aren't.
- **Swing-and-miss rate** peaks - hitters swing at Shadow pitches they can't square up.
- **Run value of a take vs. a swing** is most volatile - a take can be a ball or a called strike; a swing is usually weak contact or a whiff.

This is why the PitchCall 5x5 grid uses an inner 3x3 (Heart/STRIKE-eligible) and an outer ring (Shadow/CHASE-eligible). Chase pitches should *start* in the zone and *finish* out of it (a sweeper that begins on the corner and exits off the plate), not start already off (that's a waste pitch a hitter simply takes).

### Named locations (RHH perspective; mirror for LHH)

Using the 5x5 grid (cols 0-4 left-to-right from catcher view, rows 0-4 top-to-bottom; inner 3x3 = cols/rows 1-3):

| Name | Grid cell | Type |
| --- | --- | --- |
| Up & In | row 0, col 3 (RHH) / col 1 (LHH) | Shadow/STRIKE-ish |
| Up & Away | row 0, col 1 (RHH) / col 3 (LHH) | Shadow |
| Up & Middle | row 0, col 2 | Shadow top |
| Middle Middle | row 2, col 2 | Heart (avoid) |
| Down & Away | row 4, col 1 (RHH) / col 3 (LHH) | Shadow/Chase - best whiff location |
| Down & In | row 4, col 3 (RHH) / col 1 (LHH) | Shadow - back-foot breaker |
| Letters (high) | row 0-1, col 2 | Where high-IVB fastballs live |
| Knees (low) | row 3-4, col 2 | Where sinkers/curves/splitters live |

> **Mirroring:** for a LHH, "in" and "away" flip. A pitch that's "down & away" to a RHH is on the catcher's left; to a LHH it's on the catcher's right. The code must mirror location names by batter handedness.

---

## Pitch sequencing and tunneling

A pitch is only as good as what it tunnels off. **Tunneling** = two pitches sharing the same early flight path, then diverging after the hitter's ~175 ms decision window closes (about 23.8 ft from the plate, per Baseball Prospectus). Greg Maddux described it as "a column of milk" - all his pitches looking identical until it was too late to adjust.

### The classic tunnel pairs

| Primary | Secondary | Why it works |
| --- | --- | --- |
| 4-seam (high IVB, up) | Curveball (steep drop, down) | Maximum vertical contrast (+19 in up vs. -16 in down). Same arm path, late divergence. |
| 4-seam (up) | Changeup (down, arm-side fade) | Timing disruption - same path, 10 mph slower. Hitter commits early, bat arrives in front. |
| 4-seam (up) | Sweeper (glove-side sweep) | Horizontal contrast - hitter must defend full width of zone. |
| Sinker (arm-side run) | Sweeper/gyro (glove-side) | Arm-side vs. glove-side horizontal contrast. The "in-out" combo. |
| 4-seam (up) | Splitter (late drop) | Fastball plane then sudden drop below zone. |
| Cutter (glove-side) | Sinker (arm-side) | Opposite horizontal movement from similar velocity - hard to cover both. |

### Same-pitch repetition

- **Repeating a pitch is correct** when: the hitter just made weak contact on it (rolled over), the hitter is late on a fastball (they can't catch up - go back up), or the hitter is chasing the pitch off the plate (feed them another one just off).
- **Repeating is wrong** when: the hitter squared it up (On Time), the hitter was early on offspeed (they're sitting soft - don't go back), or you've thrown it 3+ times in the AB (predictability cost rises fast).
- **Fastball-up, fastball-up-again** is a real and effective pattern against hitters who are late; the second one often gets a swing-through or a popup.

### Sequencing principles

1. **Establish the fastball early** (even if you don't live there). It sets the tunnel for everything else.
2. **Change elevation and/or horizontal plane on the next pitch.** Don't throw two pitches in the same tunnel at the same height unless you're deliberately repeating.
3. **Use the previous pitch's location to set up the next.** A fastball up opens the bottom of the zone for the curve. A fastball in opens the outer half for the sweeper back-door.
4. **Velocity separation compounds.** A 97 mph 4-seam followed by an 83 mph sweeper is a 14 mph gap on top of the movement gap - two prediction errors at once.
5. **Don't be predictable in predictable counts.** The 3-1 offspeed is the modern counter to the hitter who "knows" a fastball is coming.
6. **Movement-vector separation score:** for two pitches, separation = sqrt((IVB1 - IVB2)^2 + (Horz1 - Horz2)^2). A 4-seam (+19, +8) vs. a curveball (-16, -10) = sqrt(35^2 + 18^2) = ~39 in of total separation. Anything above ~25 in is a strong contrast.

---

## Player data: Statcast metrics explained

Statcast (MLB-wide since 2015) tracks every pitch and batted ball with radar + cameras. These are the metrics a pitch-calling tool or a coach reads to understand a player.

### Hitter metrics

| Metric | What it means | Typical MLB range |
| --- | --- | --- |
| **Exit Velocity (EV)** | Ball speed off the bat. Higher = harder contact. | Avg ~88 mph; elite >90 mph; EV50 (avg of hardest 50%) elite >95 |
| **Launch Angle (LA)** | Vertical angle of the batted ball off the bat. | Ideal for hits: 10-30 degrees; line drives ~15-20; HRs ~25-28 |
| **Hard-Hit Rate** | % of batted balls EV >= 95 mph. | Avg ~38%; elite >50% |
| **Barrel** | Perfect EV + LA combo (the sweet spot for damage). | Barrel rate avg ~7%; elite >15% |
| **xwOBA** | Expected weighted on-base average, based on EV + LA + sprint speed for K/BB. | League avg ~.310-.320; elite >.370 |
| **xBA** | Expected batting average from EV + LA. | Removes defense/luck from BA |
| **Sprint Speed** | Feet/sec on a competitive run. | Avg ~27 ft/s; elite >29 (Billy Hamilton-tier >30) |
| **Whiff% / K%** | Swing-and-miss rate / strikeout rate. | Whiff% avg ~25%; K% avg ~22% |
| **Chase% (O-Swing%)** | Swing rate at pitches outside the zone. | Avg ~28%; low is good for hitter |
| **Contact%** | Contact rate on swings. | Avg ~76% |
| **Bat Speed** (2024+) | Speed of the bat at the sweet spot. | Avg ~72 mph; elite >75 |
| **Attack Angle** (2024+) | Upward angle of the swing path. | Avg ~10-15 degrees; matches pitch descent |
| **Swing Path Tilt** (2024+) | Horizontal tilt of the swing. | Affects pull/spray tendency |

### Pitcher metrics

| Metric | What it means | Typical MLB range |
| --- | --- | --- |
| **Velo** | Release speed. | 4-seam avg ~94; elite >98 |
| **Spin Rate** | RPM of the ball. | 4-seam 2200+; breaking 2500-2800+ |
| **IVB / Horz** | Movement (see above). | Varies by pitch |
| **VAA** | Vertical approach angle. | 4-seam avg -4.4 degrees |
| **Extension** | Release distance toward home. | Avg ~6.5 ft; elite >7 (adds ~1-1.5 mph perceived velo) |
| **Release Height / Side** | Where the ball comes out. | Drives tunnel + VAA |
| **Whiff%** | Swing-and-miss rate on the pitch. | Avg ~25%; elite breaking balls >40% |
| **Chase%** | Hitter swing rate out of zone on the pitch. | Elite sweepers >40% |
| **Zone%** | % of pitches in the zone. | Avg ~45% |
| **CSW%** | Called strikes + whiffs / total pitches. | Avg ~28%; elite >33% |
| **Barrel% allowed** | % of batted balls barreled against. | Lower is better; elite <5% |
| **Hard-Hit% allowed** | % of batted balls EV >= 95. | Lower is better; elite <30% |

### Reading a player profile (what "too fast / too slow" means)

For a **hitter**:
- **High EV50 + good launch angle = power threat.** Don't challenge middle-middle; live on the edges and expand with chase.
- **High chase% = vulnerable to breaking balls off the plate.** Feed sweepers/curves in the dirt; avoid the heart.
- **Low chase% + high walk rate = disciplined.** Must attack the zone; can't live off chase. Use tunnel pairs to force weak contact.
- **High whiff% / K% = swing-and-miss prone.** Elevated fastballs and tunnel put-away pitches work.
- **Low sprint speed = double-play / station-to-station.** Infield in, force contact.
- **Late on fastballs (swing-timing data)** = bat speed or reaction deficit. **Best pitch: high-IVB 4-seam up**, or a hard cutter on the hands. Avoid offspeed (they're already sitting soft).
- **Early on fastballs** = cheating to velo. **Best pitch: changeup or splitter in the tunnel**, or a curveball for a timing freeze. A high fastball up also works (swing under).

For a **pitcher**:
- **Low IVB 4-seam** = vulnerable at the top of the zone; must live low or rely on secondaries.
- **High walk rate** = command issues; in hitter's counts, expect fastballs because they can't afford to miss with breaking balls.
- **High chase-inducing sweeper** = use it in pitcher's counts for the put-away.
- **Flat VAA + high IVB** = elite top-of-zone fastball; build the arsenal around it.

---

## Pitcher evaluation metrics: Stuff+, Location+, Pitching+

Three composite models (popularized by FanGraphs / Baseball Prospectus) grade the *process* behind a pitcher's results, not just the outcomes.

- **Stuff+** grades the raw physical quality of a pitch from its velocity, movement (IVB, Horz), release height, and extension. 100 = league average. A 115 Stuff+ fastball is 15% better than average at generating whiffs, controlling for location. Stuff+ ignores location - it's pure "how nasty is the pitch." This is what pitch-design labs optimize.
- **Location+** grades how well a pitcher commands each pitch to the optimal location for that pitch type and count. 100 = average. It isolates command from stuff.
- **Pitching+** combines Stuff+ and Location+ into an overall pitch-quality grade. It correlates better with future strikeout rate and run prevention than raw ERA or FIP because it strips out defense, luck, and sequencing noise.

**How to use them:** Stuff+ tells you a pitcher's ceiling (can the pitch miss bats?). Location+ tells you if he can actually deploy it. A pitcher with 120 Stuff+ and 90 Location+ has elite raw stuff but leaks damage because he can't locate. A pitcher with 100 Stuff+ and 115 Location+ is a crafty command artist who overperforms his raw grade. Pitching+ is the blend - the best single number for "how good is this pitch, overall."

For PitchCall's purposes: a pitcher's Stuff+ by pitch type tells you *which of his pitches to trust in high-leverage counts*. If his sweeper grades 120 and his curve grades 95, the put-away pitch in a 1-2 count is the sweeper, full stop.

---

## Sources

- MLB.com Glossary (pitch type definitions, Statcast glossary)
- Baseball Savant / Statcast leaderboards (spin direction, movement, swing-take, bat tracking, attack regions)
- Rapsodo pitching data guides (spin rate, efficiency, break profiles, gyro spin)
- Driveline Baseball pitch grips series and pitch-design articles
- FanGraphs: Count Effects, Hitter's Count trends, Stuff+/Location+/Pitching+ primer, platoon splits library
- Baseball Prospectus: swing-timing analysis, pitch-tunneling research (23.8 ft decision point)
- mkdcbaseball.com Pitch Arsenal & Design Guide 2026 (IVB/VAA/tunneling framework, pitch atlas)
- bayesball.github.io Count Effects (run values by count, count leverage, Statcast count effects)
- Wikipedia (pitch-type articles, verified against Statcast conventions)
- ESPN / The Athletic: splitter coverage (2025 World Series), "rising fastball" IVB reporting, Stuff+ feature
- Pitcher List, Premier Pitching, Rockland Peak Performance, BRUCE BOLT (pitch grips and design)
- Frontiers in Sports and Active Living (2025): acceptable timing error at bat-ball impact
- ScienceDirect (2019): acceptable timing error by pitch type

Movement ranges are typical MLB averages synthesized from these sources; individual pitchers vary widely. "Gyro" slider is a pitch-design term for a low-spin-efficiency, bullet-spin slider - not an official Statcast category (Statcast lumps it under "Slider"). Count run values are approximate and vary slightly by season and run environment.
