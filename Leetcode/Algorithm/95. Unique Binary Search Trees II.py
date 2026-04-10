from typing import List, Optional
from lib.builders import TreeNode

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        cache = {}

        def memoiz(l, r):
            if (l > r):
                return [None]
            elif (l == r):
                return [TreeNode(l)]
            
            if ((l, r) not in cache):
                res = []

                for i in range(l, r + 1):
                    lefts = memoiz(l, i - 1)
                    rights = memoiz(i + 1, r)

                    for left in lefts:
                        for right in rights:
                            res.append(TreeNode(i, left, right))
                
                cache[(l, r)] = res
            
            return cache[(l, r)]
        
        return memoiz(1, n)

"""
Time Complexity: O(4^N / N^(3/2))
Space Complexity: O(4^N / N^(3/2))

Where
N = the given integer n
"""