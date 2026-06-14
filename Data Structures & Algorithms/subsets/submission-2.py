class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # BIT MANIPULATION SOL
        # idea : every subset reperesented using bits
            # each subset corresponds to num from 0 to 2^n - 1

        n = len(nums)
        res = []

        # generate all bitmasks
        for i in range(1 << n):
            # for each i, build a subset
            subset = [nums[j] for j in range(n) if (i & (1 << j))]
        
        # add the subset to the result list
            res.append(subset)
        
        return res
