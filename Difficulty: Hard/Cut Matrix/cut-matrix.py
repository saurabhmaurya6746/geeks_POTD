class Solution:
    def findWays(self, matrix, k):
        MOD = 10**9 + 7
        n = len(matrix)
        m = len(matrix[0])
        
        # Prefix sum to check if submatrix has at least one 1
        pref = [[0]*(m+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                pref[i+1][j+1] = pref[i+1][j] + pref[i][j+1] - pref[i][j] + matrix[i][j]
        
        def has_one(r1, c1, r2, c2):
            if r1 > r2 or c1 > c2:
                return False
            total = pref[r2+1][c2+1] - pref[r1][c2+1] - pref[r2+1][c1] + pref[r1][c1]
            return total > 0
        
        # Precompute first_r[i][j] = first row >= i such that submatrix (i,j) to (row, m-1) has a 1
        first_r = [[n]*m for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if has_one(i, j, i, m-1):
                    first_r[i][j] = i
                elif i+1 < n:
                    first_r[i][j] = first_r[i+1][j]
                else:
                    first_r[i][j] = n  # no valid row
        
        # Precompute first_c[i][j] = first column >= j such that submatrix (i,j) to (n-1, col) has a 1
        first_c = [[m]*m for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if has_one(i, j, n-1, j):
                    first_c[i][j] = j
                elif j+1 < m:
                    first_c[i][j] = first_c[i][j+1]
                else:
                    first_c[i][j] = m  # no valid column
        
        # dp[i][j][p] = ways for submatrix from (i,j) to bottom-right with p pieces
        dp = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]
        
        # Base case: p = 1
        for i in range(n):
            for j in range(m):
                if has_one(i, j, n-1, m-1):
                    dp[i][j][1] = 1
        
        # Fill for p from 2 to k
        for p in range(2, k+1):
            # Prefix sums of dp from previous layer
            # hpref[i][j] = sum of dp[i][j][p-1] from i to n-1
            hpref = [[0]*(m+1) for _ in range(n+1)]
            for i in range(n-1, -1, -1):
                for j in range(m-1, -1, -1):
                    hpref[i][j] = (hpref[i+1][j] + dp[i][j][p-1]) % MOD
            
            # vpref[i][j] = sum of dp[i][j][p-1] from j to m-1
            vpref = [[0]*(m+1) for _ in range(n+1)]
            for i in range(n-1, -1, -1):
                for j in range(m-1, -1, -1):
                    vpref[i][j] = (vpref[i][j+1] + dp[i][j][p-1]) % MOD
            
            for i in range(n):
                for j in range(m):
                    total = 0
                    
                    # Horizontal cuts
                    r = first_r[i][j]
                    if r < n-1:  # valid cut exists
                        # r is the first row where top part has a 1
                        # We can cut at r, r+1, ..., n-2
                        # For each cut at row x, add dp[x+1][j][p-1]
                        # So sum dp[x+1][j][p-1] for x from r to n-2
                        # = sum dp[row][j][p-1] for row from r+1 to n-1
                        total = (total + hpref[r+1][j]) % MOD
                    
                    # Vertical cuts
                    c = first_c[i][j]
                    if c < m-1:  # valid cut exists
                        # c is the first column where left part has a 1
                        # We can cut at c, c+1, ..., m-2
                        # For each cut at column x, add dp[i][x+1][p-1]
                        # = sum dp[i][col][p-1] for col from c+1 to m-1
                        total = (total + vpref[i][c+1]) % MOD
                    
                    dp[i][j][p] = total % MOD
        
        return dp[0][0][k] % MOD