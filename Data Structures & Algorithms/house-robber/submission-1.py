class Solution:
    def rob(self, nums: List[int]) -> int:
        # keep a memo of which houses we've already visited
        memo = [-1] * len(nums)

        def dfs(i):
            # if i is out of bounds, no money
            if i >= len(nums):
                return 0
            
            # if we've already seen this house before
            if memo[i] != -1:
                # return what we already computed
                return memo[i]
            
            # compute if we haven't seen it
            # skip : dfs(i + 1)
            # rob : nums[i] + dfs(i + 2)
            memo[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
            return memo[i]

        return dfs(0)