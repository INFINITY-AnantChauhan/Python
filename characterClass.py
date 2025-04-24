import re

pattern=r"[aeiou]"

if re.search(pattern, "clue"): print("Match clue")

if re.search(pattern, "bcdfg"): print("Match bcdfg")
