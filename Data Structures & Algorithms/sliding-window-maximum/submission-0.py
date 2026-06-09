class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
       # HEAP SOL : O(nlogn) time, O(n) space
        maxheap = []
        maxes = []

        for i, n in enumerate(nums):
            heapq.heappush(maxheap, (-n, i)) # use negative because we're doing maxheap
            if i >= k - 1: # only start adding new values when we're past the initial window
                while maxheap[0][1] <= i - k: # if the current largest (with its index) is outside the window (window is i - k + 1)
                    # pop the heap until we get to the window size
                    heapq.heappop(maxheap)
                maxes.append(-maxheap[0][0]) # append the numerical value of max
        return maxes