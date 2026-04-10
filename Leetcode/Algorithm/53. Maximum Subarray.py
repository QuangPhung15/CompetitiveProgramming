from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-inf")
        curr = float("-inf")

        for n in nums:
            if (n > curr + n):
                curr = 0
            
            curr += n
            res = max(res, curr)
        
        return res
    
"""
Time Complexity: O(N)
Space Complexity: O(1)

Where 
N = length of list nums
"""