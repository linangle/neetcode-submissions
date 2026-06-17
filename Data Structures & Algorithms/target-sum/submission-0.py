class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp map where possible sum --> number of ways to form
        dp = defaultdict(int)
        dp[0] = 1 # one way to reach sum 0 before using any numbers

        for num in nums:
            # store updated sums in a new map
            next_dp = defaultdict(int)
            for total, count in dp.items():
                next_dp[total + num] += count
                next_dp[total - num] += count
            # move after we process the current number
            dp = next_dp
        
        return dp[target]