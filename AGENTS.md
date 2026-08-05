# Agent instructions

Before editing:
1. Read repository-local instructions and recent history.
2. Identify the canonical source of truth and downstream consumers.
3. Keep credentials and private data out of prompts, logs, commits, and artifacts.

For conflicts, compare the merge base, both heads, relevant tests, and surrounding commits. Reconstruct intent and produce a coherent combined implementation. Never use blanket ours/theirs resolution for substantive conflicts.

Validate the exact commit being proposed. Do not claim tests or deployments that were not actually run.
