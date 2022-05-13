class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n
        
        def find(node):
            if parent[node] == node:
                return node
            else:
                return find(parent[node])
                
        def union(n1, n2):
            r1 = find(n1)
            r2 = find(n2)
            
            if r1 == r2:
                return 0
            
            if rank[r1] > rank[r2]:
                parent[r2] = r1
                rank[r1] += rank[r2]
            else:
                parent[r1] = r2
                rank[r2] += rank[1]
                
            return 1
        
        components = n
        for n1,n2 in edges:
            components-=union(n1,n2)
        return components