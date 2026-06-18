class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    # topo sort --> kahn's alg , O(V + E) time and space
    # idea : repeatedly take course with zero prereqs, remove its dependency effect from others
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        # indegree[n] = number of courses this class is a prereq for
        # adj[src] = courses that are unlocked after finishing this course
        for course, prereq in prerequisites:
            indegree[prereq] += 1 # how many class this class is a prereq
            adj[course].append(prereq) # the prereqs for this class
        
        q = deque()
        for n in range(numCourses):
            # if this course is not a prereq for anything
            if indegree[n] == 0: 
                # append it to the q
                q.append(n)
        
        finish = 0
        while q:
            # pop the nodes with no dependencies
            node = q.popleft()
            finish += 1 # we are able to "finish" a class
            for nei in adj[node]: # for each prereq of this class
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return finish == numCourses
