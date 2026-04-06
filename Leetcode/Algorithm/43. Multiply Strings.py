class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1, num2 = num1[::-1], num2[::-1]
        n = len(num1) + len(num2)
        prod = [0] * n

        for i1, n1 in enumerate(num1):
            for i2, n2 in enumerate(num2):
                j = i1 + i2
                carry = prod[j]
                curr = int(n1) * int(n2) + carry
                prod[j] = curr % 10
                prod[j + 1] += curr // 10
        
        while (len(prod) > 1 and prod[-1] == 0):
            prod.pop()
        
        return "".join([str(p) for p in reversed(prod)])
    
"""
Time Complexity: O(M * N)
Space Complexity: O(M + N)

Where
M = length of string num1
N = length of string num2
"""