# Semantic conflict resolver

A conflict is a design reconciliation task, not a text-selection task.

1. Establish the merge base and read the full conflicting files.
2. Inspect several relevant commits on both branches and identify the invariant each side protects.
3. Classify edits as independent, complementary, superseding, or incompatible.
4. Preserve independent and complementary work from both sides.
5. For incompatible assumptions, choose or synthesize the design that best satisfies current requirements, tests, compatibility, security, and maintainability.
6. Remove obsolete duplication and update tests/docs to express the final contract.
7. Verify the exact resolved head and summarize the semantic decisions.
