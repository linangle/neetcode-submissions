class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp (bottom up) sol : O(n^2) time and space
        # keep track of palindromes we've seen
        resIdx, resLen = 0, 0
        n = len(s)

        dp = [[False] * n for _ in range(n)]

        # initialize two pointers starting at beginning and end
        for i in range(n - 1, -1, -1): # going backwards
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if resLen < (j - i + 1):
                        resIdx = i
                        resLen = j - i + 1

        return s[resIdx : resIdx + resLen]