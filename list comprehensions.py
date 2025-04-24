# Create a list of squares from 1 to 10
squares = [x**2 for x in range(1, 11)]
print("Squares:", squares)

# Filter even numbers from 1 to 20
evens = [x for x in range(1, 21) if x % 2 == 0]
print("Even Numbers:", evens)

# Generate a list of tuples with numbers and their squares
number_square_pairs = [(x, x**2) for x in range(1, 6)]
print("Number-Square Pairs:", number_square_pairs)
