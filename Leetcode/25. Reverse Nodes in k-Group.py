from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy

        while (curr):
            start, end = curr.next, curr

            for _ in range(k):
                if (not end.next):
                    return dummy.next
                
                end = end.next
            
            temp = start
            prev = end.next
            end.next = None

            while (start):
                temp1 = start.next
                start.next = prev
                prev = start
                start = temp1
            
            curr.next = end
            curr = temp
        
        return dummy.next
    
"""
Time Complexity: O(N)
Space Complexity: O(1)

Where
N = number of ListNodes in head
"""