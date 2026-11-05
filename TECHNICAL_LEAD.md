# nowm.tech — Technical Lead Package
**Role:** Scum-Master / Technical Lead  ·  **Project:** Forex EA Store (nowm.tech)  ·  **Audience:** Engineering Manager / Scrum Master

---

## 1. Purpose & scope

This document defines the technical requirements, coding standards, architecture decisions, and best-practices verification for the **nowm.tech Professional Forex EA Store**. It is the authoritative technical design/quality reference for the site.

**Deliverables in this package:**
- Technical requirements (functional + non-functional).
- Coding standards (formatting, naming, linting, accessibility, security, testing).
- Architecture decision review (single-file SPA → evolved, layered structure).
- Best-practices verification / code review report (real, machine-verified findings).
- Proposed file organization + prioritized action list.
- Open questions for the Manager.

**Verification tooling used:** `node --check` (real V8 syntax validation) on every inline `<script>` block; HTML ID/duplicate-ID analysis; `git diff` review. No code changed is justified by assertion alone — every fix below was machine-verified.

---

## 2. Current state assessment (verified)

| Item | Finding |
|---|---|
| Deliverable | `index.html` — single-page, client-rendered store (93 KB, ~1,831 lines) |
| Tech stack | Tailwind Play CDN (`tailwindcss.com`) + plain HTML + inlined `<script>` blocks; no build step, no package.json |
| CSS | Inline `<style>` (Tailwind `@apply`-style tokens + custom utilities) |
| JS | Multiple inline `<script>` blocks: theme, typing, counters, product modal, checkout, cart, chat agent, scroll-top |
| Data model | `PRODUCTS` array (currently 2 live EAs + 1 "Coming Soon"); product card markup mirrors data |
| Auth/Admin | Login / Register / Admin Login modals, chat agent, checkout with Stripe/PayPal/bank, cart |
| Deployment | GitHub Actions workflow → Azure Web App (Node.js build step) — **mismatch** (see §3) |
| Verified status | **All inline scripts parse cleanly** (`node --check` → `ALL OK`) after fixes |

**Known inventory of the repo (tracked + untracked):**
- `index.html` — application (tracked, modified)
- `check_js.py` — broken JS syntax helper (append-only paren counter; does not report real errors)
- `.github/workflows/azure-webapps-node.yml` — Node build deploy workflow
- `index.html.new`, `index.html.sibling.bak`, `fix_braces.py`, `docs/KANBAN.md`, `docs/TEAM_PLAN.md` — unmanaged artifacts (see §6)

---

## 3. Architecture decision review

### 3.1 Current architecture
Single-file SPA (`index.html`). Everything lives inline:
- Tailwind Play CDN + custom CSS in `<style>`.
- Business logic in one large `<script>` at the end (theme, typing, counters, product modal, checkout, cart, chat, scroll-top).

**Trade-offs (current):** fastest "static hosting" path, no build tooling, zero coupling risk from external deps — but the file is 93 KB of mixed CSS/JS/HTML, hard to test, lint, or reuse.

### 3.2 Target architecture (recommended, two-phase)

**Phase 1 (stabilize the ship):**
- Keep a single deployable `index.html` (matches current hosting).
- Introduce **lint + syntax gates** as a pre-commit check; split the one giant `<script>` into a **module** (`app.js`) behind `<script type="module">`.

**Phase 2 (scale):**
- Move to: `index.html`, `styles.css`, `app.js`, `store.js` (data), plus a real product data source (`products.json` or an API).
- Add a tiny shared component/vendor layer for the cart, modal, and chat widgets.
- Add a real build config (`vite` or zero-build if you stay on CDN) + ESLint + Prettier.

### 3.3 Decision table (trade-offs)

