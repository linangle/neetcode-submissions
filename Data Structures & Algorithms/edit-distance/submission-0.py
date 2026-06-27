class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
    # optimal dp
        m, n = len(word1), len(word2)
        # if word2 is longer than word1, swap them so n is the smaller length (smaller dp array)
        if m < n:
            m, n = n, m
            word1, word2 = word2, word1
        
        dp = [n - i for i in range(n + 1)]
        
        for i in range(m - 1, -1, -1):
            # store the diagonal values in nextDp
            nextDp = dp[n] # nextDp stores the former diagonal value
            dp[n] = m - i
            for j in range(n - 1, -1, -1):
                temp = dp[j]
                if word1[i] == word2[j]:
                    dp[j] = nextDp 
                else:
                    dp[j] = 1 + min(dp[j], dp[j + 1], nextDp)
                nextDp = temp
        return dp[0]