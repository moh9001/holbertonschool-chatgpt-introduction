#!/usr/bin/python3
import sys

def factorial(n):
    """
    Recursively calculates the factorial of a non-negative integer.

    Parameters:
        n (int): A non-negative integer whose factorial is to be computed.

    Returns:
        int: The factorial of the input number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    try:
        num = int(sys.argv[1])
        if num < 0:
            print("Error: Factorial is not defined for negative numbers.")
        else:
            print(factorial(num))
    except (IndexError, ValueError):
        print("Usage: ./factorial_recursive.py <non-negative integer>")

