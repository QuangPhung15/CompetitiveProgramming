class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        s = s.strip()
        sign, i = 1, 0
        UPPER, LOWER = 2**31 - 1, -2**31

        if (i < len(s) and s[0] == "-"):
            sign = -1
            i += 1
        elif (i < len(s) and s[0] == "+"):
            i += 1
        
        while (i < len(s) and s[i].isdigit()):
            res = res * 10 + int(s[i])
            i += 1
        
        res *= sign

        if (res < LOWER):
            return LOWER
        elif (res > UPPER):
            return UPPER
        
        return res

"""
Time Complexity: O(N)
Space Complexity: O(1)

Where
N = length of string s
"""