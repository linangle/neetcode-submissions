class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
    # prim's algorithm
    # idea : this is a minimum spanning tree (MST) problem
    # every pair of points has edge weight = manhattan dist
    # need min way to connect w/o forming unnecessary cycles --> MST
        # start with node = 0
        n, node = len(points), 0
        dist = [100000000] * n
        visit = [False] * n
        edges, res = 0, 0 # connected edges, total cost

        # tree has n - 1 edges
        while edges < n - 1:
            visit[node] = True
            nextNode = -1
            for i in range(n):
                if visit[i]: # if visited already, skip
                    continue
                # compute cost to connect i from current node
                curDist = (abs(points[i][0] - points[node][0]) +
                            abs(points[i][1] - points[node][1]))
                dist[i] = min(dist[i], curDist)
                # choose nextNode as unvisited point with smallest dist[i]
                if nextNode == -1 or dist[i] < dist[nextNode]:
                    nextNode = i
        
            res += dist[nextNode]
            node = nextNode
            edges += 1
        return res