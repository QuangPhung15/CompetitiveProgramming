from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        res = 0
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n

        def helper(heights):
            res = 0
            stack = []

            for r, h in enumerate(heights):
                l = r

                while (stack and h <= stack[-1][0]):
                    curr, l = stack.pop()
                    res = max(res, curr * (r - l))
                
                stack.append((h, l))
            
            while (stack):
                curr, l = stack.pop()
                res = max(res, curr * (n - l))
            
            return res

        for i in range(m):
            for j in range(n):
                if (matrix[i][j] == "0"):
                    heights[j] = 0
                else:
                    heights[j] += 1
            
            res = max(res, helper(heights))
        
        return res

"""
Time Complexity: O(M * N)
Space Complexity: O(N)

Where
M = number of rows in matrix matrix
N = number of columns in matrix matrix
"""