from typing import List, Optional
from lib.builders import TreeNode

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def dfs(l, r):
            if (l > r):
                return None
            
            m = l + (r - l) // 2
            root = TreeNode(nums[m])
            root.left = dfs(l, m - 1)
            root.right = dfs(m + 1, r)
            return root
        
        return dfs(0, len(nums) - 1)

"""
Time Complexity: O(N)
Space Complexity: O(N)

Where
N = length of list nums
"""