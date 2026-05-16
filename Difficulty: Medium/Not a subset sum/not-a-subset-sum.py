class Solution:
    def findSmallest(self, arr):
        arr.sort()
        
        res = 1   # smallest value we are trying to form
        
        for num in arr:
            if num > res:
                return res
            
            res += num
        
        return res