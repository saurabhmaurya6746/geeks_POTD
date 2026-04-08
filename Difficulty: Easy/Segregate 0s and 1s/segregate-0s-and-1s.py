class Solution:
    def segregate0and1(self, arr):
        left, right = 0, len(arr) - 1
        
        while left < right:
            # Move left pointer forward if it's already 0
            while left < right and arr[left] == 0:
                left += 1
            # Move right pointer backward if it's already 1
            while left < right and arr[right] == 1:
                right -= 1
            # Swap misplaced 1 on left with 0 on right
            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        return arr