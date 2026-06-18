class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
    # multi source bfs : O(m * n) time and space
        q = deque()
        fresh = 0
        time = 0
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        m, n = len(grid), len(grid[0])

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1: # if we see a fresh orange
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()

                # try every direction from the rotten fruit
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # if we're within bounds and find a fresh fruit
                    if (nr in range(m) and nc in range(n) and grid[nr][nc] == 1):
                        # turn the fresh fruit rotten
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1


        