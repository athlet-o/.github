# Repository boundaries

Each repository should have one primary responsibility and an explicit dependency direction.

- `*-interfaces`: schemas, protocol contracts, and stable cross-language boundaries.
- `*-lib`: reusable domain logic built on interfaces.
- `*-clients`: client SDKs and transport adapters.
- `*-sync`: synchronization and offline/replication behavior.
- `*-cli`: command-line workflows composed from clients, interfaces, and libraries.
- web/API/backend repositories: deployable services consuming the shared contracts.
- `*-e2e`: black-box and integration verification, not production implementation.

When repositories overlap, choose a canonical home, migrate callers, preserve attribution and useful history, and leave a clear deprecation pointer.