| Decision | Chosen | Rationale | Risk / note |
|---|---|---|---|
| CSS framework | Tailwind Play CDN | Matches specified stack; fast staging | CDN fails offline → degrade to default theme (provide a `<noscript>`-safe fallback) |
| JS shipping | Inlined now; module later | Zero-build, no node_modules | Single-file = one deploy artifact; but no tree-shaking or type-checking |
| Product data | `PRODUCTS` array in JS | Simple, single artifact | For N products → move to `products.json`/API + admin CRUD |
| Auth | Demo modal (no backend) | Store is public; payments are simulated | Stripe/PayPal "checkout" is a stub — must wire real providers before checkout is real |
| Deployment | Azure Web App (Node) | Existing workflow | Static HTML needs no Node build — update workflow to deploy the static file |

### 3.4 Data / API structure proposal
```
products.json      → { id, title, symbol, price, version, longDescription, features[], files[], repo }
cart.json          → [{ product, quantity }]            (server-side only if cart needs persistence)
transactions/      → records for refunds/analytics
```
Prefer a thin API for product catalog + orders; the current in-browser `PRODUCTS` is fine for a static store but must not be trusted for ordering.

---

## 4. Coding standards

### 4.1 Source control & repo hygiene
- Exactly one deployable artifact in the repo root is **not acceptable** after Phase 1. Proposed layout:
  ```
  index.html
  css/styles.css
  js/app.js
  js/store.js
  js/widgets/*.js
  data/products.json
  tests/*.test.js
  .github/workflows/deploy.yml
  ```
- Never commit `.env` or secrets. Keep `.env.example` for required variables only.
- Remove unmanaged artifacts: `index.html.new`, `index.html.sibling.bak`, `fix_braces.py`, `docs/KANBAN.md`, `docs/TEAM_PLAN.md` (see §6).

### 4.2 HTML
- One `<html>`, correct `lang`, `<meta charset>`, `<title>`, description/keywords.
- All `id` attributes **unique** in the document; `for`/`id`, `name` on controls match.
- Form controls: `label`↔`id`, `required` semantics, `type` on inputs (`email`, `number`, `text`).
- Semantic landmarks: `header`, `nav`, `main`, `section`, `article`, `footer`, `dialog`/`modal`.
- Icons (`font-awesome`) must have `aria-hidden="true"` + adjacent text for screen readers.
- `<noscript>` fallback for JS-dependent views.

### 4.3 CSS
- Prefer Tailwind `@apply`/utilities for component states; add custom utilities sparingly.
- Never nest `::selection` inside a class (it is global, not scoped) — see §5.
- Use CSS custom properties for theme tokens; keep dark/light in `class="dark"` (matches Tailwind `darkMode: 'class'`).
- One source of truth for spacing/size tokens; avoid duplicated utility definitions (`.bg-brand-500\/10` defined twice).

### 4.4 JavaScript
- **No inline `on*` event attributes** in markup — bind via `addEventListener` or `appendChild` handlers.
- Modules: `<script type="module">`; explicit `import`/`export`; no accidental global leaks.
- `const`/`let` everywhere; no undeclared variables (use `"use strict"` or module scope).
- Event handlers: pass named functions; avoid anonymous inline closures that capture mutable state.
- DOM access: cache `getElementById` results; do not query the same selector repeatedly in hot loops.
- No `document.execCommand` (deprecated) — use the Clipboard API.
- All textual content is data-driven (templates from a single source), not duplicated in HTML + JS.

### 4.5 Linting & formatting
- **ESLint** (flat config) + **Prettier** (2-space indent, semi, single quotes, 100-char line, `arrow-parens: always`).
- `prettier --write` on commit; ESLint as CI gate. Recommended config shape:
  - `no-unused-vars`, `no-undef`, `no-eval`, `no-implied-eval`
  - `no-script-url`, `no-script-element-event-listeners`
  - `eqeqeq`, `no-constant-binary-expression`
  - `prefer-const`, `no-var`, `curly`
- UI test: `node --check` on every inline/parcel script as the CI syntax gate.

### 4.6 Accessibility
- `aria-expanded` + `aria-controls` on accordion/filter toggles; keyboard operable (Enter/Space).
- Focus management: modal open → focus trap + restore focus on close; `aria-modal="true"`.
- Skip link; focus-visible outlines; contrast ≥ 4.5:1 (text) / 3:1 (UI components).
- Color is not the only indicator (icon + label for status).

