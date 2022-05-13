class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        elif len(grid) == 1 and len(grid[0]) == 1:
            return 1
        
        shortest_path = 1
        q = deque([(0,0)])
        r = len(grid)
        c = len(grid[0])
        bottom_right = (r-1,c-1)
        grid[0][0] = 1
        
        while q:
            n = len(q)
            for i in range(n):
                x,y = q.popleft()
                # add 8-directionally adj. fields
                for new_x, new_y in ((x+1,y),(x-1,y),(x,y+1),(x,y-1),(x+1,y+1),(x-1,y-1),(x+1,y-1),(x-1,y+1)):
                    if new_x < 0 or new_y < 0 or new_x >= r or new_y >= c or grid[new_x][new_y]==1:
                        continue
                    elif (new_x,new_y) == bottom_right:
                        return shortest_path + 1
                    else:
                        grid[new_x][new_y] = 1
                        q.append((new_x,new_y))
            shortest_path += 1
        
        
        return -1