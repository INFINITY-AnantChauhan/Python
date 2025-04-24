import functools  # functools is a module that contains the function reduce()

def add(x, y):
    return x + y

num_list = [1, 2, 3, 4, 5]
print("Sum of values in list = ", end="")
print(functools.reduce(add, num_list))
