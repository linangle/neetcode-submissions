class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # O(1) space complexity
        n = len(s) 
        length = 0

        # start the pointer from the end
        i = n - 1

        # if we see spaces, skip them until we see a word
        while s[i] == " ":
            i -= 1
        
        while i >= 0 and s[i] != " ":
            i -= 1
            length += 1
        
        return length
        

