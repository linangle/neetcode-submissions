class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    # Hierholzer's Algorithm (Recursion)
    # idea : eulerian path problem
    # take available edge, go as deep as possible, add airports to answer only when no outgoing edges remain
        adj = defaultdict(list)
        # pop takes from the end
            # want lexicographically sorted so sort in reverse to pop the smallest
        for source, destination in sorted(tickets)[::-1]:
            adj[source].append(destination)
        
        res = []
        def dfs(source):
            while adj[source]:
                destination = adj[source].pop()
                dfs(destination)
            res.append(source)
        
        dfs('JFK')
        return res[::-1]