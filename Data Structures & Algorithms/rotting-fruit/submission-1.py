class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
    # bfs w/o q : O((m * n)**2) time, O(1) space
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        m, n = len(grid), len(grid[0])
        fresh = 0
        time = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fresh += 1
        
        while fresh > 0:
            flag = False # did we rot anything this minute
            for r in range(m):
                for c in range(n):
                    # if we find a rotten fruit
                    if grid[r][c] == 2:
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            # if the direction we moved in has a fresh fruit
                            if nr in range(m) and nc in range(n) and grid[nr][nc] == 1:
                                grid[nr][nc] = 3 # mark it with 3
                                fresh -= 1
                                flag = True

            if not flag:
                return -1
            
            for r in range(m):
                for c in range(n):
                    if grid[r][c] == 3:
                        grid[r][c] = 2
            time += 1

        return time
        