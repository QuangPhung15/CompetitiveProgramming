class Solution:
    def isNumber(self, s: str) -> bool:
        dfa = [
            {"digit": 1, "sign": 2, "dot": 3},
            {"digit": 1, "dot": 4, "exponent": 5},
            {"digit": 1, "dot": 3},
            {"digit": 4},
            {"digit": 4, "exponent": 5},
            {"sign": 6, "digit": 7},
            {"digit": 7},
            {"digit": 7},
        ]
        state = 0

        for c in s:
            if (c.isdigit()):
                group = "digit"
            elif (c in ["+", "-"]):
                group = "sign"
            elif (c in ["e", "E"]):
                group = "exponent"
            elif (c == "."):
                group = "dot"
            else:
                return False

            if (group not in dfa[state]):
                return False

            state = dfa[state][group]

        return state in [1, 4, 7]
    
"""
Time Complexity: O(N)
Space Complexity: O(1)

Where 
N = length of string s
"""