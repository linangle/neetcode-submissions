class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 # left pointer starting index
        mp = {} # initialize a hash map to track the last index of each character --> l jumps instead of incrementing
        best = 0

        for r in range(len(s)): # iterate over the indices, r is the right pointer
            # if we've seen the character already, shrink the window size up to the duplicate
            if s[r] in mp: # if we've already mapped this character, jump 
                l = max(mp[s[r]] + 1, l) # take the max because multiple duplicates --> one could be behind l (need to jump to duplicate in front of l)
            mp[s[r]] = r
            best = max(best, r - l + 1)
        return best
        
            





