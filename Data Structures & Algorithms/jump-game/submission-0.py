class Solution:
    def canJump(self, nums: List[int]) -> bool:
    # greedy sol
    # idea : think about problem in reverse
        # what positions can reach the end
        # move backward to see if earlier positions can reach those

        # intialize goal as last index
        goal = len(nums) - 1

        # iterate from the second last index down to index 0
        for i in range(len(nums) - 2, -1, -1):
            # check if we can reach the goal from that position
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
