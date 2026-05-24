class Solution:
    def coin(self, arr):
        i = 0
        j = len(arr) - 1

        while i < j:
            # Pick the larger coin from both ends
            if arr[i] >= arr[j]:
                i += 1
            else:
                j -= 1

        return arr[i]