from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key = lambda x: x[0])
        l, r = intervals[0]

        for s, e in intervals:
            if (s <= r):
                r = max(r, e)
            else:
                res.append([l, r])
                l, r = s, e
        
        res.append([l, r])
        return res

"""
Time Complexity: O(NlogN)
Space Complexity: O(N)

Where 
N = length of list intervals
"""
