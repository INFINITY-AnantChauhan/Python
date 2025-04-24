num_list = [1, 2, 3, 4, 5]

# Create an iterator
it = iter(num_list)

# Iterate through the list using next()
for i in range(len(num_list)):
    print("Element at index", i, "is:", next(it))
