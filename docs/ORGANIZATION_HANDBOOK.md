# athlet-o organization handbook

> Shared operating defaults for repositories maintained under **athlet-o**. Repository-local policy may strengthen these rules but should not silently weaken them.

## Mission

athlet-o maintains athlete, training, and performance software. This `.github` repository is the canonical home for organization-wide community health files, reusable templates, engineering policy, and planning links.

## Repository contract

Each active repository must document purpose, ownership, maturity, supported platforms, development and test commands, authoritative data models, release and rollback procedures, compatibility policy, and GitHub Project/Linear links. Training and performance components should also document units, sensor assumptions, data provenance, privacy and consent boundaries, offline behavior, accessibility, and interpretation limits.

## Change and review workflow

1. Anchor work in an issue, Linear item, or documented maintenance objective.
2. Keep branches and pull requests focused.
3. Explain motivation, scope, user and data impact, validation, compatibility, migration, and rollback.
4. Test permission, sync, offline, boundary-value, accessibility, and device-variation paths as relevant.
5. Resolve conflicts semantically by reconstructing both sides' intent.
6. Prefer squash merges for focused work unless commit structure materially improves auditability.

## Evidence and quality

Pull requests should include reproducible commands, sanitized fixtures, expected and observed results, negative-path coverage, documentation updates, and CI or local-equivalent evidence. Data-model changes require consumer impact analysis and explicit migration guidance.

## Security and data

Never commit credentials, personal health or performance data, production identities, private media, or sensitive logs. Use synthetic or irreversibly sanitized fixtures. Follow `SECURITY.md` for private vulnerability reporting and pin dependencies and actions where reproducibility or supply-chain integrity matters.

## Documentation and decisions

Keep examples executable and sanitized, links current, assumptions explicit, units consistent, and interpretation boundaries clear. Record architectural, device, privacy, compatibility, and operational decisions that future maintainers would otherwise have to rediscover.

## Planning ownership

GitHub owns code, reviews, checks, releases, and delivery evidence. Linear owns priority, dependencies, sequencing, and cross-project planning. The organization GitHub Project is the cross-repository execution view; see `PROJECTS.md` for routing details.

## Organization health

- [ ] Profiles, descriptions, topics, and READMEs are current.
- [ ] Contribution, security, support, governance, issue, and PR guidance is present.
- [ ] Units, data provenance, privacy boundaries, and interpretation limits are documented.
- [ ] Required checks reflect correctness, device compatibility, privacy, and supply-chain risk.
- [ ] Stale repositories are archived or clearly marked.
- [ ] Project links resolve and completed work is reflected in GitHub and Linear.
