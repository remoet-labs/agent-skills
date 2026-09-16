#!/usr/bin/env python3
"""Package a skill for SkillDock, which will not take our frontmatter as written.

SkillDock validates `metadata` as a flat map of string to string (its OpenAPI
types it that way, and /v1/skills/validate rejects anything else). Our canonical
SKILL.md needs nested metadata for the harnesses that actually matter: Hermes
reads metadata.hermes.tags, OpenClaw reads metadata.openclaw.envVars and
metadata.openclaw.requires.env. Flattening the canonical file to suit the
weakest registry would break both.

So this generates a SkillDock-shaped copy at publish time instead. The body is
untouched, only the frontmatter metadata is flattened, and nothing is committed:
there is one source of truth and this is a build step, not a second skill.

Usage:
    python3 scripts/package-for-skilldock.py skills/remoet <outdir>

Then:
    skilldock skill upload --path <outdir>/remoet --namespace remoet \\
        --slug remoet --version <version>
"""

import pathlib
import shutil
import sys

import yaml


def flatten(value):
    """One metadata value as a string SkillDock will accept."""
    if isinstance(value, str):
        return value
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, list):
        # Only flat lists survive as a readable string. A list of dicts (the
        # openclaw envVars shape) carries structure a comma list would lose, so
        # it is dropped rather than mangled into something misleading.
        if all(isinstance(item, str) for item in value):
            return ", ".join(value)
        return None
    return None


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2

    source = pathlib.Path(sys.argv[1])
    outdir = pathlib.Path(sys.argv[2])
    skill_md = source / "SKILL.md"
    text = skill_md.read_text()

    if not text.startswith("---\n"):
        print(f"error: no frontmatter in {skill_md}")
        return 1
    _, frontmatter, body = text.split("---\n", 2)
    data = yaml.safe_load(frontmatter)

    metadata = data.get("metadata")
    if isinstance(metadata, dict):
        flattened = {}
        dropped = []
        for key, value in metadata.items():
            as_string = flatten(value)
            if as_string is None:
                dropped.append(key)
            else:
                flattened[key] = as_string
        data["metadata"] = flattened
        if dropped:
            print(f"dropped nested metadata (harness-only): {', '.join(dropped)}")

    # SkillDock wants a single top-level folder holding SKILL.md.
    target = outdir / source.name
    if target.exists():
        shutil.rmtree(target)
    target.mkdir(parents=True)
    for item in source.iterdir():
        if item.is_file() and item.name != "SKILL.md":
            shutil.copy2(item, target / item.name)
        elif item.is_dir():
            shutil.copytree(item, target / item.name)

    rebuilt = "---\n" + yaml.safe_dump(data, sort_keys=False, allow_unicode=True) + "---\n" + body
    (target / "SKILL.md").write_text(rebuilt)
    print(f"packaged: {target}")
    print(f"version: {data.get('version')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
