class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1count, s2count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1count[ord(s1[i]) - ord("a")] += 1 # normalize by setting a has index 0
            s2count[ord(s2[i]) - ord("a")] += 1 # to intialize both tables at the same time
        
        matches = 0 # initialize
        for i in range(26): # hard code because we know alphabet has 26 characters
            matches += (1 if s1count[i] == s2count[i] else 0) 

        l = 0
        for r in range(len(s1), len(s2)): # we start at s1 because we initialized earlier with s1
            if matches == 26: return True

            # we move to the right 1
            index = ord(s2[r]) - ord("a") # normalize this index
            s2count[index] += 1
            if s2count[index] == s1count[index]: # processing this character led to a match --> increment match
                matches += 1
            elif s1count[index] + 1 == s2count[index]: # the freqs were already matched, processing this made it go over --> decrement match
                matches -= 1

            # also move the left pointer to the right 1
            index = ord(s2[l]) - ord("a") # normalize this index
            s2count[index] -= 1
            if s2count[index] == s1count[index]: # processing this character led to a match --> increment match
                matches += 1
            elif s1count[index] - 1 == s2count[index]: # the freqs were already matched, moving to the left made it unequal
                matches -= 1
            l += 1 
        return matches == 26

            
           

