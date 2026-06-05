class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # maintain (index, height) pairs here

        # since width is determined by the indices, keep track of i and h using enumerate
        for i, h in enumerate(heights):
            start = i
            # if the stack exists and the next bar is lower than the last bar, we can't keep moving forward
            while start and stack[-1][1] > h:
                popI, popH = stack.pop() # we can't extend, so pop that taller bar and record its index and height
                # calculate the area we were able to have the popped height extended to, compare
                maxArea = max(maxArea, popH * (i - popI))
                start = popI 
            stack.append((start, h))

        for i, h in stack: 
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
            
