class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # at each step, pay the cost[i] and then choose the minimum costing path
        # keep a memo to store and reuse results
        memo = [-1] * len(cost)

        def dfs(i):
            if i >= len(cost): # if i is beyond the last step, the cost is 0 (reached top)
                return 0
            if memo[i] != -1: # if we've seen it already
                return memo[i]
            # if we haven't seen it yet, calculate and add it to the memo
            memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return memo[i]
            
        return min(dfs(0), dfs(1))

