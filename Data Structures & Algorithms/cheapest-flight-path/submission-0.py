class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    # bellman ford
    # idea : allowed at most k stops (nodes)
        # at most k + 1 flights (edges) 
        # run a relaxation k + 1 times
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices.copy()

            for s, d, c in flights: # source, destination, cost
                if prices[s] == float("inf"):
                    continue
                if prices[s] + c < tmpPrices[d]: # if reachable
                # try relaxing the edge
                    tmpPrices[d] = prices[s] + c
            prices = tmpPrices
        return -1 if prices[dst] == float("inf") else prices[dst]
    