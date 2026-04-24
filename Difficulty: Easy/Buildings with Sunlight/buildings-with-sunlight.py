class Solution:
    def visibleBuildings(self, arr):
        max_height = 0
        count = 0
        
        for h in arr:
            if h >= max_height:  # allow equal height too
                count += 1
                max_height = h
        return count