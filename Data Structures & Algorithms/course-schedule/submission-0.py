class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    # dfs cycle detection
    # can finish all courses if there is no cycle 
        # map each course to its prereqs
        preMap = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)
        
        # store all courses along the current dfs path
        visiting = set()

        def dfs(course):
            if course in visiting:
                # cycle detected
                return False
            if preMap[course] == []:
                return True
            
            visiting.add(course)
            for pre in preMap[course]:
                if not dfs(pre): # if one of the prereqs has a cycle
                    return False

            visiting.remove(course)
            preMap[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False

        return True