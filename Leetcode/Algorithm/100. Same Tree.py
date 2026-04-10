from typing import Optional
from lib.builders import TreeNode

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p and not q):
            return True
        elif (not p or not q):
            return False
        
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        return p.val == q.val and left and right

"""
Time Complexity: O(N)
Space Complexity: O(h)

Where
N = number of TreeNodes in smaller tree (p or q)
h = the height of smaller tree (p or q)
"""