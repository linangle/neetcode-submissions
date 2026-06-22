class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        have = -1 # track the farthest end of current merged interval
        interval_start = -1 # mark start of current merged interval

        # find max start value among all intervals
        maxVal = max(interval[0] for interval in intervals)

        # mp[start] stores the farthest (end + 1) among intervals that start at start
        mp = [0] * (maxVal + 1)
        for start, end in intervals:
            mp[start] = max(end + 1, mp[start])

        for i in range(len(mp)):
            if mp[i] != 0: # some interval starts at i
                if interval_start == -1:
                    interval_start = i
                have = max(mp[i] - 1, have)
            if have == i: # we reach the end of an interval
                res.append([interval_start, have])
                have = -1
                interval_start = -1

        # if a merged interval is still open
        if interval_start != -1:
            res.append([interval_start, have])
        
        return res