class Solution:
    def count(self, n: int, m: int) -> int:
        # Precompute valid transitions for each number from 1 to m
        adj = [[] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, m + 1):
                if i % j == 0 or j % i == 0:
                    adj[i].append(j)
        
        # Base case: length 1 ke liye har number ka 1 valid array hai
        dp = [1] * (m + 1)
        
        # Length 2 se n tak DP tabulate karenge
        for _ in range(n - 1):
            next_dp = [0] * (m + 1)
            for val in range(1, m + 1):
                for prev in adj[val]:
                    next_dp[val] += dp[prev]
            dp = next_dp
            
        # Overall sum across all possible last elements (1 to m)
        return sum(dp[1:])