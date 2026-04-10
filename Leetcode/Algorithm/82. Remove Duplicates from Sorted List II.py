from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        
        while (curr and curr.next):
            if (curr.val == curr.next.val):
                target = curr.val

                while (curr and curr.val == target):
                    curr = curr.next
                
                prev.next = curr
            else:
                prev = curr
                curr = curr.next
        
        return dummy.next

"""
Time Complexity: O(N)
Space Complexity: O(1)

Where
N = number of ListNodes in head
"""