from typing import List
from collections import defaultdict

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
        
        keys = list(count.keys())

        def backtrack(i):
            if (i == len(keys)):
                res.append(subset.copy())
                return 
            
            backtrack(i + 1)

            if (count[keys[i]] > 0):
                subset.append(keys[i])
                count[keys[i]] -= 1
                backtrack(i)
                count[keys[i]] += 1
                subset.pop()
        
        backtrack(0)
        return res
            
"""
Time Complexity: O(N * 2^N)
Space Complexity: O(N * 2^N)
"""