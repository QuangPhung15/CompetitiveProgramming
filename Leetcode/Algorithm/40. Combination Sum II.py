from typing import List
from collections import defaultdict

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        count = defaultdict(int)

        for c in candidates:
            count[c] += 1
        
        nums = sorted(list(count.keys()))

        def backtrack(i, curr):
            if (i == len(nums) or curr > target):  
                return
            
            if (curr == target):
                res.append(comb.copy())
                return
            
            backtrack(i + 1, curr)

            if (count[nums[i]] > 0):
                count[nums[i]] -= 1
                comb.append(nums[i])
                backtrack(i, curr + nums[i])
                comb.pop()
                count[nums[i]] += 1
        
        backtrack(0, 0)
        return res
    
"""
Time Complexity: O(2^N)
Space Complexity: O(2^N)

Where
N = length of list candidates
"""