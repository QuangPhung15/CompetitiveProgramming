from typing import Optional, List
from lib.builders import TreeNode
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if (not root):
            return []
        
        res = []
        q = deque([root])

        while (q):
            level = []
            n = len(q)

            for _ in range(n):
                curr = q.popleft()
                level.append(curr.val)

                if (curr.left):
                    q.append(curr.left)
                if (curr.right):
                    q.append(curr.right)
            
            res.append(level)
        
        return res

"""
Time Complexity: O(N)
Space Complexity: O(N)

Where
N = number of TreeNodes in root
"""