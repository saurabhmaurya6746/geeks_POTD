class Solution:
    def findMotherVertex(self, V, edges):
        # Build adjacency list
        graph = [[] for _ in range(V)]
        rev_graph = [[] for _ in range(V)]  # reverse graph
        
        for u, v in edges:
            graph[u].append(v)
            rev_graph[v].append(u)

        # DFS function
        def dfs(node, graph, visited):
            visited[node] = True
            
            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei, graph, visited)

        # Step 1: Find candidate
        visited = [False] * V
        candidate = -1

        for i in range(V):
            if not visited[i]:
                dfs(i, graph, visited)
                candidate = i

        # Step 2: Verify candidate
        visited = [False] * V
        dfs(candidate, graph, visited)

        if not all(visited):
            return -1

        # Step 3: Find smallest mother vertex
        # Any vertex that can reach candidate in reverse graph
        # and candidate reaches all nodes.
        reachable = [False] * V
        dfs(candidate, rev_graph, reachable)

        for i in range(V):
            if reachable[i]:
                return i

        return candidate