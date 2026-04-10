from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]

        for i in range(n):
            mask = 1 << i

            for j in reversed(range(mask)):
                res.append(res[j] | mask)
        
        return res
    
"""
Time Complexity: O(2^N)
Space Complexity: O(2^N)

Where
N = the given integer n
"""