class Solution:
    def minDeletions(self, arr):
        # Find length of Longest Increasing Subsequence
        n = len(arr)
        
        # Using patience sorting for O(n log n) LIS
        lis = []
        for num in arr:
            # Binary search to find position
            left, right = 0, len(lis)
            while left < right:
                mid = (left + right) // 2
                if lis[mid] < num:
                    left = mid + 1
                else:
                    right = mid
                    
            # If position is at end, append else replace
            if left == len(lis):
                lis.append(num)
            else:
                lis[left] = num
        
        lis_length = len(lis)
        
        # Minimum deletions = total elements - LIS length
        return n - lis_length