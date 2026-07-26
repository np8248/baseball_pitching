# Pitch Predictor - Project Handoff

## Goal
Build **Pitch Predictor**, an iPad-first, in-game pitch-calling assistant for the dugout. Single self-contained `index.html`, no backend, works offline, deployable via GitHub Pages. Referenced design: `/Users/noahp/Desktop/Screenshot 2026-07-25 at 10.24.08 AM.png`.

## Division of Labor (user's intent)
- **The other AI (GPT, via Factory)** = domain expert. It researches pitch-calling facts and produces an exact specification. It also audits the implementation against the facts afterward.
- **This AI (the implementer)** = writes the code from the spec, then fixes any findings the audit surfaces.
- The user wants the result "very accurate" - not a demo/heuristic.

## Repo
- GitHub: `https://github.com/np8248/baseball_pitching`
- Local: `/Users/noahp/baseball_pitching`
- Default branch: `main`
- Note: `/Users/noahp` itself is a separate git repo (`cmd-help`); `baseball_pitching` is nested inside it as its own repo. Run git commands with `cd /Users/noahp/baseball_pitching` or `-C /Users/noahp/baseball_pitching`.

## What's Done
1. **Codex channel established.** No OpenAI login needed. Factory ships GPT models under existing auth. Confirmed working:
   ```
   droid exec -m gpt-5.3-codex --auto low "Reply with exactly: CODEX_ONLINE via Factory"
   ```
   Available GPT models include: `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-5.5`, `gpt-5.5-fast`, `gpt-5.5-pro`, `gpt-5.4`, `gpt-5.4-fast`, `gpt-5.4-mini`, `gpt-5.3-codex`, `gpt-5.3-codex-fast`, `gpt-5.2`.
2. **UI shell built** at `index.html` (21KB, single file, no deps). Layout matches the screenshot:
   - Header (Pitch Predictor logo, New At-Bat / Full Reset)
   - Left column: strike-zone tap grid (5x5: inner 3x3 = zone, outer ring = chase), velocity slider (60-106), count stepper (balls/strikes), pitcher handedness (L/R)
   - Right column: timing (Early/Late/On Time/Unknown), pitch-type buttons (4 Seam, Sinker, Cutter, Gyro, Sweeper, Curve, Split, Change), editable Pitcher Average Movements table (Velo/Vert/Horz per pitch)
   - GO button + ranked recommendations list (top 5) with STRIKE/CHASE tags
   - localStorage persistence for averages + handedness
   - Mobile-responsive, iPad-optimized (safe-area insets, no zoom, apple-mobile-web-app-capable)
   - Engine hook `recommend()` is a stub returning `[]`; badge reads "Awaiting Spec".
3. **Domain-spec prompt ready** at `.codex-prompts/domain-spec.md`. It asks for: movement sign conventions, per-pitch-type MLB reference table, zone coordinate model, the deterministic scoring engine spec, correctness traps, and sources. It includes a worked-example request using the screenshot's pitcher (4 Seam 94/+19/+8, Curve 79/-20/-9, Cutter 85/+3/-3, Sweeper 83/-3/-20, RHP vs LHH, 0-1 count, last pitch 4 Seam 97 up-and-away, timing Unknown).

## What's NOT Done (next steps, in order)
1. **Generate the domain spec.** Previous `gpt-5.5-pro` run hit the user's 5-hour Factory usage limit before writing output. Re-run with either:
   - `gpt-5.5-pro -r high` (strongest, slowest, ~5-10 min)
   - `gpt-5.3-codex` (faster, still strong)
   Command (background, captures stdout):
   ```
   cd /Users/noahp/baseball_pitching && nohup droid exec -m gpt-5.5-pro -r high --auto low -f /Users/noahp/baseball_pitching/.codex-prompts/domain-spec.md > /Users/noahp/baseball_pitching/.codex-prompts/DOMAIN_SPEC.out 2> /Users/noahp/baseball_pitching/.codex-prompts/domain-spec.err &
   ```
   **Watch out:** stdout buffers until the process exits, so `DOMAIN_SPEC.out` stays 0 bytes while running. Poll with `ps -p $PID`. If the run dies with "Exec failed" + a usage-limit message, the spec is recoverable from the session transcript at `~/.factory/sessions/-Users-noahp-baseball_pitching/<session-id>.jsonl` (look for the last `assistant` message with text content).
   Alternative if usage limits keep biting: have the implementer write the spec from its own baseball knowledge, then use a cheaper/faster GPT model only to audit.
