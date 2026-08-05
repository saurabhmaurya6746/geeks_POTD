
class Solution:
    def countSubarray(self, arr: list[int], l: int, r: int) -> int:
        # Helper function to count subarrays with sum <= target
        def count_less_equal(target: int) -> int:
            if target < 0:
                return 0
            count = 0
            current_sum = 0
            left = 0
            for right in range(len(arr)):
                current_sum += arr[right]
                # Shrink window if sum exceeds target
                while left <= right and current_sum > target:
                    current_sum -= arr[left]
                    left += 1
                # All subarrays ending at `right` with start from `left` to `right`
                count += (right - left + 1)
            return count

        # Number of subarrays with sum in [l, r]
        return count_less_equal(r) - count_less_equal(l - 1)
