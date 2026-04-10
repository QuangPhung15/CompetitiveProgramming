from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if (n <= 0):
                nums[i] = len(nums) + 1
        
        for n in nums:
            n = abs(n) - 1

            if (n >= len(nums)):
                continue

            nums[n] = -1 * abs(nums[n])
        
        for i, n in enumerate(nums):
            if (n > 0):
                return i + 1
        
        return len(nums) + 1
    
"""
Time Complexity: O(N)
Space Complexity: O(1)

Where 
N = length of list nums
"""