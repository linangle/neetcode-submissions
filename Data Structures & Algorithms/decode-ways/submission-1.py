class Solution:
    def numDecodings(self, s: str) -> int:
    # space optimized bottom up
        # dp1 --> ways to decode from i + 1
        # dp2 --> ways to decode from i + 2
        # dp[i] : ways to decode the substring
        dp = dp2 = 0
        dp1 = 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp = 0
            else:
                dp = dp1
            
            # process 2 digits
            if i + 1 < len(s) and (s[i] == "1" or 
            s[i] == "2" and s[i + 1] in "0123456"):
                dp += dp2
            # shift values
            dp, dp1, dp2 = 0, dp, dp1
        return dp1
