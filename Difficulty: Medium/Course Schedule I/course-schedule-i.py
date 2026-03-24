from collections import deque

class Solution:
    def canFinish(self, n, prerequisites):
        # Build adjacency list
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        
        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1
        
        # Queue for courses with no prerequisites
        q = deque([i for i in range(n) if indegree[i] == 0])
        count = 0
        
        while q:
            node = q.popleft()
            count += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return count == n
        