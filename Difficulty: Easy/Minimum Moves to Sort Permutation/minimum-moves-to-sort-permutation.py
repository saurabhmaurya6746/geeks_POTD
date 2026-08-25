 
class Solution:
    def minMoves(self, arr):
        n = len(arr)
    
        # Create a position map: value -> index in array
        pos = {}
        for i, val in enumerate(arr):
            pos[val] = i
    
        # Find the longest consecutive sequence in correct relative order
        max_len = 1
        curr_len = 1
    
        # Check for consecutive numbers starting from 1
        for i in range(1, n):
            # If i+1 appears after i in the array, they're in correct order
            if pos[i] < pos[i + 1]:
                curr_len += 1
                max_len = max(max_len, curr_len)
            else:
                curr_len = 1
    
        # Elements not in the longest consecutive sequence need to be moved
        return n - max_len