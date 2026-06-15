class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    # top down sol
        memo = {}

        def dfs(i, j):
            # base cases : either index reaches the end of the string
            if i == len(text1) or j == len(text2):
                return 0
            # if we've seen this result before, return it
            if (i, j) in memo:
                return memo[(i, j)]
            
            # if we found a match, record it and recurse on the next position
            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + dfs(i + 1, j + 1)
            # if we didn't find a match, try incrementing one at a time
            else:
                memo[(i, j)] = max(dfs(i + 1, j), dfs(i, j + 1))
            
            return memo[(i, j)]
        
        return dfs(0, 0)