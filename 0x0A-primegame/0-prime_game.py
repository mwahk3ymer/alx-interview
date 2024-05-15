#!/usr/bin/python3
"""
This module contains functions to determine winner of game played between
"""


def sieve(n):
    """Use the Sieve of Eratosthenes to find all primes up to n."""
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p in range(2, n + 1) if is_prime[p]]
    return primes


def play_game(n, primes):
    """Simulate a game and determine the winner."""
    available = [True] * (n + 1)
    move_count = 0
    for p in primes:
        if p > n:
            break
        if available[p]:
            move_count += 1
            for multiple in range(p, n + 1, p):
                available[multiple] = False
    return "Maria" if move_count % 2 == 1 else "Ben"


def isWinner(x, nums):
    """Determine the overall winner after x rounds."""
    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    primes = sieve(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n, primes)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


if __name__ == "__main__":
    x = 3
    nums = [4, 5, 1]
    print(isWinner(x, nums))
