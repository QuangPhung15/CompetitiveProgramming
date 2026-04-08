class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        i = len(s) - 1

        while (i >= 0 and s[i] == " "):
            i -= 1
        
        while (i >= 0 and s[i] != " "):
            res += 1
            i -= 1
        
        return res

"""
Time Complexity: O(N)
Space Complexity: O(1)

Where
N = length of string s
"""