#!/usr/bin/python3
""" N queens """
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """ N queens function"""
        cols = set()
        diagpos = set()
        diagneg = set()

        res = []
        board = [['.'] * n for _ in range(n)]

        def backtrack(row):
            if row == n:
                res.append(["".join(row) for row in board])
                return
            for c in range(n):
                if c not in cols and row + c not in diagpos and
                row - c not in diagneg:
                    board[row][c] = 'Q'
                    cols.add(c)
                    diagpos.add(row + c)
                    diagneg.add(row - c)
                    backtrack(row + 1)
                    board[row][c] = '.'
                    cols.remove(c)
                    diagpos.remove(row + c)
                    diagneg.remove(row - c)
        backtrack(0)
        return res
