from typing import List, Optional
from lib.builders import TreeNode

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        indices = {}

        for j, i in enumerate(inorder):
            indices[i] = j
        
        def dfs(i, l, r):
            if (l > r):
                return None
            
            root = TreeNode(preorder[i])

            m = indices[preorder[i]]
            leftSize = m - l

            root.left = dfs(i + 1, l, m - 1)
            root.right = dfs(i + 1 + leftSize, m + 1, r)
            return root
        
        return dfs(0, 0, n - 1)

"""
Time Complexity: O(N)
Space Complexity: O(N)

Where
N = length of list preorder or inorder
"""