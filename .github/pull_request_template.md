## Summary

Describe the problem, the chosen design, and the user or operational outcome.

## Verification

List commands, tests, checks, and manual validation actually performed against this exact head.

## Compatibility and risk

Explain API/data/configuration changes, security implications, rollout, migration, and rollback.

## Conflict reconciliation

When conflicts were present, summarize both sides' intent and how the final implementation preserves or deliberately supersedes each part.

- [ ] No secrets or private data are included.
- [ ] Documentation and tests reflect the final contract.
- [ ] The exact proposed head was verified.

<!-- ore-org-baseline:begin -->
## Summary

Describe the behavior and intent, not only the files changed.

## Planning and dependencies

- Linear project or issue: [github.com/athlet-o](https://linear.app/denman/project/githubcomathlet-o-b5a995fed9bb)
- Related GitHub issues or pull requests:
- Related repositories or external contracts:

## Risk, security, migration, and rollback

- User or operational impact:
- Security/privacy impact and secret-handling review:
- Migration or compatibility considerations:
- Rollback or recovery approach:

## Validation

List exact commands, environments, and results. Include unit, integration, contract, build, and end-to-end evidence as applicable.

## Conflict-resolution record

- [ ] Remote state was fetched before editing and before pushing.
- [ ] Concurrent work was preserved; no destructive operation or history rewrite was used.
- [ ] Conflicts, if any, were resolved semantically using the merge base, both sides, 3–10 relevant commits, tests, contracts, linked work, and related repositories.
- [ ] The complete worktree was scanned for unresolved conflict markers.
- [ ] No `ours`/`theirs` side was accepted wholesale without conceptual review.

## Final checklist

- [ ] Focused commits and reviewable diff
- [ ] Documentation and generated artifacts updated from authoritative sources
- [ ] External Actions pinned to full commit SHAs
- [ ] Explicit least-privilege workflow permissions and timeouts
- [ ] No credentials, private data, or sensitive logs included
- [ ] Authoritative remote branch/PR/check evidence verified
<!-- ore-org-baseline:end -->
