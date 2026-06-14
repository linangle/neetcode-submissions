class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # ITERATION SOL
        # idea : for every number in the array, take all the subsets we have so far
            # create new subsets by adding the current number to each of them
        res = [[]]

        for num in nums:
            res += [subset + [num] for subset in res]
        
        return res