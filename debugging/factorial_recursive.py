#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given non-negative integer.

    The factorial of a number n is defined as n * (n-1) * (n-2) * ... * 1.
    The factorial of 0 is defined as 1 by convention.

    Parameters:
    n (int): The non-negative integer for which to compute the factorial.

    Returns:
    int: The factorial of the input number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Retrieve the first command-line argument, convert it to an integer, and calculate its factorial
f = factorial(int(sys.argv[1]))

# Print the result to the console
print(f)

