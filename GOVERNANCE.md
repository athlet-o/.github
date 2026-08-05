# Governance

Repository maintainers own technical direction for their scope. Cross-repository changes must identify the canonical owner of each interface and avoid duplicating sources of truth.

Material changes should record:
- the decision and alternatives considered;
- compatibility and migration consequences;
- security and operational risks;
- validation evidence;
- rollback or deprecation strategy.

Conflicted changes are merged by intent, not line selection. A semantic reconciliation should preserve non-conflicting additions from both sides and explicitly resolve incompatible assumptions.
