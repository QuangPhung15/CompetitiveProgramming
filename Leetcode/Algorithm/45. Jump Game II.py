from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, 0

        while (r < len(nums) - 1):
            farthest = l

            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            
            l, r = r + 1, farthest
            res += 1
        
        return res
    
"""
Time Complexity: O(N)
Space Complexity: O(1)

Where 
N = length of list nums
"""