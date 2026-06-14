class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # BACKTRACKING (hash map)
            # idea : store frequencies in a math to track how many times a number appears
        self.res = []
        self.count = defaultdict(int) # build a frequency map for all nums
        cur = []
        A = [] # build a list of unique numbers

        for num in candidates:
            if self.count[num] == 0: # if we haven't seen the number before
                A.append(num) # append it to unique numbers
            self.count[num] += 1 # increment its frequency
        self.backtrack(A, target, cur, 0) # find combinations with this number
        return self.res

    def backtrack(self, nums, target, cur, i):
        if target == 0: # found
            self.res.append(cur.copy())
            return
        if target < 0 or i >= len(nums): # overshot
            return
        
        if self.count[nums[i]] > 0:
            cur.append(nums[i])
            self.count[nums[i]] -= 1 # decrement the counter for this num
            # include the number
            self.backtrack(nums, target - nums[i], cur, i)
            self.count[nums[i]] += 1
            # backtrack
            cur.pop()
        
        self.backtrack(nums, target, cur, i + 1)
