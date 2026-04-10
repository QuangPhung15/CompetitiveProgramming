class Solution:
    def countAndSay(self, n: int) -> str:
        dp = "1"

        for _ in range(n - 1):
            curr, count = "", 1

            for i in range(1, len(dp)):
                if (dp[i] == dp[i - 1]):
                    count += 1
                else:
                    curr += str(count) + dp[i - 1]
                    count = 1
            
            curr += str(count) + dp[-1] 
            dp = curr
        
        return dp

"""
Time Complexity: O(2^N)
Space Complexity: O(2^N)

Where
N = the given integer n
"""