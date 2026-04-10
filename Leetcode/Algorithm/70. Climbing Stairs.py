class Solution:
    def climbStairs(self, n: int) -> int:
        dp1, dp2 = 1, 0

        for _ in range(n):
            curr = dp1 + dp2
            dp2 = dp1
            dp1 = curr
        
        return dp1
    
"""
Time Complexity: O(N)
Space Complexity: O(1)

Where
N = the given integer n
"""