from typing import List, Optional
from ast import literal_eval
from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val = 0, next: ListNode = None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val = 0, left: TreeNode = None, right: TreeNode = None):
        self.val = val
        self.left = left
        self.right = right

def parse_linked_list(input: str) -> List[int]:
    return literal_eval(input)

def parse_binary_tree(input: str) -> List[Optional[int]]:
    return literal_eval(input.replace("null", "None"))

def build_linked_list(input: str) -> Optional[ListNode]:
    nodes = parse_linked_list(input)
    dummy = ListNode()
    curr = dummy

    for n in nodes:
        curr.next = ListNode(n)
        curr = curr.next
    
    return dummy.next
 
def build_binary_tree(input: str) -> Optional[TreeNode]:
    nodes = parse_binary_tree(input)

    if (not nodes or nodes[0] is None):
        return None

    root = TreeNode(nodes[0])
    q = deque([root])
    i = 1

    while (i < len(nodes)):
        curr = q.popleft()
        
        if (nodes[i] is not None):
            curr.left = TreeNode(nodes[i])
            q.append(curr.left)
        if (i + 1 < len(nodes) and nodes[i + 1] is not None):
            curr.right = TreeNode(nodes[i + 1])
            q.append(curr.right)
        
        i += 2
    
    return root