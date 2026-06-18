class Solution:
    def solve(self, board: List[List[str]]) -> None:
    # dfs sol
        m, n = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            # if out of bounds or not an O
            if r < 0 or c < 0 or r >= m or c >= n or board[r][c] != "O":
                return
            # mark the spot with a safe "T"
            board[r][c] = "T"
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)
        
        # run dfs from every bordercell that is "O"
        for r in range(m):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][n - 1] == "O":
                dfs(r, n - 1)
        
        for c in range(n):
            if board[0][c] == "O":
                dfs(0, c)
            if board[m - 1][c] == "O":
                dfs(m - 1, c)
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
