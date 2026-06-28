class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # scan left to right, calculating prefix values straight into results
        prefix = 1 # base case for the first element
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        
        # scan right to left, multiplying each prefix by the suffix
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res
