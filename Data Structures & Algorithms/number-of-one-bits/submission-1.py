class Solution:
    def hammingWeight(self, n: int) -> int:
    # idea: instead of checking every bit, look at least significant bit of n
        # shift the number right to bring the next bit into that position
        res = 0
        while n:
            res += 1 if n & 1 else 0
            n >>= 1
        return res