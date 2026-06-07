class Solution:
    def sumOfSquares(self, n: int) -> int:
        output = 0

        while n:
            digit = n % 10 # gets us the last digit
            digit = digit ** 2 # square it
            output += digit
            n = n // 10 # take off that last digit to process the next one
        return output


    def isHappy(self, n: int) -> bool:
        # HASH SET
        # hash set to keep track of what we've already seen
    #     visit = set()

    #     while n not in visit:
    #         visit.add(n)
    #         n = self.sumOfSquares(n) 
    #         if n == 1:
    #             return True
    #     return False

    # FAST AND SLOW POINTERS I
    # cycle detection using Floyd's tortoise and hare --> avoid storing all visited numbers
    # slow pointer starts at the original number, fast starts at the first sum of squares
        slow, fast = n, self.sumOfSquares(n)

        while slow != fast: # have not met yet, no cycle detected
            # fast moves two steps, slow moves one
            fast = self.sumOfSquares(fast)
            fast = self.sumOfSquares(fast)
            slow = self.sumOfSquares(slow)
        return True if fast == 1 else False # fast will reach a "happy" number before slow (if we are capable of reaching happy), also returns False if cycle


