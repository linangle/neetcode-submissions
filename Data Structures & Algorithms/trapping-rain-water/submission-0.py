class Solution:
    def trap(self, height: List[int]) -> int:
        # edge case : if the list of heights is empty, no rain water can be trapped
        if not height: 
            return 0

        res = 0
        l, r = 0, len(height) - 1
        # idea : the height at a given i is min(maxL, maxR) - height[i]
            # where maxL and maxR are the highest walls to the left and right of a position
        # move the pointer that had the smaller value of the two
            # this is because we're bounded by the min --> moving the larger pointer returns same min(maxL, maxR) val
        
        maxL, maxR = height[l], height[r]
        while l < r:
            # if the left max smaller, move it forwards
            if maxL <= maxR: # use <= because we can move either if they're equal
                l += 1
                # update the new max value
                    # we need to keep track of this separately from height[l] because it can be reused
                        # later height[l] might have smaller heights
                # compare the height we just moved the pointer to the max height
                maxL = max(maxL, height[l])
                # compute the water, add it to total result
                res += maxL - height[l]
            
            # same process for the right pointer
            else:
                r -= 1
                maxR = max(maxR, height[r])
                res += maxR - height[r]

        return res
            
