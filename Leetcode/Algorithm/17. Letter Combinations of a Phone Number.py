from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        n = len(digits)
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(i, curr):
            if (i == n):
                res.append(curr)
                return
            
            for c in mapping[digits[i]]:
                backtrack(i + 1, curr + c)
        
        backtrack(0, "")
        return res
    
"""
Time Complexity: O(4^N)
Space Complexity: O(4^N)

Where 
N = length of string digits
"""