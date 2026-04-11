from typing import Optional
from lib.builders import TreeNode

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if (not root):
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)

"""
Time Complexity: O(N)
Space Complexity: O(h)

Where
N = number of TreeNodes in root
h = the height of tree root
"""