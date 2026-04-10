class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp1, dp2 = 1, 0

        for i in reversed(range(n)):
            curr = 0

            if (0 < int(s[i]) <= 9):
                curr += dp1
            if (i + 1 < n and 10 <= int(s[i:i + 2]) <= 26):
                curr += dp2
            
            dp2 = dp1
            dp1 = curr
        
        return dp1
    
"""
Time Complexity: O(N)
Space Complexity: O(1)

Where
N = length of string s
"""