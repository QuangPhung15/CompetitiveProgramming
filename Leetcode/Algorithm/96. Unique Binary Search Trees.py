class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1] + [0] * n

        for i in range(1, n + 1):
            l, r = 0, i - 1

            for j in range(i):
                dp[i] += dp[l] * dp[r]
                l += 1
                r -= 1
        
        return dp[-1]
    
"""
Time Complexity: O(N^2)
Space Complexity: O(N)

Where
N = the given integer n
"""