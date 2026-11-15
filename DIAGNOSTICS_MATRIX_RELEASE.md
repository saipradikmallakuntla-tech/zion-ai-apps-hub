# Failure-Mode Diagnostics Matrix & Cross-App Triage Guide — release evidence

Batch: `zion-diagnostics-matrix-2026-11-15-en-es-pt`  
Owner: `saipradikmallakuntla-tech`  
Date: 2026-11-15 UTC  
Container: `zion_app_network`  
Parent progress checkpoint: `6BT7igZuD59TQW6RB8qePW`  
Earlier architecture checkpoint: `iAR9z4Fkaw62TrB4BHoTUw`

## Delivered and verified

Three fully equivalent English, Spanish and Portuguese guides contain nine failure-mode rows, three two-destination handoff sections, a bounded triage path, sanitized-evidence guidance and explicit limitations. Each has a caption, five column headers, nine row headers, one h1/main landmark, a focusable skip target, native section/language navigation, correct document lang, self-canonical HTTPS URL, reciprocal en/es/pt hreflang and English x-default. The new guides contain no scripts or forms.

All three existing localized homepages promote the guide outside app filters while retaining their three utility cards, prior showcases and architecture changelog. Each satellite index.html, README.md and NETWORK.md adds two manual handoff recipes with triggers, minimal sanitized evidence, next actions and limits. The network retains all 12 directed four-node links; the new matrix has nine HTML satellite locale returns and 27 returns across the nine edited satellite files. No diagnostic input is encoded in navigation URLs.

Only the four approved owned repositories changed. Eight runtime JavaScript/CSS assets, nine prior showcase/changelog pages, historical reports, existing engines/interfaces, .nojekyll and Pages/DNS settings are preserved. The utility interfaces remain English-only; full EN/ES/PT parity applies to hub documentation. No third-party repository, backend, telemetry, model API, catalog or upstream registration was modified.

## Live canonical pages

- [English diagnostics matrix](https://saipradikmallakuntla-tech.github.io/zion-ai-apps-hub/diagnostics-matrix.html) · [English hub](https://saipradikmallakuntla-tech.github.io/zion-ai-apps-hub/)
- [Español diagnostics matrix](https://saipradikmallakuntla-tech.github.io/zion-ai-apps-hub/es/diagnostics-matrix.html) · [Español hub](https://saipradikmallakuntla-tech.github.io/zion-ai-apps-hub/es/)
- [Português diagnostics matrix](https://saipradikmallakuntla-tech.github.io/zion-ai-apps-hub/pt/diagnostics-matrix.html) · [Português hub](https://saipradikmallakuntla-tech.github.io/zion-ai-apps-hub/pt/)
- [llm-stream-inspector](https://saipradikmallakuntla-tech.github.io/llm-stream-inspector/)
- [agent-retry-safety-lab](https://saipradikmallakuntla-tech.github.io/agent-retry-safety-lab/)
- [cors-cookie-doctor](https://saipradikmallakuntla-tech.github.io/cors-cookie-doctor/)

## Direct content commits

- [Guides and initial pending report](https://github.com/saipradikmallakuntla-tech/zion-ai-apps-hub/commit/ac7548536f568b04f6bcd445204431b1b498c367)
- [Localized homepage promotions and static harness](https://github.com/saipradikmallakuntla-tech/zion-ai-apps-hub/commit/04a3ef5e6dedcc9fbaa336994aeeb0af3e4b0da7)
- [Stream handoffs](https://github.com/saipradikmallakuntla-tech/llm-stream-inspector/commit/6e10eb6a5bfedffee04b05821fd254c3a9b2b16c)
- [Retry handoffs](https://github.com/saipradikmallakuntla-tech/agent-retry-safety-lab/commit/5694bf05bbe395ea7b2dfc5117e09f7ca61e306c)
- [CORS handoffs](https://github.com/saipradikmallakuntla-tech/cors-cookie-doctor/commit/61f0b433a19c4208b253b203eef9105f929cdd39)

## Observed verification

- Certificate-validated HTTPS GET completed at **2026-11-15T10:52:29.807841+00:00**: **36/36 resources returned HTTP 200 and matched exact committed source bytes**, Git blob hashes and SHA-256 hashes. This includes 18 canonical HTML pages, three explicit homepage index aliases, six satellite Markdown documents, eight runtime assets and the new source harness. All passed on the first round.
- Request limits: 5-second connect and 10-second request timeout; four concurrent lightweight curl processes; at most three rounds. Redirects were not followed; no TLS certificate exception or insecure option was used.
- Fresh post-commit source checks passed under a 15-second cap per command: matrix harness **1,949 assertions / 369 owned links and fragments / 18 canonical HTML pages**; all three localization/filter checks; existing Legal/Compliance/Care harness **228 assertions**; existing network harness **797 assertions / 261 owned-link checks**. Node was v24.22.1.
- Immutable Git trees independently match all prepared bytes and the exact 17-path content allowlist: 12 modified baseline blobs and five additions, no deletions or unexpected edits. All 40 other baseline blobs remain unchanged. The final evidence commit adds the verification JSON and replaces only this initially pending report.
- Initial S3-mounted preparation checks hit their timeouts and are not passing evidence. The same existing checks passed on tmpfs; the new Python harness memoizes reads. The fresh post-commit runs above are the authoritative source-check observations.

## Evidence and reproduction

[Machine-readable verification receipt](DIAGNOSTICS_MATRIX_VERIFICATION.json) lists the immutable source commits, baseline/tree reconciliation, per-resource hashes, source-check results and preserved-file pins. [Bounded matrix source harness](tests/diagnostics-matrix.test.py) uses Python's standard library only.

Place the four checkouts side by side and run from the hub on a local filesystem, with a 15-second timeout for each command:

```sh
python3 tests/diagnostics-matrix.test.py --output matrix-results.json
node tests/localization.test.cjs
node tests/legal-compliance-care.test.cjs
node tests/network-interlinks.test.cjs
```

For live resources, use certificate-validating HTTPS GET with no insecure option; compare both `sha256(body)` and `sha1("blob " + byte_length + NUL + body)` to the committed bytes. The receipt covers content/runtime resources before its own publication. The report and receipt are then checked separately after the evidence commit, with those two observed hashes/statuses recorded in the final Supermemory completion checkpoint to avoid self-reference.

## Continuation reconciliation and limits

The older architecture/interlinks checkpoint described homepage promotions and satellite notes as uncommitted, but they were already on the captured main refs. This batch extended those files rather than duplicating them. The older NETWORK_INTERLINK_BATCH_RELEASE.md remains historical and explicitly unfinished; no old receipt was silently relabeled. This cycle independently verifies the actual current navigation and deployed bytes.

Mem0 remains **blocked_credential_encoding_no_new_call**. No Mem0 call was made during implementation or this resumption. Chromium workers, rendered/mobile/keyboard/browser interaction audits and fresh engine self-tests were **not run** and are not claimed as passed. Historical 33/33 engine results are not new results. Exact preserved/live asset hashes establish that the engine bytes did not change, not that a fresh engine run occurred.

These are offline diagnostic aids, not production benchmarks, security certificates, semantic-correctness proof, browser-conformance proof, exactly-once guarantees, monitoring or an SLA. Handoffs require manual sanitization and authorization; no automatic secret scanner is claimed. Actual mutation outcomes require server-side reconciliation before replay.
