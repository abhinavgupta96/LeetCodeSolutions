class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        visit = set()

        def bfs(r,c):
            queue = collections.deque()
            queue.append((r,c))
            visit.add((r,c))
            directions = [[0,1], [0,-1], [1,0], [-1,0]]
            while queue: 
                r,c = queue.popleft()
                for dr, dc in directions:
                    nr,nc = r+dr, c+dc
                    if nr in range(rows) and nc in range(cols) and (nr,nc) not in visit and grid[nr][nc]=="1":
                        queue.append((nr,nc))
                        visit.add((nr,nc))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visit:
                    bfs(r,c)
                    islands+=1
        return islands


