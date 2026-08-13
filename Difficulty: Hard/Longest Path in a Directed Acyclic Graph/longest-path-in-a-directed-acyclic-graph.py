class Solution:
    def maxDistance(self, V, src, edges):
        from collections import defaultdict
        
        # Create adjacency list
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
        
        # Function to perform topological sort using DFS
        def topologicalSort():
            visited = [False] * V
            stack = []
            
            def dfs(node):
                visited[node] = True
                for neighbor, _ in adj[node]:
                    if not visited[neighbor]:
                        dfs(neighbor)
                stack.append(node)
            
            # Call DFS for all unvisited vertices
            for i in range(V):
                if not visited[i]:
                    dfs(i)
            
            # Return reversed stack (topological order)
            return stack[::-1]
        
        # Get topological order
        topo_order = topologicalSort()
        
        # Initialize distances with INT_MIN
        INT_MIN = -2147483648  # 32-bit integer minimum
        dist = [INT_MIN] * V
        dist[src] = 0
        
        # Process vertices in topological order
        for node in topo_order:
            # If current node is reachable
            if dist[node] != INT_MIN:
                # Update distances to all neighbors
                for neighbor, weight in adj[node]:
                    if dist[neighbor] < dist[node] + weight:
                        dist[neighbor] = dist[node] + weight
        
        return dist