# Remoet for Hermes

Track tech jobs from companies you love, by asking Hermes. Search the public board of open tech roles, find companies by the stack they actually hire for, star the ones that fit, and pull new roles from your shortlist.

**Try this first:**

> I work in Rails, React, and Postgres. Find open roles that use that stack and tell me which companies are hiring for it.

## Install

```bash
hermes plugins install remoet --enable
```

The catalogue tools (`search_jobs`, `search_listings`, `get_listing`) work right away, with no account.

## Sign in for the personal tools

Your profile, stars, saved jobs, feed and applications need a free Remoet account. Sign in once through your browser (OAuth 2.1, no key to paste):

```bash
hermes mcp add remoet --url https://api.remoet.dev/mcp/oauth --auth oauth --connect-timeout 300
```

Before you sign in, Hermes may tell you to run `hermes mcp login remoet`; run the `hermes mcp add` command above instead. After sign-in, `hermes mcp login remoet` is the right way to sign in again, and it keeps your `trust` setting.

The sign-in writes a `remoet` entry to `~/.hermes/config.yaml`, which replaces the plugin's own entry. Hermes stores and refreshes the OAuth tokens. After sign-in, Hermes runs write tools, `apply_to_job` included, without asking, unless you add `trust: untrusted` to that entry:

```yaml
mcp_servers:
  remoet:
    trust: untrusted
```

## What it connects to and what it does

- One remote MCP server, `https://api.remoet.dev/mcp/oauth`, and nothing else: no Python, no hooks, no local code.
- Your requests go to `api.remoet.dev`, and through the session to your model provider.
- Write tools (`star_listing`, `save_job`, `update_profile`, `apply_to_job` and the like) change your Remoet account. `apply_to_job` submits an application to an employer. For scraped roles (most of the board) it only returns the employer's link, and you apply there.
- Your profile (name, photo, summary, location, links) and the work, project and education entries you save are public. `visibility` (`NONE`, `STARRED` or `ALL`) controls which companies can see you as a candidate.
- The tool list comes from Remoet's server at run time. [Full tool catalog](https://github.com/remoet-labs/remoet-mcp/blob/main/tools.md) · [Privacy policy](https://www.remoet.dev/legal/privacy-policy) · [remoet.dev](https://remoet.dev)
