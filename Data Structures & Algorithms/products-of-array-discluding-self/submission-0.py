class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # idea : multiply by all prefix, then multiply by all suffixes
        # initialize a result array
        res = [1] * len(nums)

        # initialize prefix value as 1
        prefix = 1
        # start at the beginning of nums
        for i in range(len(nums)): 
            # for res[0] no prefix, default 1 --> will have value when we do suff
            res[i] = prefix
            prefix *= nums[i]
        
        # initialize postfix value as 1 (suffix)
        postfix = 1
        # start at the end of the array, go all the way to beginning, decrementing by 1
        for i in range(len(nums)- 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
            