from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]
        col = set()
        diag1 = set()
        diag2 = set()

        def backtrack(r):
            if (r == n):
                res.append(["".join(b) for b in board])
                return

            for c in range(n):
                d1, d2 = r - c, r + c

                if (c not in col and d1 not in diag1 and d2 not in diag2):
                    board[r][c] = "Q"
                    col.add(c)
                    diag1.add(d1)
                    diag2.add(d2)

                    backtrack(r + 1)

                    diag2.remove(d2)
                    diag1.remove(d1)
                    col.remove(c)
                    board[r][c] = "."
        
        backtrack(0)
        return res

"""
Time Complexity: O(N!)
Space Complexity: O(N! * N^2)

Where
N = the given integer n
"""