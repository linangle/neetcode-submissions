class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # initialize a hash map : number --> frequency it appears
        count = {}
        # initialize a table to bucket sort; this is a list of lists
        # we map frequency (index) --> list of nums with that frequency 
        # the highest index is going to be the length of nums
            # the largest possible freq is if all nums are the same number
            # add one to account for 0 
        freq = [[] for i in range(len(nums) + 1)]

        # count the frequency
        # we use dict.get() to have a default value of 0 to avoid KeyErrors
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for num, cnt in count.items(): # items.() returns number, freq pairs
            # make freq the index, num the values
            freq[cnt].append(num) # append to the empty list
        
        # make a results list
        result = []
        # start at the end of freq (this is the highest frequency)
            # go to 0
                # decrementing by 1 each time
        for i in range(len(freq) - 1, 0, -1):
            # for each frequency, append each num that has that freq to results
            for num in freq[i]:
                result.append(num)
                if len(result) == k: # we only want the top k
                    return result



