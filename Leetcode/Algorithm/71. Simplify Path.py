class Solution:
    def simplifyPath(self, path: str) -> str:
        directory = path.split("/")
        stack = []

        for d in directory:
            if (not d or d == "."):
                continue
            elif (d == ".."):
                if (stack):
                    stack.pop()
            else:
                stack.append(d)
        
        return "/" + "/".join(stack)

"""
Time Complexity: O(N)
Space Complexity: O(N)

Where 
N = length of string s
"""