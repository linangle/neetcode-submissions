class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    # hash set dp sol
    # idea : a word can only be as long as the maximum wordlength in wordDict
    # use a hash set for O(1) word lookup
    # use memoization so each index in the string is only solved once

        wordSet = set(wordDict)
        t = 0 # t = max length of any word in wordDict
        for w in wordDict:
            t = max(t, len(w))
        
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(s): # we've gone through and split the whole word
                return True
            # j pointer runs from i to the end of the word or to the longest string
            for j in range(i, min(len(s), i + t)):
                if s[i : j + 1] in wordSet:
                    if dfs(j + 1): # if we find more substrings following this one
                        memo[i] = True 
                        return True
            memo[i] = False
            return False
        
        return dfs(0)
                    

            