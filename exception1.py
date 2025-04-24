num = int(input("Enther the numerator"))
deno = int(input("Enter the denominator"))
try:
    quo = num/deno
    print("QUOTIENT:",quo)
except ZeroDivisionError:
