import re

pattern = r"gr(ea)*t"

if re.match(pattern, "greaeaeaeaeaeaeat"): print("Match greaeaeaeaeaeaeat")
