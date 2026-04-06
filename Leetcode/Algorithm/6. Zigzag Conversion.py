class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if (numRows == 1):
            return s
            
        lines = [""] * numRows
        r, dr = 0, -1

        for c in s:
            lines[r] += c

            if (r == 0 or r == numRows - 1):
                dr *= -1
            
            r += dr
        
        return "".join(lines)

"""
Time Complexity: O(N)
Space Complexity: O(N)

Where 
N = length of string s
"""