class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp space optimized
        # idea : only keep two variables and update as we move forward
        # rob1 is the best up to house i - 2
        # rob2 is the best up to house i - 1
        rob1, rob2 = 0, 0 

        for num in nums:
            newRob = max(num + rob1, rob2)
            # move the pointers
            rob1 = rob2
            rob2 = newRob

        return rob2