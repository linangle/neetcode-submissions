class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build graph where each course points to its prereqs
        prereq = {c: [] for c in range(numCourses)}
        for course, pre in prerequisites:
            prereq[course].append(pre)
        
        output = []
        # visit tracks fully processed courses, cycle tracks current DFS path
        visit, cycle = set(), set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True
            
            cycle.add(course)
            for pre in prereq[course]:
                # check cycles for the prereqs
                if dfs(pre) == False:
                    return False
            
            # if the course and all its prereqs don't have a cycle, remove from this current path
            cycle.remove(course)
            # add the course to fully processed courses list
            visit.add(course)
            output.append(course)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output

