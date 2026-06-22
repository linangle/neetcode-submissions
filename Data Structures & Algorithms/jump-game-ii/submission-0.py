class Solution:
    def jump(self, nums: List[int]) -> int:
    # greedy bfs
    # idea : move level by level, using a greedy window
        res = 0 # to count num jumps
        l, r = 0, 0 # current reachable range
        # while the right boundary has not reached the last index
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res
        