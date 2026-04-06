from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0

        for i, n in enumerate(nums):
            if (i - 1 >= 0 and nums[i] == nums[i - 1]):
                continue
            
            nums[k] = n
            k += 1
        
        return k
    
"""
Time Complexity: O(N)
Space Complexity: O(1)

Where 
N = length of list nums
"""