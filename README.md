# athlet-o organization defaults

This public `.github` repository contains organization-wide community health files, contributor guidance, shared agent policy, and an explicit repository-relationship contract.

Repository-local policy wins when it is stricter or more specific. Existing project history must be preserved during consolidation and conflict resolution.

<!-- ore-org-baseline:begin -->
## Organization-wide defaults

This public repository is the canonical source for GitHub-supported community-health fallbacks, organization profile content, contribution guidance, public security/support policy, issue and pull-request templates, and agent-governance declarations for [`athlet-o`](https://github.com/athlet-o).

## Canonical organization links

- GitHub organization: https://github.com/athlet-o
- Public organization defaults: https://github.com/athlet-o/.github
- Canonical Linear project: https://linear.app/denman/project/githubcomathlet-o-b5a995fed9bb
- Fleet tracking issue: https://github.com/ORESoftware/k8s-cluster/issues/1222

## Safety baseline

All Git conflicts must be resolved semantically with full historical, repository-wide, organization-wide, and relevant external-organization context. Automated agents are hard-denied from destructive or history-rewriting operations, including all forms of `git stash`, `git reset`, `git clean`, `git filter-repo`, force pushing, destructive deletion, data or infrastructure teardown, credential revocation, and policy bypass.

## GitHub inheritance boundary

GitHub can use supported community-health files from a public organization `.github` repository as fallbacks and can render `profile/README.md` on the organization page. `agents.md`, `AGENTS.md`, Copilot instructions, workflows, settings, rulesets, branch protections, permissions, and secrets are not automatically inherited merely because they exist here. Each repository must carry or synchronize compatible local policy and explicitly call reusable workflows where enforcement is required.

Generated managed-policy version: `2026-08-08`.
<!-- ore-org-baseline:end -->

<!-- BEGIN MANAGED REPOSITORY RELATIONSHIPS v1 -->
## Repository relationship registry

`athlet-o` declares repository roles, dependency edges, cross-organization capabilities, deployment ownership, and the git-submodule/Zed-package contract:

- [Human-readable map](architecture/REPOSITORY_RELATIONSHIPS.md)
- [Machine-readable manifest](architecture/repository-relationships.json)
- [JSON Schema](architecture/repository-relationships.schema.json)

The public registry withholds private repository names and edges.
<!-- END MANAGED REPOSITORY RELATIONSHIPS v1 -->
