from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = -1
        mn = float("inf")
        n = len(nums)
        nums.sort()

        for i in range(n - 2):
            if (i - 1 >= 0 and nums[i] == nums[i - 1]):
                continue
            
            l, r = i + 1, n - 1

            while (l < r):
                curr = nums[i] + nums[l] + nums[r]
                diff = abs(target - curr)

                if (diff < mn):
                    res = curr
                    mn = diff
                
                if (curr <= target):
                    l += 1

                    while (l < r and nums[l] == nums[l - 1]):
                        l += 1
                else:
                    r -= 1

                    while (l < r and nums[r] == nums[r + 1]):
                        r -= 1
            
        return res
    
"""
Time Complexity: O(N^2)
Space Complexity: O(1)

Where 
N = length of list nums
"""