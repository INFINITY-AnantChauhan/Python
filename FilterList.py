def check(x):
    if (x % 2 == 0 or x % 4 == 0):
        return True
    else:
        return False

# Call check() for every value between 2 to 21
result = list(filter(check, range(2, 22)))
print(result)
