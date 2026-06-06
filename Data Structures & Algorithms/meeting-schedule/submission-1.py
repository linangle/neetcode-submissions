"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sort the intervals by their start times
        # the intervals are pairs ( , ) not lists
        intervals.sort(key = lambda i : i.start)

        # if the ending time of one meeting later than the start time of the next meeting --> overlap
        for i in range(1, len(intervals)): # start at the second meeting to compare with the previous
            i1 = intervals[i - 1]
            i2 = intervals[i]
            if i1.end > i2.start:
                return False
        
        return True