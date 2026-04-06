from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        r = n - 1

        for i in reversed(range(n - 1)):
            if (i + nums[i] >= r):
                r = i
        
        return r == 0

"""
Time Complexity: O(N)
Space Complexity: O(1)

Where 
N = length of list nums
"""