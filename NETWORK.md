# Four-repository interlinking architecture

Owner: [saipradikmallakuntla-tech](https://github.com/saipradikmallakuntla-tech)

```text
                    zion-ai-apps-hub
                   /       |       \
                  /        |        \
     llm-stream-inspector  |   cors-cookie-doctor
                  \        |        /
                   agent-retry-safety-lab
```

The diagram is conceptual; the actual navigation graph is fully connected: the hub links to all three satellites, and each satellite links to the hub and both sibling apps.

| Repository | Live HTTPS URL | Responsibility |
| --- | --- | --- |
| [zion-ai-apps-hub](https://github.com/saipradikmallakuntla-tech/zion-ai-apps-hub) | https://saipradikmallakuntla-tech.github.io/zion-ai-apps-hub/ | Discovery, app cards, source links, architecture and roadmap |
| [llm-stream-inspector](https://github.com/saipradikmallakuntla-tech/llm-stream-inspector) | https://saipradikmallakuntla-tech.github.io/llm-stream-inspector/ | Saved SSE/NDJSON framing and tool-argument diagnostics |
| [agent-retry-safety-lab](https://github.com/saipradikmallakuntla-tech/agent-retry-safety-lab) | https://saipradikmallakuntla-tech.github.io/agent-retry-safety-lab/ | Offline nested retries, duplicate effects and idempotency retention |
| [cors-cookie-doctor](https://github.com/saipradikmallakuntla-tech/cors-cookie-doctor) | https://saipradikmallakuntla-tech.github.io/cors-cookie-doctor/ | Browser CORS, preflight, credentials and cookie-policy reasoning |

## Link and privacy contract
1. Use canonical absolute HTTPS URLs with the repository prefix and trailing slash.
2. Every app must offer a hub link and direct links to its siblings. The hub must provide a working app card and source link for each launched satellite.
3. Links carry no captures, headers, cookies, prompts, secrets or scenario parameters.
4. Applications are independent static deploys. No shared hosted script, iframe, backend, authentication service or mandatory runtime package couples their availability.
5. Use repository-relative `./styles.css` and `./app.js` assets. Publish `main:/` with `.nojekyll` and HTTPS enforcement; do not add custom-domain CNAME records unless separately approved.
6. A proposed app remains a roadmap entry, not a live product card, until a real implementation, tests and HTTPS deployment are verified.

See [NEXT_BATCH_ROADMAP.md](NEXT_BATCH_ROADMAP.md#https-and-deployment-status) for dated deployment observations. A link is not an uptime guarantee.

The broader [Zion reference network](https://ziontechgroup.com/) and [original master catalog](https://github.com/Zion-support/zion-app-network/blob/main/CATALOG.md) remain separate. This release does not change their repositories, catalogs, APIs or DNS.
