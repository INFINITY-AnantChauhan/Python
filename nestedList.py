 # Define a nested list
nested_list = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]


# Loop through all elements in the nested list
for i in range(len(nested_list)):
    for j in range(len(nested_list[i])):
        print(f"Element at nested_list[{i}][{j}]:", nested_list[i][j])

#length of list
print("LENGTH OF LIST",len(nested_list))

# Define the nested list
nested_list = [1, 2, [33, 44, [555, 666]], 7, 8]

# Using nested for loops to access elements
for i in range(len(nested_list)):
        for j in i:
                for k in j:
                    print(f"Element at nested_list[{i}][{j}][{k}]:", nested_list[i][j][k])
           
