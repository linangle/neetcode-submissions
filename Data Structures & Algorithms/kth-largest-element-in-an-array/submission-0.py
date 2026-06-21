class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
    # keep a min heap of size k : O(nlogk) time, O(k) space
        # .nlargest() returns a list in descending order
        # use -1 to get the last valuein this list, the kth value
        return heapq.nlargest(k, nums)[-1]
