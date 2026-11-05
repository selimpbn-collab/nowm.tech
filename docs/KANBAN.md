# Kanban — nowm.tech

**Sprint:** 2026-11-05 → 2026-11-19
**Sprint goal:** Release-ready homepage: finish code review, restore docs, centralize catalog data, fix placeholders, harden quality gates.

---

## Ready / Backlog

| ID | Task | Owner | Due | Status |
|----|------|-------|-----|--------|
| T1 | Replace `check_js.py` with a real JS syntax checker (esprima/Node) + wire into CI | Developer | 2026-11-10 | Not started |
| T2 | Centralize product catalog (Mohit Maya $149 / GoldLadderBasket $199) into one JSON + drive UI & chat agent from it | Developer | 2026-11-12 | Not started |
| T3 | Restore root `README.md`; add docs/ + CONTRIBUTING with quality gates | Developer | 2026-11-10 | Not started |
| T4 | Fix placeholders: analytics ID, Azure `AZURE_WEBAPP_NAME`, `github.com/nowm-tech` link | Developer | 2026-11-11 | Not started |
| T5 | Accessibility & semantics: semantic tags, `alt`/`aria` roles, keyboard controls, mobile-menu ARIA | Developer | 2026-11-12 | Not started |
| T6 | Tester QA harness: HTML validation, Lighthouse/PWA, responsive + dark-mode, cross-browser regression | Testers | 2026-11-13 | Not started |
| T7 | Verify catalog data consistency across UI, chat agent, static copy | Testers | 2026-11-13 | Not started |
| T8 | QA sign-off on release candidate (RC) | Testers | 2026-11-17 | Not started |
| S1 | Scum-Master review of 67b5b92 & be011d3; approve quality gates | Scum-Master | 2026-11-07 | In progress |
| S2 | Scum-Master review of T1–T3 designs + JSON catalog model | Scum-Master | 2026-11-10 | Not started |
| S3 | Final release approval + RC deploy to staging, blueprint for prod | Scum-Master | 2026-11-17 | Not started |

---

## In Progress

| ID | Task | Owner | Due | Status |
|----|------|-------|-----|--------|
| S1 | Code review + quality gate setup | Scum-Master | 2026-11-07 | In progress |

---

## Done (current state)

- Core homepage delivered (`fd218a4`): portfolio + tech stack + playground + contact.
- Comparison section, testimonials, FAQ, CTA (`be011d3`).
- AI customer service chat agent with product/pricing/payment/shipping/refund Q&A (`67b5b92`).
- Azure Web App GitHub Actions pipeline (`2154b7f`).

---

## Notes / blockers

- No blockers for sprint start. Watch: `check_js.py` is a broken shim and must be replaced (T1) before we can rely on it in CI.
