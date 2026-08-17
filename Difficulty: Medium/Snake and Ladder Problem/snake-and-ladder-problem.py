from collections import deque

class Solution:
    def minThrows(self, n, lad, sn):
        # Total number of cells on the board
        total_cells = n * n

        # Create mapping for snakes and ladders
        jump = [-1] * (total_cells + 1)

        # Process ladders
        for i in range(0, len(lad), 2):
            start, end = lad[i], lad[i + 1]
            jump[start] = end

        # Process snakes
        for i in range(0, len(sn), 2):
            start, end = sn[i], sn[i + 1]
            jump[start] = end

        # BFS initialization
        queue = deque([(1, 0)])  # (current_position, dice_throws)
        visited = [False] * (total_cells + 1)
        visited[1] = True

        # BFS traversal
        while queue:
            current, throws = queue.popleft()

            # Check if we reached the destination
            if current == total_cells:
                return throws

            # Try all possible dice outcomes (1 to 6)
            for dice_value in range(1, 7):
                next_pos = current + dice_value

                # Ensure we don't go beyond the board
                if next_pos <= total_cells:
                    # Apply snake or ladder if present
                    if jump[next_pos] != -1:
                        next_pos = jump[next_pos]

                    # Add to queue if not visited
                    if not visited[next_pos]:
                        visited[next_pos] = True
                        queue.append((next_pos, throws + 1))

        # Destination unreachable
        return -1
  