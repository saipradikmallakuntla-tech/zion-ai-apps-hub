# Next batch roadmap — AI & IT utility satellites

**Owner:** [saipradikmallakuntla-tech](https://github.com/saipradikmallakuntla-tech)  
**Prepared:** 2026-11-14 UTC  
**Deployment verification completed:** 2026-11-14 at 14:58:34 UTC  
**Scope:** one live hub and three existing live satellite apps. The six proposals below are design candidates only; no next-batch repositories have been created.

## Four-repository architecture

| Role | Repository | Live HTTPS URL |
| --- | --- | --- |
| Central directory | [zion-ai-apps-hub](https://github.com/saipradikmallakuntla-tech/zion-ai-apps-hub) | https://saipradikmallakuntla-tech.github.io/zion-ai-apps-hub/ |
| AI stream diagnostics | [llm-stream-inspector](https://github.com/saipradikmallakuntla-tech/llm-stream-inspector) | https://saipradikmallakuntla-tech.github.io/llm-stream-inspector/ |
| Agent side-effect simulation | [agent-retry-safety-lab](https://github.com/saipradikmallakuntla-tech/agent-retry-safety-lab) | https://saipradikmallakuntla-tech.github.io/agent-retry-safety-lab/ |
| IT browser-policy diagnostics | [cors-cookie-doctor](https://github.com/saipradikmallakuntla-tech/cors-cookie-doctor) | https://saipradikmallakuntla-tech.github.io/cors-cookie-doctor/ |

The navigation graph is fully connected: hub → all satellites, and each satellite → hub + both siblings. Navigation uses plain absolute HTTPS links; runtime assets are relative to each repository. No sensitive inputs travel in URLs. Each app can run independently without a common server, account system, model API, database or shared hosted JavaScript. See [NETWORK.md](NETWORK.md).

## HTTPS and deployment status

Verified on 2026-11-14, completed at 14:58:34 UTC. GitHub Pages API observations confirmed the public sites, `main:/` publishing source, successful build state, and HTTPS enforcement. Independent TLS-verified live fetches returned HTTP 200, and all runtime files matched the committed sources.

| Repository | Visibility | Pages source | Pages state | HTTPS enforced | Live HTTP check |
| --- | --- | --- | --- | --- | --- |
| zion-ai-apps-hub | Public | `main:/` | `built` | `true` | `200`, TLS verified |
| llm-stream-inspector | Public | `main:/` | `built` | `true` | `200`, TLS verified |
| agent-retry-safety-lab | Public | `main:/` | `built` | `true` | `200`, TLS verified |
| cors-cookie-doctor | Public | `main:/` | `built` | `true` | `200`, TLS verified |

### Verification evidence

- **Hub implementation commit:** [1944a7d](https://github.com/saipradikmallakuntla-tech/zion-ai-apps-hub/commit/1944a7de7fe8a9563631f3e8d4d16ebf9ef8af3a). The subsequent verification commit changes documentation/receipt files, not runtime HTML/CSS/JS.
- **Deployment receipt:** [DEPLOYMENT_VERIFICATION.json](DEPLOYMENT_VERIFICATION.json), a dated, machine-readable snapshot.
- **Live navigation:** all four sites offered the required links to the other three. Existing satellite code was not modified.
- **Hub browser checks:** local filtering and category combinations, no-results/reset behavior, no-JavaScript card navigation, semantic HTML and three WebApplication schema entries. Responsive layouts at 320, 390, 768, 900 and 1440 pixels had no horizontal overflow. No script errors or unexpected runtime network requests were observed in these checks.
- **Live satellite regression checks:** Stream Inspector 9/9; Retry Safety Lab 10/10; CORS & Cookie Doctor 14/14 — **33/33 passed** in Chromium.

These are dated observations, not continuous monitoring, an SLA, or proof that a model/analysis result is correct. All apps use GitHub's default `github.io` domain; no custom DNS or CNAME changes were required.

## Scope and duplicate-avoidance principles

The original source audit examined the [master catalog](https://github.com/Zion-support/zion-app-network/blob/main/CATALOG.md), [five-shard app registry](https://github.com/Zion-support/zion-network/blob/main/network.json), and [website service inventory](https://github.com/Zion-support/zion-support.github.io/blob/main/data/services.json). Its 484 linked-repository / 421 registry-ID / 1,637 service-record counts were source snapshots, not counts of verified functioning products.

The reviewed material already includes schema-contract testers, RAG evaluation, model routing, webhook management, cron execution and global scheduling. The proposals below deliberately target different, small offline workflows. Their boundaries were screened against that saved audit corpus, but catalog descriptions can be incomplete. Before creating any candidate, recheck current registries and the closest neighboring implementations. If the practical workflow already exists, extend/link to it rather than launch a duplicate.

## Six scoped proposals

### 1. Structured Output Portability Checker — AI engineering
**Candidate slug:** `structured-output-portability-checker`  
**Problem:** a JSON Schema accepted by one model API can use keywords or shapes unsupported by another provider's structured-output dialect.

- **Inputs:** a JSON Schema and explicitly versioned provider-profile selections.
- **MVP:** compare against dated support profiles; flag unsupported keywords, unresolved references, required/nullable differences and unknown cases. Export a per-provider compatibility report with rule provenance.
- **Outputs:** compatibility matrix, JSON Pointer locations, safe manual adjustment suggestions and synthetic fixtures.
- **Boundary:** not sample-to-schema generation, general data-contract validation, model evaluation, SDK generation or live inference. Complements [Agent Contract Tester](https://github.com/Zion-support/zion-agent-contract-tester) and Stream Inspector rather than replacing them.
- **Acceptance tests:** nested schemas, recursive/unresolved `$ref`, nullable unions, unsupported keywords and rule-profile version changes. Unknown support must remain unknown, not be labeled accepted.
- **Limit:** profiles are snapshots; no offline tool can guarantee a provider will accept a future request.

### 2. Citation Span Verifier — AI evidence tooling
**Candidate slug:** `citation-span-verifier`  
**Problem:** an answer can cite the right document ID but quote text that is missing, offset incorrectly, or from a changed document revision.

- **Inputs:** local plain-text sources, stable source IDs, and JSON citation records containing quoted spans or offsets.
- **MVP:** exact span matching with explicit newline/Unicode normalization modes; source SHA-256 fingerprints; offset-unit labels and revision mismatch findings.
- **Outputs:** found/missing/ambiguous span report and exportable evidence map, without uploading sources.
- **Boundary:** no citation generation, web research, PDF OCR, semantic entailment, hallucination scoring or RAG retrieval evaluation. Complements [RAG Eval Kit](https://github.com/Zion-support/zion-rag-eval-kit) with deterministic evidence-location checks.
- **Acceptance tests:** emoji/code-point boundaries, CRLF, repeated quotations, edited source revisions and normalization-sensitive matches.
- **Limit:** a matching quote does not establish that the answer is true or that the quote supports its claim.

### 3. Conversation Portability Inspector — AI integration
**Candidate slug:** `conversation-portability-inspector`  
**Problem:** moving a saved conversation between provider message formats can silently lose roles, tool-result associations, or multimodal references.

- **Inputs:** a saved, non-streaming message-history JSON file and a target message-format profile.
- **MVP:** validate role sequencing and tool-call/result IDs; produce a dry-run mapping and explicit loss/unsupported-feature ledger for two dated provider adapters.
- **Outputs:** a portability report and user-reviewed draft mapping, with original content excluded from exports by default.
- **Boundary:** not the existing SSE/NDJSON Stream Inspector, an agent runner, a chatbot, model router, conversation summarizer or general code/data migrator. It inspects saved conversation structure, not transport events.
- **Acceptance tests:** dangling/duplicate tool IDs, multiple tool results, system-role differences, unsupported attachments and content-omitting exports.
- **Limit:** adapters cannot promise equivalent model behavior; media bytes are not fetched or rendered.

### 4. Webhook Signature Fixture Lab — IT integration security
**Candidate slug:** `webhook-signature-fixture-lab`  
**Problem:** seemingly harmless body normalization can break signature verification, while timestamp handling can accidentally accept stale requests.

- **Inputs:** synthetic payload bytes, test-only secrets, signed-header examples and a supplied verification time/tolerance.
- **MVP:** native Web Crypto HMAC verification for two documented signature formats; compare exact body bytes, canonical signed strings and replay-window checks. Include expected-pass and expected-fail fixtures.
- **Outputs:** byte/digest mismatch explanations and receiver-side verification test vectors.
- **Boundary:** no live webhook receiver, delivery platform, retry manager, arbitrary endpoint calls or production secret storage. Complements the [existing webhook management service inventory](https://github.com/Zion-support/zion-support.github.io/blob/main/data/services.json) and Retry Safety Lab.
- **Acceptance tests:** changed whitespace, UTF-8 payloads, malformed signatures, stale/future timestamps and multiple signature-header versions.
- **Limit:** timestamp checking is not a durable replay store, and valid signatures do not replace authorization or server-side idempotency.

### 5. CSP Policy Explainer — IT browser security
**Candidate slug:** `csp-policy-explainer`  
**Problem:** a resource can load under one Content Security Policy and fail under another; weakening the policy is not a sound debugging strategy.

- **Inputs:** an origin, one or more CSP header values, and hypothetical resource URL/type/nonce metadata.
- **MVP:** explain common directive fallbacks and policy intersections; distinguish report-only from enforcement; compare before/after decisions for explicit sources, schemes, self, nonces and hashes.
- **Outputs:** resource-by-resource reasoning and a policy diff, without loading resources or executing content.
- **Boundary:** separate from CORS/cookie handling, TLS scanning, uptime monitoring or general security posture scoring. It must not suggest blanket `unsafe-inline`/`unsafe-eval` bypasses.
- **Acceptance tests:** multiple enforcing policies, report-only policies, missing directive fallbacks, nonce mismatch and conditional `strict-dynamic` cases.
- **Limit:** dynamic trust and DOM-dependent cases must be marked conditional/unknown when context is insufficient, not claimed browser-conformant.

### 6. Cron & DST Previewer — IT scheduling reliability
**Candidate slug:** `cron-dst-previewer`  
**Problem:** a wall-clock schedule can skip or repeat local times when daylight-saving transitions occur.

- **Inputs:** a five-field cron expression, an IANA time zone and a bounded preview date window.
- **MVP:** validate documented cron syntax, preview upcoming UTC/local occurrences with native `Intl` time-zone data, and highlight repeated or missing wall-clock candidates. Make chosen DST execution semantics explicit.
- **Outputs:** a local calendar/timeline and JSON/CSV preview with UTC offsets and duplicate-local-time flags.
- **Boundary:** not job execution, cron health monitoring, calendar booking, technician scheduling or patch-window planning. Complements the existing CronJob Manager / TimeZone service concepts in the [service inventory](https://github.com/Zion-support/zion-support.github.io/blob/main/data/services.json).
- **Acceptance tests:** spring-forward gaps, fall-back repeats, no-DST zones, month/day boundaries and invalid expressions.
- **Limit:** time-zone databases and cron schedulers differ; a preview is not a guarantee of a particular server's execution behavior. Bound computation and disclose the supported cron dialect.

## Delivery and release gates

1. **Approve scope first:** choose candidate(s), resolve any actual overlap, and separately approve repository creation/publication. This roadmap does not authorize or create six more repositories.
2. **Keep the static architecture:** `index.html`, `styles.css`, `app.js`, README, NETWORK, synthetic examples/tests and `.nojekyll`; optional additional local assets only when justified. No mandatory packages, backend, inference calls or external runtime scripts.
3. **Build genuine analysis:** deterministic behavior where possible, input/compute bounds, unknown-state handling and clear non-goals. No fake scores or security claims.
4. **Test:** pure-engine fixtures, actual-browser input/output and export flows, safe text rendering, mobile layout, keyboard labels/focus and no unexpected network requests. Never commit real credentials or customer captures.
5. **Publish and verify:** public repository, correct branch-root Pages source, `https_enforced=true`, successful Pages build, TLS-verified HTTP 200 and correct deployed bytes.
6. **Interlink after acceptance:** add the launch card to the hub, link the new app back to the hub and relevant siblings, and record a dated status observation. Never label a roadmap-only idea as live.

Suggested sequencing: first prove demand for one AI portability/evidence tool and one IT policy/integration tool; expand only after real use and overlap review. The six scopes are not a commitment to simultaneous launch.
