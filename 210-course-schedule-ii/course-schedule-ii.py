class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        stateList = [UNVISITED]*numCourses
        adjList = defaultdict(list)

        for a,b in prerequisites:
            adjList[a].append(b)
        
        order = []

        def dfs(course):
            state = stateList[course]
            if state == VISITING:
                return False
            elif state == VISITED:
                return True

            stateList[course] = VISITING
            
            for nei in adjList[course]:
                if not dfs(nei):
                    return False
                    
            stateList[course] = VISITED
            order.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return order