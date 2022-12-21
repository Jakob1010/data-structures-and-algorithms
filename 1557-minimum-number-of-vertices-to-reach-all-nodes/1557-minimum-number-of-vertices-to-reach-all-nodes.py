class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        rank = [0] * n
        output = []
        
        for u,v in edges:
            rank[v] += 1
            
        for node,rank in enumerate(rank):
            if rank == 0:
                output.append(node)
                
        return output
                
        