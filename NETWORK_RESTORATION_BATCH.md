# Network restoration and multilingual showcase batch

- **Batch ID:** `zion-restoration-2026-11-14-en-es-pt`
- **Date:** 2026-11-14 UTC
- **Owner:** `saipradikmallakuntla-tech`
- **Scope:** this hub plus `llm-stream-inspector`, `agent-retry-safety-lab`, and `cors-cookie-doctor`; no third-party writes.
- **Baseline hub commit:** [`b36cc60`](https://github.com/saipradikmallakuntla-tech/zion-ai-apps-hub/commit/b36cc6021dcef34de1779a8299ec4044a748a0bc).

## Checkpoint reconciliation
The baseline already contained a deployed four-node network and all 12 directed links. Its initial receipt dated 2026-11-14 14:58:34 UTC reported 33 satellite tests. Those historical observations are not substituted for fresh verification.

## Delivered implementation
- Complete static English `/`, Spanish `/es/`, and Portuguese `/pt/` showcase views.
- Accessible native language links with each language's self-name, `lang`/`hreflang`, and visible `aria-current` state; switching also works without JavaScript.
- Fully localized interface copy, category/search labels, result counts, reset and no-results messages, descriptions, boundaries, privacy, and release information.
- Per-view HTML language, canonical/alternate/x-default metadata and localized structured data.
- Local accent-insensitive filtering, no-JavaScript cards, keyboard skip link and visible focus, responsive layouts, local-only runtime assets, and restrictive CSP.
- Satellite engines remain unchanged and their current English-language interfaces are disclosed rather than represented as translated.
- Refreshed README and network contract; the historical six-proposal roadmap is preserved.

## Verification sequence
Before publication, all three locale views passed real Chromium checks for categories, combined filtering, translated counts, empty/reset states, accent-insensitive search, literal input rendering, keyboard skip navigation, no-JavaScript cards/language links, zero script errors, and no unexpected runtime requests. Widths 320, 390, 768, 900, and 1440 px had no horizontal overflow.

Fresh live satellite checks passed with TLS verification enabled: Stream Inspector **9/9**, Retry Safety Lab **10/10**, CORS & Cookie Doctor **14/14**; all three returned HTTP 200, offered their required three outgoing links, and served HTML/engines matching the anchored GitHub sources. The same pure-engine suites passed in Node: **33/33**.

Final post-publication hub/locale HTTP results, the 12-edge live graph, source-byte comparisons, Pages states, timestamps, and commit references are recorded in `DEPLOYMENT_VERIFICATION.json` and the final verification section below once deployment has completed. No pending check should be read as passed.

## Reproduce basic local checks
```sh
python3 -m http.server 8000
node tests/localization.test.cjs
```
In each satellite repository:
```sh
node -e "const t=require('./app.js').selfTest();console.table(t);if(t.some(x=>!x.pass))process.exit(1)"
```
Browser verification additionally disables JavaScript, exercises each language link, changes search/category inputs, and uses each satellite's **Run built-in tests** button. All evidence is point-in-time, not monitoring, an SLA, or a correctness/security guarantee.
