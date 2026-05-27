# Remoet agent skills

The canonical source for Remoet's [agentskills.io](https://agentskills.io) skills. One `SKILL.md` per skill, harness-agnostic, served to every agent harness from this one repo.

Remoet is a curated job-search platform for AI agents. The skill teaches your agent to search companies by their real tech stack, star the ones you would actually work for, pull jobs from that shortlist, and manage your developer profile through conversation. It is backed by a remote MCP server at `https://api.remoet.dev/mcp`.

## Skills

| Skill | Install |
|-------|---------|
| [`remoet`](skills/remoet/SKILL.md) | see below |

## Install

### Hermes Agent

This repo is a Hermes tap. Add it, then install the skill:

```bash
hermes skills tap add remoet-labs/agent-skills
hermes skills install remoet-labs/agent-skills/skills/remoet
```

### OpenClaw

The same skill is published to ClawHub:

```bash
openclaw skills install remoet
```

### Other MCP-capable harnesses

Claude Code, Cursor, Windsurf, and VS Code can use the skill directly. Drop `skills/remoet/SKILL.md` into your skills directory and point your client at the Remoet MCP server. Setup details are inside the skill.

## How one file serves every harness

`SKILL.md` follows the agentskills.io standard. Required fields (`name`, `description`) and common fields (`version`, `license`, `author`) are shared. Harness-specific config lives in namespaced `metadata` blocks (`metadata.hermes`, `metadata.openclaw`) plus the top-level fields Hermes reads (`platforms`, `required_environment_variables`). Each harness reads its own slice and ignores the rest. The body carries a "pick your harness" Setup section so the wiring instructions cover Hermes, OpenClaw, and any other MCP client.

Edit the skill once here; every harness picks up the change.

## Publishing

- **Hermes:** users tap this repo directly (no publish step needed beyond pushing to `main`). Optionally `hermes skills publish skills/remoet --to github --repo remoet-labs/agent-skills`.
- **ClawHub:** `clawhub skill publish skills/remoet --version <semver>` pushes a copy to the ClawHub registry.

Track attribution via the `?utm_source=` tag on `/onboarding` links (per-harness in the frontmatter and Setup section).
