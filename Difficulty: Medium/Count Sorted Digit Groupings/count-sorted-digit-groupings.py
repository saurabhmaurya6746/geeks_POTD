class Solution:
    def validGroups(self, s):
        n = len(s)
        
        # Prefix sum for quick digit sum calculation
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + int(s[i])
        
        from functools import lru_cache
        
        # dfs(index, prev_sum)
        @lru_cache(None)
        def dfs(idx, prev):
            if idx == n:
                return 1
            
            ans = 0
            
            # Try every possible substring
            for j in range(idx, n):
                curr_sum = prefix[j + 1] - prefix[idx]
                
                # Non-decreasing condition
                if curr_sum >= prev:
                    ans += dfs(j + 1, curr_sum)
            
            return ans
        
        return dfs(0, 0)