2. **Implement the engine.** Replace the `recommend()` stub in `index.html` with the spec'd deterministic scoring function. Output shape: `[{type, locationName, intent: "strike"|"chase", score}, ...]` sorted desc, top 5. Update the `#engineBadge` from "Awaiting Spec" to something like "Spec v1".
3. **Audit.** Send the engine implementation (just the `recommend()` function + any helpers) to a GPT model with the spec and a strict "find real bugs, verify the math against the spec, cite line numbers" prompt. Fix findings.
4. **Commit and push.** See commit guidance below.

## Key Technical Decisions
- **Stack:** single-file `index.html`, no build step. Matches the user's other projects (`endless.html`). Opens instantly on iPad via GitHub Pages.
- **Zone grid:** 5x5. Columns 1-3, rows 1-3 = rulebook strike zone. Outer ring = chase/shadow. Column index increases left-to-right from the catcher's view. Row 0 = top, row 4 = bottom.
- **Pitch types:** exactly the 8 from the screenshot: 4 Seam, Sinker, Cutter, Gyro, Sweeper, Curve, Split, Change. "Gyro" likely = gyro-spin slider (bullet spin, near-zero efficiency); confirm in spec.
- **Movement signs (UNCONFIRMED - spec must resolve):** the screenshot shows RHP with 4 Seam Horz = +8 and Sweeper Horz = -20. This implies Horz is signed from the pitcher's/catcher's view with arm-side positive for an RHP... but a sweeper breaks glove-side for an RHP, so -20 glove-side fits if the convention is "arm side = +". The spec must nail this down because a sign error mirrors every recommendation. Internal math should convert to handedness-neutral "glove side / arm side" before scoring.
- **Vert:** likely Induced Vertical Break (IVB, gravity removed) in inches - the number coaches get from Rapsodo/Trackman/Hawk-Eye. Positive = "rise" / less drop than gravity. Spec must confirm.
- **No backend, no tracking.** Everything client-side. Pitcher averages persist in localStorage.

## Codex CLI (the brew-installed one) - optional, not needed
- `codex` was reinstalled via `brew reinstall --cask codex` (now v0.145.0) but is **not authenticated** (401 Unauthorized, no `~/.codex/auth.json`). If the user ever wants to use the real Codex CLI instead of Factory's GPT models, they need to run `codex login` in their own terminal.
- The dead `unityMCP` entry in `~/.codex/config.toml` was commented out to stop transport-error spam.

## Commit Guidance
The UI shell is working, self-contained, and useful on its own. Commit it now so progress is saved on GitHub. Suggested message:
```
Add Pitch Predictor UI shell with zone grid, pitch controls, and rec list

Single-file index.html matching the target screenshot. Engine is a stub
pending the domain spec from the GPT reviewer channel. localStorage
persists pitcher averages and handedness.
```
Include `index.html`, `HANDOFF.md`, and `.codex-prompts/` (the spec prompt is reusable). Do NOT commit `DOMAIN_SPEC.out` / `domain-spec.err` (transient run artifacts) - add to `.gitignore`.

## File Map
```
/Users/noahp/baseball_pitching/
  index.html                       # the app (UI shell, engine stub)
  HANDOFF.md                       # this file
  README.md                        # original 19-byte placeholder
  .codex-prompts/
    domain-spec.md                 # reusable spec prompt for the GPT reviewer
    DOMAIN_SPEC.out                # transient: spec output (currently empty)
    domain-spec.err                # transient: run stderr
```
