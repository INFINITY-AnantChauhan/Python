# Create an initial list
my_list = [1, 2, 3, 4, 5]

# Append: Add an element to the end of the list
my_list.append(6)
print("After append:", my_list)

# Insert: Insert an element at a specific position
my_list.insert(2, 7)  # Insert 7 at index 2
print("After insert:", my_list)

# Pop: Remove and return the last element of the list
popped_element = my_list.pop()
print("After pop:", my_list)
print("Popped element:", popped_element)

# Remove: Remove the first occurrence of a value
my_list.remove(7)  # Remove the first occurrence of 7
print("After remove:", my_list)

# Extend: Extend the list by appending elements from another list
my_list.extend([8, 9, 10])
print("After extend:", my_list)

# Update a specific index
my_list[0] = 11  # Update the value at index 0
print("After updating index 0:", my_list)

# Slice assignment: Replace a portion of the list
my_list[1:3] = [12, 13]  # Replace elements at index 1 and 2
print("After slice assignment:", my_list)

# Clear: Remove all elements from the list
my_list.clear()
print("After clear:", my_list)
