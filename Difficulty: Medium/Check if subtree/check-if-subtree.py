# Definition for Node
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

class Solution:
    def isIdentical(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        return (root1.data == root2.data and 
                self.isIdentical(root1.left, root2.left) and 
                self.isIdentical(root1.right, root2.right))

    def isSubTree(self, root1, root2):
        if not root2:
            return True
        if not root1:
            return False
        if self.isIdentical(root1, root2):
            return True
        return self.isSubTree(root1.left, root2) or self.isSubTree(root1.right, root2)