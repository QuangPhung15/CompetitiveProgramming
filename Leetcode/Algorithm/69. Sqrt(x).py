class Solution:
    def mySqrt(self, x: int) -> int:
        res = -1
        l, r = 0, x

        while (l <= r):
            m = l + (r - l) // 2

            if (m * m <= x):
                res = m
                l = m + 1
            else:
                r = m - 1
        
        return res
    
"""
Time Complexity: O(logN)
Space Complexity: O(1)

Where
N = the given integer x
"""