import re

string = "She sells sea shells on the sea shore"
pattern1 = "sells"

if re.match(pattern1, string):
    print("Match Found")
else:
    print(pattern1, "is not present in the string")

pattern2 = "She"

if re.match(pattern2, string):
    print("Match Found")
else:
    print(pattern2, "is not present in the string")
