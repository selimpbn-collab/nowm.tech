# Code Review — nowm.tech (Forex EA Store)

**Reviewer:** Scum-Master (tech lead)
**Review date:** 2026-11-05
**Scope:** All local commits ahead of origin/main (4 commits)

## Commit summary

| Commit | Subject | Files | Verdict |
|---|---|---|---|
| fd218a4 | Add professional Forex EA store website | README_old.md, check_js.py, index.html (+~2221) | Approved w/ notes |
| 173bdc7 | Update product descriptions | README.md (rm), index.html (-941/+50) | Approved w/ notes |
| be011d3 | Comparison table, testimonials, FAQ, CTA | index.html | Approved w/ notes |
| 67b5b92 | AI customer service chat agent | index.html | Approved w/ notes |

## Strengths
- Clean glassmorphism UI; coherent dark/light theme via `dark` class.
- All four historical commits follow a consistent visual language.
- Product/pricing copy is consistent across the AI chat agent and site content.
- Deployment pipeline wired (Azure Web App GitHub Actions + node build step).

## Issues found & required fixes (must-haves before merge)

### 1. check_js.py is not a real JS syntax checker
- It only balances parentheses per line and prints a count. It does not parse braces/brackets, and it never flags syntax errors. This gives a false "passing" signal. → Replace with a real parser (e.g., esprima/Node) or a Node-based lint step in CI.

### 2. Placeholder / incomplete tokens in production UI
- Analytics ID `G-XXXXXXXXXX` hardcoded — no real measurement. → Replace with real ID or remove.
- `.github/workflows/azure-webapps-node.yml` has `AZURE_WEBAPP_NAME: your-app-name` placeholder and unconfigured publish-profile secret. → Per-env config required before first deploy.
- `github.com/nowm-tech` repository link is a placeholder. → Point to actual repo.

### 3. Hardcoded product data in UI + AI chat agent
- Product info (Mohit Maya $149 / GoldLadderBasket $199, features, prices) is duplicated in HTML and duplicated again inside the JS chat agent. → Centralize into a single JSON source of truth and drive both UI and chat from it.

### 4. Accessibility / semantics
- Heavy use of `<div>` and `<i>` icons with no `alt`/`aria` fallbacks; JS-only interactivity (mobile menu) should have `aria-expanded`/`aria-controls`. → Normalize markup & add ARIA.

### 5. No real README at repo root
- `README.md` was deleted in 173bdc7; root holds only site artifacts plus a misnamed `README_old.md` (which is actually the site HTML). → Restore a root README.md with setup/deploy instructions.

## Recommended fixes (details in TEAM_PLAN.md)

- F1: Centralize product catalog JSON; drop duplicate chat-inlined copy.
- F2: Replace check_js.py with a real JS syntax check (esprima/Node).
- F3: Remove/complete analytics & Azure placeholders.
- F4: Restore root README.md; add docs/.
- F5: Fix accessibility + ARIA gaps.
