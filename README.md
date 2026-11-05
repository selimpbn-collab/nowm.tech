# nowm.tech — Professional Forex EA Store

A professional landing page + digital storefront for MT5 Expert Advisors, built
for XAUUSD (gold) and major pairs. It showcases two averaging/martingale EAs,
drives the comparison table, product detail modal, cart, checkout, and a
self-contained AI customer-service chat agent — all from one HTML file.

## What's here

| Artifact | Purpose |
|---|---|
| `index.html` | The storefront. Single-file deployment (no build step, no build tools required). |
| `check_js.py` | Real JavaScript syntax checker (wraps `node --check`). |
| `.github/workflows/azure-webapps-node.yml` | Azure Web App deploy pipeline. |
| `docs/` | Project planning (kanban, reviews, team plan) — see below. |

## Features implemented

- **Product catalog (single source of truth)** — `PRODUCTS` drives the store
  grid, comparison table, product detail modal, stock/stats, and the AI chat
  agent. No duplicated copy between the UI and the chat.
- **Product details expansion** — rich modal with strategy & mechanics,
  "for traders who", requirements & license, files included, plus buy/checkout.
- **Comparison table** — dynamic, responsive (horizontal scroll on mobile).
- **Testimonials** — rendered from a `TESTIMONIALS` catalog (5 quotes).
- **FAQ** — 10 items rendered from `FAQS` with an accordion (ARIA). 10 Q's.
- **CTA section** — data-driven headline + two action buttons.
- **Automated customer service** — `customerService` pattern-matching bot
  (products, pricing, payments, shipping, refunds, support, general, fallback).
- **Cart / Checkout** — price-driven checkout with stripe/paypal/bank transfer.
- **Accessibility** — semantic tags, `aria-expanded`/`aria-controls` on the
  FAQ and mobile menu, keyboard-driven controls, `focus:outline-none` focus
  rings, `alt`-equivalent aria-labels.

## Repository layout

```
nowm.tech/
├── index.html          # storefront (single-file, no build step)
├── check_js.py         # real JS syntax checker (node --check based)
├── .github/
│   └── workflows/
│       └── azure-webapps-node.yml   # Azure deployment pipeline
└── docs/
    ├── KANBAN.md       # task board + deadlines
    ├── REVIEWS.md      # code review record
    └── TEAM_PLAN.md    # project plan & operating procedure
```

## Quality gates (must pass before merge)

1. `python3 check_js.py` — zero parse errors.
2. `node --check` — the inline scripts are valid (see `check_js.py`).
3. No placeholder tokens (`G-XXXXXXXXXX`, `your-app-name`, `TODO`, `FIXME`) in
   production content.
4. Content consistency across catalog UI, AI chat agent, and static copy.
5. Accessibility — semantic tags, aria roles, keyboard controls.
6. CI steps pass (install/build/test) before merge.

## Docs

Read the planning & review record in `docs/`:

- `docs/KANBAN.md` — tasks, owners, deadlines.
- `docs/REVIEWS.md` — the Scum-Master code review + required fixes.
- `docs/TEAM_PLAN.md` — project plan, roles, cadence, quality gates.

## Notes

- The site is hosted via GitHub Pages (`nowm.tech`) and deployable to Azure.
- Purchase processing is simulated in-browser (Stripe/PayPal redirects and the
  bank-transfer flow are wired but not connected to a live processor).
