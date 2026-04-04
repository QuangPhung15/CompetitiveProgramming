class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        def build_lps(pattern):
            n = len(pattern)
            lps = [0] * n
            i, l = 1, 0

            while (i < n):
                if (pattern[i] == pattern[l]):
                    l += 1
                    lps[i] = l
                    i += 1
                else:
                    if (l == 0):
                        lps[i] = 0
                        i += 1
                    else:
                        l = lps[l - 1]
            
            return lps
        
        def kmp_search(s, pattern):
            lps = build_lps(pattern)
            i, j = 0, 0

            while (i < len(s)):
                if (s[i] == pattern[j]):
                    i += 1
                    j += 1
                else:
                    if (j > 0):
                        j = lps[j - 1]
                    else:
                        i += 1
                
                if (j == len(pattern)):
                    return i - len(pattern)
            
            return -1
        
        return kmp_search(haystack, needle)

"""
Time Complexity: O(M + N)
Space Complexity: O(N)

Where 
M = length of string haystack
N = length of string needle
"""