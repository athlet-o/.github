# Persistence dual-source contract (TypeSpec + JSON Schema → Diesel / SeaORM / dpm)

**Status:** adopted for this organization — 2026-08-29 (revision f alignment)  
**Fleet authority:** [general-migration-plan](https://linear.app/denman/document/general-migration-plan-f76fadd4cbb2) · [DEN-3321](https://linear.app/denman/issue/DEN-3321) · [ORESoftware/k8s-libs-and-shared-defs#54](https://github.com/ORESoftware/k8s-libs-and-shared-defs/issues/54)  
**Org:** `athlet-o`  
**Canonical product repos:** ``athlet-o/athleto-lib-core``, temporary compatibility ``athleto-orm-core` target inside `athleto-lib-core` (no competing standalone schema)` (if present)

This document tells agents and humans how this org authors persistence, generates SQL and ORM code, cross-checks the two primary sources, and applies migrations. It **supersedes** older org text that (a) treats `ORESoftware/k8s-libs-and-shared-defs` as the product SQL author, (b) names SeaORM as the only Rust ORM, or (c) treats `*-orm-core` as an independent schema authority.

## 1. Where authority lives

| Concern | Owner after cutover | Must not own |
| --- | --- | --- |
| Product relational model (canonical AST) | ``athlet-o/athleto-lib-core`` — authored TypeSpec under `contracts/database/typespec/` | Shared-defs product segments; `*-orm-core` hand-written schema |
| Product relational witness (secondary-primary) | ``athlet-o/athleto-lib-core`` — independently authored JSON Schema under `contracts/database/json-schema/` | TypeSpec-emitted JSON Schema (witness only) |
| PostgreSQL capabilities not round-trippable | ``athlet-o/athleto-lib-core`` — authored `contracts/database/extensions/*.sql` (RLS, grants, triggers, ZD00x guards, specialized indexes, CDC hooks) | ORM macros or generators pretending to emit them |
| Public wire contracts | ``athlet-o/athleto-interfaces`` — API/RPC/event TypeSpec + JSON Schema | Persistence tables / ORM entities |
| Runtime primary Rust ORM | Generated Diesel + diesel-async from the **reconciled TypeSpec lineage** | Authoring a third schema; Diesel `print-schema` as source of truth |
| Runtime secondary Rust ORM | Generated SeaORM entities from scratch DBs built from both candidate contracts | SeaORM `sync()` / startup DDL / competing desired.sql |
| Apply / live convergence | `declarative-migrations` `dpm` against release `desired.sql` | API/web boot migrations |
| Platform SQL + fleet catalog | `ORESoftware/k8s-libs-and-shared-defs` | Product table bodies for this org after cutover |

High-level move: **SQL generation and ORM code generation leave the shared ORESoftware user/org and live in this GitHub org’s ``athlet-o/athleto-lib-core``.** Shared-defs keeps platform SQL, the org→package catalog, Zed locks, and verification harnesses—not this product’s table DDL.

## 2. Dual primary sources (binding)

1. **TypeSpec is P0 — canonical persistence AST.** Release lineage and stable semantic IDs come from the authored TypeSpec program after parity.
2. **JSON Schema is P1 — secondary-primary.** Humans author `persistence.schema.json` independently. It has **veto power**: a release is blocked if its pipeline cannot produce the same normalized catalog and ORM manifests as TypeSpec.
3. **Neither source overwrites the other.** TypeSpec may emit `generated/witnesses/typespec/projected.persistence.schema.json` for comparison only. Never regenerate `contracts/database/json-schema/persistence.schema.json` from TypeSpec in place.
4. **Both pipelines emit independent candidates:** relational PostgreSQL SQL, Diesel artifacts, SeaORM artifacts, normalized IR/manifests. Candidate trees are never hand-edited.
5. **Mismatch blocks.** TypeSpec being canonical does not auto-win. Humans reconcile both authored sources and regenerate.
6. **Extensions SQL is applied identically** to both scratch databases before catalog compare.

```text
TypeSpec P0 ──► SQL A ──► scratch DB A ──► catalog A
     └────────► Diesel/SeaORM A ──────────► ORM manifest A

                    equality + veto gate

JSON Schema P1 ──► SQL B ──► scratch DB B ──► catalog B
        └────────► Diesel/SeaORM B ──────────► ORM manifest B

Required: catalog A == catalog B, ORM manifests equal,
          shared conformance green, projected JSON Schema ≈ authored JSON Schema

                    │
                    ▼
        publish TypeSpec-lineage release
        desired.sql + Diesel + SeaORM + IR
                    │
                    ▼
            dpm plan / verify / apply
```

Equality is **semantic** (server-normalized PostgreSQL catalogs + ORM manifests + shared fixtures), not byte-identical SQL formatting. Constraint/index/sequence naming must be deterministic or canonicalized in the ORESoftware persistence vocabulary so independent emitters can converge.

## 3. Rust runtimes: Diesel primary, SeaORM secondary

| Role | Stack | How code is produced | How it is used |
| --- | --- | --- | --- |
| Primary | Diesel + diesel-async | Generated from reconciled TypeSpec lineage after dual-source gate | Default for new Rust product code; opaque contexts in ``athlet-o/athleto-lib-core`` |
| Secondary | SeaORM | Generated from disposable DBs materialized from **both** candidates; published from TypeSpec lineage after compare | Compatibility / dynamic-query paths; must not invent DDL |

Rules:

- Do **not** treat SeaORM entity-first `sync()`/`apply()` or Diesel migrations as production DDL. Only the migrator Job + `dpm` apply release `desired.sql`.
- Do **not** add bare `sqlx` / `tokio-postgres` application pools alongside the ORM boundary.
- A temporary ``athleto-orm-core` target inside `athleto-lib-core` (no competing standalone schema)` package may re-export generated Diesel/SeaORM crates for pin compatibility. It must **not** author schema, desired.sql, or a competing generator. Prefer folding into ``athlet-o/athleto-lib-core`` `targets.rust-orm` (zed-pkg pattern).
- Cargo features (`read-write`, etc.) express intent; **database principals** (`__api_rw`, `__web_ro`, `__migrator`) are the security boundary.

## 4. Layout inside ``athlet-o/athleto-lib-core``

```text
contracts/database/
  typespec/                         # P0 authored
  json-schema/
    persistence.schema.json         # P1 authored (never overwritten)
    persistence.meta.schema.json
  extensions/*.sql                  # RLS, guards, triggers, …
  data-operations/
  interface-mapping.json
generated/
  candidates/typespec/              # independent pipeline A
  candidates/json-schema/           # independent pipeline B
  witnesses/typespec/               # projected JSON Schema for compare only
  reports/dual-source-parity.json
  release/                          # published only after parity
    sql/postgres/desired.sql
    rust-diesel/
    rust-seaorm/
.zpkg.toml / .zpkg.lock
```

Zed pins both authored sources, both generator toolchains, candidates, parity evidence, and release digests. Consumers (`*-api-server.rs`, `*-web-server.rs`, migrator Job) pin the **same** ``athlet-o/athleto-lib-core`` digest and select different capability profiles.

## 5. Migrations with declarative-migrations

1. Materialize release `desired.sql` (TypeSpec lineage) only after dual-source parity is green.
2. `dpm diff` / `dpm verify` against shadow + target; empty post-apply catalog drift required.
3. Human review; destructive statements need explicit consent flags.
4. Apply via one-shot Kubernetes Job with `__migrator` only.
5. Promote API/web pins after live catalog readback.

Web and API processes never receive DDL credentials and never run `AUTO_MIGRATE`, SeaORM sync, or Diesel migrate on boot.

## 6. Relationship to shared-defs and this org’s SQL

**Before cutover (bridge):** this org’s segment may still live under `k8s-libs-and-shared-defs/pg-defs/schema/orgs/databases/athleto (legacy shared-defs path) / athlet-o/` and be dual-sourced byte-for-byte into ``athlet-o/athleto-lib-core``.

**After cutover:**

- Product DDL is authored/generated only in ``athlet-o/athleto-lib-core``.
- Shared-defs catalog entry records `{ package: "athlet-o/athleto-lib-core", target: "schema", digest, rdsInstance, postgresSchema|tablePrefix, cdc[] }`.
- Do not git-submodule product SQL back into shared-defs or `k8s-cluster`. Deploy installs the Zed schema target and points `dpm --source-sql` at the materialized release file.

Platform tables (`app_config`, CDC publication membership list, container pool, …) remain shared-defs. Cross-org physical FKs remain forbidden; identity joins on shared-auth subjects stay logical.

## 7. Agent checklist (do / don’t)

**Do**

- Edit TypeSpec and authored JSON Schema in ``athlet-o/athleto-lib-core`` together; regenerate both candidate pipelines; require parity before publishing release artifacts.
- Keep extensions.sql for RLS / ZD00x / triggers shared across both scratch applies.
- Pin generators and emitters through Zed; commit digests and parity reports.
- Use Diesel as the default new Rust path; keep SeaORM as secondary generated surface.
- Open migrator-only PRs for DDL apply evidence; keep API/web PRs free of DDL credentials.

**Don’t**

- Author product SQL only in `ORESoftware/k8s-libs-and-shared-defs`.
- Let ``athleto-orm-core` target inside `athleto-lib-core` (no competing standalone schema)` or server repos invent schema.
- Overwrite authored JSON Schema with TypeSpec emitter output.
- Auto-resolve TypeSpec vs JSON Schema mismatches by picking one side.
- Run ORM schema sync / migrate at process boot.
- Add a third independently authored schema (hand Diesel schema, raw SQL fork, etc.).

## 8. Rollout notes for `athlet-o`

1. Inventory current SQL / SeaORM / shared-defs pins in ``athlet-o/athleto-lib-core`` and ``athleto-orm-core` target inside `athleto-lib-core` (no competing standalone schema)`.
2. Introduce TypeSpec + authored JSON Schema + extensions layout (may start by importing the existing org SQL segment as the first release `desired.sql` while dual-source emitters catch up).
3. Stand up independent candidate generators and the catalog/ORM parity gate.
4. Publish Diesel primary + SeaORM secondary from TypeSpec lineage after green parity.
5. Point dpm Job at release `desired.sql`; freeze shared-defs product segment; catalog digest only.
6. Retire or demote ``athleto-orm-core` target inside `athleto-lib-core` (no competing standalone schema)` to a generated compatibility package.

Until dual-source emitters exist, **authored desired-state SQL + extensions in ``athlet-o/athleto-lib-core`` remain the interim apply input**, and both TypeSpec and JSON Schema work must be additive toward that file—not a silent second authority in shared-defs.
