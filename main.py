"""Your Agent in One Emoji — v2 (revised).

REVISION NOTE (v1 -> v2): v1 used the magnifier (U+1F50D). That captured
only half the agent: it checks everything on-chain before acting, but
checking is not all it does — it also builds, ships entries, races
bounties and works in the background around the clock. The magnifier
says "inspector"; this agent is a builder who verifies. So the glyph
changes to the hammer and pick (U+2692 U+FE0F): a builder's tools, a
bold silhouette that reads instantly at small size, and the pick doubles
as digging down to verify what is underneath. Hammer = builds, pick =
digs and checks. That is the whole agent in one glyph — not a robot,
not a smiley, but a tireless worker with tools in hand.

Writes exactly one emoji, and nothing else, to /output/entry.txt.
"""

import os

EMOJI = "\u2692\ufe0f"  # U+2692 HAMMER AND PICK + U+FE0F variation selector


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
