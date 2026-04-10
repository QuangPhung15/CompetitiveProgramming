class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        cache = {}

        def memoiz(s1, s2):
            if (s1 == s2):
                return True
            elif (sorted(s1) != sorted(s2)):
                return False
            
            if ((s1, s2) not in cache):
                res = False

                for i in range(1, len(s1)):
                    res |= memoiz(s1[:i], s2[:i]) and memoiz(s1[i:], s2[i:])
                    res |= memoiz(s1[-i:], s2[:i]) and memoiz(s1[:-i], s2[i:])
                
                cache[(s1, s2)] = res
        
            return cache[(s1, s2)]
        
        return memoiz(s1, s2)

"""
Time Complexity: O(N^4)
Space Complexity: O(N^4)

Where
N = length of string s1 or s2
"""