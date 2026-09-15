class Solution:
    def getCount(self, root, k):
        if not root:
            return 0

        # Collect costs (levels) of all leaf nodes using BFS/level-order
        costs = []
        queue = [(root, 1)]  # (node, level)

        while queue:
            node, level = queue.pop(0)

            # Check if leaf node
            if not node.left and not node.right:
                costs.append(level)
            else:
                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))

        # Sort costs to pick cheapest leaves first
        costs.sort()

        # Greedily pick leaves within budget
        count = 0
        total = 0
        for cost in costs:
            if total + cost <= k:
                total += cost
                count += 1
            else:
                break

        return count