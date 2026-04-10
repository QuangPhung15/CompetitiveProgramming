from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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