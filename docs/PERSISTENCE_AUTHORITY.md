# Persistence authority — TypeSpec, JSON Schema, Diesel, SeaORM, and dpm

**Status:** adopted org policy — 2026-08-29 (revision f)
**Scope:** this GitHub organization and every database-backed product under it

**Organization:** `athlet-o`
**Canonical lib-core:** [`athlet-o/athleto-lib-core`](https://github.com/athlet-o/athleto-lib-core)
**ORM package:** `athleto-orm-core` (fold into lib-core; do not keep a second SQL authority)
**Org note:** Dedicated commerce database. Supersedes `athleto-lib-core/SERVICE_AND_DATA_ARCHITECTURE.md` claims that k8s-libs-and-shared-defs owns physical desired-state SQL for athleto.

**Fleet plan:** [general-migration-plan](https://linear.app/denman/document/general-migration-plan-f76fadd4cbb2)
**Execution:** [DEN-3321](https://linear.app/denman/issue/DEN-3321), [ORESoftware/k8s-libs-and-shared-defs#54](https://github.com/ORESoftware/k8s-libs-and-shared-defs/issues/54)

This document supersedes older org text that names `ORESoftware/k8s-libs-and-shared-defs` as the human-authored **product** SQL/ORM generation authority, or that names SeaORM as the sole / primary Rust ORM for new product persistence work.

---

## 1. Decision

Product SQL generation, ORM generation, and dual-source validation move **out of** the shared `ORESoftware` / `k8s-libs-and-shared-defs` tree and **into this org’s** `*-lib-core` (with `*-orm-core` only as a generated or folded compatibility package).

| Tier | Source | Role |
| --- | --- | --- |
| **P0 canonical primary** | Authored persistence **TypeSpec** in `*-lib-core` | Canonical AST and release lineage after parity |
| **P1 secondary-primary** | Independently authored persistence **JSON Schema** in `*-lib-core` | Independent witness with **release veto**; never overwritten by TypeSpec |
| **PG capability primary** | Authored PostgreSQL **extension SQL** (RLS, grants, triggers, ZD00x guards, partial indexes, CDC hooks) | Applied identically to both candidate pipelines |
| **Runtime primary** | Generated **Diesel + diesel-async** | Default Rust persistence runtime for new product code |
| **Runtime secondary** | Generated **SeaORM** | Compatibility / dynamic-query runtime; compared from both scratch DBs |
| **Apply authority** | Generated release `desired.sql` + reviewed **dpm** plan | Only production DDL path |

`*-interfaces` owns wire TypeSpec / JSON Schema for HTTP, events, and clients. Persistence TypeSpec and persistence JSON Schema live only in `*-lib-core`. Interfaces never depend on lib-core.

---

## 2. Why both TypeSpec and JSON Schema are “primary”

- **TypeSpec is canonical** because its compiler AST is the stable semantic identity and the lineage used for published release artifacts after parity.
- **JSON Schema is primary** because humans author it independently; disagreement **blocks** release.
- **JSON Schema is secondary** because it does not choose the published lineage and must not overwrite TypeSpec.
- TypeSpec may emit a **projected** JSON Schema under `generated/witnesses/…` for comparison only. That projection never replaces `contracts/database/json-schema/persistence.schema.json`.

A mismatch is never auto-resolved by precedence. Humans reconcile both authored sources and regenerate.

---

## 3. Dual pipeline (must converge)

```text
TypeSpec P0 ──► SQL A ──► scratch DB A ──► catalog A
     └────────► Diesel/SeaORM A ──────────► ORM manifest A

                    equality + veto gate

JSON Schema P1 ──► SQL B ──► scratch DB B ──► catalog B
        └────────► Diesel/SeaORM B ──────────► ORM manifest B

Required before publish:
  catalog A == catalog B   (server-normalized PostgreSQL)
  ORM manifest A == ORM manifest B
  shared conformance tests pass
  common extension SQL has identical normalized definitions
  TypeSpec-projected JSON Schema ≈ authored JSON Schema (declared lossy edges explicit)

Then publish TypeSpec-lineage release:
  desired.sql + Diesel + SeaORM + IR + digests
        │
        ▼
  dpm plan / verify / apply  (migrator Job only)
```

Text-identical SQL is not required. Equality is semantic: normalized catalogs, ORM manifests, compile success, and shared behavior fixtures.

---

## 4. Repository roles in this org

### `*-lib-core` (required)

Owns:

- `contracts/database/typespec/*.tsp` (P0)
- `contracts/database/json-schema/persistence.schema.json` (+ meta-schema) (P1)
- `contracts/database/extensions/*.sql`
- generators, candidate trees, parity reports, release digests
- opaque named read/write operations
- `.zpkg.toml` / `.zpkg.lock` for schema + rust-orm (or diesel/seaorm) targets

### `*-orm-core` (optional / transitional)

- Must **not** author a second schema.
- Prefer folding into `*-lib-core` as `targets.rust-orm` / Diesel package (zed-pkg already merged).
- Until folded: publish only generated Diesel/SeaORM adapters from the lib-core release; pin the same digests.

### `*-api-server.rs` / `*-web-server.rs`

- Pin the same `*-lib-core` Zed digest.
- API: Diesel (primary) and/or SeaORM write profile + `__api_rw`.
- Web: read profile only + `__web_ro` (or API-mediated reads).
- **Never** run DDL, `AUTO_MIGRATE`, SeaORM `sync()`, Diesel migrate, or sqlx migrate at process boot.

### Migrator Job (`*-infra` / `k8s-cluster`)

- Installs `*-lib-core` schema target via Zed.
- Runs `dpm` from [declarative-migrations](https://github.com/declarative-migrations/declarative-postgres-migrate.rs) against release `desired.sql`.
- Sole production DDL principal (`__migrator`).

### `ORESoftware/k8s-libs-and-shared-defs`

Keeps **only**:

- platform / cluster-shared SQL
- org catalog (org → RDS → schema/prefix → Zed package + digest)
- NATS / Redis / non-product shared contracts
- optional verification harnesses that **resolve** org packages (do not re-author product tables)

After cutover, product table bodies and product ORM generation **do not** live here.

---

## 5. Suggested layout inside `*-lib-core`

```text
contracts/database/
  typespec/                 # authored P0
  json-schema/
    persistence.schema.json # authored P1 (never TypeSpec-overwrite)
    persistence.meta.schema.json
  extensions/               # RLS, ZD00x, triggers, grants
  interface-mapping.json
generated/
  candidates/typespec/      # SQL A, ORM A, IR A
  candidates/json-schema/   # SQL B, ORM B, IR B
  witnesses/typespec/       # projected JSON Schema only
  reports/dual-source-parity.json
  release/
    sql/postgres/desired.sql
    diesel/
    sea-orm/
```

Use Zed targets such as `schema`, `rust-diesel`, `rust-seaorm` (names may vary; digests must be explicit).

---

## 6. Diesel vs SeaORM (runtime)

| Concern | Diesel + diesel-async | SeaORM |
| --- | --- | --- |
| Fleet role | **Primary** Rust runtime for new product code | **Secondary** compatibility / dynamic queries |
| Schema authorship | Generated from reconciled TypeSpec lineage after P1 gate | Generated from scratch DBs / release SQL; not a second authority |
| Web tier | Read-only compiled surface or named reads only | Default features read-only; no write symbols in web graphs |
| Migrations | Not applied by the app; dpm owns apply | No `SchemaBuilder.sync()` / entity-first apply in prod |

Do **not** adopt Diesel (or SeaORM) as a third independently authored schema source. ORM models are release artifacts, not competing DDL.

---

## 7. Transition from today’s shared-defs pin

Until dual-source generators land in this org:

1. **Freeze** new product SQL in `k8s-libs-and-shared-defs` for this org’s segment.
2. **Extract** the org SQL segment into `*-lib-core` as transitional authored SQL / extensions (byte-identical dual-source with shared-defs until cutover).
3. Author TypeSpec + JSON Schema against that contract; turn on candidate emission and the veto gate.
4. Flip consumers to Zed pins of this org’s `*-lib-core`; drop product segment from shared-defs; catalog records the package digest.
5. Fold or retire standalone `*-orm-core` once Diesel/SeaORM packages publish from lib-core.

Lossless relocation, dual-source conversion, and namespace redesign are **separate** evidence-bearing changes.

---

## 8. Hard refusals

- Product SQL/ORM generation remaining forever in `k8s-libs-and-shared-defs`
- Overwriting authored JSON Schema with TypeSpec JSON Schema emitter output
- Releasing when catalogs or ORM manifests disagree
- DDL at API/web boot
- Physical FKs across org packages or across RDS instances (use logical `shared_auth_subject` + realm)
- Git-submodule of product SQL into shared-defs or `k8s-cluster` (use Zed)
- Treating SeaORM `sync()` or Diesel CLI migrate as production apply

---

## 9. Related org documents

- Keep the four web↔API connection modes in athleto-lib-core service architecture; only the SQL ownership / ORM primacy sections change.

Update older ORM / service-architecture docs in this `.github` repository to point here when they still say “SeaORM-only” or “schema lives only in shared-defs.” Keep their still-valid web/API capability rules (API writes, web read-only, migrator DDL).
