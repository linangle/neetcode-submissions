class Solution:
    def rob(self, nums: List[int]) -> int:
    # space optimized
    # idea : we can't rob from both the first and second
        # split this problem into two cases
            # one excluding the first house, one excluding the last house
            # do house robber i
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
    
    def helper(self, nums):
        rob1, rob2 = 0, 0 

        for num in nums:
            newRob = max(num + rob1, rob2)
            # move the pointers
            rob1 = rob2
            rob2 = newRob
        return rob2
    
