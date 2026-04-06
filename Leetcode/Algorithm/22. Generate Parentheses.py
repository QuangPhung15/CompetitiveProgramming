from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        comb = []

        def backtrack(opens, closes):
            if (opens == 0 and closes == 0):
                res.append("".join(comb))
                return 
            
            if (opens > 0):
                comb.append("(")
                backtrack(opens - 1, closes)
                comb.pop()

            if (closes > opens):
                comb.append(")")
                backtrack(opens, closes - 1)
                comb.pop()
        
        backtrack(n, n)
        return res

"""
Time Complexity: O(4^N / sqrt(N))
Space Complexity: O(N)

Where
N = number of pairs of parentheses
"""