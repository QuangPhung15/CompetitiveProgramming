from typing import Optional
from lib.builders import ListNode

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while (curr and curr.next):
            if (curr.val == curr.next.val):
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return head

"""
Time Complexity: O(N)
Space Complexity: O(1)

Where
N = number of ListNodes in head
"""