class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # no extra space sol
        # idea 
            # l = write pointer
            # r = search for non-zero pointer
        
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l] = nums[r]
                l += 1

        # now all the non-zeros are at the front of nums
        # fill the rest with zeros
        while l < len(nums):
            nums[l] = 0
            l += 1

        