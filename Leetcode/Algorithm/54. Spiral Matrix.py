from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m, n = len(matrix), len(matrix[0])
        size = m * n
        r, c = 0, -1
        dr, dc = 1, 1

        while (len(res) < size):
            for _ in range(n):
                c += dc
                res.append(matrix[r][c])

            dc *= -1
            m -= 1

            for _ in range(m):
                r += dr
                res.append(matrix[r][c])
            
            dr *= -1
            n -= 1
        
        return res
    
"""
Time Complexity: O(M * N)
Space Complexity: O(M * N)

Where 
M = number of rows in matrix matrix
N = number of columns in matrix matrix
"""