class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = 0
        LOWER, UPPER = -2**31, 2**31 - 1
        neg = 0

        if (dividend == LOWER and divisor == -1):
            return UPPER

        if (dividend < 0):
            neg += 1
            dividend = -dividend
        if (divisor < 0):
            neg += 1
            divisor = -divisor
        
        i = 1

        while (divisor <= dividend):
            divisor <<= 1 
            i <<= 1
        
        while (divisor > 0):
            if (divisor <= dividend):
                res += i
                dividend -= divisor
            
            divisor >>= 1
            i >>= 1
        
        return -res if (neg == 1) else res
    
"""
Time Complexity: O(logN)
Space Complexity: O(1)

Where
N = the number dividend
"""