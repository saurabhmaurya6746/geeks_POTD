class Solution:
    def findWays(self, grid):
        n = len(grid)
        MOD = 10**9 + 7
        
        # dp_paths[i][j] = number of paths from (i,j) to (n-1,n-1)
        # dp_max[i][j] = maximum adventure from (i,j) to (n-1,n-1)
        dp_paths = [[0] * n for _ in range(n)]
        dp_max = [[0] * n for _ in range(n)]
        
        # Base case: destination cell
        dp_paths[n-1][n-1] = 1
        dp_max[n-1][n-1] = grid[n-1][n-1]
        
        # Process from bottom-right to top-left
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == n-1 and j == n-1:
                    continue
                
                paths = 0
                max_adv = 0
                
                # Check right move (if allowed)
                if j + 1 < n and (grid[i][j] == 1 or grid[i][j] == 3):
                    if dp_paths[i][j+1] > 0:
                        paths = (paths + dp_paths[i][j+1]) % MOD
                        max_adv = max(max_adv, dp_max[i][j+1])
                
                # Check down move (if allowed)
                if i + 1 < n and (grid[i][j] == 2 or grid[i][j] == 3):
                    if dp_paths[i+1][j] > 0:
                        paths = (paths + dp_paths[i+1][j]) % MOD
                        max_adv = max(max_adv, dp_max[i+1][j])
                
                dp_paths[i][j] = paths
                if paths > 0:
                    dp_max[i][j] = grid[i][j] + max_adv
                else:
                    dp_max[i][j] = 0
        
        return [dp_paths[0][0] % MOD, dp_max[0][0]]