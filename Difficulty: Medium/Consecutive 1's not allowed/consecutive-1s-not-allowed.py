class Solution:
    def countStrings(self, n):
        if n == 1:
            return 2
        if n == 2:
            return 3
        
        # dp[i] = total valid strings of length i
        dp = [0] * (n + 1)
        dp[1], dp[2] = 2, 3
        
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]