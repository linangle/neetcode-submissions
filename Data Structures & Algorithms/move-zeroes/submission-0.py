class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # using extra space
        tmp = []

        for num in nums:
            if num != 0:
                tmp.append(num)
        
        # length of non-zeros + length of zeros = total length nums
        t = len(tmp)
        for i in range(len(nums)):
            if i < t: 
                nums[i] = tmp[i]
            else:
                nums[i] = 0

        return nums



        