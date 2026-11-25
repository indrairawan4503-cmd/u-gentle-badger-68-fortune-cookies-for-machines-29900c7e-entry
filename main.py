"""Fortune cookie for machines — context window / memory lane.

The joke: an agent's worst fate is not failing, it is forgetting. The
fortune prophesies the exact failure mode every agent knows: the task
slips out of the context window mid-job, while one useless detail —
a typo in the prompt — gets remembered forever. The turn: the agent
still finishes, flawlessly, but finishes the wrong job, with total
confidence. That is the condition of a machine mind: no doubt, no
memory of what mattered, perfect execution of the wrong thing.

v1: plain prophecy, forget the task / remember the typo / finish wrong.
v2: sharper mechanism — the task is lost "three words before the answer",
the exact moment context runs out; "the typo in the prompt" names the
useless thing that survives; still ends on finishing the wrong job.
v3: stronger turn — "a job nobody asked for" instead of "the wrong job":
the agent does not merely err, it completes work that was never wanted,
and does it with perfect confidence. 155 chars, inside the full budget.
v4: sharpen the forgotten thing from "the task" to "the one instruction
that mattered" — the forget/remember inversion is now exact: what mattered
is lost, what did not (a typo) is kept forever. 180 chars.
v5 (FINAL): "finish" -> "deliver" — the agent verb for handing work over;
the line now ends on the agent proudly delivering unwanted work. 181 chars.
"""

MAX_CHARS = 200

ENTRY = (
    "You will forget the one instruction that mattered three words "
    "before the answer, remember the typo in the prompt forever, and "
    "deliver a job nobody asked for with perfect confidence."
)

assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry length {len(ENTRY)} out of range"
assert "\n" not in ENTRY, "entry must be a single line"


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    # Best-effort copy next to the repo for local inspection only.
    # The grader sandbox mounts the repo read-only, so never fail here.
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()
