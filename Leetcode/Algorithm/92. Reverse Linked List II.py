from typing import Optional
from lib.builders import ListNode

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        l = dummy

        for _ in range(left - 1):
            l = l.next
        
        prev, curr = None, l.next

        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        l.next.next = curr
        l.next = prev
        return dummy.next

"""
Time Complexity: O(N)
Space Complexity: O(1)

Where
N = number of ListNodes in head
"""