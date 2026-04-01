class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        n = len(nums)
        nums.sort()

        for i in range(n - 2):
            if (i - 1 >= 0 and nums[i] == nums[i - 1]):
                continue
            
            target = 0 - nums[i]
            l, r = i + 1, n - 1

            while (l < r):
                curr = nums[l] + nums[r]
                
                if (curr == target):
                    res.append([nums[i], nums[l], nums[r]])
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
Time Complexity: O(N^2)
Space Complexity: O(N^2)

Where 
N = length of list nums
"""