def print_diamond(n):
    for i in range(1, n + 1, 2):
        print(" " * ((n - i) // 2) + "*" * i)
    for i in range(n - 2, 0, -2):
        print(" " * ((n - i) // 2) + "*" * i)

size = int(input("Enter the size : "))
if size % 2 == 0:
    print("Please enter an odd number.")
else:
    print_diamond(size)
