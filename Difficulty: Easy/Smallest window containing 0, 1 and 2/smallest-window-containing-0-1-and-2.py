class Solution:
    def smallestSubstring(self, s: str) -> int:
        n = len(s)
        count = {'0': 0, '1': 0, '2': 0}
        left = 0
        min_len = float('inf')
        
        for right in range(n):
            count[s[right]] += 1
            while all(count[c] > 0 for c in '012'):
                min_len = min(min_len, right - left + 1)
                count[s[left]] -= 1
                left += 1
        
        return min_len if min_len != float('inf') else -1