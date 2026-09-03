class Solution:
    def maxDiffSum(self, arr):
        n = len(arr)
        if n <= 1:
            return 0
    
        # dp[i][0] = max sum ending at i with arr[i] unchanged
        # dp[i][1] = max sum ending at i with arr[i] = 1
        dp_keep = 0  # keeping current element as original
        dp_change = 0  # changing current element to 1
    
        for i in range(1, n):
            # Previous values
            prev_keep = dp_keep
            prev_change = dp_change
    
            # Current element kept as original
            # Previous element could have been kept or changed
            dp_keep = max(
                prev_keep + abs(arr[i] - arr[i-1]),
                prev_change + abs(arr[i] - 1)
            )
    
            # Current element changed to 1
            # Previous element could have been kept or changed
            dp_change = max(
                prev_keep + abs(1 - arr[i-1]),
                prev_change + abs(1 - 1)
            )
    
        return max(dp_keep, dp_change)