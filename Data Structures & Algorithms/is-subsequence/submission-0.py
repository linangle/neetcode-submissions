class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
   
        if m == 0:
            return True
        if m > n:
            return False

        i, j = 0, 0
        while j < n:
            if s[i] == t[j]:
                i += 1
                if i == m:
                    return True
            j += 1
        return False