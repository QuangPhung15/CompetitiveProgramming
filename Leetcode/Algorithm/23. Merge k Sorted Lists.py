from typing import List, Optional
from lib.builders import ListNode
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        heap = []

        for i, l in enumerate(lists):
            if (l):
                heap.append((l.val, i))

        heapq.heapify(heap)

        while (heap):
            _, i = heapq.heappop(heap)
            curr.next = lists[i]
            lists[i] = lists[i].next

            if (lists[i]):
                heapq.heappush(heap, (lists[i].val, i))
            
            curr = curr.next
        
        return dummy.next

"""
Time Complexity: O(NlogK)
Space Complexity: O(K)

Where
N = total number of ListNodes in lists
K = length of list lists
"""