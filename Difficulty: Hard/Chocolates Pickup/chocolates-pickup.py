class Solution:
    def maxChocolate(self, grid):
        n, m = len(grid), len(grid[0])
        
        # dp[row][col1][col2]
        dp = [[[0] * m for _ in range(m)] for _ in range(n)]
        
        # Base case: last row
        for c1 in range(m):
            for c2 in range(m):
                if c1 == c2:
                    dp[n-1][c1][c2] = grid[n-1][c1]
                else:
                    dp[n-1][c1][c2] = grid[n-1][c1] + grid[n-1][c2]
        
        # Bottom-up calculation
        for row in range(n-2, -1, -1):
            for c1 in range(m):
                for c2 in range(m):
                    max_choco = 0
                    for dc1 in (-1, 0, 1):
                        for dc2 in (-1, 0, 1):
                            nc1, nc2 = c1 + dc1, c2 + dc2
                            if 0 <= nc1 < m and 0 <= nc2 < m:
                                max_choco = max(max_choco, dp[row+1][nc1][nc2])
                    if c1 == c2:
                        dp[row][c1][c2] = grid[row][c1] + max_choco
                    else:
                        dp[row][c1][c2] = grid[row][c1] + grid[row][c2] + max_choco
        
        return dp[0][0][m-1]