class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = {}
        size = {}
        
        for u,v in edges:
            if u not in parents:
                parents[u] = u
                size[u] = 1
            if v not in parents:
                parents[v] = v
                size[v] = 1
        
        def find_parent(x):
            if parents[x] == x:
                return x
            else:
                return find_parent(parents[x])
            
        def union(x,y):
            parent_x = find_parent(x)
            parent_y = find_parent(y)
            
            if parent_x == parent_y: return True
            
            if size[parent_x] > size[parent_y]:
                parents[parent_y] = parent_x
                size[parent_x] += size[parent_y]
            else:
                parents[parent_x] = parent_y
                size[parent_y] += size[parent_x]
                
            return False
                
        for u,v in edges:
            if union(u,v):
                solution = [u,v]
        
        return solution
                
            