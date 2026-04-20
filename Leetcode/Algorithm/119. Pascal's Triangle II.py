from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [1]

        for n in range(1, rowIndex + 1):
            curr = [1]

            for i in range(n - 1):
                curr.append(dp[i] + dp[i + 1])
            
            curr.append(1)
            dp = curr.copy()
        
        return dp
    
"""
Time Complexity: O(N^2)
Space Complexity: O(N)

Where
N = the given integer rowIndex
"""