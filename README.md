# Zion AI Apps Hub

A dependency-free, multilingual directory for six browser-local AI and IT utilities.

## Language views
- [English](https://saipradikmallakuntla-tech.github.io/zion-ai-apps-hub/) — `index.html`, the default.
- [Español](https://saipradikmallakuntla-tech.github.io/zion-ai-apps-hub/es/) — `es/index.html`.
- [Português](https://saipradikmallakuntla-tech.github.io/zion-ai-apps-hub/pt/) — `pt/index.html`.

Each URL contains a complete static view: navigation, app descriptions, limitations, search/category labels, result counts, empty state, privacy information, and release links. Language links work without JavaScript. Each page sets its own HTML `lang`, canonical URL, alternate `hreflang` links, x-default, and localized CollectionPage metadata. Brand/product names remain unchanged. The satellite interfaces are currently **English-only**; the selector localizes this hub, not those tools.

The English default is deterministic. There is no automatic locale redirect, language cookie, local-storage preference, or transfer of search text between pages. Optional filtering is accent-insensitive and entirely local. Without JavaScript, all six cards and language links remain usable and the inactive filters stay hidden.

## Live apps and source
| App | Live HTTPS URL | Source |
| --- | --- | --- |
| LLM Stream Inspector | https://saipradikmallakuntla-tech.github.io/llm-stream-inspector/ | https://github.com/saipradikmallakuntla-tech/llm-stream-inspector |
| Agent Retry Safety Lab | https://saipradikmallakuntla-tech.github.io/agent-retry-safety-lab/ | https://github.com/saipradikmallakuntla-tech/agent-retry-safety-lab |
| CORS & Cookie Doctor | https://saipradikmallakuntla-tech.github.io/cors-cookie-doctor/ | https://github.com/saipradikmallakuntla-tech/cors-cookie-doctor |

## Batch 99 expansion

- [Prompt Token Budget Lab](https://saipradikmallakuntla-tech.github.io/prompt-token-budget-lab/) · [source](https://github.com/saipradikmallakuntla-tech/prompt-token-budget-lab)
- [Tool Schema Drift Auditor](https://saipradikmallakuntla-tech.github.io/tool-schema-drift-auditor/) · [source](https://github.com/saipradikmallakuntla-tech/tool-schema-drift-auditor)
- [Webhook Replay Guard](https://saipradikmallakuntla-tech.github.io/webhook-replay-guard/) · [source](https://github.com/saipradikmallakuntla-tech/webhook-replay-guard)

[Discovery EN](https://saipradikmallakuntla-tech.github.io/zion-ai-apps-hub/batch-99-discovery.html) · [ES](https://saipradikmallakuntla-tech.github.io/zion-ai-apps-hub/es/batch-99-discovery.html) · [PT](https://saipradikmallakuntla-tech.github.io/zion-ai-apps-hub/pt/batch-99-discovery.html). All three views provide equivalent rule-based questions, recommendations, and user-triggered copy/export/mailto drafts. They collect no prompts, captures, headers, IDs or other free-form evidence. A mailto link opens a draft, never sends automatically. All six utility interfaces remain English-only. Historical six-candidate roadmap proposals remain unlaunched and are not these three new apps.

## Run and test
Serve the repository root, then open the default or localized path:
```sh
python3 -m http.server 8000
node tests/localization.test.cjs
```
There is no installation, bundler, framework, API key, inference call, shared script host, or backend. `styles.css` and `app.js` are local assets; `.nojekyll` keeps Pages publishing static. Publish `main:/` with HTTPS enforcement. Spanish and Portuguese pages reference assets relative to their directories.

## Privacy and scope
No fetch/XHR, uploads, telemetry, cookies, persistent storage, external fonts, iframes, or external runtime assets. Ordinary canonical HTTPS navigation carries no captures, prompts, secrets, headers, cookies, or scenario parameters. CSP disables runtime connections and object embedding. Input text is never interpreted as HTML.

These are diagnostic aids, not security certificates, model-quality guarantees, or exactly-once guarantees. This batch does not change satellite engines or third-party repositories, catalogs, APIs, registration, or DNS. The complementary network is independent; a reference is not an endorsement.

## Release evidence
- [Current restoration/localization batch](NETWORK_RESTORATION_BATCH.md).
- [Seven-repository link and locale contract](NETWORK.md).
- [Dated deployment receipt](DEPLOYMENT_VERIFICATION.json): point-in-time evidence, not monitoring.
- [Prior six-candidate roadmap](NEXT_BATCH_ROADMAP.md): historical launch verification and design proposals, **not six launched apps**. Its dated observations are retained rather than silently rewritten.

Español: el directorio está traducido; las aplicaciones satélite siguen en inglés. Português: o diretório está traduzido; os aplicativos satélites continuam em inglês.
