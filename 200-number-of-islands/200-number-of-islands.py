class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        checked = set()
        
        
        def explore_island(i,j,checked):
            if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or (i,j) in checked or grid[i][j] == "0":
                return 
            else:
                checked.add((i,j))
                for row, col in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                    explore_island(row,col,checked)
                    
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and (i,j) not in checked:
                    islands += 1
                    explore_island(i,j,checked)
                    
        return islands
        