#!/usr/bin/python3

import sys

def is_safe(board, row, col, n):
    # Check if there is a queen in the same column up to the current row
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True

def solve_n_queens_util(board, row, n):
    if row == n:
        print_solution(board)
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_n_queens_util(board, row + 1, n)
            board[row] = -1

def solve_n_queens(n):
    if not isinstance(n, int):
        print("N must be a number", file=sys.stderr)
        sys.exit(1)

    if n < 4:
        print("N must be at least 4", file=sys.stderr)
        sys.exit(1)

    board = [-1] * n
    solve_n_queens_util(board, 0, n)

def print_solution(board):
    print("[", end="")
    for i, col in enumerate(board):
        if i != 0:
            print(", ", end="")
            print("[{}, {}]".format(i, col), end="")
            print("]")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N", file=sys.stderr)
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        solve_n_queens(n)
    except ValueError:
        print("N must be a number", file=sys.stderr)
        sys.exit(1)
