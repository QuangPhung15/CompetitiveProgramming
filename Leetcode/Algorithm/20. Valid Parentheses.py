class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for c in s:
            if (c in "([{"):
                stack.append(c)
            else:
                if (not stack or stack[-1] != mapping[c]):
                    return False
                
                stack.pop()
        
        return len(stack) == 0

"""
Time Complexity: O(N)
Space Complexity: O(N)

Where
N = length of string s
"""