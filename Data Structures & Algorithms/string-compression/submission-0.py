class Solution:
    def compress(self, chars: List[str]) -> int:
    # extra space sol
        n = len(chars)
        s = ""

        i = 0
        while i < n:
            s += chars[i]
            j = i + 1
            # find the consecutive characters
            while j < n and chars[i] == chars[j]:
                j += 1
            
            if j - i > 1: # if we did find a consecutive
                s += str(j - i) # append the frequency
            
            # move i to the next non-consecutive
            i = j

        # compress chars
        i = 0
        while i < len(s):
            chars[i] = s[i]
            i += 1
        
        return len(s)