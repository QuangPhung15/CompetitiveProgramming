from typing import Optional
from lib.builders import ListNode

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while (l1 or l2 or carry):
            total = carry

            if (l1):
                total += l1.val
                l1 = l1.next
            if (l2):
                total += l2.val
                l2 = l2.next
            
            curr.next = ListNode(total % 10)
            carry = total // 10
            curr = curr.next
        
        return dummy.next

"""
Time Complexity: O(N1 + N2)
Space Complexity: O(N1 + N2)

Where
N1 = number of ListNodes in l1
N2 = number of ListNodes in l2
"""