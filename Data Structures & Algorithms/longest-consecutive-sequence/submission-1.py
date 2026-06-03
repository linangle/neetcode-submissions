class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # has map solution
        # create a set to avoid duplicates
        hs = set(nums)
        longest = 0 # initialize the longest sequence counter
        # the start of a sequence only exists if n-1 does not exist
        for num in hs:
            if (num - 1) not in hs: # if we have found the start of a seq
                length = 1 # the start of a sequence is length 1 itself
                while (num + length) in hs: # while consecutive numbers exist
                    length += 1 # increment the length by 1
                longest = max(longest, length)
        return longest