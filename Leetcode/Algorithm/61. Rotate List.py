from typing import Optional
from lib.builders import ListNode

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if (not head or k == 0):
            return head
            
        n = 0
        dummy = ListNode(0, head)
        slow, fast = head, head

        while (head):
            n += 1
            head = head.next
        
        for _ in range(k % n):
            fast = fast.next
        
        while (fast.next):
            slow = slow.next
            fast = fast.next
        
        fast.next = dummy.next
        dummy.next = slow.next
        slow.next = None
        return dummy.next

"""
Time Complexity: O(N)
Space Complexity: O(1)

Where 
N = number of ListNodes in head
"""