# Governance

Repository maintainers own technical direction for their scope. Cross-repository changes must identify the canonical owner of each interface and avoid duplicating sources of truth.

Material changes should record:
- the decision and alternatives considered;
- compatibility and migration consequences;
- security and operational risks;
- validation evidence;
- rollback or deprecation strategy.

Conflicted changes are merged by intent, not line selection. A semantic reconciliation should preserve non-conflicting additions from both sides and explicitly resolve incompatible assumptions.

<!-- ore-org-baseline:begin -->
## Sources of truth

- GitHub is authoritative for source, policy, architecture records, public organization context, reviewed implementation, and immutable commit history.
- [github.com/athlet-o](https://linear.app/denman/project/githubcomathlet-o-b5a995fed9bb) is the planning and delivery ledger.
- Repository-local documentation is authoritative for repository-specific behavior and may strengthen this baseline.
- `repository-relationships.manual.json` is authoritative for reviewed public relationship declarations; the generated JSON graph is a deterministic projection.
- The approved private project registry is authoritative for private repository inventory and private-only edges.
- Private member context belongs in an approved private system, such as `.github-private`, never in this public repository.

## Change control

Material policy and architecture changes use issues or pull requests, focused commits, reviewable diffs, tests, and linked planning context. Existing content must be preserved unless a change explicitly supersedes it. Generated and mirrored artifacts must be updated from their authoritative source. Inferred relationship edges remain advisory until reviewed and declared.

Conflicts are resolved semantically with full history and cross-repository context. Destructive operations, history rewrites, force pushes, bypasses, and deletion of shared resources are default-deny and require exact authorization.

## Precedence

A repository may impose stricter requirements. It must not weaken secret handling, non-destructive collaboration, semantic conflict resolution, evidence-backed completion, or required review and checks.
<!-- ore-org-baseline:end -->
