class Solution:
    def articulationPoints(self, V, edges):
        from collections import defaultdict
        
        # Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        disc = [-1] * V      # discovery time
        low = [-1] * V       # low-link values
        parent = [-1] * V
        ap = set()           # articulation points
        time = [0]           # mutable counter
        
        def dfs(u):
            children = 0
            disc[u] = low[u] = time[0]
            time[0] += 1
            
            for v in graph[u]:
                if disc[v] == -1:  # if v is not visited
                    parent[v] = u
                    children += 1
                    dfs(v)
                    low[u] = min(low[u], low[v])
                    
                    # root case
                    if parent[u] == -1 and children > 1:
                        ap.add(u)
                    # non-root case
                    if parent[u] != -1 and low[v] >= disc[u]:
                        ap.add(u)
                elif v != parent[u]:  # back edge
                    low[u] = min(low[u], disc[v])
        
        for i in range(V):
            if disc[i] == -1:
                dfs(i)
        
        return sorted(ap) if ap else [-1]