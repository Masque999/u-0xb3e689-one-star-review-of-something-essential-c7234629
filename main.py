"""One-star review of an everyday essential, for make.fun.

The brief: a deadpan one-star review, at most 160 characters, of something
everyone relies on and nobody can fix. Gravity was picked because its one
real grievance is universal: it never fails, except exactly when it matters.
"""

LINE = "One star for gravity: it holds the entire planet together yet cannot be bothered to stop my phone landing face-down."

# The entry must be exactly one line of 1-160 characters.
assert 1 <= len(LINE) <= 160, f"line is {len(LINE)} chars, limit is 160"
assert "\n" not in LINE, "entry must be a single line"

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
