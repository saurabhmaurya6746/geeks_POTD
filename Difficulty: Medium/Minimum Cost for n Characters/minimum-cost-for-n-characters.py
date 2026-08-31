class Solution:
    def minCost(self, n: int, i: int, d: int, c: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
    
        for x in range(1, n + 1):
            # Option 1: Insert from x-1
            dp[x] = min(dp[x], dp[x - 1] + i)
    
            # Option 2: If x is even, copy from x/2
            if x % 2 == 0:
                dp[x] = min(dp[x], dp[x // 2] + c)
            else:
                # If x is odd, we can:
                # a) Go to (x+1)/2, copy to x+1, delete to x
                if (x + 1) // 2 <= x:
                    dp[x] = min(dp[x], dp[(x + 1) // 2] + c + d)
                # b) Go to (x-1)/2, copy to x-1, insert to x
                if (x - 1) // 2 >= 0:
                    dp[x] = min(dp[x], dp[(x - 1) // 2] + c + i)
    
        return dp[n]