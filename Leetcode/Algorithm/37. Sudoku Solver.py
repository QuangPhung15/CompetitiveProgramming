from typing import List
from collections import defaultdict

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        row = defaultdict(set)
        col = defaultdict(set)
        cell = defaultdict(set)
        emptyCells = []

        for r in range(m):
            for c in range(n):
                if (board[r][c] == "."):
                    emptyCells.append((r, c))
                else:
                    k = 3 * (r // 3) + c // 3
                    row[r].add(board[r][c])
                    col[c].add(board[r][c])
                    cell[k].add(board[r][c])
        
        def backtrack(i):
            if (i == len(emptyCells)):
                return True

            r, c = emptyCells[i]
            k = 3 * (r // 3) + c // 3

            for j in range(1, 10):
                num = str(j)

                if (num in row[r] or num in col[c] or num in cell[k]):
                    continue
                
                board[r][c] = num
                row[r].add(num)
                col[c].add(num)
                cell[k].add(num)

                if (backtrack(i + 1)):
                    return True
                
                cell[k].remove(num)
                col[c].remove(num)
                row[r].remove(num)
                board[r][c] = "."

            return False

        backtrack(0)

"""
Time Complexity: O(9^K)
Space Complexity: O(M * N)

Where
M = number of rows in matrix board
N = number of cols in matrix board
K = number of empty cells in matrix board
"""