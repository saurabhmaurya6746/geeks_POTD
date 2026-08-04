class Solution:
    def countPairs(self, arr: list[int], k: int) -> int:
        # Step 1: Sort the array
        arr.sort()
        
        n = len(arr)
        count = 0
        i = 0
        
        # Step 2: Two-pointer expansion
        for j in range(n):
            # Shrink window from the left until difference is strictly less than k
            while arr[j] - arr[i] >= k:
                i += 1
            
            # Add all valid pairs ending at index j
            count += (j - i)
            
        return count