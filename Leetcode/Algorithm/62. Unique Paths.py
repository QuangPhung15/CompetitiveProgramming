class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] * (n - 1) + [1]

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if (j + 1 < n):
                    dp[j] += dp[j + 1]
        
        return dp[0]
    
"""
Time Complexity: O(M * N)
Space Complexity: O(N)

Where
M = the given integer m
N = the given integer n
"""