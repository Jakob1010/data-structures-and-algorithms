class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_o = set()
        rotten_o = deque()
        minutes = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh_o.add((i,j))
                elif grid[i][j] == 2:
                    rotten_o.append((i,j))
        
        if len(fresh_o) == 0: return 0
        
        while rotten_o:
            n = len(rotten_o)
            for i in range(n):
                x,y = rotten_o.popleft()
                for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                    if (x+dx,y+dy) in fresh_o:
                        fresh_o.remove((x+dx,y+dy))
                        rotten_o.append((x+dx,y+dy))
            minutes += 1
            if len(fresh_o) == 0: return minutes
                
        return -1
        