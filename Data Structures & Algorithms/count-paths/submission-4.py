class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
    # bottom up ; space optimized 
    # idea : instead of storing the entire grid, keep one row at a time
        # initialize a 1D array row of size n with all 1s
            # only one way to move right along the bottom row
        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            # traverse cols right to left (excluding the last)
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]