class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [0] * (n + 1)

        for i in reversed(range(m + 1)):
            if (i == m):
                curr = [float("inf")] * n + [0]
            else:
                curr = [float("inf")] * (n + 1)

            for j in reversed(range(n + 1)): 
                if (i < m and j < n):
                    curr[j] = min(curr[j], (not word1[i] == word2[j]) + dp[j + 1])
                if (i < m):
                    curr[j] = min(curr[j], 1 + dp[j])
                if (j < n):
                    curr[j] = min(curr[j], 1 + curr[j + 1])
            
            dp = curr.copy()
        
        return dp[0]
    
"""
Time Complexity: O(M * N)
Space Complexity: O(N)

Where
M = length of string word1
N = length of string word2
"""