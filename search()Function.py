import re

string = "She sells sea shells on the sea shore"
pattern = "sells"

if re.search(pattern, string):
    print("Match Found")
else:
    print(pattern, "is not present in the string")
