class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # initialize two pointers
        l = 0
        r = len(nums) - 1

        while l <= r:
            # the middle index is in between these
            mid = (l + r) // 2

            if nums[mid] > target: # if we're over, move the right pointer to where we are
                r = mid - 1 # don't have to check mid so move another one over
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        # no solution, return -1
        return -1