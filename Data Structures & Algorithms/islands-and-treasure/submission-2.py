class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
    # bfs sol (multi-source)
        m, n = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addCell(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == -1 or (r, c) in visit:
                return
            visit.add((r, c))
            q.append([r, c])

        for r in range(m):
            for c in range(n):
                # add all treasure chests to the queue
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))
        
        dist = 0
        while q:
            # bfs from the treasure chests to find shortest paths
            for i in range(len(q)): 
                r, c = q.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1


