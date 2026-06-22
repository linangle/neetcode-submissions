class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
    # greedy optimal
    # idea : when we merge, take max --> values can only increase
        # if any triplet has greater value than target, cannot be used
    
        # initialize 3 boolean flags, each checking for each target triplet value
        x = y = z = False

        for t in triplets:
            # |= is or= (stays true if reaches true once)
            x |= (t[0] == target[0] and t[1] <= target[1] and t[2] <= target[2])
            y |= (t[1] == target[1] and t[0] <= target[0] and t[2] <= target[2])
            z |= (t[2] == target[2] and t[0] <= target[0] and t[1] <= target[1])

            if x and y and z:
                return True
        return False