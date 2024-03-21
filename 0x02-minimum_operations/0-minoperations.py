#!/usr/bin/python3

"""
This module implements a method to calculate the fewest number of operations needed to result in exactly n H characters in a text file.
"""

def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly n H characters.

    Args:
        n (int): The desired number of H characters in the file.

    Returns:
        int: The minimum number of operations required. If n is impossible to achieve, returns 0.
    """
    if n <= 1:
        return n

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n /= divisor
        divisor += 1

    return operations

# Example usage:
if __name__ == "__main__":
    n = 9
    print(f"Number of operations for {n} H characters: {minOperations(n)}")
