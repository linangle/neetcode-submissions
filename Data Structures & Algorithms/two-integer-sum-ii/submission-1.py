class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum < target:
                l += 1 # shift the the right 1
            elif sum > target:
                r -= 1 # shift to the left 1
            else: 
                return [l + 1, r + 1] # since the question specifies for 1-indexed
        return [] # return nothing if there's no two sum solution