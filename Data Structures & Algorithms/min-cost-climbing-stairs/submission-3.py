class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
    # top down
        # create a cache to track if we've been on this step before
        cache = [-1] * len(cost)
        curMin = float("inf")

        def dfs(i):
            # base cases
            if i >= len(cost): # if we're beyond the last step, cost is 0
                return 0
            
            # if we've already seen this step, return what we already computed
            if cache[i] != -1:
                return cache[i]

            cache[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return cache[i]
        
        return min(dfs(0), dfs(1))