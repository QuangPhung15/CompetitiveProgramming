from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[-1] * n for _ in range(n)]
        i, size = 1, n * n
        r, c = 0, -1
        dr, dc = 1, 1

        while (i <= size):
            for _ in range(n):
                c += dc
                res[r][c] = i
                i += 1
            
            n -= 1
            dc *= -1

            for _ in range(n):
                r += dr
                res[r][c] = i
                i += 1

            dr *= -1
        
        return res

"""
Time Complexity: O(N^2)
Space Complexity: O(N^2)

Where
N = the given integer n
"""