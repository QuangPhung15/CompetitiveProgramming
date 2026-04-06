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
                match = i < m and (s[i] == p[j] or p[j] == ".")

                if (j + 1 < n and p[j + 1] == "*"):
                    curr[j] |= curr[j + 2]

                    if (match):
                        curr[j] |= dp[j]

                if (match):
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