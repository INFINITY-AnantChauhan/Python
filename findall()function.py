import re

pattern = r'[A-Z]{3} \d{4}'
text = "LXJ 2013, VXI 2015, VOI 20104, Maruti Suzuki Cars in India."

matches = re.findall(pattern, text)

for match in matches:
    print(match, end=" ")
print("\n\n\n\n__________________________________________\n\n\n\n")
import re
line="pet:cat i love cats pet:cow i love cows"
match = re.findall(r"pet:\w\w\w", line)
print(match)
