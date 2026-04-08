class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        i, j = len(a) - 1, len(b) - 1
        carry = 0

        while (i >= 0 or j >= 0 or carry):
            curr = carry

            if (i >= 0):
                curr += int(a[i])
                i -= 1
            if (j >= 0):
                curr += int(b[j])
                j -= 1
            
            res += str(curr % 2)
            carry = curr // 2
        
        return res[::-1]
    
"""
Time Complexity: O(M + N)
Space Complexity: O(M + N)

Where 
M = length of string a
N = length of string b
"""
