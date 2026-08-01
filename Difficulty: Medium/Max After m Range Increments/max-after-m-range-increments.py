class Solution:
    def findMax(self, n, a, b, k):
        # Difference array of size n
        diff = [0] * n
        
        m = len(a)
        
        # Apply range updates in O(1) time each
        for i in range(m):
            l = a[i]
            r = b[i]
            val = k[i]
            
            diff[l] += val
            if r + 1 < n:
                diff[r + 1] -= val
                
        # Calculate prefix sum to find the actual array values and track maximum
        max_val = 0
        current_sum = 0
        
        for val in diff:
            current_sum += val
            if current_sum > max_val:
                max_val = current_sum
                
        return max_val