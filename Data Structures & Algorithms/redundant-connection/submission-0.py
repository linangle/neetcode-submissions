class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    # optimal dfs
        n = len(edges)
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = [False] * (n + 1)
        cycle = set()
        cycleStart = -1

        def dfs(node, par):
            nonlocal cycleStart
            # if dfs enters an already visited node, mark it as cycleStart
            if visit[node]:
                cycleStart = node
                return True
            
            visit[node] = True
            # add nodes to cycle until reaching cycleStart, then stop marking
            for nei in adj[node]:
                if nei == par:
                    continue
                if dfs(nei, node):
                    if cycleStart != -1: # if we're in a cycle
                        cycle.add(node)
                    if node == cycleStart:
                        cycleStart = -1 # reached the beginning of the cycle again
                    return True
            return False
        
        dfs(1, -1)

        # return the first edge (u, v) where both endpoints are in cycle
        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]
        
        return []

