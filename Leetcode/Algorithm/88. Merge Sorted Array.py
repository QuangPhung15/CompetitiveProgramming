from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        r = len(nums1) - 1
        i, j = m - 1, n - 1

        while (i >= 0 or j >= 0):
            if (i >= 0 and j >= 0):
                if (nums1[i] >= nums2[j]):
                    nums1[r] = nums1[i]
                    i -= 1
                else:
                    nums1[r] = nums2[j]
                    j -= 1
            elif (i >= 0):
                nums1[r] = nums1[i]
                i -= 1
            else:
                nums1[r] = nums2[j]
                j -= 1
            
            r -= 1

"""
Time Complexity: O(M + N)
Space Complexity: O(1)

Where
M = the given integer m
N = the given integer n
"""