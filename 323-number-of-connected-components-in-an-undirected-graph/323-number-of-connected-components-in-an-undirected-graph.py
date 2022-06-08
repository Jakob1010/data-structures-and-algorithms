class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = {}
        size = [1] * n
        
        for i in range(n):
            parents[i] = i
        
        def find(x):
            if parents[x] == x:
                return x
            else:
                return find(parents[x])
            
        def union(x,y):
            parent_x = find(x)
            parent_y = find(y)
            
            if parent_x == parent_y: return False          # already same subset
            
            if size[parent_x] > size[parent_y]:
                parents[parent_y] = parent_x
                size[parent_x] += size[parent_y]
            else:
                parents[parent_x] = parent_y
                size[parent_y] += size[parent_x]
            
            return True
        
        components = n
        for x,y in edges:
            if union(x,y):
                components -= 1
        return components
        
                