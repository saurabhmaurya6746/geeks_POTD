from collections import deque, Counter

class Solution:
    def areAnagrams(self, root1, root2):
        # If both are None, they're anagrams
        if not root1 and not root2:
            return True
        # If only one is None, they're not anagrams
        if not root1 or not root2:
            return False

        # BFS queues for both trees
        q1 = deque([root1])
        q2 = deque([root2])

        while q1 and q2:
            # Check if current level sizes match
            size1 = len(q1)
            size2 = len(q2)

            if size1 != size2:
                return False

            # Collect values at current level for both trees
            level1_values = []
            level2_values = []

            # Process entire level for tree1
            for _ in range(size1):
                node = q1.popleft()
                level1_values.append(node.data)

                if node.left:
                    q1.append(node.left)
                if node.right:
                    q1.append(node.right)

            # Process entire level for tree2
            for _ in range(size2):
                node = q2.popleft()
                level2_values.append(node.data)

                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)

            # Check if current level values are anagrams
            if Counter(level1_values) != Counter(level2_values):
                return False

        # If one tree has more levels than the other
        if q1 or q2:
            return False

        return True