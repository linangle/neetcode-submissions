class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # at worst, we append len(t)
        m, n = len(s), len(t)
        subseq = 0
        i, j = 0, 0
        
        # while there are still characters in s to check
        while i < m and j < n:
            if s[i] == t[j]: # if we find a match
                i += 1
                j += 1
                subseq += 1
            else:
                i += 1

        return n - subseq
