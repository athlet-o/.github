# `athlet-o` repository relationships

Generated from reviewed policy and the current **public** repository inventory.

- Public repositories declared: **3**
- Private repository names withheld: **9**
- Relationship edges: **6**

## Repository roles

| Repository | Role | Lifecycle |
|---|---|---|
| [`.github`](https://github.com/athlet-o/.github) | `organization_governance` | `active` |
| [`athleto-app-rs`](https://github.com/athlet-o/athleto-app-rs) | `application` | `active` |
| [`athlet-o.github.io`](https://github.com/athlet-o/athlet-o.github.io) | `site` | `active` |

## Declared edges

| From | Relationship | To | Status/basis |
|---|---|---|---|
| `athlet-o/.github` | `governs` | `athlet-o/athlet-o.github.io` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `athlet-o/.github` | `governs` | `athlet-o/athleto-app-rs` | `inferred` / `role-convention`: organization defaults, safety, and relationship declarations |
| `organization://athlet-o` | `coordinates_via` | `capability://fiducia-cloud/distributed-coordination` | `platform-default` / `explicit-platform-decision`: locks, leases, idempotency, elections, schedules, budgets, and task claims |
| `organization://athlet-o` | `authenticates_via` | `capability://shared-auth/human-identity` | `platform-default` / `explicit-platform-decision`: platform human identity and session authority |
| `organization://athlet-o` | `deployed_via` | `platform://ORESoftware/k8s-cluster` | `platform-default` / `platform-policy`: immutable artifacts are promoted by digest through GitOps |
| `organization://athlet-o` | `packaged_via` | `platform://zed-pkg` | `platform-default` / `platform-policy`: Zed resolves artifacts while submodules compose editable source |

## Composition, service, and observability contract

Git submodules compose editable source; Zed packages resolve packages/artifacts; dual-managed commits must match. Production deploys immutable image digests, not runtime source builds. Cross-service access uses APIs/SDKs/events rather than another service database. MCP uses the product API/SDK. Services emit OpenTelemetry traces, bounded metrics, and correlated structured logs.

## Privacy boundary

This public registry deliberately omits private repository names and edges; the count above makes the boundary explicit.
