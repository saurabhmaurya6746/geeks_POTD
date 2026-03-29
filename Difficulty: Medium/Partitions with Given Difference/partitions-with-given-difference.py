class Solution:
    def countPartitions(self, arr, diff):
        total_sum = sum(arr)
        
        # sum(S1) - sum(S2) = diff
        # sum(S1) + sum(S2) = total_sum
        # => 2*sum(S1) = diff + total_sum
        if (total_sum + diff) % 2 != 0 or total_sum < diff:
            return 0
        
        target = (total_sum + diff) // 2
        n = len(arr)
        
        # DP to count subsets with given sum
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        
        for i in range(1, n + 1):
            for s in range(target + 1):
                dp[i][s] = dp[i-1][s]
                if s >= arr[i-1]:
                    dp[i][s] += dp[i-1][s - arr[i-1]]
        
        return dp[n][target]