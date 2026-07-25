class Solution:
    def maximumSum(self, mat, k):
        n = len(mat)
        
        # Handle edge case
        if n == 0 or k > n:
            return 0
        
        # Create prefix sum matrix (1-indexed for easier calculation)
        # pref[i][j] = sum of submatrix from (0,0) to (i-1,j-1)
        pref = [[0] * (n + 1) for _ in range(n + 1)]
        
        # Fill prefix sum
        for i in range(n):
            row_sum = 0
            for j in range(n):
                row_sum += mat[i][j]
                pref[i+1][j+1] = pref[i][j+1] + row_sum
        
        # Find maximum k×k sub-grid sum
        max_sum = float('-inf')
        
        for i in range(k, n + 1):
            for j in range(k, n + 1):
                # Sum of submatrix from (i-k, j-k) to (i-1, j-1)
                curr_sum = (pref[i][j] - pref[i-k][j] 
                           - pref[i][j-k] + pref[i-k][j-k])
                max_sum = max(max_sum, curr_sum)
        
        return max_sum