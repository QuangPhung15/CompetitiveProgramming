from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for n in nums:
            if (n == val):
                continue
            
            nums[k] = n
            k += 1

        return k 
    
"""
Space Complexity: O(N)
Time Complexity: O(1)

Where 
N = length of list nums
"""