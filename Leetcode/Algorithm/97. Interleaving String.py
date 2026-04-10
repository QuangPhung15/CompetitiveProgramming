class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if (len(s1) + len(s2) != len(s3)):
            return False
            
        m, n = len(s1), len(s2)
        dp = [False] * n + [True]

        for i in reversed(range(m + 1)):
            if (i == m):
                curr = [False] * n + [True]
            else:
                curr = [False] * (n + 1)
            
            for j in reversed(range(n + 1)):
                if (i + j == m + n):
                    continue
                
                target = s3[i + j]

                if (i < m and s1[i] == target):
                    curr[j] |= dp[j]
                if (j < n and s2[j] == target):
                    curr[j] |= curr[j + 1]
        
            dp = curr.copy()
        
        return dp[0]
    
"""
Time Complexity: O(M * N)
Space Complexity: O(N)

Where
M = length of string s1
N = length of string s2
"""