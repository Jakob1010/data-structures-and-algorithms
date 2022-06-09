
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None: return
        
        processed = {}
        start = Node(node.val)
        q = deque([(start,node)])
        processed[start.val] = start
     
        
        while q:
            deep_copy, original = q.popleft()
            neighbors = []
            
            # set neighbors of copy graph and add neighbors to q
            for neighbor in original.neighbors:
                if neighbor.val in processed:
                    neighbors.append(processed[neighbor.val])
                else:
                    neighbor_copy = Node(neighbor.val)
                    processed[neighbor_copy.val] = neighbor_copy
                    q.append((neighbor_copy,neighbor))
                    neighbors.append(neighbor_copy)
                    
            deep_copy.neighbors = neighbors
        
        return start