class Solution:
    def searchWord(self, mat, word):
        n = len(mat)
        m = len(mat[0])
        word_len = len(word)
        result = []

        # 8 directions: right, left, down, up, right-down, left-down, right-up, left-up
        directions = [
            (0, 1),   # right
            (0, -1),  # left
            (1, 0),   # down
            (-1, 0),  # up
            (1, 1),   # right-down
            (1, -1),  # left-down
            (-1, 1),  # right-up
            (-1, -1)  # left-up
        ]

        for i in range(n):
            for j in range(m):
                # Check if first character matches
                if mat[i][j] == word[0]:
                    # Try all 8 directions
                    for dx, dy in directions:
                        found = True

                        # Check all characters in this direction
                        for k in range(word_len):
                            new_i = i + k * dx
                            new_j = j + k * dy

                            # Check if position is within bounds
                            if new_i < 0 or new_i >= n or new_j < 0 or new_j >= m:
                                found = False
                                break

                            # Check if character matches
                            if mat[new_i][new_j] != word[k]:
                                found = False
                                break

                        if found:
                            result.append([i, j])
                            break  # Break to avoid duplicates from same starting position

        return result