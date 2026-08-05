<!-- ore-org-baseline:begin -->
# Repository relationships for `athlet-o`

This file is rendered from `repository-relationships.json`. The JSON registry is authoritative.

- Audience: `public`
- Repositories represented: **3**
- Relationships represented: **3**
- Inventory digest: `sha256:b8ec69b6bc09da75db1f22882e9e183079ce4b26ce389efe2e851ca5a58800d5`

## Immutable routing identity

| Field | Value |
|---|---|
| Mapping ID | `context:athlet-o` |
| GitHub owner ID | `306008767` |
| Linear project ID | `0de9ab82-98b3-4c1d-950b-2020d80bbccc` |
| Linear team ID | `eb8ab169-5afe-4b6f-9cab-3f2aa3e887dc` |

## Repositories

| Repository | Visibility | Roles | Archived |
|---|---|---|---|
| `athlet-o/.github` | `public` | `community-health`, `governance`, `relationship-registry` | no |
| `athlet-o/athlet-o.github.io` | `public` | `documentation-site` | no |
| `athlet-o/athleto-app-rs` | `public` | `repository` | no |

## Relationships

| From | Type | To | Status | Required |
|---|---|---|---|---|
| `athlet-o/.github` | `governs` | `athlet-o/athlet-o.github.io` | `declared` | yes |
| `athlet-o/.github` | `governs` | `athlet-o/athleto-app-rs` | `declared` | yes |
| `athlet-o/athlet-o.github.io` | `documents` | `athlet-o/.github` | `inferred` | no |

## Editing relationships

Put reviewed public declarations in `repository-relationships.manual.json`; do not edit the generated registry directly.
Private repository names and private-only relationships belong in the private `ORESoftware/project-registry` mirror.
Inferred edges are advisory and must remain visibly labeled until reviewed.
<!-- ore-org-baseline:end -->
