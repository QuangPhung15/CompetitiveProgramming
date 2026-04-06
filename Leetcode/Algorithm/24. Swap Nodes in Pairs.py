from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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