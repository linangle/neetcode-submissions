class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = set(nums)
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in ht:
                jidx = nums.index(diff)
                if i != jidx:
                    return sorted([i, jidx])