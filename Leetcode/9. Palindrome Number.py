class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False
        
        n = 0
        temp = x

        while (temp > 0):
            n = n * 10 + temp % 10
            temp //= 10
        
        return n == x

"""
Time Complexity: O(31) = O(1)
Space Complexity: O(1)
"""