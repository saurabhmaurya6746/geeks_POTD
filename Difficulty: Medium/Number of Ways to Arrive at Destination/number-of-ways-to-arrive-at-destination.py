import heapq

class Solution:
    def countPaths(self, V, edges):
        MOD = 10**9 + 7
        adj = [[] for _ in range(V)]
        for u, v, t in edges:
            adj[u].append((v, t))
            adj[v].append((u, t))
        
        dist = [float('inf')] * V
        ways = [0] * V
        dist[0] = 0
        ways[0] = 1
        
        heap = [(0, 0)]  # (time, node)
        
        while heap:
            time, node = heapq.heappop(heap)
            if time > dist[node]:
                continue
            for nei, wt in adj[node]:
                new_time = time + wt
                if new_time < dist[nei]:
                    dist[nei] = new_time
                    ways[nei] = ways[node]
                    heapq.heappush(heap, (new_time, nei))
                elif new_time == dist[nei]:
                    ways[nei] = (ways[nei] + ways[node]) % MOD
        
        return ways[V-1] % MOD