from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0

        for n in nums:
            if (k - 2 >= 0 and (n == nums[k - 1] and n == nums[k - 2])):
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