from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        minLen = float("inf")
        l, countS, countT = 0, defaultdict(int), defaultdict(int)
        matches = 0

        for c in t:
            countT[c] += 1
        
        for r, c in enumerate(s):
            if (c in countT):
                countS[c] += 1

                if (countS[c] == countT[c]):
                    matches += 1
            
            while (l <= r and (s[l] not in countT or countS[s[l]] > countT[s[l]])):
                if (s[l] in countT):
                    countS[s[l]] -= 1
                
                l += 1

            if (matches == len(countT) and r - l + 1 < minLen):
                res = s[l:r + 1]
                minLen = r - l + 1
        
        return res
                
"""
Time Complexity: O(M + N)
Space Complexity: O(26) = O(1)

Where
M = length of string t
N = length of string s
"""