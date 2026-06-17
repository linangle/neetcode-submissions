class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0

        def dfs(r, c):
            # check if we're out of bounds
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 0
            # sink the current 
            grid[r][c] = 0
            # area of 1 square is 1
            curArea = 1

            for dr, dc in directions:
                curArea += dfs(dr + r, dc + c)
            
            return curArea
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r, c))
        
        return maxArea