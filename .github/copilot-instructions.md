Read AGENTS.md and repository-local instructions before editing. Keep changes focused and evidence truthful. Resolve conflicts by understanding both branches and constructing the best coherent result; never select ours/theirs wholesale for substantive conflicts. Preserve security, compatibility, data durability, and repository boundaries.

<!-- ore-org-baseline:begin -->
Read and obey [`../agents.md`](../agents.md); the lowercase file is canonical.

At minimum: preserve concurrent work; fetch before editing and before pushing; avoid git rebase in favor of git merge; never use `git stash`, `git reset`, `git clean`, `git filter-repo`, force-push, or another destructive operation without exact authorization; resolve conflicts semantically using the merge base, 3–10 relevant commits, tests, contracts, Linear context, and related repositories; never choose `ours` or `theirs` wholesale; scan for conflict markers; validate affected behavior; and never claim remote completion without authoritative evidence.
<!-- ore-org-baseline:end -->
