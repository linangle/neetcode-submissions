class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # BACKTRACKING
        res = []
        candidates.sort() # so that if we overshoot, don't have to keep computing w higher nums

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i == len(candidates):
                return
            
            cur.append(candidates[i])
            # include the number, recurse with the next number
            dfs(i + 1, cur, total + candidates[i])
            # backtrack by popping
            cur.pop()

            # skip duplicates by advancing i forward while the next number is the same
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            # exclude the number
            dfs(i + 1, cur, total)
        
        dfs(0, [], 0)
        return res