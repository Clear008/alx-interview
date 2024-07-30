#!/usr/bin/python3
""" N queens """
import sys

def is_safe(board, row, col):
    """Check this column on upper side"""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(N):
    """ N queens function"""
    def solve(board, row):
        if row == N:
            solutions.append(board[:])
            return
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                solve(board, row + 1)
                board[row] = -1

    solutions = []
    board = [-1] * N
    solve(board, 0)
    return solutions

