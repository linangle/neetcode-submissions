class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    # dijkstra's algorithm
        # build an adjacency list
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        # initialize with time, node
        minHeap = [(0, k)]
        visit = set() # avoid reprocessing nodes
        while minHeap:
            # pop node with smallest processing time
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit: # if we've visited this node already
                continue # skip
            visit.add(n1) # if we haven't visited, add to list
            t = w1

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        return t if len(visit) == n else -1

