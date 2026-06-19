class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    # dp (top down) where we store longest lengths from a cell in a cache
        dp = {}
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        m, n = len(matrix), len(matrix[0])

        def dfs(r, c, prevVal):
            # if out of bounds or isn't larger than the previous value
            if (r < 0 or c < 0 or r >= m or c >= n or
            matrix[r][c] <= prevVal):
                return 0
            # if we've seen this cell before, return the longest path
            if (r, c) in dp:
                return dp[(r, c)]
            
            # moving one cell is + 1
            res = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                res = max(res, 1 + dfs(nr, nc, matrix[r][c]))
            dp[(r, c)] = res
            return res
        
        for r in range(m):
            for c in range(n):
                dfs(r, c, -1)
        
        return max(dp.values())