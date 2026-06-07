class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) -1, -1, -1): # start at the end, go backwards
            if digits[i] != 9:
                digits[i] = digits[i] + 1
                return digits
            else:
                digits[i] = 0
        # in the case all digits are 9, e.g. 999, return a 1 in front to get 1000
        return [1] + digits
        
