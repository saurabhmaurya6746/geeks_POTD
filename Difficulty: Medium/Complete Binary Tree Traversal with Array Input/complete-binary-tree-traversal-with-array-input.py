class Solution:
    def levelSort(self, arr):
        n = len(arr)
        result = []
        start = 0
        level = 0
        
        while start < n:
            nodes_at_level = 1 << level  # 2^level
            end = min(start + nodes_at_level, n)
            
            # Sort current level nodes
            level_nodes = sorted(arr[start:end])
            result.append(level_nodes)
            
            start = end
            level += 1
        
        return result