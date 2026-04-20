from typing import Optional
from lib.builders import TreeNode

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if (not root):
            return False
        elif (not root.left and not root.right):
            return targetSum - root.val == 0
        
        left = self.hasPathSum(root.left, targetSum - root.val)
        right = self.hasPathSum(root.right, targetSum - root.val)
        return left or right
    
"""
Time Complexity: O(N)
Space Complexity: O(h)

Where
N = number of TreeNodes in root
h = the height of tree root
"""