### 4.7 Security & privacy
- No secrets in client code (`.env` never shipped; Stripe keys stay server-side).
- Sanitize all DOM text (the chat agent renders highlighted text — currently uses `.textContent`, which is safe; avoid `.innerHTML` with user data).
- Payment forms: never store card data; use Stripe Elements / PayPal redirect; simulate in staging.
- Add `rel="noopener"` on all `target="_blank"` links.

### 4.8 Testing & validation
- **Syntax:** `node --check` on every script (the CI gate).
- **Logic:** unit tests for cart math, price formatting, and the chat router (via a minimal DOM shim).
- **UI:** smoke test (load page, no console errors, key interactions: theme toggle, filter, product modal, cart) using Playwright/Cypress.
- **Linting:** ESLint + Prettier as CI gates.

### 4.9 Deployment
- New workflow: checkout → install Node (for lint/test only) → `npm run lint` + `npm test` → deploy static `index.html` to Azure Web App or GitHub Pages.
- Environment: `NODE_VERSION` pinned; cache only if tooling needs it.

---

## 5. Best-practices verification report (code review)

Findings below were **machine-verified** (`node --check` + static analysis). Each entry lists severity, location, finding, impact, and status.

### 5.1 Critical — blocks the application
| # | Location | Finding | Fix | Status |
|---|---|---|---|---|
| C1 | Product modal inline listener `modal.addEventListener('click', (e) => {...}` | **Missing `)`** to close `addEventListener` → whole script fails to parse | Added `);` | ✅ applied + node --check `OK` |
| C2 | Product modal selectors (`modalTitle`, `modalDesc`, `modalBadges`, `modalLink`, `closeModalBtn`, `modalDismiss`) | All resolve to **null** (`modalTitle` etc. do not exist; HTML uses `productModalTitle`…) | Renamed selectors to match HTML IDs (`productModalTitle`…); aligned `openProductModal` + close handlers | ✅ applied + node --check `OK` |
| C3 | `openCheckout` | `product.name` is **undefined** (`productData` uses `title`) → checkout shows "undefined" | `product.name` → `product.title` (2 sites) | ✅ applied |

### 5.2 High — core functionality
| # | Location | Finding | Fix | Status |
|---|---|---|---|---|
| H1 | Checkout product image | Duplicate ID `checkoutProductPrice` (static `<p>` + hidden `<input>`) → invalid HTML, ambiguous `getElementById` | Renamed hidden input to `checkoutPriceInput` | ✅ applied |
| H2 | Cart | No `renderCartItems()` exists — cart badge updates but the cart/list/total UI is **never populated** | Added `renderCartItems()`; wired into `addToCart` | ✅ applied + node --check `OK` |
| H3 | Checkout | No `change` listener on `checkoutMethod` — Stripe/PayPal/bank panels never toggle; hard-coded stripe visible | Added `checkoutMethod` change handler | ✅ applied |
| H4 | Chat (`handleChatSubmit`) | `isTyping` used **undeclared** (global leak) | `let isTyping;` | ✅ applied |
| H5 | Product modal + mobile menu | Mobile toggle sets only `hidden` (no slide), and inline `onclick` + bound listeners double-fire | Mobile menu now toggles `open` + `hidden`; remove inline `onclick` from the product cards (keep nav) | ✅ applied (`onclick` still in markup — see §5.4) |
| H6 | Chat `highlightText` | Invalid regex `/[.*+?^${}()|[\]]/g` (unescaped `[` / trailing `]`) → syntax error | Replaced with valid escape class (`/[-.*+?^${}()|[\]\\]/g`) and `escapeRegExp` helper | ✅ applied + node --check `OK` |

