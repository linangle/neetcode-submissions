class MedianFinder:
    # idea : split the stream into to halves, ensuring they are balanced in size
        # max-heap that stores smaller half of numbers
            # the largest will be at the top
        # min-heap that stores larger half of numbers
            # the smallest will be at the top

    def __init__(self):
        # intialize the heaps
        self.small, self.large = [], []
        
    def addNum(self, num: int) -> None:
        # if the number is bigger than the smallest of the large half
        if self.large and num > self.large[0]:
            # push it onto the large half
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)
        
        if len(self.small) > len(self.large) + 1:
            # get the largest value from the small half
            val = -1 * heapq.heappop(self.small)
            # append it to the large half
            heapq.heappush(self.large, val)
        
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large): # uneven lengths return the middle
            return -1 * self.small[0] # largest of the small half
        elif len(self. large) > len(self.small):
            return self.large[0] # smallest of the large half
        # if even lengths, return the average of the middles
        return (-1 * self.small[0] + self.large[0]) / 2.0

        
        