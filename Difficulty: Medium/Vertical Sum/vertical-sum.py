# Structure of binary tree node
'''
class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None
'''

from collections import defaultdict

class Solution:
    def verticalSum(self, root):
        mp = defaultdict(int)
        
        def dfs(node, hd):
            if not node:
                return
            
            mp[hd] += node.data
            
            dfs(node.left, hd - 1)
            dfs(node.right, hd + 1)
        
        dfs(root, 0)
        
        return [mp[i] for i in sorted(mp)]