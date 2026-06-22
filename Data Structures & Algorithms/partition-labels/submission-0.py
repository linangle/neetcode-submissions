class Solution:
    def partitionLabels(self, s: str) -> List[int]:
    # greedy two pointers
    # idea : current partition must extend at least up to the last occurrence of any character

        # record last index of every character in the string
        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i

        res = [] # store partition sizes
        size = 0 # current partition length
        end = 0 # farthest index partition must reach

        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])

            if i == end:
                res.append(size)
                size = 0 
        return res