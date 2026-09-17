from collections import deque

class Solution:
    def minimumEdgeReversal(self, edges: list[list[int]], n: int, src: int, dst: int) -> int:
        # Build adjacency list for 0-1 BFS
        # adj[u] = list of (v, weight)
        adj = [[] for _ in range(n + 1)]

        for u, v in edges:
            adj[u].append((v, 0))  # original direction, cost 0
            adj[v].append((u, 1))  # reverse direction, cost 1

        # 0-1 BFS
        INF = float('inf')
        dist = [INF] * (n + 1)
        dist[src] = 0
        dq = deque([src])

        while dq:
            u = dq.popleft()
            for v, w in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    if w == 0:
                        dq.appendleft(v)
                    else:
                        dq.append(v)

        return dist[dst] if dist[dst] != INF else -1