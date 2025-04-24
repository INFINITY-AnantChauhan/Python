# Using map to double the values in a list
numbers = [1, 2, 3, 4, 5]

# Use map to apply a lambda function that doubles each value
doubled = list(map(lambda x: x * 2, numbers))

print("Original list:", numbers)
print("Doubled values:", doubled)
