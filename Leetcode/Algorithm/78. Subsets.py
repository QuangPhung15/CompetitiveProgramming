from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        n = len(nums)

        def backtrack(i):
            if (i == n):
                res.append(subset.copy())
                return
            
            backtrack(i + 1)

            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()
        
        backtrack(0)
        return res

"""
Time Complexity: O(N * 2^N)
Space Complexity: O(N * 2^N)

Where 
N = length of list nums
"""