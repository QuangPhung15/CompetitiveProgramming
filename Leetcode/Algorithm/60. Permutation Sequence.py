class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = ""
        nums, factorials = ["1"], [1]

        for i in range(1, n):
            nums.append(str(i + 1))
            factorials.append(factorials[-1] * i)
        
        k -= 1

        for i in range(n - 1, -1, -1):
            j = k // factorials[i]
            k %= factorials[i]
            res += nums[j]
            nums.pop(j)
        
        return res
    
"""
Time Complexity: O(N^2)
Space Complexity: O(N)

Where
N = the given integer n
"""