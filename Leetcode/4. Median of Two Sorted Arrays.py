from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)

        if (n2 < n1):
            return self.findMedianSortedArrays(nums2, nums1)

        total = n1 + n2
        half = total // 2
        l, r = 0, n1 - 1

        while (True):
            m1 = l + (r - l) // 2
            m2 = half - m1 - 2
            left1 = nums1[m1] if (m1 >= 0) else float("-inf")
            right1 = nums1[m1 + 1] if (m1 + 1 < n1) else float("inf")
            left2 = nums2[m2] if (m2 >= 0) else float("-inf")
            right2 = nums2[m2 + 1] if (m2 + 1 < n2) else float("inf")

            if (left1 <= right2 and left2 <= right1):
                if (total % 2 == 0):
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return min(right1, right2)
            elif (left1 > right2):
                r = m1 - 1
            elif (left2 > right1):
                l = m1 + 1
        
        return -1

"""
Time Complexity: O(log(min(M, N)))
Space Complexity: O(1)

Where:
M = length of list nums1
N = length of list nums2
"""

