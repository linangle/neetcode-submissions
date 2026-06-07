class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} # hash maps characters --> frequency
        l = 0
        best = 0 
        maxfreq = 0

        for r in range(len(s)):
            # update the frequency each time we see a character
            count[s[r]] = 1 + count.get(s[r], 0) # default of 0 if we haven't seen it before
            maxfreq = max(maxfreq, count[s[r]]) # check if the character we just updated is the new max

            while (r - l + 1) - maxfreq > k:
                # shrink the window, update the count
                count[s[l]] -= 1
                l += 1
            
            # if we're haven't hit more than k replacements required
            best = max(best, (r - l + 1)) # update our best value
        
        return best

