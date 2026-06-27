class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # update the input array to have a 1 at beginning and end
        nums = [1] + nums + [1]
        dp = {}

        def dfs(l, r):
            if l > r:
                return 0 # 
            if (l, r) in dp: # if we've seen this sub array be popped already
                return dp[(l, r)]
            
            dp[(l, r)] = 0 # initialize
            for i in range(l, r + 1):
                # suppose we pop i last
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                # compute coins from left and right subarrays
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                dp[(l, r)] = max(dp[l, r], coins)
            return dp[(l, r)]

        # return without popping the padding 1s
        return dfs(1, len(nums) - 2)