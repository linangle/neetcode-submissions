class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # backtracking optimal
        # idea : mark the current cell as used by replacing character with a special value like #
            # do dfs to match word character by character

        # let rows, cols be the grid size
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word): # we matched all characters
                return True
            # fail cases:
                # if out of bonds, if current cell doesn't match, if cell is already used
            if (r < 0 or c < 0 or r >= rows or c >= cols or 
                word[i] != board[r][c] or board[r][c] == '#'):
                return False

            # mark cell as used 
            board[r][c] = '#'
            res = (dfs(r + 1, c, i + 1) or
                    dfs(r - 1, c, i + 1) or
                    dfs(r, c + 1, i + 1) or
                    dfs(r, c - 1, i + 1))
            # backtrack by resetting the cell to its original character
            board[r][c] = word[i]
            return res
                
        # run the dfs for every cell
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False