class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # initialize a results list, keeping 0 for defaults where we don't find a higher temp 
        res = [0] * len(temperatures)
        stack = [] # here, we will store [temp, index] pairs

        # since we're concerned with the indices (to calculate days), we use enumerate
        for i, t in enumerate(temperatures):
            # if the stack exists (we're past the starting point / etc) 
                # and the temperature we're processing is higher, we've found a max
                # notice that the temperatures are monotonically decreasing, so 
                    # we only need to check the last pushed value for whether something is greater than everything before that last pushed val
            while stack and t > stack[-1][0]: # [-1] for last val, [0] to get the temp val in stack [temp, index] pairs
                stackT, stackI = stack.pop() # retrieve the temp, index from the stack (original pair we pushed)
                res[stackI] = (i - stackI)
            # if we haven't run into a higher value yet, append to the stack
            stack.append([t, i])

        return res
