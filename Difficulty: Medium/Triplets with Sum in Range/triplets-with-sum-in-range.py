class Solution:
   
    def countTriplets(self, arr: list[int], l: int, r: int) -> int:
        n = len(arr)
        count = 0
        
        # For each middle element
        for j in range(1, n - 1):
            # Count pairs (i, k) where i < j < k
            # and l - arr[j] <= arr[i] + arr[k] <= r - arr[j]
            
            # Create sorted arrays for left and right elements
            left_elements = sorted(arr[:j])
            right_elements = sorted(arr[j+1:])
            
            # Use two pointers to count pairs with sum in range
            target_l = l - arr[j]
            target_r = r - arr[j]
            
            # Count pairs with sum <= target_r
            count_le_r = self.countPairsLessThanOrEqual(left_elements, right_elements, target_r)
            # Count pairs with sum < target_l (i.e., <= target_l - 1)
            count_lt_l = self.countPairsLessThanOrEqual(left_elements, right_elements, target_l - 1)
            
            count += count_le_r - count_lt_l
        
        return count
    
    def countPairsLessThanOrEqual(self, left_arr, right_arr, target):
        """Count pairs (a, b) where a from left_arr, b from right_arr, and a + b <= target"""
        count = 0
        i = 0  # pointer for left_arr
        j = len(right_arr) - 1  # pointer for right_arr
        
        while i < len(left_arr) and j >= 0:
            if left_arr[i] + right_arr[j] <= target:
                # All elements from right_arr[0..j] will work with left_arr[i]
                count += (j + 1)
                i += 1
            else:
                j -= 1
        
        return count