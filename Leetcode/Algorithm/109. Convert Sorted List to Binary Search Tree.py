from typing import Optional
from lib.builders import ListNode, TreeNode

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        n = 0
        curr = head

        while (curr):
            n += 1
            curr = curr.next
        
        def dfs(l, r):
            nonlocal head
            
            if (l > r):
                return None
            
            m = l + (r - l) // 2
            root = TreeNode()
            root.left = dfs(l, m - 1)
            root.val = head.val
            head = head.next
            root.right = dfs(m + 1, r)
            return root
        
        return dfs(0, n - 1)
    
"""
Time Complexity: O(N)
Space Complexity: O(logN)

Where
N = number of ListNodes in head
"""