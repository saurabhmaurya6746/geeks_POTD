class Solution:
    def maxSum(self, n):
        memo = {}
        
        def helper(x):
            if x == 0:
                return 0
            if x in memo:
                return memo[x]
            memo[x] = max(x, helper(x // 2) + helper(x // 3) + helper(x // 4))
            return memo[x]
        
        return helper(n)