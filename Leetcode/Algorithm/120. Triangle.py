from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        for i in reversed(range(n - 1)):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])

        return triangle[0][0]

"""
Time Complexity: O(N^2)
Space Complexity: O(1)

Where
N = number of row in matrix triangle
"""