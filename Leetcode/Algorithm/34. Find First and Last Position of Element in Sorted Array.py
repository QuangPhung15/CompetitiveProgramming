from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        n = len(nums)
        l, r = 0, n - 1

        while (l <= r):
            m = l + (r - l) // 2

            if (nums[m] == target):
                res[0] = m
                r = m - 1
            elif (nums[m] > target):
                r = m - 1
            else:
                l = m + 1
        
        l, r = 0, n - 1

        while (l <= r):
            m = l + (r - l) // 2

            if (nums[m] == target):
                res[1] = m
                l = m + 1
            elif (nums[m] > target):
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