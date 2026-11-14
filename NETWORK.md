# Four-repository network and locale contract

Owner: [saipradikmallakuntla-tech](https://github.com/saipradikmallakuntla-tech). Updated for batch `zion-restoration-2026-11-14-en-es-pt` on 2026-11-14 UTC.

| Node | Canonical live HTTPS URL | Source |
| --- | --- | --- |
| Hub | https://saipradikmallakuntla-tech.github.io/zion-ai-apps-hub/ | https://github.com/saipradikmallakuntla-tech/zion-ai-apps-hub |
| Stream Inspector | https://saipradikmallakuntla-tech.github.io/llm-stream-inspector/ | https://github.com/saipradikmallakuntla-tech/llm-stream-inspector |
| Retry Safety Lab | https://saipradikmallakuntla-tech.github.io/agent-retry-safety-lab/ | https://github.com/saipradikmallakuntla-tech/agent-retry-safety-lab |
| CORS & Cookie Doctor | https://saipradikmallakuntla-tech.github.io/cors-cookie-doctor/ | https://github.com/saipradikmallakuntla-tech/cors-cookie-doctor |

## Required directed graph
Every row must link directly to all three other nodes: **12 directed edges**, not 12 different apps.

| From / to | Hub | Stream | Retry | CORS |
| --- | --- | --- | --- | --- |
| Hub | — | required | required | required |
| Stream | required | — | required | required |
| Retry | required | required | — | required |
| CORS | required | required | required | — |

The three hub presentations share the same app destinations; localized views are not additional app nodes. [English](https://saipradikmallakuntla-tech.github.io/zion-ai-apps-hub/), [Spanish](https://saipradikmallakuntla-tech.github.io/zion-ai-apps-hub/es/), and [Portuguese](https://saipradikmallakuntla-tech.github.io/zion-ai-apps-hub/pt/) are complete static pages. Switching works without JavaScript and does not preserve or transmit filter input. The hub openly identifies the current satellite interfaces as English-only.

## Link, privacy, and deployment contract
1. Use canonical absolute HTTPS app URLs with repository prefix and trailing slash. Each hub view includes a live card and source link for every launched satellite.
2. Every satellite retains its hub link and both sibling links. No engine changes are required merely to reverify this graph.
3. Never append captures, headers, cookies, prompts, secrets, or scenario input to navigation URLs.
4. Deploy independently from `main:/` with `.nojekyll` and HTTPS enforcement. Assets are local and repository-relative, including `../` references from locale directories.
5. No mandatory backend, account service, package, iframe, shared hosted JavaScript, model API, or custom CNAME/DNS change.
6. Proposed apps stay in the roadmap until implementation, tests, and HTTPS deployment are verified. Do not label source-catalog record counts as functioning products.
7. Do not modify third-party repositories or claim upstream registration or endorsement. Broader Zion catalogs remain separate.

See [the dated batch summary](NETWORK_RESTORATION_BATCH.md) and [verification receipt](DEPLOYMENT_VERIFICATION.json) for observed outcomes. A successful fetch or build is not an uptime guarantee.
