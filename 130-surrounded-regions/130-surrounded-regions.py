class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        no_flip = set()
        
        
        def explore(i,j):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] == "X" or (i,j) in no_flip:
                return
            else:
                no_flip.add((i,j))
                explore(i+1,j)
                explore(i-1,j)
                explore(i,j+1)
                explore(i,j-1)
            
        # check horizontal boarders
        for i in range(len(board[0])):
            if board[0][i] == "O":
                explore(0,i)
            if board[len(board)-1][i] == "O":
                explore(len(board)-1,i)
        # check vertical borders        
        for j in range(len(board)-1):
            if board[j][0] == "O":
                explore(j,0)
            if board[j][len(board[0])-1] == "O":
                explore(j,len(board[0])-1)
                
        for i in range(1,len(board)-1):
            for j in range(1,len(board[0])-1):
                if board[i][j] == "O" and (i,j) not in no_flip:
                    board[i][j] = "X"
                    
        return board
        