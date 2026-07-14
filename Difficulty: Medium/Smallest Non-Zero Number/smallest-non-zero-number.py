class Solution:
    def find(self, arr):
        # We work backwards from the end of the array to find the minimum required x
        # to ensure x never becomes negative at any point.
        x = 0
        for num in reversed(arr):
            # In the forward transition:
            # If x > num:  x_new = x + (x - num) = 2x - num
            # If x <= num: x_new = x - (num - x) = 2x - num
            # Both cases simplify to: x_new = 2x - num
            # Working backwards: x = (x_new + num) / 2
            # Since x must be an integer and we want the minimum valid starting point,
            # we take the ceiling of the division: (x + num + 1) // 2
            x = (x + num + 1) // 2
            
        return x