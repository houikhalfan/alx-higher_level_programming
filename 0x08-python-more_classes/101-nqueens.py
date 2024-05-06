#!/usr/bin/python3
"""
N queens backtracking program to print the coordinates of N queens
on an NxN grid such that they are all in non-attacking positions
"""

import sys

print("Script is executing...")

def solve_n_queens(n):
    """Solve the N queens problem and return all solutions"""
    solutions = []

    def is_valid(board, row, col):
        """Check if placing a queen at board[row][col] is valid"""
        # Check if there's already a queen in the same column
        for i in range(row):
            if board[i][col] == 1:
                return False

        # Check upper diagonal on the left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        # Check upper diagonal on the right side
        for i, j in zip(range(row, -1, -1), range(col, n)):  # Adjusted range
            if board[i][j] == 1:
                return False

        return True

    def n_queens_helper(board, row):
        """Helper function for recursive backtracking"""
        if row == n:
            queens = []
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 1:
                        queens.append([i, j])
            solutions.append(queens)
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row][col] = 1
                n_queens_helper(board, row + 1)
                board[row][col] = 0

    # Initialize empty board
    board = [[0] * n for _ in range(n)]

    # Start recursive backtracking
    n_queens_helper(board, 0)

    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = solve_n_queens(n)
    if not solutions:
        print("No solutions found.")
    else:
        for solution in solutions:
            print(solution)
            