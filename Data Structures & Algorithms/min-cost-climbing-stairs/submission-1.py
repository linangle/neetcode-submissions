class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # at each step, pay the cost[i] and then choose the minimum costing path
        # keep a memo to store and reuse results

        # TOP DOWN
        # memo = [-1] * len(cost)

        # def dfs(i):
        #     if i >= len(cost): # if i is beyond the last step, the cost is 0 (reached top)
        #         return 0
        #     if memo[i] != -1: # if we've seen it already
        #         return memo[i]
        #     # if we haven't seen it yet, calculate and add it to the memo
        #     memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
        #     return memo[i]

        # return min(dfs(0), dfs(1))

        # BOTTOM UP
        n = len(cost)
        dp = [0] * (n + 1) 

        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1],
                        dp[i - 2] + cost[i - 2])

        return dp[n]

