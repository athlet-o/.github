# AthletO web/API connection patterns

Status: organization architecture guidance, tracked by [DEN-4254](https://linear.app/denman/issue/DEN-4254/flesh-out-athlet-o-commerce-marketing-webapi-split-and-shared-data).

This policy applies to the customer-facing Rust web/BFF, the Rust JSON API, background workers, and `athleto-lib-core`. A repository ADR may narrow these choices for a specific service, but it must not weaken the identity, authorization, payment, or data-boundary rules below.


> **Persistence authority (2026-08-29):** Product SQL and ORM generation are owned in this org’s `*-lib-core` under the dual TypeSpec (P0) + authored JSON Schema (P1) model. Diesel + diesel-async is the primary Rust runtime; SeaORM is secondary. See [`docs/PERSISTENCE_DUAL_SOURCE.md`](docs/PERSISTENCE_DUAL_SOURCE.md). Claims that `ORESoftware/k8s-libs-and-shared-defs` authors this org’s product tables, or that SeaORM is the sole Rust ORM / schema authority, are superseded for product persistence.

## Ownership boundaries

- The browser talks to the web/BFF. The BFF owns HTML, the opaque secure session cookie, CSRF protection, and OAuth authorization-code plus PKCE flow.
- The API owns product authorization, customer-private reads, every mutation, inventory and checkout orchestration, and the versioned JSON contract from `athleto-interfaces`.
- `athleto-lib-core` owns typed SeaORM entities, scoped query helpers, transaction behavior, and the application-facing schema boundary. It does not decide whether a user may perform a product action.
- `ORESoftware/k8s-libs-and-shared-defs` owns the canonical DDL and forward migrations. Services verify the expected schema at startup; they never migrate production at boot.
- `ORESoftware/k8s-cluster` owns deployment composition, secrets wiring, ingress, and cloud placement. The service repositories keep deployable manifests and health contracts.

## Choose one of four avenues

| Avenue | Use it when | Do not use it for | Required controls |
| --- | --- | --- | --- |
| Direct database read | A named, stable, non-sensitive read projection has a measured latency or availability need that HTTP cannot meet | Customer-private data, identity, carts, orders, gift cards, payments, inventory, or any write | Distinct `SELECT`-only role, `READ ONLY` transaction, non-owner and `NOBYPASSRLS`, explicit projection, deadline, audit telemetry |
| Stateless HTTP/JSON | The BFF needs a synchronous answer from the API | Unbounded streams or fire-and-forget effects | Default avenue; typed/versioned interfaces, bounded bodies and timeouts, propagated correlation context, idempotency for mutations, retry budget |
| Stateful TCP | A measured low-latency subscription or high-frequency stream cannot fit HTTP | Checkout, authorization authority, database writes, or ordinary request/response traffic | ADR, mTLS or authenticated sidecar, delegated identity, bounded frames, deadlines, backpressure, reconnect policy, correlation IDs |
| NATS/message queue | A durable effect should happen asynchronously after the authoritative transaction commits | Login, interactive authorization, payment approval, inventory reservation, or the response the customer is waiting for | Transactional outbox, durable subject, idempotent consumer, retry/dead-letter policy, schema version, trace context |

Stateless HTTP is the normal answer. Direct reads, stateful TCP, and messaging are explicit exceptions for specific access shapes; they are not interchangeable shortcuts.

## Request decision procedure

1. If the operation changes state or touches customer-private, identity, financial, inventory, gift-card, or order data, call the API over HTTP.
2. If the caller needs an immediate authoritative answer, call the API over HTTP.
3. If the work is a post-commit side effect, publish it from a transactional outbox to NATS.
4. If the workload is a measured high-frequency stream, record an ADR before adding bounded stateful TCP.
5. Only then consider a direct database read, and only for a named public/read-model projection with a dedicated restricted role.

The web/BFF must fail closed when the selected avenue is unavailable. It must not silently fall back from API authorization to a direct query or from a durable publish to an in-memory task.

## Identity and authorization

Shared Auth proves identity and session assurance; it does not own AthletO carts, orders, promotions, gift cards, or payment permissions. Each authenticated request validates the expected realm, issuer, audience, tenant, app/client, scopes, session state, authentication freshness, and assurance level. Product authorization remains local to the API and is evaluated against the authenticated subject and resource.

Protected introspection uses a service credential for the API-to-Shared-Auth call while passing the user's token only in the introspection body. Do not substitute the service credential for user identity. Do not log bearer tokens, cookies, authorization codes, PKCE verifiers, card details, provider secrets, gift-card codes, or raw introspection responses.

Pin official Shared Auth clients to immutable revisions. Use `opto-sync` for declared synchronization/outbox workflows, `ores-otel` for trace and metric propagation with secret redaction, and `zed-pkg` for declared dependency provenance. These integrations do not move authorization or schema ownership out of the API/core boundaries.

## Commerce invariants

- Checkout creation is a mutation and always crosses the API boundary with an idempotency key.
- A Stripe or Coinbase redirect is navigation, not proof of settlement. Only a signature-verified, replay-safe, deduplicated provider webhook may advance payment state.
- Card data stays on the hosted payment provider. AthletO persists provider references and safe display metadata, never primary account numbers or security codes.
- Gift-card redemption, promotion application, inventory reservation, order creation, and payment state changes occur transactionally under the API's product authorization.
- Events are emitted from an outbox after the database transaction commits; a consumer must tolerate duplicate delivery.

## Deployment and public hosts

- `api.athleto.store` routes to the Rust API service.
- `app.athleto.store` and `user.athleto.store` route to the Rust web/BFF service.
- Readiness must prove required dependencies are usable. Liveness must not turn a transient dependency outage into a restart loop.
- Create and validate ingress/TLS before publishing DNS. DNS records do not grant permission to expose an unhealthy origin.

## Review checklist

Every service or endpoint review records:

- the chosen avenue and why the simpler/default path is insufficient;
- the data classification and authorization owner;
- timeout, body/frame limit, retry, idempotency, and backpressure behavior;
- failure and fallback behavior;
- schema/interface version and migration compatibility;
- trace propagation and secret/PII redaction;
- payment settlement evidence where money moves;
- the ADR and expiry/review date for any direct-read or TCP exception.

Executable examples and comments live with the AthletO web transport selector and API handlers. This organization document is the durable decision policy; code comments explain the local choice at the call site.
