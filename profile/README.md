# athlet-o

This organization maintains software, infrastructure, interfaces, clients, services, and supporting documentation under a shared engineering baseline.

## Working principles

- Keep changes reviewable, tested, and reversible.
- Treat security, privacy, compatibility, and data durability as design constraints.
- Resolve merge conflicts semantically: reconstruct both sides' intent, preserve compatible behavior, and document deliberate trade-offs.
- Prefer canonical repositories and short, stable names; deprecate duplicates with migration notes rather than silently deleting history.
- Keep cross-repository dependencies explicit and pinned where reproducibility matters.

Organization-wide contribution and security guidance lives in this `.github` repository.

<!-- org-project-routing:start -->
## Planning and delivery

- [GitHub Project: athlet-o-project](https://github.com/orgs/athlet-o/projects/1)
- [Linear planning project](https://linear.app/denman/project/githubcomathlet-o-b5a995fed9bb)
- [Detailed project-routing contract](../docs/PROJECTS.md)

GitHub owns code and delivery evidence; Linear owns planning and dependencies. The linked organization Project provides the cross-repository execution view.
<!-- org-project-routing:end -->

<!-- ore-org-baseline:begin -->
## Planning and governance

- Canonical Linear project: https://linear.app/denman/project/githubcomathlet-o-b5a995fed9bb
- Organization defaults: https://github.com/athlet-o/.github
- Canonical agent policy: https://github.com/athlet-o/.github/blob/main/agents.md
- Security policy: https://github.com/athlet-o/.github/security/policy

Repositories in this organization use semantic conflict resolution with 3–10 relevant prior commits when useful, full cross-repository context, pull-request delivery, and a hard automated-agent denylist for destructive or history-rewriting operations.
<!-- ore-org-baseline:end -->

<!-- BEGIN MANAGED REPOSITORY RELATIONSHIPS v1 -->
## Repository relationship registry

`athlet-o` declares repository roles, dependency edges, cross-organization capabilities, deployment ownership, and the git-submodule/Zed-package contract:

- [Human-readable map](architecture/REPOSITORY_RELATIONSHIPS.md)
- [Machine-readable manifest](architecture/repository-relationships.json)
- [JSON Schema](architecture/repository-relationships.schema.json)

The public registry withholds private repository names and edges.
<!-- END MANAGED REPOSITORY RELATIONSHIPS v1 -->
