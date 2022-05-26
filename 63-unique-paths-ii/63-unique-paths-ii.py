class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = {}
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        
        def explore_field(x,y):
            if (x,y) in memo:
                return memo[(x,y)]
            if x < 0 or y < 0 or x>=n or y>=m or obstacleGrid[x][y]==1:
                return 0
            if (x,y) == (n-1,m-1):
                return 1
            
            paths_found = 0
            for x_new, y_new in ((x+1,y),(x,y+1)):
                paths_found += explore_field(x_new,y_new)
            memo[(x,y)] = paths_found
            
            return paths_found
        
        return explore_field(0,0)
            