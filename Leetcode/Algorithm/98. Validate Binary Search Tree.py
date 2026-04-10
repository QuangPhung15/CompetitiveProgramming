from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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