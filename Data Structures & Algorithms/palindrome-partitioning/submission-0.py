class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # backtracking 1
        res = []
        part = []

        # j is the start index of the current substring we're forming
        # i is the end index we're expanding

        def dfs(j, i):
            if i == len(s): # if i reaches the end of the string
                if i == j: # if j is also at the end, we've perfectly partitioned the whole string
                    res.append(part.copy()) # add a copy to the results
                return
            
            # if we find a palindrome, append it to the parts
            if self.isPalin(s, j, i):
                part.append(s[j : i + 1])
                # recurse with the next position to build the next piece
                dfs(i + 1, i + 1)
                # backtrack by removing the last added substring
                part.pop()
                
            # try making the substring longer without cutting yet
            dfs(j, i + 1)

        dfs(0, 0)
        return res

    def isPalin(self, s, l, r): # use two pointers
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1 # move the pointers inward
        return True