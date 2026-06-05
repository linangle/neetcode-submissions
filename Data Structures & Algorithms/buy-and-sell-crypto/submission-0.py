class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointers solution (sliding window)
        # l is buy day, r is sell day
        l, r = 0, 1 
        best = 0 # track max profit

        # there can only be a profit if a day on the right is higher than a day on the left
        while r < len(prices):
            # if the price at r is higher than l, we can make a profit --> update max
            if prices[r] > prices[l]:
                best = max(best, prices[r] - prices[l])
            # if price at r is lower, no profit can be made
                # r becomes the new l because a cheaper buying price is better
            else:
                l = r
            r += 1
        return best
