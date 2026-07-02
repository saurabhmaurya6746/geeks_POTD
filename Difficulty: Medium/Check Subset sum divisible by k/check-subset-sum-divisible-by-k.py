class Solution:
    def divisibleByK(self, arr: list, k: int) -> bool:
        # dp[i] will store True if a subset sum with remainder 'i' is possible
        dp = [False] * k
        
        for num in arr:
            rem = num % k
            
            # If the number itself is divisible by k, we found our subset
            if rem == 0:
                return True
                
            # Temporary list to store new remainders formed in this step
            next_dp = dp[:]
            
            # Check all existing remainders we have formed so far
            for i in range(k):
                if dp[i]:
                    new_rem = (i + rem) % k
                    # If adding the current number creates a sum divisible by k
                    if new_rem == 0:
                        return True
                    next_dp[new_rem] = True
            
            # Also mark the remainder of the current element itself as reachable
            next_dp[rem] = True
            dp = next_dp
            
        return False