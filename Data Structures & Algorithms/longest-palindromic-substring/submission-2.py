class Solution:
    def longestPalindrome(self, s: str) -> str:
        # two pointers : O(n^2) time, O(1) extra space
        resIdx = 0
        resLen = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen: # new max found, update
                    resIdx = l
                    resLen = r - l + 1
                # expand the pointers
                l -= 1
                r += 1
            
            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen: 
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1

        return s[resIdx : resIdx + resLen]