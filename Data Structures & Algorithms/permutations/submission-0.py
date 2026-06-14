class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # backtracking 1 
        # idea : choose nums one-by-one and explore all possible orders
        self.res = []
        # start with an empty permutation and no numbers picked yet
        self.backtrack([], nums, [False] * len(nums))
        return self.res

    def backtrack(self, perm: List[int], nums: List[int], pick: List[bool]):
        if len(perm) == len(nums): # we have a full permutation
            self.res.append(perm.copy()) # add a copy
            return
        for i in range(len(nums)): # loop through all indices i
            if not pick[i]: # if we haven't already chosen a number
                perm.append(nums[i]) # append it to the perm
                pick[i] = True # mark that we've picked it already
                self.backtrack(perm, nums, pick) # recurse to build further
                # backtrack by removing nums[i] and marking pick[i] as false
                perm.pop() 
                pick[i] = False
