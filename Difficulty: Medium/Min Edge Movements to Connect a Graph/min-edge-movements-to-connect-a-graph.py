class Solution:
    def minEdgesReq(self, n, edges):
        from collections import defaultdict
        
        m = len(edges)
        
        # Build adjacency list, ignoring self-loops for connectivity
        graph = defaultdict(list)
        self_loops = 0
        
        for u, v in edges:
            if u == v:
                self_loops += 1
            else:
                graph[u].append(v)
                graph[v].append(u)
        
        # Total useful edges (excluding self-loops)
        useful_edges = m - self_loops
        
        # Find connected components
        visited = [False] * n
        components = []
        
        for i in range(n):
            if not visited[i]:
                vertices = set()
                stack = [i]
                visited[i] = True
                
                while stack:
                    node = stack.pop()
                    vertices.add(node)
                    
                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            stack.append(neighbor)
                
                # Count edges in this component (excluding self-loops)
                edge_count = 0
                for v in vertices:
                    for neighbor in graph[v]:
                        if v < neighbor:  # Count each edge once
                            edge_count += 1
                
                components.append((len(vertices), edge_count))
        
        num_components = len(components)
        
        # If already connected
        if num_components == 1:
            return 0
        
        # Calculate extra edges available (including self-loops)
        extra_edges = self_loops  # Self-loops can always be removed
        for vertices_count, edge_count in components:
            min_edges = max(0, vertices_count - 1)  # Need at least v-1 edges to stay connected
            extra_edges += max(0, edge_count - min_edges)
        
        # Need num_components - 1 operations
        operations_needed = num_components - 1
        
        # Total edges must be enough for spanning tree
        if m < n - 1:
            return -1
        
        # Check if we have enough extra edges
        if extra_edges >= operations_needed:
            return operations_needed
        else:
            return -1