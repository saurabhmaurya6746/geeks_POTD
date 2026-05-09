class Solution:
    def countSpanTree(self, n, edges):
        import numpy as np
        
        # Special cases
        if n <= 1:
            return 1
        if len(edges) == n - 1:
            return 1
        
        # Step 1: Build adjacency matrix
        adj = [[0]*n for _ in range(n)]
        for u, v in edges:
            adj[u][v] += 1
            adj[v][u] += 1
        
        # Step 2: Build Laplacian matrix
        lap = [[0]*n for _ in range(n)]
        for i in range(n):
            lap[i][i] = sum(adj[i])
            for j in range(n):
                if i != j:
                    lap[i][j] = -adj[i][j]
        
        # Step 3: Remove one row & column
        minor = [row[:-1] for row in lap[:-1]]
        
        # Step 4: Determinant gives spanning tree count
        return round(np.linalg.det(np.array(minor)))