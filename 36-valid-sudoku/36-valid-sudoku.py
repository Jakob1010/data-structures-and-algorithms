class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = set()
        col = set()
        cell = set()
        n, m = len(board), len(board[1])
        
        def get_cell_num(r,c):
            return (r//3,c//3)
        
        for i in range(n):
            for j in range(m):
                num = board[i][j]
                if num == ".":
                    continue
                    
                if (i,num) in rows:
                    return False
                else:
                    rows.add((i,num))
                    
                if (j,num) in col:
                    return False
                else:
                    col.add((j,num))
                    
                cell_num = get_cell_num(i,j)
                if (cell_num, num) in cell:
                    return False
                else:
                    cell.add((cell_num,num))
                    
        return True
        