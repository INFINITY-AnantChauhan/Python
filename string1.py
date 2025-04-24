# Taking input from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Comparing the strings
if string1 == string2:
    print("Both strings are equal.")
elif string1 > string2:
    print(f'"{string1}" is greater than "{string2}".')
else:
    print(f'"{string1}" is less than "{string2}".')

# Comparing the strings based on their length
if len(string1) == len(string2):
    print("Both strings have the same length.")
elif len(string1) > len(string2):
    print(f'"{string1}" is longer than "{string2}".')
else:
    print(f'"{string1}" is shorter than "{string2}".')
