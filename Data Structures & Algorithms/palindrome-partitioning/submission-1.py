class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # backtracking 2
        # idea : partition from left to right
        res = []
        part = []

        def dfs(i): 
            # base case
            if i == len(s): # we have partitioned the whole string
                res.append(part.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPalin(s, i, j):
                    part.append(s[i : j + 1])
                    # recurse on the next position
                    dfs(j + 1)
                    # backtrack by removing the previous substring
                    part.pop()
        dfs(0)
        return res
            
    def isPalin(self, s, l, r): # two pointers
        while l < r: 
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
    