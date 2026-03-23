class Solution:
    def longestCycle(self, V, edges):
        # Build next-node mapping
        next_node = [-1] * V
        for u, v in edges:
            next_node[u] = v

        visited = [0] * V  # 0 = unvisited, 1 = visiting, 2 = visited
        depth = [0] * V
        ans = -1

        def dfs(node, d):
            nonlocal ans
            visited[node] = 1
            depth[node] = d
            nxt = next_node[node]
            if nxt != -1:
                if visited[nxt] == 0:
                    dfs(nxt, d + 1)
                elif visited[nxt] == 1:
                    ans = max(ans, d - depth[nxt] + 1)
            visited[node] = 2

        for i in range(V):
            if visited[i] == 0:
                dfs(i, 0)
        return ans