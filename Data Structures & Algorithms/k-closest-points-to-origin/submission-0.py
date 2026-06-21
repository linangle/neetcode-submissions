class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    # max heap sol
    # idea : heap keeps the k closest points found so far
    # point with largest distance among these k sits at the top
    # when a new point is closer than the farthest heap, 
        # remove farthest and insert the new one
    
        maxHeap = []
        for x, y in points:
            # negative because we're doing a max heap
            dist = -(x ** 2 + y ** 2)
            heapq.heappush(maxHeap, [dist, x, y])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
            
        res = []
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x, y])
        return res