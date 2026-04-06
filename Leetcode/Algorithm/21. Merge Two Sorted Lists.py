from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        while (list1 or list2):
            if (list1 and list2):
                if (list1.val <= list2.val):
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next
            elif (list1):
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
        
            curr = curr.next
        
        return dummy.next
    
"""
Time Complexity: O(N1 + N2)
Space Complexity: O(1)

Where
N1 = number of ListNodes in list1
N2 = number of ListNodes in list2
"""