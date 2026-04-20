from typing import Optional
from lib.builders import TreeNode
from collections import deque

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if (not root):
            return 0

        q = deque([(1, root)])

        while (q):
            depth, curr = q.popleft()

            if (not curr.left and not curr.right):
                return depth
            
            if (curr.left):
                q.append((depth + 1, curr.left))
            if (curr.right):
                q.append((depth + 1, curr.right))
        
        return -1

"""
Time Complexity: O(N)
Space Complexity: O(w)

Where 
N = number of TreeNodes in root
w = the width of the tree root
"""