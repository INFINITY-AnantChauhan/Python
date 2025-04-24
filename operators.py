"""airthmetic """
print("<<<<<<<     AIRTHMETIC    >>>>>>>>>")
# Variables
a = int(input("enter the 1st variable"))
b = int(input("enter the 2nd variable"))

# Addition
addition = a + b
print(f"Addition: {a} + {b} = {addition}")

# Subtraction
subtraction = a - b
print(f"Subtraction: {a} - {b} = {subtraction}")

# Multiplication
multiplication = a * b
print(f"Multiplication: {a} * {b} = {multiplication}")

# Division
division = a / b
print(f"Division: {a} / {b} = {division}")

# Modulus (Remainder)
modulus = a % b
print(f"Modulus: {a} % {b} = {modulus}")

# Exponentiation (Power)
exponentiation = a ** b
print(f"Exponentiation: {a} ** {b} = {exponentiation}")

# Floor Division
floor_division = a // b
print(f"Floor Division: {a} // {b} = {floor_division}")

print("_________________________________________________________________________________________________")
"""Comparision"""
print("<<<<<<<     COMPARISION    >>>>>>>>>")
# Variables
a = int(input("enter the 1st variable"))
b = int(input("enter the 2nd variable"))

# Equal to
print(f"{a} == {b} : {a == b}")

# Not equal to
print(f"{a} != {b} : {a != b}")

# Greater than
print(f"{a} > {b} : {a > b}")

# Less than
print(f"{a} < {b} : {a < b}")

# Greater than or equal to
print(f"{a} >= {b} : {a >= b}")

# Less than or equal to
print(f"{a} <= {b} : {a <= b}")


print("_________________________________________________________________________________________________")
""" bitwise"""
print("<<<<<<<     BITWISE    >>>>>>>>>")
# Variables
a = int(input("Enter the 1st variable: "))
b = int(input("Enter the 2nd variable: "))
print("Binary of", a, "is", bin(a))
print("Binary of", b, "is", bin(b))

# Bitwise AND
print(f"{a} & {b} = {a & b}")
print(f"bin(a) & bin(b) = {bin(a & b)}")
print(" ")

# Bitwise OR
print(f"{a} | {b} = {a | b}") 
print(f"bin(a) | bin(b) = {bin(a | b)}")
print(" ")

# Bitwise XOR
print(f"{a} ^ {b} = {a ^ b}")
print(f"bin(a) ^ bin(b) = {bin(a ^ b)}")
print(" ")

# Bitwise NOT
print(f"~{a} = {~a}")
print(f"~bin(a) = {bin(~a)}")
print(" ")
 
# Left Shift
print(f"{a} << 2 = {a << 2}")
print(f"bin(a) << 2 = {bin(a << 2)}")
print(" ")

# Right Shift
print(f"{a} >> 2 = {a >> 2}")  
print(f"bin(a) >> 2 = {bin(a >> 2)}")

print("_________________________________________________________________________________________________")
""" logical """
print("<<<<<<<    LOGICAL     >>>>>>>>>")
# Variables
a = int(input("Enter the 1st variable: "))
b = int(input("Enter the 2nd variable: "))
# Logical AND
if a > 5 and b > 15:
    print("Both conditions are True (Logical AND)")

# Logical OR
if a > 15 or b > 15:
    print("At least one condition is True (Logical OR)")

# Logical NOT
if not (a > 15):
    print("Condition is False, so NOT operator makes it True")





















































    
