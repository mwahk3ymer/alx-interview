#!/usr/bin/python3

def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly n H characters.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The fewest number of operations needed, or 0 if n is impossible to achieve.
    """
    if n <= 1:
        return 0

    # Initialize count and clipboard size
    count = 0
    clipboard = 1

    while clipboard < n:
        if n % clipboard == 0:
            # If clipboard is a divisor of n, paste clipboard 'n // clipboard' times
            count += (n // clipboard) - 1
            return count
        else:
            # If clipboard is not a divisor of n, increase clipboard
            clipboard += clipboard
            count += 1

    return count

if __name__ == "__main__":
    n = 9
    print("Number of operations:", minOperations(n))
