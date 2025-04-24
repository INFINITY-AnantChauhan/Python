# Sample list
my_list = [10, 20, 30, 40, 50]

# Using enumerate to iterate through the list with index and value
print("Index and Value:")
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")

# Using range and the list to print only the values
print("\nJust Values:")
for i in range(len(my_list)):
    print(my_list[i])
