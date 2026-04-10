class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        n = len(s)
        
        def helper(l, r):
            while (l >= 0 and r < n and s[l] == s[r]):
                l -= 1
                r += 1
            
            return s[l + 1:r]

        for i in range(len(s)):
            p1, p2 = helper(i, i), helper(i, i + 1)

            if (len(p1) > len(res)):
                res = p1
            if (len(p2) > len(res)):
                res = p2
        
        return res

"""
Time Complexity: O(N^2)
Space Complexity: O(N)

Where 
N = length of string s
"""