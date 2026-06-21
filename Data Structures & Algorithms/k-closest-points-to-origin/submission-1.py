class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    # quick select
    # idea : pick a pivot point 
        # partition other points into closer or farther than the point
        euclidean = lambda x: x[0] ** 2 + x[1] ** 2
        def partition(l, r):
            pivotIdx = r
            pivotDist = euclidean(points[pivotIdx])
            i = l
            # rearrange points so all smaller distances go left
                # larger go right
            for j in range(l, r):
                if euclidean(points[j]) <= pivotDist:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            points[i], points[r] = points[r], points[i]
            return i

        # maintain two pointers
        l, r = 0, len(points) - 1 
        pivot = len(points)

        while pivot != k:
            pivot = partition(l, r)
            if pivot < k:
                l = pivot + 1
            else:
                r = pivot - 1
        return points[:k]