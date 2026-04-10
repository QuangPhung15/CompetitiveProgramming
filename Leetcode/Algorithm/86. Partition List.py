from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1, dummy2 = ListNode(), ListNode()
        left, right = dummy1, dummy2

        while (head):
            if (head.val < x):
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            
            head = head.next
        
        right.next = None
        left.next = dummy2.next
        return dummy1.next
    
"""
Time Complexity: O(N)
Space Complexity: O(1)

Where
N = number of ListNodes in head
"""