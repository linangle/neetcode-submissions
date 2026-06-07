class Solution:
    def isHappy(self, n: int) -> bool:
        # HASH SET
        # hash set to keep track of what we've already seen
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n) 
            if n == 1:
                return True
        return False

    def sumOfSquares(self, n: int) -> int:
        output = 0

        while n:
            digit = n % 10 # gets us the last digit
            digit = digit ** 2 # square it
            output += digit
            n = n // 10 # take off that last digit to process the next one
        return output