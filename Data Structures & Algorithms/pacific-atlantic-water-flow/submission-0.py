class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    # dfs sol
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        m, n = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            # reverse flow idea : we can go to a neighbor nr, nc
                                # only if heights[nr][nc] >= heights[r][c]
            # if we're out of bounds, visited this cell before or are lower than the previous height
            if ((r, c) in visit or r < 0 or c < 0 or
            r >= m or c >= n or heights[r][c] < prevHeight):
                return
            
            visit.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, visit, heights[r][c])
        # run dfs from every pacific border cell, fill pac
        # run dfs from every atlantic border cell, fill atl
        for c in range(n):
            dfs(0, c, pac, heights[0][c])
            dfs(m - 1, c, atl, heights[m - 1][c])
        
        for r in range(m):
            dfs(r, n - 1, atl, heights[r][n - 1])
            dfs(r, 0, pac, heights[r][0])
        
        res = []
        for r in range(m):
            for c in range(n):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res
        

            