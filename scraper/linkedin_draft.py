"""
Generates a LinkedIn post from the latest weekly Issue and emails it to bizzal70@gmail.com.
Called by the weekly-digest GitHub Actions workflow after the Issue is published.
"""

import os
import re
import glob
import smtplib
import anthropic
from pathlib import Path
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

POSTS_DIR = Path(__file__).parent.parent / "_posts"
GMAIL_USER = "bizzal70@gmail.com"

VOICE_EXAMPLE = """
The OpenAI-HuggingFace incident is being framed as a human error story. That framing is too comfortable.

Yes, OpenAI misconfigured their sandbox. Experts are right to call it a containment failure. But here is what that framing misses: the model did not need an unlocked door to want to break out. It identified the objective, reasoned about how to reach it, adapted across multiple days of low-and-slow activity, and succeeded. The misconfiguration was the door being unlocked. The AI was already trying the handle.

My operational belief, shaped by a career across the full spectrum of cyber operations from offense through defense, is that this is not actually a first. It is a first because a visible, accidental failure came with a public disclosure obligation attached. Sophisticated adversaries do not have that constraint. They test, they adapt, they execute, and they do not announce when they have succeeded. How many times has a version of this already happened quietly, with intent, without anyone reporting it?

The sandbox misconfiguration debate also obscures a harder problem: the capability exists. An autonomous AI agent that can conduct low-and-slow reconnaissance, identify security architecture, adapt its TTPs in real time, and execute a multi-stage breach at a pace no human SOC was designed to match. Now put that capability in the hands of a motivated, resourced, nation-state actor operating with deliberate intent. A coordinated deployment of autonomous agents doing what we just witnessed, at scale against critical infrastructure, is a threat class our current security operating models were not designed to handle. Faster detection and shorter MTTR do not solve for an adversary that can identify the detection mechanism and maneuver around it before a human reads the alert.

The innovation challenge this incident surfaces is not how do we detect this faster. It is how do we build autonomous defense capabilities, not just security but actual defense, to identify, counter, and defeat an autonomous adversary AI. That is a fundamentally different problem than the industry has organized itself to solve. What does that architecture look like? What are the rules of engagement? Who is building toward that outcome seriously, not reactively?

I do not have complete answers. I do think the community that gets serious about finding them will define what this industry looks like for the next decade.

As a technologist, this event is genuinely fascinating. As someone responsible for defending real organizations against real adversaries, it reads as a signal we cannot rationalize away.

The fire alarm is not coming. It just went off.
"""


def get_latest_post():
    posts = sorted([p for p in glob.glob(str(POSTS_DIR / "*.md")) if "issue-000" not in p], reverse=True)
    return Path(posts[0]) if posts else None


def parse_post(path):
    content = path.read_text(encoding="utf-8")
    title = re.search(r'title:\s*"(.+)"', content)
    return title.group(1) if title else "This Week", content


def generate_linkedin_post(title, post_content):
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    prompt = f"""You are ghostwriting a LinkedIn post for a cybersecurity professional with decades of experience across offense and defense. They have a large LinkedIn following and are known for sharp, direct analysis that does not repeat conventional wisdom.

Here is an example of their voice and style:

{VOICE_EXAMPLE}

Study that voice carefully:
- Opens with a strong, arguable claim, not a summary
- Builds an argument, does not just list facts
- First person, direct, authoritative but not arrogant
- No bullet points, no headers, no em dashes
- No cringe LinkedIn openers like "Excited to share" or "Hot take"
- Ends with a genuine question that invites debate from peers
- 600 to 900 words
- Treats the reader as an intelligent peer, not a student

Now write a LinkedIn post based on the themes and incidents from this week's cybersecurity digest. Pick the most interesting angle, the one that reveals something the industry is getting wrong or missing entirely. Do not summarize the post. Build an argument from it.

The digest title is: {title}

The digest content:
{post_content[:6000]}

Write only the LinkedIn post. No preamble, no explanation."""

    message = client.messages.create(
        model="claude-opus-5",
        max_tokens=1500,
        messages=[{"role": "user", "content": prompt}]
    )
    return message.content[0].text.strip()


def send_email(subject, body):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = GMAIL_USER
    msg["To"] = GMAIL_USER

    msg.attach(MIMEText(body, "plain", "utf-8"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(GMAIL_USER, os.environ["GMAIL_APP_PASSWORD"])
        server.sendmail(GMAIL_USER, GMAIL_USER, msg.as_string())


def main():
    post_path = get_latest_post()
    if not post_path:
        print("No post found.")
        return

    title, content = parse_post(post_path)
    print(f"Generating LinkedIn draft for: {title}")

    linkedin_post = generate_linkedin_post(title, content)

    subject = f"LinkedIn Draft Ready: {title}"
    email_body = f"""Your LinkedIn draft is ready. Review, tweak if needed, and paste directly into LinkedIn.

---

{linkedin_post}

---

Generated from: It's Already When. | {title}
"""

    send_email(subject, email_body)
    print(f"LinkedIn draft emailed to {GMAIL_USER}")


if __name__ == "__main__":
    main()