from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 1

        for i in reversed(range(n)):
            curr = carry + digits[i]
            digits[i] = curr % 10
            carry = curr // 10
        
        return digits if (carry == 0) else [carry] + digits
    
"""
Time Complexity: O(N)
Space Complexity: O(N)

Where
N = length of list digits
"""