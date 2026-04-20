from typing import Optional
from lib.builders import ListTreeNode

class Solution:
    def connect(self, root: Optional[ListTreeNode]) -> Optional[ListTreeNode]:
        curr = root

        while (curr and curr.left):
            head = curr

            while (head):
                head.left.next = head.right

                if (head.next):
                    head.right.next = head.next.left
                
                head = head.next
            
            curr = curr.left
        
        return root

"""
Time Complexity: O(N)
Space Complexity: O(1)

Where
N = number of ListTreeNodes in root
"""