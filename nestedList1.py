# Define the initial nested list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]



# Append: Add an element to the end of the list
nested_list.append(6)
print("After append:", nested_list)

# Insert: Insert an element at a specific position
nested_list.insert(2, 7)  # Insert 7 at index 2
print("After insert:", nested_list)

# Pop: Remove and return the last element of the list
popped_element = nested_list.pop()
print("After pop:", nested_list)
print("Popped element:", popped_element)

popped_element = nested_list.pop()
print("After pop:", nested_list)
print("Popped element:", popped_element)

# Remove: Remove the first occurrence of a value
nested_list.remove(7)  # Remove the first occurrence of 7
print("After remove:", nested_list)

# Extend: Extend the list by appending elements from another list
nested_list.extend([8, 9, 10])
print("After extend:", nested_list)

# Update a specific index
nested_list[0] = 11  # Update the value at index 0
print("After updating index 0:", nested_list)

# Slice assignment: Replace a portion of the list
nested_list[1:3] = [12, 13]  # Replace elements at index 1 and 2
print("After slice assignment:", nested_list)

# Clear: Remove all elements from the list
nested_list.clear()
print("After clear:", nested_list)
