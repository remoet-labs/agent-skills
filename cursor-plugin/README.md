# Remoet for Cursor

Track tech jobs from companies you love, by asking your agent. Search the public board of open tech roles, find companies by the stack they actually hire for, star the ones that fit, and pull new jobs from your shortlist.

**Try this first:**

> I work in Rails, React, and Postgres. Find open roles that use that stack and tell me which companies are hiring for it.

## Signing in

If you added Remoet to `~/.cursor/mcp.json` by hand earlier, remove that entry so its tools don't show up twice.

The catalogue tools (`search_jobs`, `search_listings`, `get_listing`) work without an account. For the personal tools (profile, stars, saved jobs, your feed, applications), open Cursor Settings > MCP, find `remoet`, click Connect and sign in to Remoet with GitHub or Google in your browser (OAuth 2.1). There is no key to paste, and the account is free.

## What it connects to

This plugin is one remote MCP server, `https://api.remoet.dev/mcp/oauth`, and nothing else: no rules, hooks, scripts or local code. It connects to `api.remoet.dev` only.

Every write is a tool call your agent makes. Write tools carry annotations your client can use to ask you first, and `apply_to_job` tells the agent to get your consent before submitting. Your profile (name, photo, summary, location, links) and the work, project and education entries you save are public. `visibility` (`NONE`, `STARRED` or `ALL`) controls which companies can see you as a candidate.

[Privacy policy](https://www.remoet.dev/legal/privacy-policy) · [Full tool catalog](https://github.com/remoet-labs/remoet-mcp/blob/main/tools.md) · [remoet.dev](https://remoet.dev)
