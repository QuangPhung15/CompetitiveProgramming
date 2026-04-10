from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        comb = []

        def backtrack(i):
            if (n + 2 - i < k - len(comb)):
                return 
            
            if (len(comb) == k):
                res.append(comb.copy())
                return 
            
            for j in range(i, n + 1):                
                comb.append(j)
                backtrack(j + 1)
                comb.pop()
        
        backtrack(1)
        return res

"""
Time Complexity: O((K * N!) / (K! * (N - K)!))
Space Complexity: O((K * N!) / (K! * (N - K)!))

Where
N = the given integer n
K = the given integer k
"""