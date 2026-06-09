class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # HEAP SOL : O(nlogn) time, O(n) space
        # maxheap = []
        # maxes = []

        # for i, n in enumerate(nums):
        #     heapq.heappush(maxheap, (-n, i)) # use negative because we're doing maxheap
        #     if i >= k - 1: # only start adding new values when we're past the initial window
        #         while maxheap[0][1] <= i - k: # if the current largest (with its index) is outside the window (window is i - k + 1)
        #             # pop the heap until we get to the window size
        #             heapq.heappop(maxheap)
        #         maxes.append(-maxheap[0][0]) # append the numerical value of max
        # return maxes

        # DP SOL : O(n) time, O(n) space
        n = len(nums)
        leftmax = [0] * n
        rightmax = [0] * n

        leftmax[0] = nums[0]
        rightmax[n - 1] = nums[n - 1] 

        for i in range(1, n): # start at 1 because we started with base cases
            # left max
            if i % k == 0: # we're at a new block, reset the leftmax
                leftmax[i] = nums[i]
            else: # if we're inside a block, get the max for that range (previous plus current)
                leftmax[i] = max(leftmax[i - 1], nums[i])

            # right max
            if (n - 1 - i) % k == 0: # starting a new block coming from the right side
                rightmax[n - 1 - i] = nums[n - 1 - i]
            else:
                rightmax[n - 1 - i] = max(rightmax[n - i], nums[n - 1 - i])

        output = [0] * (n - k + 1) # there are n - k + 1 windows total

        for i in range(n - k + 1):
            output[i] = max(leftmax[i + k - 1], rightmax[i])

        return output









