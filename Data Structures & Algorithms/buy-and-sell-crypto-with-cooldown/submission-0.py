class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two choices:
            # don't sell neetcoin, dfs(i + 1)
            # sell neetcoin, dfs(i + 2)
        
        # keep a memo to track the max profit on each day, track whether we can buy or not
        memo = {} # (i, buying) --> max profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0 # reached the end of the list
            if (i, buying) in memo:
                return memo[(i, buying)] # return if we've seen value before
            
            # always consider option to skip the current day
            cooldown = dfs(i + 1, buying)

            if buying:
                # buy the stock today, move to selling state
                buy = dfs(i + 1, not buying) - prices[i]
                memo[(i, buying)] = max(buy, cooldown)
            else: # if we're holding a stock
                # sell the stock, add price and skip to next day
                sell = dfs(i + 2, not buying) + prices[i]
                memo[(i, buying)] = max(sell, cooldown)
            return memo[(i, buying)]
        
        return dfs(0, True)
        