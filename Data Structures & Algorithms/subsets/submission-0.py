class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # BACKTRACKING SOL
        res = [] # final list of all subsets
        subset = [] # current subset being built

        def dfs(i):
            if i >= len(nums): # we've gone through all
                res.append(subset.copy()) # add a copy of subset to res
                return
            # choice 1 : include nums[i]
            subset.append(nums[i])  # append num to the subset
            dfs(i + 1) # recurse to the next index

            # remove the number (backtrack)
            subset.pop()
            # choice 2: skip nums[i], recurse to the next index
            dfs(i + 1)
        
        # start recursion with dfs(0)
        dfs(0)
        return res