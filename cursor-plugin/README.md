# Remoet for Cursor

Track tech jobs from companies you love, by asking your agent. Search the public board of open tech roles, find companies by the stack they actually hire for, star the ones that fit, and pull new jobs from your shortlist.

**Try this first:**

> I work in Rails, React, and Postgres. Find open roles that use that stack and tell me which companies are hiring for it.

## Signing in

After you install the plugin, the Remoet server (`plugin-remoet-remoet`) asks you to sign in. Click Authenticate and sign in to Remoet with GitHub or Google in your browser (OAuth 2.1). There is no key to paste, and the account is free. Every tool, job search included, needs that sign-in in Cursor.

## What it connects to

This plugin is one remote MCP server, `https://api.remoet.dev/mcp/oauth/strict`, and nothing else: no rules, hooks, scripts or local code. Tool traffic goes to `api.remoet.dev` only; sign-in happens on remoet.dev.

Every write is a tool call your agent makes. Write tools carry annotations your client can use to ask you first, and `apply_to_job` tells the agent to get your consent before submitting. Your profile (name, photo, summary, location, links) and the work, project and education entries you save are public. `visibility` (`NONE`, `STARRED` or `ALL`) controls which companies can see you as a candidate.

[Privacy policy](https://www.remoet.dev/legal/privacy-policy) · [Full tool catalog](https://github.com/remoet-labs/remoet-mcp/blob/main/tools.md) · [remoet.dev](https://remoet.dev)
