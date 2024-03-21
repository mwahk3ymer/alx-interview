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

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            # If clipboard is a divisor of n, paste clipboard 'n // clipboard' times
            operations += divisor
            n //= divisor
            divisor += 1
            
            return operations

if __name__ == "__main__":
    n = 4
    print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))
