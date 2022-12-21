class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parents = [i for i in range(n)]
        
        size = [1] * n
        
        def find(x):
            if parents[x] == x:
                return x
            else:
                return find(parents[x])
            
        def union(x, y):
            parent_x = find(x)
            parent_y = find(y)
            
            # already in same set
            if parent_x == parent_y: 
                return False
        
            if size[parent_x] > size[parent_y]:
                parents[parent_y] = parent_x
                size[parent_x] += size[parent_y]
            else:
                parents[parent_x] = parent_y
                size[parent_y] += size[parent_x]
                
            return True
          
        needed = n-1
        for x, y in edges:
            if union(x,y):
                needed -= 1
            else:
                return False
            
        return needed == 0