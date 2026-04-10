from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        
        for l in range(len(strs[0])):
            for s in strs:
                if (l == len(s) or s[l] != strs[0][l]):
                    return res
            
            res += strs[0][l]
        
        return res
    
"""
Time Complexity: O(M * N)
Space Complexity: O(N)

Where 
M = length of list strs
N = minimum length of a string in strs
"""