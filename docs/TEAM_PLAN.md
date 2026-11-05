---
role: manager
created: 2026-11-05
status: active
---

# nowm.tech — Project Plan & Operating Procedure

**Project:** Professional Forex EA Store website (MT5 Expert Advisors for XAUUSD)
**Repo:** `nowm.tech` (git, `main` branch)
**Site:** portfolio / storefront homepage with embedded EA catalog & AI customer service
**Manager:** coordinates the team; Scum-Master leads technical review; Developer implements; Testers QA.

## Team roles

| Role | Responsibility | Authority |
|---|---|---|
| **Scum-Master** | Architecture, code review, release approval, CI quality gates | Must approve merge & release |
| **Developer** | Frontend implementation, catalog/store features, docs | Creates PRs against `main` |
| **Testers** | QA checklist, regression, accessibility, browser/responsive validation | Blocks ship on failing QA |
| **Manager** | Task assignment, deadlines, cadence, risk tracking, escalations | Owns process |

## Cadence

- **Daily standup (15 min):** what shipped, blockers, next.
- **Weekly review (Fri 16:00 UTC):** sprint cadence, demo of stuck items, schedule adjustment.
- **Sprint:** 2 weeks. Sprint 1 runs 2026-11-05 → 2026-11-19.

## Quality gates (must pass before any merge to `main`)

1. **JS syntax:** `check_js.py` replaced with a real syntax check (esprima/Node). Zero parse errors.
2. **HTML structure:** well-formed markup; no unclosed tags in shipped UI.
3. **No placeholder tokens:** no `G-XXXXXXXXXX`, `your-app-name`, `TODO`, `FIXME` in production content.
4. **Content consistency:** product names, prices, features must be identical across catalog UI, AI chat agent, and static copy.
5. **Accessibility:** semantic tags, `alt`/`aria` where needed, keyboard-accessible controls.
6. **Browser/responsive:** renders on desktop + mobile; dark/light toggle works.
7. **CI:** azure-webapps-node.yml steps pass (install/build/test) before merge.

## Artifacts

See `docs/KANBAN.md` for tasks + deadlines. See `docs/REVIEWS.md` for full code review of the 4 local commits.

## Rules

- No direct pushes to `main`. All changes via PR from a feature branch, reviewed by Scum-Master.
- Anyone can raise a quality gate failure; the owning role fixes it within one working day.
- Escalate blockers that block a deadline to the Manager immediately.
- Do not remove `check_js.py` until a real checker replaces it (keep a shim, do not delete).
