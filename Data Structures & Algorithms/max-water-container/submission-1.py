class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        biggest = 0

        while i < j:
            # area = width * height
            w = j - i
            h = min(heights[i], heights[j])
            area = w * h
            biggest = max(biggest, area)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return biggest
