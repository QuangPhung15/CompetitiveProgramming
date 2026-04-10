from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = None
        node1, node2 = None, None
        stack = [(root, False)]

        while (stack):
            curr, v = stack.pop()

            if (not curr):
                continue
            
            if (v):
                if (prev and curr.val < prev.val):
                    node2 = curr

                    if (not node1):
                        node1 = prev
                    else:
                        break
                
                prev = curr
            else:
                stack.append((curr.right, False))
                stack.append((curr, True))
                stack.append((curr.left, False))
        
        node1.val, node2.val = node2.val, node1.val

"""
Time Complexity: O(N)
Space Complexity: O(h)

Where
N = number of TreeNodes in root
h = the height of tree root
"""