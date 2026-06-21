class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
    # backtracking hash set sol
    # idea : remember the attacked positions using hash sets
        # use 3 hash sets:
            # col --> tracks used c (columns)
            # posDiag --> tracks (row + col)
            # negDiag --> tracks (row - col)
        
        col = set()
        posDiag = set()
        negDiag = set()
    
        res = []

        # initialize an nxn board with "."
        board = [["."] * n for i in range(n)]
        
        # backtrack(r) means place a queen in row r
        def backtrack(r):
            # we've successfully placed queens in rows 0 through n - 1, valid solution found
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                # for the current row, try every column
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue # skip if already in the attacked sets
                
                # if safe, add to the sets
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                # recurse to the next row
                backtrack(r + 1)

                # backtrack by removing entries from sets
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res




