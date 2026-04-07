from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            
            group[tuple(count)].append(s)
        
        return list(group.values())
    
"""
Time Complexity: O(M * N)
Space Complexity: O(M)

Where 
M = length of list strs
N = maximum length of a string in strs
"""