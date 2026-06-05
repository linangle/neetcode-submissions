class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])

        # initialize pointers for scanning the rows 
        top, bot = 0, r - 1 
        while top <= bot:
            midr = (top + bot) // 2
            # check the first value in the row because it is the least ; we can skip it if target is smaller
            if target < matrix[midr][0]:
                # if the target is less, we know the target is either in that row or doesn't exist
                # move the bottom pointer up
                bot = midr - 1
            # check last value (greatest) ; can skip it if target is larger
            elif target > matrix[midr][-1]:
                top = midr + 1
            # the target may be in the row
            else:
                break
        
        if not (top <= bot):
            return False # target does not lie in the range of any row
        
        # binary search the row (row is a list of column values)
        row = (top + bot) // 2
        l, r = 0, c - 1
        while l <= r:
            midc = (l + r) // 2
            if target > matrix[row][midc]:
                l = midc + 1
            elif target < matrix[row][midc]:
                r = midc - 1
            else:
                return True
        return False
                
            
                
                