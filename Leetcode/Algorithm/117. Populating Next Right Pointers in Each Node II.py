from lib.builders import ListTreeNode

class Solution:
    def connect(self, root: ListTreeNode) -> ListTreeNode:
        curr = root

        while (curr):
            prev, head = None, curr
            leftmost = None

            while (head):
                if (head.left):
                    if (not prev):
                        leftmost = head.left
                    else:
                        prev.next = head.left
                        
                    prev = head.left

                if (head.right):
                    if (not prev):
                        leftmost = head.right
                    else:
                        prev.next = head.right
                    
                    prev = head.right
                
                head = head.next
            
            curr = leftmost
        
        return root
    
"""
Time Complexity: O(N)
Space Complexity: O(1)

Where
N = number of ListTreeNodes in root
"""