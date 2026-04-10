from typing import Optional
from lib.builders import ListNode

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy

        while (curr.next and curr.next.next):
            node1, node2 = curr.next, curr.next.next
            node1.next = node2.next
            node2.next = node1
            curr.next = node2
            curr = node1
        
        return dummy.next

"""
Time Complexity: O(N)
Space Complexity: O(1)

Where
N = number of ListNodes in head
"""