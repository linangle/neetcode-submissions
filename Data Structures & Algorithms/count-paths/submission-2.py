class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
    # top down sol
        # create a grid to track the squares on the board
        memo = [[-1] * n for _ in range(m)]
        
        def dfs(i, j):
            # if (i, j) is the destination --> one path
            if i == (m - 1) and j == (n - 1):
                return 1
            # if (i, j) is outside the grid --> no path
            if i >= m or j >= n:
                return 0
            
            # if we've seen this cell before, return the number of paths to get there
            if memo[i][j] != -1:
                return memo[i][j]
            
            memo[i][j] = dfs(i + 1, j) + dfs(i, j + 1)
            return memo[i][j]
        
        return dfs(0, 0)