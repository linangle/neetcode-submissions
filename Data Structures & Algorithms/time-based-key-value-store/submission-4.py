class TimeMap:
    def __init__(self):
        self.store = {} # hash map : key = string, value = [list of [value, timestamp]]

    def set(self, key: str, value: str, timestamp: int) -> None:
        # if the key isn't in the map yet, store it
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        # use binary search to get in O(logn) time
        res, values = "", self.store.get(key, []) # values are strings --> use ""
        # remember that .get() gives default val of [] if it doesn't exist

        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp: # search to the right portion
                res = values[m][0] # closest we've seen so far, keep iterating
                l = m + 1
            else: # if greater than timestamp, not allowed --> search to the left portion
                r = m - 1 
                # don't assign result bc invalid value

        return res

        
