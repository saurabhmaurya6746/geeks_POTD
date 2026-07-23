class Solution:
    def canRepresentBST(self, arr):
        # Stack to keep track of nodes
        stack = []
        # Initialize root with minimum possible value
        root = -float('inf')
        
        for value in arr:
            # If current value is less than root, it violates BST property
            if value < root:
                return False
            
            # Pop from stack while stack is not empty and current value is greater
            # than the top of stack. This means we're moving to right subtree
            while stack and stack[-1] < value:
                root = stack.pop()
            
            # Push current value to stack
            stack.append(value)
        
        return True