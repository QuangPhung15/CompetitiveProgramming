from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                dp = float("inf")

                if (i + 1 < m):
                    dp = min(dp, grid[i + 1][j])
                if (j + 1 < n):
                    dp = min(dp, grid[i][j + 1])
                
                grid[i][j] += dp if (dp != float("inf")) else 0
        
        return grid[0][0]
    
"""
Time Complexity: O(M * N)
Space Complexity: O(1)

Where
M = the number of rows in matrix grid
N = the number of columns in matrix grid
"""