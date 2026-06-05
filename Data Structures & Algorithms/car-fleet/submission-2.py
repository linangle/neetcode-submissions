class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
   
        # pair the positions, times
        pspairs = [(p,s) for p, s in zip(position, speed)]

        # sort the positions based on descending order
        pspairs.sort(reverse = True)
        
        # track the times using a stack
        stack = []

        # we can calculate the time it takes the last car to reach target
            # if this time is less than the time of the car in front of it, they form a fleet
            # increment res by 1 
        for p, s in pspairs:
            time = ((target - p) / s)
            stack.append(time)
            # if stack also works, but if only 1, no merges so nothing happens
            if len(stack) >= 2 and stack[-1] <= stack[-2]: # they merge
                stack.pop()
        
        return len(stack)