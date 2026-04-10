from typing import Optional
from lib.builders import TreeNode

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, mn, mx):
            if (not root):
                return True
            
            left = dfs(root.left, mn, root.val)
            right = dfs(root.right, root.val, mx)
            return mn < root.val < mx and left and right
        
        return dfs(root, float("-inf"), float("inf"))

"""
Time Complexity: O(N)
Space Complexity: O(h)

Where
N = number of TreeNodes in root
h = the height of tree root
"""