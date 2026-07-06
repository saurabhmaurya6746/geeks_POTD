class Solution:
    def maxPathSum(self, a, b):
        i, j = 0, 0
        m, n = len(a), len(b)
        
        sum_a, sum_b = 0, 0
        total_max_sum = 0
        
        while i < m and j < n:
            if a[i] < b[j]:
                sum_a += a[i]
                i += 1
            elif b[j] < a[i]:
                sum_b += b[j]
                j += 1
            else:  # Common element found
                total_max_sum += max(sum_a, sum_b) + a[i]
                sum_a, sum_b = 0, 0
                i += 1
                j += 1
                
        # Add remaining elements of a[]
        while i < m:
            sum_a += a[i]
            i += 1
            
        # Add remaining elements of b[]
        while j < n:
            sum_b += b[j]
            j += 1
            
        total_max_sum += max(sum_a, sum_b)
        
        return total_max_sum