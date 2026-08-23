from collections import deque

class Solution:
    def numberOfCells(self, r: int, c: int, u: int, d: int, mat: list[list[str]]) -> int:
        if not mat or mat[r][c] == '#':
            return 0

        n, m = len(mat), len(mat[0])

        # Track minimum up and down moves to reach each cell
        min_up = [[float('inf')] * m for _ in range(n)]
        min_down = [[float('inf')] * m for _ in range(n)]

        # BFS queue: (row, col, up_moves, down_moves)
        queue = deque()
        queue.append((r, c, 0, 0))
        min_up[r][c] = 0
        min_down[r][c] = 0

        visited = set()
        visited.add((r, c))

        # Directions: left, right, up, down
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        while queue:
            row, col, up_used, down_used = queue.popleft()

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                # Check bounds and obstacles
                if (new_row < 0 or new_row >= n or 
                    new_col < 0 or new_col >= m or 
                    mat[new_row][new_col] == '#'):
                    continue

                new_up = up_used
                new_down = down_used

                # Count vertical moves
                if dr == -1:  # Moving up
                    new_up += 1
                elif dr == 1:  # Moving down
                    new_down += 1

                # Check if within limits
                if new_up > u or new_down > d:
                    continue

                # Only update if we found a strictly better path
                # A path is better if it uses fewer up moves OR fewer down moves
                if new_up < min_up[new_row][new_col] or new_down < min_down[new_row][new_col]:
                    # Update the minimums
                    if new_up < min_up[new_row][new_col]:
                        min_up[new_row][new_col] = new_up
                    if new_down < min_down[new_row][new_col]:
                        min_down[new_row][new_col] = new_down

                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col, new_up, new_down))

        return len(visited)