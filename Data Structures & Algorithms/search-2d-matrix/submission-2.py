class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for r in matrix: # each r is the nested list e.g. [1, 2, 4, 8]
            # check the last value in the row
            if r[-1] < target: # if the largest value in the row is smaller than the target, we can skip this row
                continue
            elif r[-1] > target: # if the largest value in the row is larger, check if the target is one of the earlier values in the row
                # run binary search on the row
                i, j = 0, len(r) - 1
                while i <= j:
                    mid = (i + j) // 2
                    if r[mid] < target:
                        i = mid + 1
                    elif r[mid] > target:
                        j = mid - 1
                    else:
                        return True
            else: # if the last value in the row is the target, True
                return True
        return False
                
                