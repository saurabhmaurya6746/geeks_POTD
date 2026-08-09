class Solution:
    def zigzagSequence(self, mat):
        n = len(mat)
        
        # dp for previous row
        prev_dp = [mat[0][j] for j in range(n)]
        
        for i in range(1, n):
            # Find the two largest values and their positions in prev_dp
            max1 = max2 = float('-inf')
            max1_idx = -1
            
            for j in range(n):
                if prev_dp[j] > max1:
                    max2 = max1
                    max1 = prev_dp[j]
                    max1_idx = j
                elif prev_dp[j] > max2:
                    max2 = prev_dp[j]
            
            # Current row dp
            curr_dp = [0] * n
            for j in range(n):
                # If the max value came from same column, use second max
                if j == max1_idx:
                    curr_dp[j] = mat[i][j] + max2
                else:
                    curr_dp[j] = mat[i][j] + max1
            
            prev_dp = curr_dp
        
        return max(prev_dp)