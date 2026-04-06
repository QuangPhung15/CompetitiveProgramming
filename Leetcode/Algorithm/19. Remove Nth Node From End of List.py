from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow, fast = dummy, head

        for _ in range(n):
            fast = fast.next

        while (fast):
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return dummy.next

"""
Time Complexity: O(N)
Space Complexity: O(1)

Where 
N = number of ListNodes in head
"""