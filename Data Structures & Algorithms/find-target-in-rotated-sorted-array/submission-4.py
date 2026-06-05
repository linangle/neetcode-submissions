class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # use binary search to determine where the rotation split is
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
       
            if nums[m] > nums[r]: 
                l = m + 1
            else: 
                r = m

        pivot = l

        def binary_search(left = int, right= int) -> int:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1 # if no solution is found

        
        result = binary_search(0, pivot - 1) # this searches the left subsection first 
        if result != -1: # if we found an answer, return it
            return result
        
        else: # if we didn't, search the right subsection 
            return binary_search(pivot, len(nums) -1)
