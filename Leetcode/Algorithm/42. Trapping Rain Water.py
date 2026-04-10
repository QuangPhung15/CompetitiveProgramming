from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        left, right = 0, 0

        while (l <= r):
            if (left <= right):
                res += max(0, left - height[l])
                left = max(left, height[l])
                l += 1
            else:
                res += max(0, right - height[r])
                right = max(right, height[r])
                r -= 1
        
        return res
    
"""
Time Complexity: O(N)
Space Complexity: O(1)

Where 
N = length of list height
"""