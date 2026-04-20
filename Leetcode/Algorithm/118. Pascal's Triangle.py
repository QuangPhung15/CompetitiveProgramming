from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for n in range(1, numRows):
            curr = [1]

            for i in range(n - 1):
                curr.append(res[-1][i] + res[-1][i + 1])
            
            curr.append(1)
            res.append(curr)
        
        return res

"""
Time Complexity: O(N^2)
Space Complexity: O(N^2)

Where
N = the given integer numRows
"""