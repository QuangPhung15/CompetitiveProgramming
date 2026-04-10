class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        sign = 1

        if (x < 0):
            sign = -1
            x *= -1
        
        while (x > 0):
            res = res * 10 + x % 10
            x //= 10
        
        res *= sign

        if (res < -2**31 or res > 2**31 - 1):
            return 0
        
        return res
    
"""
Time Complexity: O(31) = O(1)
Space Complexity: O(1)
"""