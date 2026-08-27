class Solution:
    def maxArea(self, mat: list[list[int]]) -> int:
        if not mat or not mat[0]:
            return 0
    
        n, m = len(mat), len(mat[0])
        max_area = 0
    
        # For each row, compute the height of consecutive 1's ending at that row
        heights = [0] * m
    
        for i in range(n):
            # Update heights for current row
            for j in range(m):
                if mat[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0
    
            # Sort heights in descending order
            # Since we can swap columns, the order doesn't matter
            # For maximum area, we want tallest columns together
            sorted_heights = sorted(heights, reverse=True)
    
            # Calculate maximum area for current row
            for j in range(m):
                # Area = height * width
                # Width is (j + 1) because we're using first (j+1) tallest columns
                current_area = sorted_heights[j] * (j + 1)
                max_area = max(max_area, current_area)
    
        return max_area