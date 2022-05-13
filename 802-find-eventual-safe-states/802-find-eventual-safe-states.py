class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        outgoing = {}
        incoming = {}
        top_sort = []
        terminate_nodes = []
        
        for i,edges in enumerate(graph):
            if len(edges) == 0:
                terminate_nodes.append(i)
                top_sort.append(i)
            else:
                for edge in edges:
                    if i in outgoing:
                        outgoing[i].add(edge)
                    else:
                        outgoing[i] = set()
                        outgoing[i].add(edge)

                    if edge in incoming:
                        incoming[edge].append(i)
                    else:
                        incoming[edge] = [i]

                
        while top_sort:
            node = top_sort.pop(0)
            if node in incoming:
                for adj_node in incoming[node]:
                    outgoing[adj_node].remove(node)
                    if len(outgoing[adj_node]) == 0:
                        top_sort.append(adj_node)
                        terminate_nodes.append(adj_node)
                
                
                
        return sorted(terminate_nodes)