class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # length of string + delimiter + string
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 # initialize
        while i < len(s): # while i is in the bounds of encoded string
            j = i # initialize the pointer
            while s[j] != "#": # increment the pointer until we hit delimiter
                j += 1
            # when we hit the delimiter, append res
            length = int(s[i:j]) # this should be the length right before the delimiter we initially encoded; make this an int (currently a string)
            # start from one character after delimiter (j + 1) and end plus length
            res.append(s[j + 1: j + 1 + length])
            # update i to go to next string
            i = j + 1 + length 
        return res

