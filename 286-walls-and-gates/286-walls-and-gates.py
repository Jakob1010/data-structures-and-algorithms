class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        q = deque()
        
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    q.append([i,j,0])
                    
        while q:
            n = len(q)
            for i in range(n):
                x,y,distance = q.popleft()
                
                for new_x, new_y in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                    if new_x < 0 or new_y < 0 or new_x >= len(rooms) or new_y >= len(rooms[0]) or rooms[new_x][new_y] != 2147483647:
                        continue
                    else:
                        rooms[new_x][new_y] = distance +1
                        q.append([new_x,new_y,distance+1])
                                
        