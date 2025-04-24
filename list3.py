#Ma'am code
num_list = [1,2,3,4,5,6,7,8,9,10]

print("num_list is : ", num_list)
print("First element in the list is ", num_list[0])
print("num_list[2:5] = ", num_list[2:5])
print("num_list[::2] = ", num_list[::2])
print("num_list[1::3] = ", num_list[1::3])
print("num_list[-1:-len(num_list)] = ", num_list[-1:-len(num_list)])
print("num_list[-1] = ", num_list[-1])

#mee
#Creating a list
num_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Traversing the list using a for loop
print("Traversing the list:")
for num in num_list:
    print(num, end=" ")  # Prints elements in a single line
print("\n")  # New line for better readability

# List Slicing Demonstrations
print("Original List:", num_list)

# Extracting a portion of the list
print("num_list[2:6] =", num_list[2:6])  # Elements from index 2 to 5

# Skipping elements using step
print("num_list[::2] =", num_list[::2])  # Every second element

# Reversing the list using slicing
print("Reversed List:", num_list[::-1])

# Extracting elements from index 1 to end, skipping 2 steps
print("num_list[1::2] =", num_list[1::2])
