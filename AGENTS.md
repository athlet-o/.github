# Agent instructions

Before editing:
1. Read repository-local instructions and recent history.
2. Identify the canonical source of truth and downstream consumers.
3. Keep credentials and private data out of prompts, logs, commits, and artifacts.

For conflicts, compare the merge base, both heads, relevant tests, and surrounding commits. Reconstruct intent and produce a coherent combined implementation. Never use blanket ours/theirs resolution for substantive conflicts.

Validate the exact commit being proposed. Do not claim tests or deployments that were not actually run.

<!-- ore-org-baseline:begin -->
Read and obey [`agents.md`](agents.md); the lowercase file is canonical.

At minimum: preserve concurrent work; fetch before editing and before pushing; avoid git rebase in favor of git merge; never use `git stash`, `git reset`, `git clean`, `git filter-repo`, force-push, or another destructive operation without exact authorization; resolve conflicts semantically using the merge base, 3–10 relevant commits, tests, contracts, Linear context, and related repositories; never choose `ours` or `theirs` wholesale; scan for conflict markers; validate affected behavior; and never claim remote completion without authoritative evidence.
<!-- ore-org-baseline:end -->
