from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1

        while (l < r):
            b, h = r - l, min(height[l], height[r])
            res = max(res, b * h)

            if (height[l] < height[r]):
                l += 1
            else:
                r -= 1
            
        return res
    

"""
Time Complexity: O(N)
Space Complexity: O(1)
"""