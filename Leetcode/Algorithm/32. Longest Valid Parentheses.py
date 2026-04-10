class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        stack = [("", -1)]

        for i, c in enumerate(s):
            if (c == "("):
                stack.append((c, i))
            else:
                if (stack and stack[-1][0] == "("):
                    stack.pop()
                    res = max(res, i - stack[-1][1])
                else:
                    stack.append((c, i))
        
        return res
    
"""
Time Complexity: O(N)
Space Complexity: O(N)

Where 
N = length of string s
"""