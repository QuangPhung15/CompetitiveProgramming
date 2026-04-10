from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        ips = []
        n = len(s)

        def backtrack(i):
            if (len(ips) == 4):
                if (i == n):
                    res.append(".".join(ips))
                
                return

            for j in range(i, min(i + 3, n)):
                curr = s[i:j + 1]

                if (curr == "0" or (curr[0] != "0" and 0 < int(curr) <= 255)):
                    ips.append(curr)
                    backtrack(j + 1)
                    ips.pop()
        
        backtrack(0)
        return res

"""
Time Complexity: O(1)
Space Complexity: O(1)
"""