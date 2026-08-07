class Solution:
    def countFriendsPairings(self, n: int) -> int:
        # code here
        if n <= 1:
            return 1
        
        # DP array to store results
        dp = [0] * (n + 1)
        dp[0] = 1  # base case: 0 friends
        dp[1] = 1  # base case: 1 friend
        
        # Fill DP array using recurrence relation
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + (i-1) * dp[i-2]
        
        return dp[n]