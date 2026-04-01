from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()

        for i in range(n - 3):
            if (i - 1 >= 0 and nums[i] == nums[i - 1]):
                continue

            for j in range(i + 1, n - 2):
                if (j - 1 >= i + 1 and nums[j] == nums[j - 1]):
                    continue
                
                l, r = j + 1, n - 1

                while (l < r):
                    curr = nums[i] + nums[j] + nums[l] + nums[r]

                    if (curr == target):
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1

                        while (l < r and nums[l] == nums[l - 1]):
                            l += 1
                        while (l < r and nums[r] == nums[r + 1]):
                            r -= 1
                    elif (curr < target):
                        l += 1

                        while (l < r and nums[l] == nums[l - 1]):
                            l += 1
                    else:
                        r -= 1

                        while (l < r and nums[r] == nums[r + 1]):
                            r -= 1
        
        return res
    
"""
Time Complexity: O(N^3)
Space Complexity: O(N^3)

Where 
N = length of list nums
"""