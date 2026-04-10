from typing import List
from collections import defaultdict

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
        
        def backtrack(i):
            if (i == len(nums)):
                res.append(perm.copy())
                return
            
            for k, v in count.items():
                if (v == 0):
                    continue
                    
                perm.append(k)
                count[k] -= 1
                backtrack(i + 1)
                count[k] += 1
                perm.pop()
        
        backtrack(0)
        return res

"""
Time Complexity: O(N * N!)
Space Complexity: O(N * N!)

Where 
N = length of list nums
"""