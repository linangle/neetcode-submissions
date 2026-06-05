class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # fastest time is when you eat the value of the largest pile, shortest time is when you eat 1
        l, r = 1, max(piles)
        res = r # take the max rate as our initial

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k) # for every entry, take the ceiling of the pile / rate to determine time it takes to eat the pile
            if totalTime <= h: # we have extra time, can make the rate slower
                res = k # there might not be an exact match where totaltime = k, takes best value
                r = k - 1
            else: # the time is too long, need to have a higher rate
                l = k + 1
        return res

                

        
