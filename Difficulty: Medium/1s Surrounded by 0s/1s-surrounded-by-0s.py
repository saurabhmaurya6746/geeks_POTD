class Solution:
    def cntOnes(self, grid):
        if not grid or not grid[0]:
            return 0
            
        n = len(grid)
        m = len(grid[0])
        
        # We will use a queue to perform BFS starting from all boundary '1's
        queue = []
        
        # 1. Identify all boundary '1's and add them to the queue
        for i in range(n):
            for j in range(m):
                # Check if it's on the boundary and is a '1'
                if (i == 0 or i == n - 1 or j == 0 or j == m - 1) and grid[i][j] == 1:
                    queue.append((i, j))
                    grid[i][j] = -1  # Mark as visited/escapable
                    
        # 4-directional movement vectors (Up, Down, Left, Right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # 2. Multi-source BFS to mark all connected '1's that can escape
        while queue:
            r, c = queue.pop(0)
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # If the neighbor is within bounds and is an unvisited '1'
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                    grid[nr][nc] = -1  # Mark it as escapable
                    queue.append((nr, nc))
                    
        # 3. Count the remaining '1's that couldn't escape
        trapped_ones = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    trapped_ones += 1
                elif grid[i][j] == -1:
                    grid[i][j] = 1 # Optional: Restore the grid to its original state
                    
        return trapped_ones