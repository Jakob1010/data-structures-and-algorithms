class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0 or grid[len(grid)-1][len(grid[0])-1] != 0:
            return -1
        if len(grid)==1 and len(grid[0])==1:
            return 1
    
        q = deque([(0,0)])
        visited = set()
        shortest_path = 1
        
        visited.add((0,0))
        while q:
            n = len(q)
            for i in range(n):
                x,y = q.popleft()
                for new_x, new_y in ((x+1,y),(x-1,y),(x,y+1),(x,y-1),(x+1,y+1),(x-1,y-1),(x+1,y-1),(x-1,y+1)):
                    if new_x < 0 or new_y < 0 or new_x >= len(grid) or new_y >= len(grid[0]) or grid[new_x][new_y] == 1 or (new_x,new_y) in visited:
                        continue
                    elif new_x == len(grid)-1 and new_y == len(grid[0])-1:
                        return shortest_path+1
                    else:
                        q.append((new_x,new_y))
                        visited.add((new_x,new_y))
            shortest_path += 1
        return -1
                    
        