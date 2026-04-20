class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(t), len(s)
        dp = [1] * (n + 1)

        for i in reversed(range(m)): 
            curr = [0] * (n + 1)

            for j in reversed(range(n)):
                curr[j] = curr[j + 1]

                if (t[i] == s[j]):
                    curr[j] += dp[j + 1]
            
            dp = curr.copy()
        
        return dp[0]

"""
Time Complexity: O(M * N)
Space Complexity: O(N)

Where
M = length of string t
N = length of string s
"""