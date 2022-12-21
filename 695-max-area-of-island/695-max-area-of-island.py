class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        checked = set()
        
        def get_island_area(i,j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0 or (i,j) in checked:
                return 0
            
            area = 1
            checked.add((i,j))
            for row, col in ((i+1,j), (i-1,j), (i,j+1), (i,j-1)):
                area += get_island_area(row,col)
            return area
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in checked:
                    max_area = max(max_area,get_island_area(i,j))
                    
        return max_area
            