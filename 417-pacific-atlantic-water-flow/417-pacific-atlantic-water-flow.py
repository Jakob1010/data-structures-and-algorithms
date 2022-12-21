class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
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
            
        
        def water_flow(ocean):
            o = set()
            
            while ocean:
                i,j = ocean.popleft()
                if (i,j) not in o:
                    o.add((i,j))
                for k,l in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                    if k >= 0 and l >= 0 and k < len(heights) and l < len(heights[0]) and heights[k][l] >= heights[i][j] and (k,l) not in o:
                        ocean.append((k,l))
                        o.add((k,l))
                            
            return o
        
        pacific = water_flow(pacific)
        atlantic = water_flow(atlantic)
        
        return list(pacific.intersection(atlantic))
        