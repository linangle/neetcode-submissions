class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    # greedy sol
    # idea : if total gas available < total cost required, impossible 
        # if tank goes negative, restart at next station
    
        # initial check
        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        res = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                res = i + 1
        
        return res

