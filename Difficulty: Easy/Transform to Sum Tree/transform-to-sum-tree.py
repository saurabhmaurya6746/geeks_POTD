''' Structure for Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

'''
class Solution:
    def toSumTree(self, root):
        def helper(node):
            if not node:
                return 0
            left_sum = helper(node.left)
            right_sum = helper(node.right)
            old_val = node.data
            node.data = left_sum + right_sum
            return node.data + old_val
        helper(root)