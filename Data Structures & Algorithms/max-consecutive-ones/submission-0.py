class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = cur = 0
        n = len(nums)

        for num in nums:
            if num == 0:
                res = max(res, cur)
                cur = 0 # reset the count
            else:
                cur += 1
        
        return max(cur, res)