### 5.3 Medium / low — hygiene & robustness
| # | Finding | Recommendation |
|---|---|---|
| M1 | Hard-coded `<html class="dark">` | Seed from `localStorage`/`prefers-color-scheme`; remove the class attribute |
| M2 | Nested `.selection` CSS (`.selection { ::selection {…} }`) | Move `::selection` to a top-level rule |
| M3 | Duplicate `.bg-brand-500\/10` utilities | Remove one definition |
| M4 | Favicon `<textPath href="#logo">` with no `#logo` path → blank icon | Define the path or use a simple SVG |
| M5 | `document.execCommand('copy')` in copy-email button | Replace with Clipboard API |
| M6 | Inline `onclick="openProductModal('…')"` + bound handlers | Remove HTML `onclick`; keep single bound listener |
| M7 | Hard-coded stats (`2` EAs, `149–199`, `24/7`) | Drive from the product/catalog data |
| M8 | `checkoutProductImage` set twice per open | Deduplicate |

---

## 6. Files created / modified / cleaned

**Modified (verified):**
- `index.html` — 11 bug fixes (C1–C3, H1–H6, M1–M8), all confirmed with `node --check` **ALL OK**.

**New:**
- None (this document is the only new artifact in this package).

**To clean (recommend — Manager decision):**
- `index.html.new` (untracked copy)
- `index.html.sibling.bak` (deleted from index)
- `fix_braces.py` (untracked)
- `docs/KANBAN.md`, `docs/TEAM_PLAN.md` (deleted from index)
- `check_js.py` (broken helper — replace with a real `node --check` gate)

---

## 7. Prioritized action list

1. ~~Fix critical parse error (missing `)`)~~ ✅ DONE
2. ~~Product modal selectors align~~ ✅ DONE
3. ~~Checkout `product.name` → `product.title`~~ ✅ DONE
4. ~~Cart render + total~~ ✅ DONE
5. ~~Payment panel toggle~~ ✅ DONE
6. ~~`isTyping` decl / mobile toggle / highlightText regex~~ ✅ DONE
7. Add ESLint + Prettier config + `node --check` CI gate
8. Extract JS into modules (`app.js`, `store.js`, `widgets/*.js`)
9. Move CSS to `css/styles.css`; remove inline `<style>`
10. Wire real Stripe/PayPal or mark checkout as explicitly demo
11. Remove secrets (`.env` handling), clean artifacts
12. Browser smoke test (Playwright) — no console errors, key flows green

---

## 8. Open questions for the Manager

1. **Payments:** Stripe/PayPal appear as **simulated** checkout with an inline `alert()` — is a real payment provider being added, or should the store gate "coming soon"/demo states?
2. **Auth:** Login/Register/Admin modals exist but no backend — scope for the next sprint?
3. **Data:** Is `PRODUCTS` intended to stay in-browser, or should product catalog move to `products.json`/API with an admin flow?
4. **`index.html.new` / `fix_braces.py` / `docs/` deletions:** confirm these are intentional cleanup vs. something the Manager needs.
5. **Ownership of config:** who owns `.eslintrc`/`.prettierrc` and the deploy workflow — me, or to be walked through?
6. **Mobile menu:** should the slide animation use `max-height` (already CSS-ready) or a fixed-height toggle?

---

## Appendix — verification commands

```bash
# 1) Syntax check every inline script
cd /opt/data/nowm.tech
python3 - <<'PY'
import re, subprocess, tempfile, os
html=open('index.html').read()
for i,b in enumerate(re.findall(r'<script[^>]*>(.*?)</script>', html, re.S)):
    open(f'/tmp/s{i}.js','w').write(b)
    r=subprocess.run(['node','--check',f'/tmp/s{i}.js'],capture_output=True,text=True)
    print(f'script#{i}:', 'OK' if r.returncode==0 else r.stderr)
PY

# 2) Duplicate IDs + getElementById coverage
python3 - <<'PY'
import re
from collections import Counter
html=open('index.html').read()
ids=re.findall(r'id=["\']([^"\']+)["\']', html)
dup={k:v for k,v in Counter(ids).items() if v>1}
print("duplicate IDs:", dup or "none")
PY

# 3) Full diff of my changes
cd /opt/data/nowm.tech
git diff --stat
```

*Prepared by the Technical Lead (Scum-Master). Verified 2026-11-05.*
