class Solution:
    def minSubsets(self, arr):
        # Sort the array to group consecutive numbers together
        arr.sort()
        
        # At least one subset is needed
        count = 1
        
        # Iterate through the array and count breaks in consecutiveness
        for i in range(1, len(arr)):
            # If current element is not consecutive to previous, we need a new subset
            if arr[i] != arr[i-1] + 1:
                count += 1
                
        return count