# /ste for Claude Code

A Claude Code skill: Claude writes to you in Simplified Technical English (a practical subset of
ASD-STE100). Short sentences, active voice, simple words, no idioms.

**Install page:** https://jedistateofmind07.github.io/claude-ste/

It works with any Claude account. It only adds files to your Claude folder (`~/.claude`, or
`$CLAUDE_CONFIG_DIR` if you set it).

## Install

Click **Install in Claude Code** on the install page. Claude Code opens in your terminal with the
prompt below already typed. Read it, then press Enter.

If no terminal opens, or you use the desktop app, paste this prompt into any Claude Code session:

<!-- prompt:start -->
```text
Install the /ste skill (Simplified Technical English for Claude Code) from https://github.com/jedistateofmind07/claude-ste

Do these steps:
1. Find my Claude folder. Use $CLAUDE_CONFIG_DIR if it is set, else ~/.claude. Call it DIR.
2. Use curl to download these two files. Make the folders if they do not exist. Replace old copies.
   - https://raw.githubusercontent.com/jedistateofmind07/claude-ste/main/skills/ste/SKILL.md to DIR/skills/ste/SKILL.md
   - https://raw.githubusercontent.com/jedistateofmind07/claude-ste/main/output-styles/ste.md to DIR/output-styles/ste.md
3. Make sure that each file starts with "---". If a download failed, stop and tell me.
4. Ask me one multiple-choice question: "STE in every session" or "Only when I type /ste".
5. If I choose "STE in every session": download https://raw.githubusercontent.com/jedistateofmind07/claude-ste/main/memory/CLAUDE-ste.md and show it to me. Then add it to the end of DIR/CLAUDE.md. Make that file if it does not exist. If DIR/CLAUDE.md already has a block from "<!-- ste:start" to "<!-- ste:end -->", replace only that block. Do not change other text in the file.
6. If I choose "Only when I type /ste": remove that block from DIR/CLAUDE.md if it is there. Make no other memory change.
7. Tell me what you installed. Tell me that it works in new sessions: /ste turns STE on, and /ste off turns it off.
```
<!-- prompt:end -->

## What it installs

| File | What it does |
| --- | --- |
| `skills/ste/SKILL.md` | The `/ste` command. `/ste` turns STE on for the session; `/ste off` turns it off. |
| `output-styles/ste.md` | The full STE rules, as an output style named `STE`. |
| `CLAUDE.md` block (optional) | Makes every session use STE. The install asks you first. Source: `memory/CLAUDE-ste.md`. |

STE applies to Claude's chat replies, questions, and recaps. Commits, PRs, docs, and messages for
other people keep their usual style.

## Remove it

1. Delete `skills/ste/` and `output-styles/ste.md` from your Claude folder.
2. In `CLAUDE.md`, delete the block from `<!-- ste:start` to `<!-- ste:end -->`.

## Maintain it

Edit `install-prompt.txt` or `scripts/page.template.html`, then run `python3 scripts/build-page.py`
to rebuild `index.html` and the prompt above. GitHub Pages serves `index.html` from `main`.
