class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # BACKTRACKING SOL
        # idea : at every index, we have two choices
            # include the number or skip the current number
        
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return # exit the function early
            if i >= len(nums) or total > target:
                return
            
            cur.append(nums[i])
            # include the number at the index
            dfs(i, cur, total + nums[i])
            # backtrack by popping
            cur.pop()
            # exclude the number at the index
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res