class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # defaultdict handles cases keys that don't exist --> []
        # we're mapping the frequencies (keys) --> list of strings with those frequencies (values)
        for s in strs: # for each string in the list of strings
            count = [0] * 26 # intialize a hash map for the 26 letters of the alphabet
            for c in s: # for each character in the string
                normalized_idx = ord(c) - ord("a") # we want "a" --> 0
                count[normalized_idx] += 1 # increment the counter every time we see the character
            # have to make count (which is a list) into a tuple bc keys must be immutable
            result[tuple(count)].append(s) # append the string to the list of anagrams (stored as the value of the dict)
        return list(result.values()) # use list() bc result.values() will return a dictionary view object; we want a list
