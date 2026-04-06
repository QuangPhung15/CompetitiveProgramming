class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [False] * n + [True]

        for i in reversed(range(m + 1)):
            if (i == m):
                curr = [False] * n + [True]
            else:
                curr = [False] * (n + 1)

            for j in reversed(range(n)):
                if (p[j] == "*"):
                    curr[j] |= curr[j + 1] or dp[j]
                
                if (i < m and (p[j] == "?" or s[i] == p[j])):
                    curr[j] |= dp[j + 1]
            
            dp = curr.copy()
        
        return dp[0]
    
"""
Time Complexity: O(M * N)
Space Complexity: O(N)

Where
M = length of string s
N = length of string p
"""