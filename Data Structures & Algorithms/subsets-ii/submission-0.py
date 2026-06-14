class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # iteration 
        # build subsets step by step

        res = [[]]
        nums.sort()
        prev_idx = idx = 0

        for i in range(len(nums)):
            # if a value is the same as one prior to it, set idx to the previous end
                # otherwise set idx to 0
            idx = prev_idx if i >= 1 and nums[i] == nums[i - 1] else 0
            # set prev_idx to the boundary of the old subset
            prev_idx = len(res)
            for j in range(idx, prev_idx):
                tmp = res[j].copy()
                tmp.append(nums[i])
                res.append(tmp)
    
        return res
