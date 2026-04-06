from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, n in enumerate(nums):
            remain = target - n

            if (remain in seen):
                return [seen[remain], i]
            
            seen[n] = i
        
        return []

"""
Time Complexity: O(N)
Space Complexity: O(N)

Where
N = length of list nums
"""