class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1) # stores number of set bits in i
        offset = 1 # most recent power of 2

        for i in range(1, n + 1):
            # if i reaches the next power of 2
            if offset * 2 == i: 
                offset = i
            dp[i] = 1 + dp[i - offset]

        return dp