class Solution:
    def canPartition(self, nums: List[int]) -> bool:
    # dp bottom up (space optimized)  
    # idea : track dp[j] --> whether sum j is achievable using numbers processed so far

        if sum(nums) % 2: # if odd
            return False
        
        target = sum(nums) // 2
        dp = [False] * (target + 1)
        nextDp = [False] * (target + 1)

        # base case 
        dp[0] = True

        # iterate through all numbers
        for i in range(len(nums)):
            # try every possible sum
            for j in range(1, target + 1):
                if j >= nums[i]:
                    # we can make j if we were already able to make j (seen it before)
                        # or we can make j with the current number and the other component to j
                    nextDp[j] = dp[j] or dp[j - nums[i]]
                else: # current number is too large to use
                    nextDp[j] = dp[j]
            # move rows to conserve space
            dp, nextDp = nextDp, dp
            
        return dp[target]
