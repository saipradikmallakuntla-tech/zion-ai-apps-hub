# Shared Terminology & Localization Glossary — Zion Apps Network

Owner: saipradikmallakuntla-tech  
Editorial date: 2026-11-16 UTC  
Batch: `zion-service-triage-glossary-2026-11-16-en-es-pt`  
Revision: G-v1; content IDs G01–G14  
State: Owner-authorized editorial reference; human language/domain review pending.

[English](#en) · [Español](#es) · [Português](#pt)

## Authority and source crosswalk

This plain-language reference makes existing meanings easier to find; it is not a competing claims policy or replacement translation baseline. [Restoration terminology](MULTILINGUAL_CONTENT_RESTORATION.md), [claims C01–C12](LEGAL_COMPLIANCE_CARE_EDITORIAL_PLAN.md), [parity controls T0–T13](TRANSLATION_PARITY_REGISTER.md), [operations O01–O06](MULTILINGUAL_ENTERPRISE_OPERATIONS.md), and [handoffs H00–H06](CROSS_REPOSITORY_HANDOFF_PLAN.md) remain authoritative. Source baseline: [hub c7f8780](https://github.com/saipradikmallakuntla-tech/zion-ai-apps-hub/commit/c7f8780367b6c485a33bf29528cca0f2575fdb28). The O04 counting clarification is logged in the approved operations update; it does not rewrite the historical 30-ID/90-entry baseline.

G01 maps to T0, G02 to T1, and so on through G14 to T13. G-IDs identify these new reader-facing editorial units, not new policies or additional products. Each table below contains the same fourteen meanings. The [service runbook](SERVICE_TRIAGE_ESCALATION_RUNBOOK.md) applies them; the parity register owns locale/source/review tracking. Exact publication commits and API read-back receipts are recorded after execution, not invented here.

## EN

### EN — How to use this reference

Choose the established term and retain its limitation when shortening copy. Translate meaning, not identical word counts. Keep product/repository names, content/control IDs, batch keys, technical tokens such as Origin, SameSite, Secure and HttpOnly, and canonical URLs literal. Use neutral Spanish and Portuguese without a new regional-locale commitment. Proposed alternatives or contradictions go to content operations and designated language/domain reviewers before a later revision.

| ID / source | Preferred term | Plain-language meaning and protected boundary |
| --- | --- | --- |
| G01 / T0 | Four-repository scope | One hub plus Stream, Retry and CORS. Wider references and roadmap proposals are context, not permission to add repositories or announce launches. |
| G02 / T1 | Saved capture; structural finding | A previously saved stream and an observation about its format. Not live monitoring, semantic correctness, a lossless-capture guarantee or permission to execute arguments. |
| G03 / T2 | Stable intent key; retention expiry | Identity kept across attempts for one logical operation, with a modeled retention end. Not a provider-contract check or exactly-once guarantee; jitter changes timing, not identity. |
| G04 / T3 | Response access; cookie eligibility | Whether browser code may read a response versus conditions for cookie sending. Neither proves authorization, consent, storage/transmission or whether the server acted. |
| G05 / T4 | Legal, Compliance & Care practices | Nine documentation practices, not nine apps. Care means operational support, not clinical care; documentation is not professional advice or certification. |
| G06 / T5 | Synthetic reference | An illustrative fixture or model value, not a customer endorsement, production benchmark, SLA or fresh measurement. Preserve its source and date. |
| G07 / T6 | Manual evidence handoff | A minimized, permitted summary reviewed by a person. Not an automatic sanitizer, state transfer, shared execution ledger or replay authorization. |
| G08 / T7 | Written; human review pending | Complete wording exists, but actual language/domain decisions are outstanding. W/P is not approved, certified or distributed, even after publication or ingestion. |
| G09 / T8 | Intake record; accountable owner | A private request record and the role responsible for the next decision. Not a deployed intake service, assigned individual, scheduled notification or invented reviewer. |
| G10 / T9 | Correction; distribution hold | An attributable wording correction or pause in downstream use pending review. Not proof that content was recalled/deleted or an incident resolved. |
| G11 / T10 | Reported historical result; evidence unavailable | A dated source reports an observation, or supporting evidence is absent from the reviewed inventory. Neither means a new passing test; unavailable is not failed or passed. |
| G12 / T11 | English-only interface | All three scoped utility interfaces remain in English. EN/ES/PT editorial coverage does not localize software or certify native-language review. |
| G13 / T12 | Receiver acknowledgment | A real private acceptance of purpose, exact source revision, permitted summary, uncertainties and next owner. Not a link click, automatic event or unassigned role. |
| G14 / T13 | Proposed adoption discussion; documentary acceptance | Unexecuted discussion/review criteria for choosing and explaining a bounded utility. Not an executed pilot, deployment decision, measured adoption or completed software test. |

### EN — Usage, counting and review

Avoid “all interfaces translated,” “fully compliant,” “guaranteed secure,” “automatic sanitization,” “production-proven,” or “exactly once” as product promises. Use “written; review pending,” “documented historical result,” or “evidence unavailable” where applicable. CORS is not authentication, authorization or consent; a timeout or hidden response is not proof of no server effect. Cookie eligibility is not storage/transmission proof. Unavailable timing is not zero; valid JSON is not execution permission.

A logical content ID counts once; its EN, ES and PT versions make three locale entries. Thus the original 30-ID baseline had 90 entries total, 30 per language—not 90 per language. Historical 41/123 and reconciled 51/153 totals are dated snapshots; use the latest dated parity extension for new totals. Controls T0–T13 are not extra translated assets counted again on top of their G crosswalk.

Keep private decisions, reviewer identities, credentials, raw/customer evidence and service receipts out of public Markdown and URLs. Human language/domain, receiving-role and channel decisions remain pending; distribution needs separate authorization. No automatic synchronization, monitoring, SLA, professional advice, certification, software change, tests, hashes, browser checks or live probes are introduced.

## ES

### ES — Cómo usar esta referencia

Elija el término establecido y conserve su límite al abreviar. Traduzca significado, no un número idéntico de palabras. Mantenga literales nombres de productos/repositorios, ID de contenido/control, claves de lote, elementos técnicos como Origin, SameSite, Secure y HttpOnly y URL canónicas. Use español neutro y portugués sin prometer una variante regional nueva. Remita alternativas o contradicciones a operaciones de contenido y revisores lingüísticos/de dominio designados antes de una revisión posterior.

| ID / fuente | Término preferido | Significado sencillo y límite protegido |
| --- | --- | --- |
| G01 / T0 | Alcance de cuatro repositorios | Un hub más Stream, Retry y CORS. Las referencias ampliadas y propuestas son contexto, no permiso para añadir repositorios o anunciar lanzamientos. |
| G02 / T1 | Captura guardada; hallazgo estructural | Flujo guardado previamente y observación de su formato. No monitorización en vivo, corrección semántica, garantía de captura sin pérdidas ni permiso de ejecutar argumentos. |
| G03 / T2 | Clave estable de intención; vencimiento del período de retención | Identidad conservada entre intentos de una operación lógica, con fin de retención modelado. No verifica contratos ni garantiza ejecución exactamente una vez; jitter cambia tiempos, no identidad. |
| G04 / T3 | Acceso a la respuesta; condiciones de envío de cookies | Si el código del navegador puede leer una respuesta frente a condiciones de envío de cookies. No prueba autorización, consentimiento, almacenamiento/envío ni si actuó el servidor. |
| G05 / T4 | Prácticas Legal, Compliance & Care; Atención operativa | Nueve prácticas documentales, no nueve aplicaciones. Atención significa apoyo operativo, no clínico; la documentación no es asesoramiento profesional ni certificación. |
| G06 / T5 | Referencia sintética | Valor de muestra o modelo ilustrativo, no testimonio de clientes, medición de producción, SLA ni resultado nuevo. Conserve fuente y fecha. |
| G07 / T6 | Transferencia manual de evidencia | Resumen mínimo y permitido revisado por una persona. No depuración automática, transferencia de estado, registro compartido de ejecución ni autorización de repetición. |
| G08 / T7 | Escrito; revisión humana pendiente | Existe redacción completa, pero faltan decisiones reales de idioma/dominio. W/P no significa aprobado, certificado ni distribuido, aun tras publicación o incorporación. |
| G09 / T8 | Registro de solicitud; propietario responsable | Registro privado y rol responsable de la siguiente decisión. No servicio desplegado, persona asignada, notificación programada ni revisor inventado. |
| G10 / T9 | Corrección; pausa de distribución | Corrección atribuible de texto o pausa del uso posterior para revisión. No prueba retirada/eliminación de contenido ni resolución de incidentes. |
| G11 / T10 | Resultado histórico documentado; evidencia no disponible | Una fuente fechada informa de una observación, o falta respaldo en el inventario revisado. No es una prueba nueva superada; no disponible no significa fallido ni superado. |
| G12 / T11 | Interfaz solo en inglés | Las tres interfaces incluidas siguen en inglés. El contenido editorial EN/ES/PT no localiza software ni certifica revisión nativa. |
| G13 / T12 | Confirmación del receptor | Aceptación privada real de propósito, revisión exacta, resumen permitido, incertidumbres y siguiente responsable. No un clic, evento automático ni rol sin asignar. |
| G14 / T13 | Conversación de adopción propuesta; aceptación documental | Criterios de conversación/revisión sin ejecutar para elegir y explicar una utilidad acotada. No piloto ejecutado, decisión de despliegue, adopción medida ni prueba completada. |

### ES — Uso, conteo y revisión

Evite prometer «todas las interfaces traducidas», «cumplimiento total», «seguridad garantizada», «depuración automática», «probado en producción» o «exactamente una vez». Use «escrito; revisión pendiente», «resultado histórico documentado» o «evidencia no disponible», según corresponda. CORS no es autenticación, autorización ni consentimiento; timeout o respuesta oculta no prueba ausencia de efecto del servidor. Elegibilidad de cookies no prueba almacenamiento/envío. Tiempo no disponible no es cero; JSON válido no permite ejecutar acciones.

Un ID lógico se cuenta una vez; sus versiones EN, ES y PT forman tres entradas de idioma. La base original de 30 ID tenía 90 entradas en total, 30 por idioma, no 90 por idioma. Los totales históricos 41/123 y conciliados 51/153 son instantáneas fechadas; consulte la última extensión de paridad para nuevos totales. Los controles T0–T13 no se vuelven a contar como activos traducidos adicionales a su correspondencia G.

No publique decisiones privadas, identidades de revisores, credenciales, evidencia bruta/de clientes ni comprobantes de servicios en Markdown o URL. Siguen pendientes decisiones lingüísticas/de dominio, receptores y canales; distribuir requiere autorización separada. No se añade sincronización automática, monitorización, SLA, asesoramiento profesional, certificación, software, pruebas, hashes, navegador ni sondeos en vivo.

## PT

### PT — Como usar esta referência

Escolha o termo estabelecido e preserve seu limite ao abreviar. Traduza significado, não quantidade idêntica de palavras. Mantenha literais nomes de produtos/repositórios, IDs de conteúdo/controle, chaves de lote, elementos técnicos como Origin, SameSite, Secure e HttpOnly e URLs canônicas. Use espanhol neutro e português sem prometer nova variante regional. Encaminhe alternativas ou contradições a operações de conteúdo e revisores linguísticos/de domínio designados antes de revisão posterior.

| ID / fonte | Termo preferido | Significado simples e limite protegido |
| --- | --- | --- |
| G01 / T0 | Escopo de quatro repositórios | Um hub mais Stream, Retry e CORS. Referências ampliadas e propostas são contexto, não permissão para adicionar repositórios ou anunciar lançamentos. |
| G02 / T1 | Captura salva; constatação estrutural | Fluxo salvo anteriormente e observação de seu formato. Não monitoramento em tempo real, correção semântica, garantia de captura sem perdas ou permissão para executar argumentos. |
| G03 / T2 | Chave estável de intenção; expiração do período de retenção | Identidade mantida entre tentativas de uma operação lógica, com fim de retenção modelado. Não verifica contratos ou garante execução exatamente uma vez; jitter muda tempo, não identidade. |
| G04 / T3 | Acesso à resposta; condições de envio de cookies | Se o código do navegador pode ler resposta versus condições de envio de cookies. Não prova autorização, consentimento, armazenamento/envio ou se o servidor agiu. |
| G05 / T4 | Práticas Legal, Compliance & Care; Cuidado operacional | Nove práticas documentais, não nove aplicativos. Cuidado significa apoio operacional, não clínico; documentação não é aconselhamento profissional ou certificação. |
| G06 / T5 | Referência sintética | Valor de amostra ou modelo ilustrativo, não depoimento de cliente, medição de produção, SLA ou resultado novo. Preserve fonte e data. |
| G07 / T6 | Encaminhamento manual de evidências | Resumo mínimo e permitido revisado por uma pessoa. Não sanitização automática, transferência de estado, registro compartilhado de execução ou autorização de repetição. |
| G08 / T7 | Escrito; revisão humana pendente | Existe redação completa, mas faltam decisões reais de idioma/domínio. W/P não significa aprovado, certificado ou distribuído, mesmo após publicação ou incorporação. |
| G09 / T8 | Registro da solicitação; proprietário responsável | Registro privado e papel responsável pela próxima decisão. Não serviço implantado, pessoa designada, notificação agendada ou revisor inventado. |
| G10 / T9 | Correção; pausa da distribuição | Correção atribuível de texto ou pausa do uso posterior para revisão. Não prova retirada/exclusão de conteúdo ou resolução de incidente. |
| G11 / T10 | Resultado histórico documentado; evidência indisponível | Fonte datada relata uma observação, ou falta respaldo no inventário revisado. Não é novo teste aprovado; indisponível não significa reprovado nem aprovado. |
| G12 / T11 | Interface somente em inglês | As três interfaces incluídas continuam em inglês. Conteúdo editorial EN/ES/PT não localiza software nem certifica revisão nativa. |
| G13 / T12 | Confirmação do receptor | Aceitação privada real de finalidade, revisão exata, resumo permitido, incertezas e próximo responsável. Não clique, evento automático ou papel sem atribuição. |
| G14 / T13 | Discussão de adoção proposta; aceitação documental | Critérios de discussão/revisão não executados para escolher e explicar utilitário delimitado. Não piloto executado, decisão de implantação, adoção medida ou teste concluído. |

### PT — Uso, contagem e revisão

Evite prometer “todas as interfaces traduzidas”, “conformidade total”, “segurança garantida”, “sanitização automática”, “comprovado em produção” ou “exatamente uma vez”. Use “escrito; revisão pendente”, “resultado histórico documentado” ou “evidência indisponível”, conforme o caso. CORS não é autenticação, autorização ou consentimento; timeout ou resposta oculta não prova ausência de efeito no servidor. Elegibilidade de cookies não prova armazenamento/envio. Tempo indisponível não é zero; JSON válido não permite executar ações.

Um ID lógico conta uma vez; suas versões EN, ES e PT formam três entradas de idioma. A base original de 30 IDs tinha 90 entradas no total, 30 por idioma, não 90 por idioma. Totais históricos 41/123 e reconciliados 51/153 são retratos datados; consulte a última extensão de paridade para novos totais. Controles T0–T13 não são contados novamente como ativos traduzidos adicionais à correspondência G.

Não publique decisões privadas, identidades de revisores, credenciais, evidência bruta/de clientes ou comprovantes de serviços em Markdown ou URLs. Continuam pendentes decisões linguísticas/de domínio, receptores e canais; distribuição exige autorização separada. Não se acrescenta sincronização automática, monitoramento, SLA, aconselhamento profissional, certificação, software, testes, hashes, navegador ou sondagens em tempo real.

## Maintenance

G01–G14 are fourteen new reader-facing units with 42 written/pending locale entries. They restate existing T0–T13 meanings without adding fourteen policies or products. Language/domain reviewers remain to be designated. Record actual feedback by G-ID, locale, exact revision, affected source control, decision, reviewer and UTC date privately. Source, wording, notice or destination changes reopen affected gates. Do not alter canonical source decks, claims controls, handoff recipes or historical archives through this glossary.
