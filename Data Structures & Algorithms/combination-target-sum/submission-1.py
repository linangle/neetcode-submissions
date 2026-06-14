class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # BACKTRACKING SOL - optimal
        # idea : sort numbers so that once we exceed the target, all numbers after also exceed the target
        
        res = []
        nums.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy()) # append the list of nums that work
                return # return early 
            
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return # overshot, everything after also overshoots
                # include the current number
                cur.append(nums[j])
                dfs(j, cur, total + nums[j])
                # backtrack by popping
                cur.pop()
                
        dfs(0, [], 0)
        return res

