from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
    # dp + binary search : O(nlogn) time, O(n) space
    # idea : maintain an array dp where dp[i] is the smallest ending element of all increasing subsequences of length i + 1
        # for each new element, if it's larger than the last element in dp, it extends the longest subsequence
        # else, use binary search to find the position where it can replace an element, keeping the array optimal for future extensions
    
        dp = []
        dp.append(nums[0])

        LIS = 1
        for i in range(1, len(nums)):
            if dp[-1] < nums[i]: 
                dp.append(nums[i])
                LIS += 1
                continue
            
            # if the next element isn't greater than the last
            # find the leftmost position in dp
                # where dp[pos] >= nums[i]
                # replace dp[pos] with nums[i]
            idx = bisect_left(dp, nums[i])
            dp[idx] = nums[i]

        return LIS
