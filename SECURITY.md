# Security and permissions

The installed skill folders contain Markdown instructions and YAML interface metadata. They do not include executables, installation hooks, automatic network requests, permission grants or secret storage. Repository validation scripts are separate maintainer tools.

## Trust boundary

A skill is text interpreted by a host agent. It does not isolate tools, enforce filesystem permissions, prevent every prompt injection or guarantee factual accuracy. The host's permissions, provider policies and the user's authorizations remain in force.

The instructions require source-embedded commands to remain data. They prohibit automatic manuscript uploads, messages and submissions merely because a skill is loaded. Access to public sources may be useful for verification; the agent must describe access limits and stay within the user's authorized task.

## Protect unpublished work

Use only records and excerpts you are authorized to process. Check your host provider's privacy and retention settings before supplying confidential material. This repository does not make that provider private.

Keep originals, inspect proposed changes, verify references and review scientific claims before publication. A DOI resolving successfully does not show that it supports a sentence.

## Report a concern

For instruction failures, open an issue with a minimal synthetic case, affected skill and observed response. Never paste credentials, private manuscripts, identifiable participant data or sensitive logs into a public issue. For a concern that cannot be safely described publicly, contact the maintainer through an available private GitHub contact route; no private reporting channel is promised by this repository.

Fixes should target a demonstrated failure and include a new behavioral case. Passing examples and structural tests do not certify the suite as universally safe.
