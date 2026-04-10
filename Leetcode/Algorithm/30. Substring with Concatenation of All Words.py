from typing import List
from collections import defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        n = len(s) 
        word_size = len(words[0])
        substring_size = word_size * len(words)
        count = defaultdict(int)

        for w in words:
            count[w] += 1
        
        for i in range(word_size):
            l, curr = i, defaultdict(int)

            for r in range(i, n, word_size):
                if (r + word_size > n):
                    break

                word = s[r:r + word_size]
                curr[word] += 1

                while (l <= r and curr[word] > count[word]):
                    curr[s[l:l + word_size]] -= 1
                    l += word_size

                if (r + word_size - l == substring_size):
                    res.append(l)
        
        return res
    
"""
Time Complexity: O(M * N)
Space Complexity: O(K)

Where
M = length of a string in list words
N = length of string s
K = length of list words
"""