class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        for i in range(len(nums)):
            # skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # reset j and k for every i
            j = i + 1
            k = len(nums) - 1
            while j < k:
                target = -nums[i]
                currsum = nums[j] + nums[k]
                if currsum < target:
                    j += 1
                elif currsum > target:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    # update j and k because there can be more solutions for one 1 starting i
                    j += 1
                    k -= 1

                    # skip duplicate second values
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
        return res


