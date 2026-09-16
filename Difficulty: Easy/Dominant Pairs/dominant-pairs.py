class Solution:
    def dominantPairs(self, arr: list[int]) -> int:
        n = len(arr)
        half = n // 2

        # Split and sort both halves
        first_half = sorted(arr[:half])
        second_half = sorted(arr[half:])

        count = 0
        j = 0  # pointer for second_half

        for x in first_half:
            # Move j while condition holds: x >= 5 * second_half[j]
            while j < half and x >= 5 * second_half[j]:
                j += 1
            count += j

        return count