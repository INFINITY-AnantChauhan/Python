#Using the copy method:
original_list = [1, 2, 3, 4, 5]
cloned_list = original_list.copy()
print("Original list:", original_list)
print("Cloned list:", cloned_list)

#Using list slicing
original_list = [1, 2, 3, 4, 5]
cloned_list = original_list[:]
print("Original list:", original_list)
print("Cloned list:", cloned_list)

original_list = [1, 2, 3, 4, 5]
cloned_list = list(original_list)
print("Original list:", original_list)
print("Cloned list:", cloned_list)

#sing the list constructor:
import copy
original_list = [1, 2, 3, 4, 5]
cloned_list = copy.copy(original_list)
print("Original list:", original_list)
print("Cloned list:", cloned_list)

#For deep cloning nested lists using the copy module:
import copy
original_list = [1, 2, [3, 4], 5]
cloned_list = copy.deepcopy(original_list)
print("Original list:", original_list)
print("Cloned list:", cloned_list)



