from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i, (s, e) in enumerate(intervals):
            if (newInterval[1] < s):
                res.append(newInterval)
                return res + intervals[i:]
            elif (e < newInterval[0]):
                res.append(intervals[i])
            else:
                newInterval[0] = min(newInterval[0], s)
                newInterval[1] = max(newInterval[1], e)
        
        res.append(newInterval)
        return res

"""
Time Complexity: O(N)
Space Complexity: O(N)

Where
N = length of list intervals
"""