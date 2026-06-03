class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, n in enumerate(nums): # index, value pairs
            # since the list is sorted, if the first value is greater than 0, there is no 3 sum --> immediately break
            if n > 0: 
                break

            # skip duplicates
            if i > 0 and n == nums[i - 1]:
                continue

            target = -n
            # j starts right after i, k starts at the end
            j, k = i + 1, len(nums) - 1
            while j < k:
                currsum = nums[j] + nums[k]
                if currsum > target:
                    k -= 1
                elif currsum < target:
                    j += 1
                else:
                    res.append([n, nums[j], nums[k]])
                    # update j and k to move to next numbers
                    j += 1
                    k -= 1
                    # skip j val duplicates
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1 
        return res
                


