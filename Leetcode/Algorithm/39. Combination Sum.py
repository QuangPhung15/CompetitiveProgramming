from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        n = len(candidates)
        candidates.sort()
        
        def backtrack(i, curr):
            if (curr == target):
                res.append(comb.copy())
                return
            
            if (curr > target or i == n):
                return
            
            backtrack(i + 1, curr)

            comb.append(candidates[i])
            backtrack(i, curr + candidates[i])
            comb.pop()
        
        backtrack(0, 0)
        return res
    
"""
Time Complexity: O(2^(T/min_val))
Space Complexity: O(2^(T/min_val))

Where
T = the given integer target
min_val = the minimum value of list candidates  
"""