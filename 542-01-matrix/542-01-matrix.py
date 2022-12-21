class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        def BFS(q,visited):
            while q:
                n = len(q)
                for i in range(n):
                    x,y = q.popleft()
                    for x_new, y_new in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                        if x_new < 0 or y_new < 0 or x_new >= len(mat) or y_new >= len(mat[0]) or (x_new,y_new) in visited:
                            continue
                        else:
                            mat[x_new][y_new] = mat[x][y] + 1
                            q.append((x_new,y_new))
                            visited.add((x_new,y_new))
                
        q = deque()   
        visited = set()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))
                    
        BFS(q,visited)
                
        return mat