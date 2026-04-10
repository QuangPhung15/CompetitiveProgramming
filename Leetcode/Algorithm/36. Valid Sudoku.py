from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n = len(board), len(board[0])
        row = defaultdict(set)
        col = defaultdict(set)
        cell = defaultdict(set)

        for r in range(m):
            for c in range(n):
                if (board[r][c] == "."):
                    continue
                
                k = 3 * (r // 3) + c // 3

                if (board[r][c] in row[r]):
                    return False
                if (board[r][c] in col[c]):
                    return False
                if (board[r][c] in cell[k]):
                    return False
                
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                cell[k].add(board[r][c])
        
        return True
    
"""
Time Complexity: O(M * N)
Space Complexity: O(M * N)

Where 
M = number of rows in matrix board
N = number of columns in matric board
"""