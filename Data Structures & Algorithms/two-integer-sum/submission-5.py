class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for i, n in enumerate(nums): # get the index, value of nums
            diff = target - n
            if diff in hmap:
                return [hmap[diff], i] # don't need to sort bc we know hmap[diff] is previous to i
            hmap[n] = i # store the value --> index into the map
