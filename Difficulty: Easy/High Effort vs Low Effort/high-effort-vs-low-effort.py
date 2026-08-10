class Solution:
    def maxTask(self, h: list[int], l: list[int]) -> int:
        n = len(h)
        
        # dp[i][0] = max tasks up to day i if we rest on day i
        # dp[i][1] = max tasks up to day i if we do low-effort task on day i
        # dp[i][2] = max tasks up to day i if we do high-effort task on day i
        
        # For day 0 (first day)
        rest = 0  # no task on day 0
        low = l[0]  # low-effort task on day 0
        high = h[0]  # high-effort task on day 0 (allowed on first day)
        
        # Process remaining days
        for i in range(1, n):
            # If we rest today, we can come from any state yesterday
            new_rest = max(rest, low, high)
            
            # If we do low-effort today, we can come from any state yesterday
            new_low = max(rest, low, high) + l[i]
            
            # If we do high-effort today, we can only come from rest yesterday
            new_high = rest + h[i]
            
            # Update states for next iteration
            rest, low, high = new_rest, new_low, new_high
        
        # Return the maximum of all possible states on the last day
        return max(rest, low, high)