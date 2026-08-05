# Desktop application allocation

Verified **2026-08-05**.

Athlet-O **might** benefit from paired native desktop applications for professional coaching, facility, team-management, and analytics workflows. The consumer fitness experience remains mobile-first:

- Rust: [`athlet-o/athleto-desktop.rs`](https://github.com/athlet-o/athleto-desktop.rs) — **proposed**, not yet verified as a published repository.
- Flutter: [`athlet-o/athleto-flutter`](https://github.com/athlet-o/athleto-flutter) — **proposed**, not yet verified as a published repository.

These names are optional allocation targets, not proof that either remote exists and not a commitment to build them. Native clients should be promoted only when bulk planning, large-screen analytics, keyboard-heavy administration, local device imports, or facility workflows materially outperform the existing mobile/web product.

## Potential product boundary

A future pair could cover semantic parity for athlete and team rosters, program and session planning, calendar and facility scheduling, bulk edits, analytics dashboards, local sensor/device imports, reports, exports, offline work, notifications, and recovery.

A shared Rust analytics or local-processing core may sit behind an explicit library, FFI, or local-service boundary, but any Flutter application must remain independently buildable, testable, and releasable. Shared schemas, clients, fixtures, sample programs, analytics definitions, and conformance tests should be versioned deliberately.

## Promotion rule

Promote this pair from optional proposal to planned only when the coach/facility workflow, ownership, milestones, data/privacy boundary, and repository creation are accepted. Once planned, desktop-facing changes must inspect both implementations, define shared acceptance criteria, update both or record an explicit no-change rationale, and report Rust and Flutter status separately.

## Project routing

- GitHub Project: [`athlet-o-project` — Project 1](https://github.com/orgs/athlet-o/projects/1)
- Linear project: `github.com/athlet-o`
- Central registry: [`ORESoftware/project-registry`](https://github.com/ORESoftware/project-registry/blob/main/registry/desktop-applications.json)
- Portfolio rollout: [`DEN-2469`](https://linear.app/denman/issue/DEN-2469/roll-out-paired-rust-flutter-desktop-repositories-across-the-portfolio)

Promotion, repository creation, renames, transfers, archival, privacy-boundary changes, or platform-status changes must update this document, Linear, the central registry, and both companion repositories together.
