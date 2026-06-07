class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set() # characters we've seen already
        l = 0 # left pointer starting index
        best = 0

        for r in range(len(s)): # iterate over the indices, r is the right pointer
            # if we've seen the character already, shrink the window size up to the duplicate
            while s[r] in seen:
                seen.remove(s[l])
                l += 1 
            seen.add(s[r])
            best = max(best, r - l + 1)
        return best

        
            





