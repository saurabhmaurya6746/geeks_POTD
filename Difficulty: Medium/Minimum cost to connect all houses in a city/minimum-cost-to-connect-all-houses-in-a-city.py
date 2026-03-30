class Solution:
    def minCost(self, houses):
        import heapq
        
        n = len(houses)
        visited = [False] * n
        min_heap = [(0, 0)]  # (cost, house_index)
        total_cost = 0
        
        while min_heap:
            cost, u = heapq.heappop(min_heap)
            if visited[u]:
                continue
            visited[u] = True
            total_cost += cost
            
            for v in range(n):
                if not visited[v]:
                    dist = abs(houses[u][0] - houses[v][0]) + abs(houses[u][1] - houses[v][1])
                    heapq.heappush(min_heap, (dist, v))
        
        return total_cost