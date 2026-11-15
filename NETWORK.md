# Seven-repository network and locale contract

Owner: [saipradikmallakuntla-tech](https://github.com/saipradikmallakuntla-tech). Current expansion: Batch 99, 2026-11-15 UTC. Historical four-node reports are retained unchanged.

- [Zion AI Apps Hub](https://saipradikmallakuntla-tech.github.io/zion-ai-apps-hub/) · [source](https://github.com/saipradikmallakuntla-tech/zion-ai-apps-hub)
- [LLM Stream Inspector](https://saipradikmallakuntla-tech.github.io/llm-stream-inspector/) · [source](https://github.com/saipradikmallakuntla-tech/llm-stream-inspector)
- [Agent Retry Safety Lab](https://saipradikmallakuntla-tech.github.io/agent-retry-safety-lab/) · [source](https://github.com/saipradikmallakuntla-tech/agent-retry-safety-lab)
- [CORS & Cookie Doctor](https://saipradikmallakuntla-tech.github.io/cors-cookie-doctor/) · [source](https://github.com/saipradikmallakuntla-tech/cors-cookie-doctor)
- [Prompt Token Budget Lab](https://saipradikmallakuntla-tech.github.io/prompt-token-budget-lab/) · [source](https://github.com/saipradikmallakuntla-tech/prompt-token-budget-lab)
- [Tool Schema Drift Auditor](https://saipradikmallakuntla-tech.github.io/tool-schema-drift-auditor/) · [source](https://github.com/saipradikmallakuntla-tech/tool-schema-drift-auditor)
- [Webhook Replay Guard](https://saipradikmallakuntla-tech.github.io/webhook-replay-guard/) · [source](https://github.com/saipradikmallakuntla-tech/webhook-replay-guard)

## Required directed graph

Each repository root page links directly to the other six nodes: **42 non-self directed edges**, not 42 apps. EN/ES/PT hub views share six satellite destinations. Discovery has equivalent complete static views at `batch-99-discovery.html`, `es/batch-99-discovery.html`, and `pt/batch-99-discovery.html`; native language navigation works without JavaScript. Satellite interfaces remain English-only.

| From / to | Hub | Stream | Retry | CORS | Budget | Schema | Replay |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Hub | — | required | required | required | required | required | required |
| Stream | required | — | required | required | required | required | required |
| Retry | required | required | — | required | required | required | required |
| CORS | required | required | required | — | required | required | required |
| Budget | required | required | required | required | — | required | required |
| Schema | required | required | required | required | required | — | required |
| Replay | required | required | required | required | required | required | — |

## Privacy and deployment contract

1. Each app is independently useful and owns local HTML/CSS/JS. No runtime backend, shared script host, model API, uploads, telemetry or persistence.
2. Use canonical HTTPS app links with repository prefix and trailing slash. Never append diagnostic input or secrets to navigation URLs.
3. Publish `main:/` with `.nojekyll` and enforced HTTPS. No custom domain, CNAME or DNS change.
4. Hub filtering and diagnostic recommendations are local progressive enhancements. Static cards, documentation, locale links and app navigation remain usable without JavaScript.
5. Discovery collects only predefined symptom/evidence categories. Copy/export/mailto draft are explicit user actions; summaries omit raw evidence and mailto never sends automatically. Review any draft before sending. Clipboard/mail-client support is browser-dependent.
6. Token budgets are heuristics; schema drift is a partial structural model; replay decisions are a sequential in-memory simulation. None is certification, a production guard or an exactly-once guarantee.
7. Do not modify third-party repositories or imply upstream registration/endorsement. The six historical roadmap proposals are not launched apps. Preserve earlier dated reports as historical evidence.

See [Batch 99 release evidence](BATCH_99_NETWORK_EXPANSION_RELEASE.md) and [the historical roadmap](NEXT_BATCH_ROADMAP.md). HTTP checks are dated observations, not uptime monitoring or semantic/security proof.
