class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # backtracking optimal
        # generate permutations in-place by swapping elements --> save space
        self.res = []
        self.backtrack(nums, 0)
        return self.res

    def backtrack(self, nums: List[int], idx: int):
        if idx == len(nums): # we reached all nums
            self.res.append(nums.copy()) # append a copy of the permutation
            return
        for i in range(idx, len(nums)):
            # swap the values at i and idx (placing nums[i] at the current position)
            nums[idx], nums[i] = nums[i], nums[idx]
            # recurse with idx + 1
            self.backtrack(nums, idx + 1)
            # backtrack by restoring original order
            nums[idx], nums[i] = nums[i], nums[idx]
 