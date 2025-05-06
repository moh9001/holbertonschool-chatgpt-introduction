#!/usr/bin/python3
import sys

def factorial(n):
    """Calculate factorial of a non-negative integer n."""
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./factorial.py <non-negative-integer>")
    else:
        try:
            num = int(sys.argv[1])
            if num < 0:
                print("Error: Factorial is not defined for negative numbers.")
            else:
                print(factorial(num))
        except ValueError:
            print("Error: Please enter a valid integer.")

