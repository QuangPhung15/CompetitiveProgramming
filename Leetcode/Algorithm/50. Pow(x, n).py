class Solution:
    def myPow(self, x: float, n: int) -> float:
        if (n < 0):
            return 1 / self.myPow(x, -n)
        
        res = 1

        while (n > 0):
            if (n % 2 == 1):
                res *= x
                n -= 1
            
            x *= x
            n >>= 1
        
        return res
        
"""
Time Complexity: O(logN)
Space Complexity: O(1)

Where 
N = the given integer n
"""