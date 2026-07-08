class Solution:
    def countCoordinates(self, mat):
        if not mat or not mat[0]:
            return 0
            
        n, m = len(mat), len(mat[0])
        
        reach_P = [[False] * m for _ in range(n)]
        reach_Q = [[False] * m for _ in range(n)]
        
        queue_P = []
        queue_Q = []
        
        # Station P covers top boundary (row 0) and left boundary (col 0)
        for j in range(m):
            reach_P[0][j] = True
            queue_P.append((0, j))
        for i in range(1, n):
            reach_P[i][0] = True
            queue_P.append((i, 0))
            
        # Station Q covers bottom boundary (row n-1) and right boundary (col m-1)
        for j in range(m):
            reach_Q[n-1][j] = True
            queue_Q.append((n-1, j))
        for i in range(n-1):
            reach_Q[i][m-1] = True
            queue_Q.append((i, m-1))
            
        def bfs(queue, reach_matrix):
            head = 0
            while head < len(queue):
                r, c = queue[head]
                head += 1
                
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and not reach_matrix[nr][nc]:
                        # Signal can move from nr, nc to r, c if mat[nr][nc] >= mat[r][c]
                        if mat[nr][nc] >= mat[r][c]:
                            reach_matrix[nr][nc] = True
                            queue.append((nr, nc))
                            
        bfs(queue_P, reach_P)
        bfs(queue_Q, reach_Q)
        
        count = 0
        for i in range(n):
            for j in range(m):
                if reach_P[i][j] and reach_Q[i][j]:
                    count += 1
                    
        return count