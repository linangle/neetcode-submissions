class Solution:
    def hammingWeight(self, n: int) -> int:
    # bit mask I
    # idea: this is known as Hamming weight or population count
          # at each position create a mask with a single 1 using 1 << i
          # use bitwise AND (&) to test whether bit is set in n
        res = 0
        for i in range(32):
            if (1 << i) & n:
                res += 1
        return res