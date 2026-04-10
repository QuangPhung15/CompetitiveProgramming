class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l, seen = 0, set()

        for r, c in enumerate(s):
            while (l < r and c in seen):
                seen.remove(s[l])
                l += 1
            
            seen.add(c)
            res = max(res, r - l + 1)
        
        return res

"""
Time Complexity: O(N)
Space Complexity: O(N)

Where 
N = length of string s
"""