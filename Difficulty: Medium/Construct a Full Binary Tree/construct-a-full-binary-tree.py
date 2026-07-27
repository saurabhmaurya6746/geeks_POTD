''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

# Definition for a Binary Tree Node
 
class Solution:
    def constructBinaryTree(self, pre, preMirror):
        n = len(pre)
        # Store index of preMirror elements for O(1) lookups
        mirror_map = {val: i for i, val in enumerate(preMirror)}
        
        self.preIndex = 0

        def helper(l, h):
            if l > h or self.preIndex >= n:
                return None

            # Create root node from current preIndex
            root = Node(pre[self.preIndex])
            self.preIndex += 1

            # Base case: if single element or leaf node
            if l == h:
                return root

            # Search the next element of pre[] in preMirror[]
            # pre[self.preIndex] is the left child of root
            if self.preIndex < n:
                idx = mirror_map[pre[self.preIndex]]

                # Left child subtree lies in [idx, h] range in preMirror
                # Right child subtree lies in [l + 1, idx - 1] range in preMirror
                if idx <= h:
                    root.left = helper(idx, h)
                    root.right = helper(l + 1, idx - 1)

            return root

        return helper(0, n - 1)