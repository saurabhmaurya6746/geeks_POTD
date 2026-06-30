import bisect

class Solution:
    def minInsAndDel(self, a, b):
        # Since b has distinct elements, we can map each element in b to its index
        b_idx = {val: i for i, val in enumerate(b)}
        
        # Filter 'a' to include only elements present in 'b', replaced by their index in 'b'
        # This transforms the problem into finding the Longest Increasing Subsequence (LIS)
        filtered_a = [b_idx[x] for x in a if x in b_idx]
        
        # Find the length of the Longest Increasing Subsequence (LIS) in filtered_a
        lis = []
        for x in filtered_a:
            idx = bisect.bisect_left(lis, x)
            if idx == len(lis):
                lis.append(x)
            else:
                lis[idx] = x
                
        len_lis = len(lis)
        
        # Minimum operations = (elements to delete from a) + (elements to insert from b)
        # Total deletions = len(a) - len_lis
        # Total insertions = len(b) - len_lis
        return len(a) + len(b) - 2 * len_lis