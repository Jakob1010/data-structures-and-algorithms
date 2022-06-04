class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        rows = set()
        cols = set()
        d_1 = set() # (0,0) -> (n-1,n-1)
        d_2 = set() # (0,n-1) -> (n-1,0)
        
        temp = [["." for i in range(n)] for j in range(n)] 
        output = []
        
        def backtrack(i,j,q,temp):
            if q == n:
                output.append(deepcopy(temp))
            else:   
                for k in range(i,n):
                    for l in range(j,n):
                        if k in rows:
                            break
                        if l in cols or (k-l) in d_1 or (k+l) in d_2:
                            continue
                        else:
                            temp[k][l] = "Q"
                            rows.add(k)
                            cols.add(l)
                            d_1.add(k-l)
                            d_2.add(k+l)
                            backtrack(k+1,0,q+1,temp)
                            temp[k][l] = "."
                            rows.remove(k)
                            cols.remove(l)
                            d_1.remove(k-l)
                            d_2.remove(k+l)
                        
                        
                    
        
        backtrack(0,0,0,temp)
        output_joined = []
        for solution in output:
            sol = []
            for row in solution:
                sol.append("".join(row))
            output_joined.append(sol)
        return output_joined
            
        
        
            
        