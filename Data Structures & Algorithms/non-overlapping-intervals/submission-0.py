class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    # greedy (sort by start)
    # choice : always choose interval with shorter end time
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1] # intialize with end of first interval

        for start, end in intervals[1:]:
            if start >= prevEnd: # non-overlapping
                prevEnd = end
            else: # overlapping, need to remove
                res += 1
                prevEnd = min(end, prevEnd)
        return res 
