from typing import List, Optional
from lib.builders import TreeNode

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        indices = {}

        for j, i in enumerate(inorder):
            indices[i] = j
        
        def dfs(l, r, i):
            if (l > r):
                return None
            
            root = TreeNode(postorder[i])
            
            m = indices[postorder[i]]
            rightSize = r - m

            root.right = dfs(m + 1, r, i - 1)
            root.left = dfs(l, m - 1, i - rightSize - 1)
            return root
        
        return dfs(0, n - 1, n - 1)

"""
Time Complexity: O(N)
Space Complexity: O(N)

Where
N = length of either list inorder or postorder
"""