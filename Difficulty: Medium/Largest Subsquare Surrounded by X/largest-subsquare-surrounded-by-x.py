class Solution:
    def largestSubsquare(self, mat):
        n = len(mat)

        # horizontal[i][j] = consecutive X's ending at (i,j) from left
        # vertical[i][j] = consecutive X's ending at (i,j) from top
        horizontal = [[0] * n for _ in range(n)]
        vertical = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if mat[i][j] == 'X':
                    horizontal[i][j] = (horizontal[i][j-1] + 1) if j > 0 else 1
                    vertical[i][j] = (vertical[i-1][j] + 1) if i > 0 else 1

        max_size = 0

        # Try each cell as bottom-right corner
        for i in range(n):
            for j in range(n):
                # Maximum possible square size at (i,j)
                cur_max = min(horizontal[i][j], vertical[i][j])

                # Try from largest to smallest to find max
                for k in range(cur_max, max_size, -1):
                    # Check top edge and left edge
                    if (horizontal[i-k+1][j] >= k and 
                        vertical[i][j-k+1] >= k):
                        max_size = k
                        break

        return max_size