class Solution:
    def hammingWeight(self, n: int) -> int:
    # bit mask optimal
    # idea: subtracting 1 from a number flips the rightmost 1 bit to 0
    # turns all bits to its right into 1
        # performing n & (n - 1) removes the rightmost 1 bit from n
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res