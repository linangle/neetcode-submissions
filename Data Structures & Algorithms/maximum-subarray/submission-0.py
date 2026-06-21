class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    # kadane's algorithm
    # idea : if running sum becomes negative
        # keeping it will only reduce sum of any future subarray
    
        maxSub, curSum = nums[0], 0
        for num in nums:
            # if we go negative
            if curSum < 0:
                # reset
                curSum = 0
            curSum += num
            maxSub = max(maxSub, curSum)
        return maxSub
        