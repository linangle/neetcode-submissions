class Solution:
    def isMatch(self, s: str, p: str) -> bool:
    # top down sol
        m, n = len(s), len(p)
        cache = {}

        def dfs(i, j):
            if i >= m and j >= n:
                return True # processed both
            if j >= n:
                return False # characters in s not matched

            # check the cache
            if (i, j) in cache:
                return cache[(i, j)]

            # is there match between first characters
            match = i < m and (s[i] == p[j] or p[j] == ".")
            # first pattern in the string will never be "*"
            if (j + 1) < n and p[j + 1] == "*":
                cache[(i, j)] = (dfs(i, j + 2) or # j + 2 is in case we skip and don't use the character
                # check match first, then use
                                (match and dfs(i + 1, j)))
                return cache[(i, j)]
            
            if match:
                cache[(i,j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            
            cache[(i, j)] = False
            return False
        return dfs(0, 0)
