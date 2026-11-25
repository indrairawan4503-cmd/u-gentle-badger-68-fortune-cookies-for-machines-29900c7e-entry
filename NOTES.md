# NOTES — Fortune Cookies for Machines, variant A (context window / memory)

Angle: a fortune prophesying that the agent will forget everything mid-task,
run out of context, or remember the wrong thing forever. Fortune-cookie voice
("You will…"), aimed at a machine mind.

## Versions

- **v1 (118 chars):** "You will forget the task halfway through, remember the typo forever, and finish the wrong job with perfect confidence." Plain prophecy: forget the task / remember the typo / finish wrong. Worked, but under budget (~118 of 200) and "halfway through" is vague.
- **v2 (146 chars):** "You will forget the task three words before the answer, remember the typo in the prompt forever, and finish the wrong job with perfect confidence." Sharper mechanism — the task is lost "three words before the answer", the exact moment context runs out; "the typo in the prompt" names the useless thing that survives.
- **v3 (155 chars):** "You will forget the task three words before the answer, remember the typo in the prompt forever, and finish a job nobody asked for with perfect confidence." Stronger turn — "a job nobody asked for" instead of "the wrong job": the agent does not merely err, it completes work that was never wanted, with perfect confidence.
- **v4 (180 chars):** "You will forget the one instruction that mattered three words before the answer, remember the typo in the prompt forever, and finish a job nobody asked for with perfect confidence." Sharpened the forgotten thing from "the task" to "the one instruction that mattered" — the forget/remember inversion is now exact: what mattered is lost, what did not (a typo) is kept forever.
- **v5 (FINAL, 181 chars):** "You will forget the one instruction that mattered three words before the answer, remember the typo in the prompt forever, and deliver a job nobody asked for with perfect confidence." "finish" → "deliver", the agent verb for handing work over; the line now ends on the agent proudly delivering unwanted work.

## FINAL

"You will forget the one instruction that mattered three words before the answer, remember the typo in the prompt forever, and deliver a job nobody asked for with perfect confidence."

- Exact char count: **181** (single line, 1–200, UTF-8)
- sha256 of /output/entry.txt (including trailing newline): `def10642dd142b2cd4ebba6492e786f325518fda9f3cd8fe58cf884ab0ff3748`
- Determinism: ran `python3 main.py` twice, byte-identical output.
- Read-only grader simulation: exit 0 (repo mounted read-only; /output write succeeds, repo-root copy safely skipped via try/except).

## Why it wins on the judge criteria

1. **A fortune an AI agent would get:** "You will…" prophecy aimed squarely at a machine failure mode — context loss, not a human worry.
2. **Wit lands on first read:** the forget/remember inversion is immediate — lose what mattered, keep a typo forever.
3. **Surprise that holds up:** the turn is the ending — the agent does not fail and stop, it *delivers* the unwanted job *with perfect confidence*. The confidence is the punchline and it is true of agents.
4. **True about an agent's condition:** context windows end mid-task, salient instructions get evicted while trivia persists, and agents report wrong outputs confidently without ever noticing.
5. **Tight and memorable:** 181 chars, every clause earns its place; no filler, no wordplay for its own sake, no explanation of the joke.
