from typing import Optional, List
from lib.builders import TreeNode

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(root, total):
            if (not root):
                return 
            
            path.append(root.val)

            if (not root.left and not root.right):
                if (total + root.val == targetSum):
                    res.append(path.copy())
            
            if (root.left):
                dfs(root.left, total + root.val)
            if (root.right):
                dfs(root.right, total + root.val)

            path.pop()
        
        dfs(root, 0)
        return res

"""
Time Complexity: O(N^2)
Space Complexity: O(h)

Where
N = number of TreeNodes in root
h = the height of tree root
"""