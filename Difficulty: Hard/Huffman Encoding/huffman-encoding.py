import heapq

class Node:
    def __init__(self, data, idx):
        self.data = data
        self.idx = idx
        self.left = None
        self.right = None

    def __lt__(self, other):
        if self.data == other.data:
            return self.idx < other.idx
        return self.data < other.data


class Solution:
    def solve(self, root, s, ans):
        if not root:
            return
        
        if not root.left and not root.right:
            ans.append(s if s else '0')
            return
        
        self.solve(root.left, s + '0', ans)
        self.solve(root.right, s + '1', ans)

    def huffmanCodes(self, s, f):
        minHeap = []
        
        for i, freq in enumerate(f):
            heapq.heappush(minHeap, Node(freq, i))
        
        while len(minHeap) > 1:
            left = heapq.heappop(minHeap)
            right = heapq.heappop(minHeap)
            
            node = Node(left.data + right.data, min(left.idx, right.idx))
            node.left = left
            node.right = right
            
            heapq.heappush(minHeap, node)
        
        root = minHeap[0]
        ans = []
        
        self.solve(root, '', ans)
        
        return ans