class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        stateList = [UNVISITED]*numCourses

        adjList = defaultdict(list)
        courses = prerequisites
        for a,b in courses:
            adjList[a].append(b)

        def dfs(course):
            state = stateList[course]
            if state == VISITING:
                return False
            elif state == VISITED:
                return True
            stateList[course] = VISITING
            for pre in adjList[course]:
                if not dfs(pre):
                    return False
            stateList[course] = VISITED
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True