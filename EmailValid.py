import re

def isvalidEmail(email):
    pattern = r'^[a-zA-Z0-9]+[a-zA-Z0-9._]*[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return "Valid Email"
    else:
        return "Invalid Email"

email = input("ENTER THE EMAIL: ")
print(isvalidEmail(email))

