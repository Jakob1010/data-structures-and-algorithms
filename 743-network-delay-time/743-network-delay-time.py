class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        costs = [float('inf')] * n
        costs[k-1] = 0
        edges = {}
        max_distance = 0
        q = deque([(k,0)])
        
         
        # direct access to outoing edges 
        # and costsfor all nodes
        for u,v,c in times:
            if u in edges:
                edges[u].append((v,c))
            else:
                edges[u] = [(v,c)]
                
        while q:
            n = len(q)
            for i in range(n):
                u,timestamp = q.popleft()
                if u in edges:
                    for v,c in edges[u]:
                        if timestamp+c < costs[v-1]:
                            q.append((v,timestamp+c))
                            costs[v-1] = timestamp+c
        
        max_cost = max(costs)
        if max_cost == float('inf'):
            return -1
        else:
            return max_cost
        