class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        diag1 = set()
        diag2 = set()

        def backtrack(r):
            if (r == n):
                return 1

            res = 0

            for c in range(n):
                d1, d2 = r - c, r + c

                if (c not in col and d1 not in diag1 and d2 not in diag2):
                    col.add(c)
                    diag1.add(d1)
                    diag2.add(d2)

                    res += backtrack(r + 1)

                    diag2.remove(d2)
                    diag1.remove(d1)
                    col.remove(c)
            
            return res
        
        return backtrack(0)

"""
Time Complexity: O(N!)
Space Complexity: O(N)

Where 
N = the given integer n
"""