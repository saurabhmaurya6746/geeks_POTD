class Solution:

    def maxFruits(self, arr: list[int], m: int) -> int:
        n = len(arr)
    
        if m >= n:
            return sum(arr)
    
        left = 0
        total = 0
        ans = 0
    
        for i in range(n + m - 1):
    
            total += arr[i % n]
    
            if i - left + 1 > m:
                total -= arr[left % n]
                left += 1
    
            if i - left + 1 == m:
                ans = max(ans, total)
    
        return ans