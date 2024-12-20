class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visit = set()
        rows, columns = len(grid), len(grid[0])

        def bfs(r,c):
            queue = collections.deque()
            queue.append((r,c))
            visit.add((r,c))
            directions = [[0,1], [0,-1], [1,0], [-1,0]]
            while queue:
                r,c = queue.popleft()
                for dr, dc in directions:
                    nr , nc = r + dr, c + dc
                    if (nr in range(rows) and nc in range(columns) and grid[nr][nc]=="1" and (nr,nc) not in visit):
                        queue.append((nr, nc))
                        visit.add((nr, nc))                


        for r in range(rows):
            for c in range(columns):
                if grid[r][c]=="1" and (r,c) not in visit:
                    bfs(r,c)
                    islands+=1
        return islands
        