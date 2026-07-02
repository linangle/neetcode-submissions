class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # one pass
        n = len(nums)
        ans = [0] * (2*n)
        for i, val in enumerate(nums):
            ans[i] = val
            ans[i + n] = val
        return ans
