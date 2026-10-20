---
name: ste
description: Turn Simplified Technical English (STE, ASD-STE100) on or off for the current session by switching the session's output style. Use only when the user types /ste, /ste on, or /ste off.
argument-hint: "[on|off]"
---

# /ste — Simplified Technical English for this session

The STE rules live in one file: `output-styles/ste.md` in the user's Claude folder
(`$CLAUDE_CONFIG_DIR` if it is set, else `~/.claude`). The output style name is `STE`.
This skill switches the current session to that output style, so the rules sit in the system
prompt for the full session and stay on after compaction.

Argument: empty or `on` turns STE on. `off` turns STE off. Any other argument: ask which one.

## /ste or /ste on

1. Read `output-styles/ste.md` in the Claude folder. Follow its rules from this reply on,
   because the output style starts only on the next turn.
2. Load the tool if it is deferred: ToolSearch with
   `select:mcp__ccd_session_mgmt__set_session_output_style`.
3. Call `mcp__ccd_session_mgmt__set_session_output_style` with `session_id: "self"` and
   `style: "STE"`.
4. If the call succeeds, reply in one or two STE sentences: STE is on for this session, and
   `/ste off` turns it off.
5. If the call fails, keep the STE rules on for this session anyway, and tell the user why in
   one sentence. Common causes:
   - The tool does not exist (terminal session): tell the user to choose the `STE` output
     style in `/config`.
   - `STE` is not in the session's list: the session started before the style was installed.
     Tell the user that new sessions will have it.
   - The style file does not exist: tell the user to install it again from
     https://jedistateofmind07.github.io/claude-ste/

## /ste off

1. Load the tool if it is deferred (see step 2 above).
2. Call `mcp__ccd_session_mgmt__set_session_output_style` with `session_id: "self"` and
   `style: "default"`.
3. Stop the STE rules for the rest of this session. This also overrides an STE rule in the
   user's memory (for example the `ste:start` block in `CLAUDE.md`) for this session only.
   New sessions still follow that memory.
4. Confirm in one sentence of normal English. If the call failed, say so and tell the user to
   choose `default` in the session's output-style menu or in `/config`.

## Notes

- Do not edit memory files or `settings.json` from this skill. The skill changes one session.
- STE applies to chat replies, questions to the user, and recaps. Text for other people
  (commits, PRs, docs, Slack, email, code comments) keeps its usual style.
