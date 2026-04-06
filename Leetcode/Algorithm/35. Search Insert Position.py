from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        res = n
        l, r = 0, n - 1

        while (l <= r):
            m = l + (r - l) // 2

            if (nums[m] >= target):
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res
    
"""
Time Complexity: O(logN)
Space Complexity: O(1)

Where 
N = length of list nums
"""