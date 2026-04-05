class Solution:
    def totalWays(self, arr, target):
        total_sum = sum(arr)
        
        # Convert to subset sum problem
        if (total_sum + target) % 2 != 0 or total_sum < abs(target):
            return 0
        
        subset_sum = (total_sum + target) // 2
        
        dp = [0] * (subset_sum + 1)
        dp[0] = 1
        
        for num in arr:
            for s in range(subset_sum, num - 1, -1):
                dp[s] += dp[s - num]
        
        return dp[subset_sum]