class Solution:
    def canSplit(self, arr):
        total_sum = sum(arr)
        
        # If total sum is odd, can't split equally
        if total_sum % 2 != 0:
            return False
        
        half_sum = 0
        for num in arr:
            half_sum += num
            if half_sum == total_sum // 2:
                return True
        
        return False