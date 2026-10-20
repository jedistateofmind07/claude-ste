#!/usr/bin/env python3
"""Build index.html and the README prompt section from install-prompt.txt.

Run after you edit install-prompt.txt or scripts/page.template.html:
    python3 scripts/build-page.py
"""
import html
import pathlib
import re
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent
MAX_QUERY = 5000  # Claude Code rejects a deep-link prompt longer than this.

prompt = (ROOT / "install-prompt.txt").read_text().strip()
if len(prompt) > MAX_QUERY:
    raise SystemExit(f"install-prompt.txt is {len(prompt)} chars; the limit is {MAX_QUERY}")

deep_link = "claude-cli://open?q=" + urllib.parse.quote(prompt, safe="")

page = (ROOT / "scripts" / "page.template.html").read_text()
page = page.replace("{{DEEP_LINK}}", html.escape(deep_link, quote=True))
page = page.replace("{{PROMPT}}", html.escape(prompt, quote=False))
(ROOT / "index.html").write_text(page)

readme_path = ROOT / "README.md"
readme = readme_path.read_text()
block = f"<!-- prompt:start -->\n```text\n{prompt}\n```\n<!-- prompt:end -->"
readme, n = re.subn(r"<!-- prompt:start -->.*?<!-- prompt:end -->", lambda _: block, readme, flags=re.S)
if n != 1:
    raise SystemExit("README.md needs one <!-- prompt:start --> ... <!-- prompt:end --> block")
readme_path.write_text(readme)

print(f"prompt: {len(prompt)} chars, deep link: {len(deep_link)} chars")
