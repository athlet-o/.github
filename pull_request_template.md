## Change summary

Describe the user-visible behavior, repositories/components affected, compatibility impact, and rollback path. Mark non-applicable checks as `N/A` with a reason.

## Review gates

### Change control and dependencies

- [ ] This work is on a topic branch; no direct default-branch commit is required.
- [ ] Cross-repository dependencies are pinned by immutable commit, lockfile, or released Zed package.
- [ ] Public contracts are generated from the canonical interface/schema source and consumer compatibility was checked.
- [ ] Breaking changes include migration, rollback, and staged rollout notes.

### SQL, persistence, and state

- [ ] No SQL changes, or every declaration has a stable organization/domain namespace and an explicit owning repository.
- [ ] Domain SQL may remain with its owning org, but identity, ordering, checksums, drift detection, and promotion are registered through `declarative-migrations`.
- [ ] Application startup validates schema compatibility and does not apply production DDL.
- [ ] Destructive changes, tenant isolation, RLS/authorization, idempotency, and state-machine invariants have evidence.

### Infrastructure and security

- [ ] Application manifests remain app-owned; cluster composition is delegated to `oresoftware/k8s-cluster` and shared components to `oresoftware/k8s-libs-and-shared-defs`.
- [ ] Workloads use least privilege, restricted pod security, explicit network policy, non-root execution, immutable images, and bounded resources where applicable.
- [ ] Secrets, credentials, personal data, and user content are excluded from source, logs, fixtures, and build artifacts.
- [ ] Authentication/authorization failures are fail-closed and sensitive operations are auditable.

### Verification and observability

- [ ] Zed lifecycle hooks run deterministic format, lint, build, contract, and publish checks.
- [ ] Unit, integration, adversarial, migration, and end-to-end tests cover the changed behavior in the appropriate test organization.
- [ ] ORES OTEL trace/correlation propagation is present where applicable, with secret and user-content capture disabled by default.
- [ ] Test evidence, residual risks, follow-up work, and any intentionally deferred repositories are listed below.

## Validation evidence and residual risk

Provide commands, checks, fixtures, test-org run links, migration/drift results, and known limitations.
