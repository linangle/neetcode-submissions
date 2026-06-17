class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)

        # check lengths first (all of s1 and s2 have to add to s3)
        if m + n != len(s3): 
            return False

        if n < m: # if s2 is shorter than s1
            s1, s2 = s2, s1 # swap them so DP array size becomes based on the smaller val
            m, n = n, m

        # idea : dp[j] represents whether s3[i + j:] can be formed using s1[:] and s2[j:]
            # at positions (i, j) we have used i characters from s1 and j characters from s2
            # the next character, we must match in s3 is at index i + j
        dp = [False for _ in range(n + 1)] # n is the smaller length
        dp[n] = True  # base case where both suffixes are empty

        for i in range(m, -1, -1):
            # nextDp represents value to the right (dp[j + 1]) of current row
            # initialize as true only when i == m (bottom row base case)
            nextDp = True if i == m else False 
            for j in range(n, -1, -1):
                # find whether state (i, j) is valid
                res = False if j < n else nextDp
                if i < m and s1[i] == s3[i + j] and dp[j]:
                    res = True
                if j < n and s2[j] == s3[i + j] and nextDp:
                    res = True
                dp[j] = res
                nextDp = dp[j]
        return dp[0]


