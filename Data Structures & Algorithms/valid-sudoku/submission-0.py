class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # initialize rows, cols, squares we've seen tracker
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for r in range(9): # there are 9 rows
            for c in range(9): # there are 9 columns
                if board[r][c] == ".": # if the cell is empty
                    continue # skip it
                # converting the digit at the square to a bit
                # 1 --> 0
                # 2 --> 1
                # 3 --> 2 etc
                val = int(board[r][c]) - 1 
                mask = 1 << val 
                # for example, if val = 4 (corresponding to a digit 5)
                # mask = 00001000

                if mask & rows[r]:
                    # if the row already has the bit turned on, 
                    # this will yield a nonzero value (only the overlap) --> duplicate exists
                    return False
                if mask & cols[c]:
                    # apply similar logic to columns and squares
                    return False
                if mask & squares[(r // 3) * 3 + (c//3)] :
                    return False
                
                # if we haven't seen it yet, add it to seen (turn the bit on)
                # |= operator turns that bit on
                rows[r] |= mask
                cols[c] |= mask
                squares[(r//3) * 3 + (c//3)] |= mask

        return True