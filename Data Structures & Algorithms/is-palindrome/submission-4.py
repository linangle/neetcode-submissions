class Solution:
    def isPalindrome(self, s: str) -> bool:
        # initialize pointers
        l, r = 0, len(s) - 1 
        # isalnum() checks if a character is alphanumeric or not
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1 # increment until we find alphanum
            while r > l and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1 # increment both
        return True
