class Solution:
    def compress(self, chars: List[str]) -> int:
        # k = write pointer
        # i = read pointer
        # j = pointer to find consecutive characters equal to chars[i]
        # overwrite as we go to conserve space

        n = len(chars)
        k, i = 0, 0

        while i < n: 
            # get the letter
            chars[k] = chars[i]
            k += 1 # preparing to receive the number
            # search for consecutive characters
            j = i + 1 
            while j < n and chars[i] == chars[j]:
                j += 1 # we will stop one character after the last consecutive one
            
            if j - i > 1: # if we have consecutive characters
                for c in str(j - i): # in case we have multi-digits
                    chars[k] = c
                    k += 1
            
            # move i to process the character after the consecutive sequence
            i = j
        
        return k


            