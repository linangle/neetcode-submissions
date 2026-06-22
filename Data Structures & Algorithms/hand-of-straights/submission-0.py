class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
    # hash map sol
    # idea : any valid group must start at the beginning of a consecutive run

        # first check if divisible into group sizes
        if len(hand) % groupSize != 0:
            return False
        
        # hash map: number --> frequency
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)
        
        # keep a minheap to always get current smallest quickly
        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                # missing a needed card
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True
