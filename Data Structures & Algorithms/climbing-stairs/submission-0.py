class Solution:
    def climbStairs(self, n: int) -> int:
        # base cases, we start at the 0 stairs and 1 stair
        cur, prev = 1, 1 # there is 1 way to get to each

        for i in range(n-1): # since we already process the first case of 1 stair, need to find remaining n - 1
            # store a temporary value to remember the original current number of ways
            temp = cur
            # update cur --> next step = number of ways to get to cur + number of ways to geet to prev
            cur = cur + prev
            # update prev --> next step = original cur
            prev = temp

        # we get out of the loop when we're at the end of the stairs, where cur is our answer
        return cur