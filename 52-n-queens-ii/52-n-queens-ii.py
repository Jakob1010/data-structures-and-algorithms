class Solution:
    def totalNQueens(self, n: int) -> int:
        cnt = 0
        
        def add_q(cols,diagonal,anti_diagonal,i,j):
            cols.add(j)
            diagonal.add(i-j)
            anti_diagonal.add(i+j)
         
        def remove_q(cols,diagonal,anti_diagonal,i,j):
            cols.remove(j)
            diagonal.remove(i-j)
            anti_diagonal.remove(i+j)
            
        
        def backtrack(cols,diagonal,anti_diagonal,k,l,q):
            if q == n:
                nonlocal cnt
                cnt += 1
            else:
                for j in range(n):
                    if j not in cols and k-j not in diagonal and k+j not in anti_diagonal:
                        add_q(cols,diagonal,anti_diagonal,k,j)
                        backtrack(cols,diagonal,anti_diagonal,k+1,l,q+1)
                        remove_q(cols,diagonal,anti_diagonal,k,j)
                            
        backtrack(set(),set(),set(),0,0,0)                            
        return cnt