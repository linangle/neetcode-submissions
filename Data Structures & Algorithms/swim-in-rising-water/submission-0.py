class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # idea : minimize the max cell height along the path
        # define cost to reach a call = smallest possible "max height" so far
        n = len(grid) # square
        directions = [[-1, 0],[1, 0], [0, 1], [0, -1]]
        visit = set()
        # timeSoFar = max height on path up to (r, c)
        minH = [[grid[0][0], 0, 0]] # (timeSoFar, r, c)
        
        visit.add((0, 0))
        while minH:
            t, r, c = heapq.heappop(minH)
            # reached end of board
            if r == n - 1 and c == n - 1:
                return t
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if (nr < 0 or nc < 0 or nr >= n or nc >= n or (nr, nc) in visit):
                    continue
                visit.add((nr, nc))
                heapq.heappush(minH, [max(t, grid[nr][nc]), nr, nc])
                
