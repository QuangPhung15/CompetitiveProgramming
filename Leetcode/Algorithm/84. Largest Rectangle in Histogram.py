from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        stack = []

        for i, h in enumerate(heights):
            l = i

            while (stack and h <= stack[-1][0]):
                curr, l = stack.pop()
                res = max(res, curr * (i - l))
            
            stack.append((h, l))
        
        while (stack):
            curr, j = stack.pop()
            res = max(res, curr * (n - j))
        
        return res

"""
Time Complexity: O(N)
Space Complexity: O(N)

Where
N = length of list heights
"""