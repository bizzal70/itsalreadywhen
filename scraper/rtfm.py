"""
Weekly RTFM generator — picks the next unused topic from rtfm_topics.yml,
sends to Claude API, writes a long-form Jekyll post to _rtfm/.

Deliberately NOT sourced from the article database — RTFM is reference-grounded,
evergreen best-practice content, distinct in tone and sourcing from Issues
and Field Notes. No current-events tie-in by design.

Run: python rtfm.py
Requires: ANTHROPIC_API_KEY environment variable
"""

import os
import re
import subprocess
import yaml
from datetime import datetime
from pathlib import Path
import anthropic
from resources import build_related_section

TOPICS_PATH = Path(__file__).parent / "rtfm_topics.yml"
RTFM_DIR = Path(__file__).parent.parent / "_rtfm"


def load_topics():
    with open(TOPICS_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def save_topics(topics):
    with open(TOPICS_PATH, "w", encoding="utf-8") as f:
        yaml.safe_dump(topics, f, sort_keys=False, allow_unicode=True, default_flow_style=False)


def next_topic(topics):
    for t in topics:
        if not t.get("used"):
            return t
    return None


def build_prompt(topic):
    return f"""You are the anonymous author of "It's Already When." — a cybersecurity publication. This piece is for "RTFM": a weekly long-form, technical, reference-grounded article. It is deliberately NOT news-driven and should not reference recent breaches, CVEs, or current events — that's what the Issues and Field Notes sections are for. RTFM is the field manual: durable, technical, best-practice writing about things security practitioners already know they should do and routinely don't.

Same voice as the rest of the publication: dry, world-weary, authoritative, allergic to hype and vendor PR. But this piece is longer-form and more technical/instructional than the news sections — closer to a respected practitioner's essay on first principles than a digest entry.

Topic: {topic['topic']}
Grounding framework: {topic['framework']}
Angle: {topic['angle']}

Write the article in Markdown with this structure. Do NOT include a top-level title or heading (no "# ..." line) — the page template already renders the title separately. Start directly with the opening paragraph.
1. Open with a sharp, opinionated framing of the problem (2-4 sentences) — why this "obvious" thing is still ignored in practice
2. ## The Standard — explain what the framework/control actually requires, in plain language, citing it by name
3. ## Where It Breaks Down — the specific, concrete ways organizations fail to implement this in practice (be technical and specific, not generic)
4. ## Doing It Right — concrete, actionable guidance a practitioner could actually implement
5. ## The Bottom Line — a short closing section that ties it back to the publication's fatalistic voice

Rules:
- Do not reference specific recent breaches, specific CVEs, or current news events — keep this evergreen
- Be technical and specific — name protocols, configurations, tooling categories, not vague generalities
- 1000-1500 words
- Do not mention that you used AI to write this
- Do not use em dashes (—) anywhere in the text. Use periods, commas, or parentheses instead
- End with a single italicized sign-off line that fits the brand voice

Also provide, on the very first line before the article content, a one-sentence summary (for the blog index) prefixed with "SUMMARY:" — this will be stripped from the post.
"""


def write_post(topic, summary, content):
    today = datetime.now().strftime("%Y-%m-%d")
    slug = re.sub(r"[^a-z0-9]+", "-", topic["topic"].lower()).strip("-")
    filename = RTFM_DIR / f"{today}-{slug}.md"

    safe_summary = summary.replace('"', "'")
    frontmatter = f"""---
layout: rtfm
title: "{topic['topic']}"
date: {today}
summary: "{safe_summary}"
framework: "{topic['framework']}"
framework_url: "{topic['framework_url']}"
---

"""
    RTFM_DIR.mkdir(exist_ok=True)
    related = build_related_section(RTFM_DIR.parent, filename.name)
    filename.write_text(
        frontmatter + content + ("\n\n" + related if related else ""),
        encoding="utf-8",
    )
    print(f"RTFM post written: {filename}")
    return filename


def git_push(filepaths):
    repo_root = Path(__file__).parent.parent
    for fp in filepaths:
        subprocess.run(["git", "add", str(fp)], cwd=repo_root, check=True)
    subprocess.run(
        ["git", "commit", "-m", f"RTFM: {filepaths[0].stem}"],
        cwd=repo_root, check=True
    )
    subprocess.run(["git", "push"], cwd=repo_root, check=True)
    print("Pushed to GitHub — GitHub Actions will deploy in ~60 seconds.")


def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise SystemExit("ERROR: Set the ANTHROPIC_API_KEY environment variable.")

    topics = load_topics()
    topic = next_topic(topics)

    if not topic:
        print("No unused RTFM topics remain. Add more to rtfm_topics.yml.")
        return

    print(f"Generating RTFM article: {topic['topic']}...")

    client = anthropic.Anthropic(api_key=api_key)
    response = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=3000,
        messages=[{"role": "user", "content": build_prompt(topic)}]
    )

    raw = response.content[0].text.strip()

    summary = ""
    content_lines = []
    for line in raw.splitlines():
        if line.startswith("SUMMARY:"):
            summary = line.replace("SUMMARY:", "").strip()
        else:
            content_lines.append(line)
    content = "\n".join(content_lines).strip()

    # Safety net: strip a leading H1 if the model adds one despite instructions,
    # since the page template already renders the title.
    if content.startswith("# "):
        content = content.split("\n", 1)[1].lstrip() if "\n" in content else ""

    filepath = write_post(topic, summary, content)

    topic["used"] = True
    save_topics(topics)

    if not os.environ.get("GITHUB_ACTIONS"):
        git_push([filepath, TOPICS_PATH])


if __name__ == "__main__":
    main()
