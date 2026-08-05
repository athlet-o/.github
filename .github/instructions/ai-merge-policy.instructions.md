---
applyTo: "**"
---

# AI-assisted merge gates

Apply these rules to the exact commit under consideration. The thresholds are strict: “more than” means `>`, not `>=`.

1. **Feature pull request → integration:** Merge only when every required test and status check for the exact pull-request head has passed, the pull request is non-draft and mergeable, no required review, security, compliance, migration, or release gate remains, and the AI documents evidence-backed confidence **greater than 99.1%** that the feature is correct, complete, compatible, and safe. Target `integration` when it exists; otherwise target `dev`. If neither exists, stop and report the missing development branch rather than guessing.
2. **Integration → production:** Merge the exact `integration` or `dev` head into production only when every required test and status check has passed, no required gate remains, and the AI documents evidence-backed confidence **greater than 99.7%** that the promotion is safe. Target `main` when it is the production branch; otherwise target `master`.
3. Recompute confidence whenever the candidate commit changes. Document the supporting evidence, tests, risks, and residual uncertainty. Never fabricate a confidence score.
4. Branch protection, required human approvals, CODEOWNERS, security and compliance controls, release freezes, and stricter repository-local policies remain mandatory. Confidence never bypasses safeguards.
5. If any condition is not met, leave the change unmerged and report the blockers. Resolve conflicts semantically and validate the exact resulting commit before reevaluating the gates.
