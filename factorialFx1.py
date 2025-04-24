def factorial(n):
    """
    Calculate the factorial of a non-negative integer n using recursion.

    Parameters:
    n (int): A non-negative integer whose factorial is to be computed.

    Returns:
    int: The factorial of n.

    Raises:
    ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
# Documantation String
print(factorial.__doc__)

print(dir())
