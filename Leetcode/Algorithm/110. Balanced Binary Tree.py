from typing import Optional
from lib.builders import TreeNode

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        
        def dfs(root):
            if (not root):
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            if (abs(left - right) > 1):
                self.res = False
            
            return 1 + max(left, right)
        
        dfs(root)
        return self.res
    
"""
Time Complexity: O(N)
Space Complexity: O(h)

Where 
N = the number of TreeNodes in root
h = the height of tree root
"""