from typing import Optional
from lib.builders import TreeNode

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root1, root2):
            if (not root1 and not root2):
                return True
            elif (not root1 or not root2):
                return False
            
            left = dfs(root1.left, root2.right)
            right = dfs(root1.right, root2.left)
            return root1.val == root2.val and left and right
        
        return dfs(root.left, root.right)

"""
Time Complexity: O(N)
Space Complexity: O(h)

Where
N = number of TreeNodes in root
h = the height of tree root
"""