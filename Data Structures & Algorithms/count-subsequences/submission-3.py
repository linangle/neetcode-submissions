class Solution:
    def numDistinct(self, s: str, t: str) -> int:
    # dp (optimal)
        m, n = len(s), len(t)
        # create a 1D array where dp[j] represents # ways to form t[j:] using the suffix of s currently being processed
        dp = [0] * (n + 1)
        # base case (one way to form an empty t --> choose nothing)
        dp[n] = 1

        # iterate from right to left through s
        for i in range(m - 1, -1, -1):
            # this corresponds to diagonal value dp[i + 1][n] (always 1)
            prev = 1
            for j in range(n - 1, -1, -1):
                res = dp[j]
                if s[i] == t[j]:
                    res += prev
                
                prev = dp[j]
                dp[j] = res
        
        return dp[0]
