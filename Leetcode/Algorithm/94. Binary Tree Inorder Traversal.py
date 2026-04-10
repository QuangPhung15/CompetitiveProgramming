from typing import Optional, List
from lib.builders import TreeNode

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [(root, False)]

        while (stack):
            curr, v = stack.pop()

            if (not curr):
                continue
            
            if (v):
                res.append(curr.val)
            else:
                stack.append((curr.right, False))
                stack.append((curr, True))
                stack.append((curr.left, False))
        
        return res
    
"""
Time Complexity: O(N)
Space Complexity: O(N)

Where
N = number of TreeNodes in root
"""