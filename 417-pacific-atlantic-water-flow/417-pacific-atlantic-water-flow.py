class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        pacific = deque()
        atlantic = deque()
        
        # horizontal
        for i in range(len(heights[0])):
            pacific.append((0,i))
            atlantic.append((len(heights)-1,i))
         
        # vertical
        for j in range(len(heights)):
            pacific.append((j,0))
            atlantic.append((j,len(heights[0])-1))
            
        def BFS(q):
            reachable = set()
            while q:
                x,y = q.popleft()
                reachable.add((x,y))
                if (x,y) not in reachable:
                    reachable.add((x,y))
                # add all adjacent nodes 
                # with heigh < current to q
                for new_x, new_y in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                    if new_x < 0 or new_y < 0 or new_x >= len(heights) or new_y >= len(heights[0]) or heights[x][y] > heights[new_x][new_y] or (new_x,new_y) in reachable:
                        continue
                    else:
                        q.append((new_x,new_y))                   
            return reachable
                            
        pacific = BFS(pacific)
        atlantic = BFS(atlantic)
        pacific_atlantic = pacific.intersection(atlantic)
        return list(pacific_atlantic)