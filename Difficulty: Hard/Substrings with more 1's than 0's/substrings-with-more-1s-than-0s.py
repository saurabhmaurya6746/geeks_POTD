class Solution:
    def countSubstring(self, s):
        n = len(s)
        
        # Fenwick Tree (Binary Indexed Tree) implementation
        # Maximum possible prefix sum is n, minimum is -n.
        # Total range size = 2 * n + 1. We shift indices by +n to avoid negative indices.
        OFFSET = n + 1
        bit = [0] * (2 * n + 5)
        
        def update(idx, val):
            while idx < len(bit):
                bit[idx] += val
                idx += idx & (-idx)
                
        def query(idx):
            s_sum = 0
            while idx > 0:
                s_sum += bit[idx]
                idx -= idx & (-idx)
            return s_sum

        ans = 0
        curr_sum = 0
        
        # Initially, prefix sum before starting the string is 0.
        # Store its count in BIT.
        update(0 + OFFSET, 1)
        
        for char in s:
            # 1 -> +1, 0 -> -1
            if char == '1':
                curr_sum += 1
            else:
                curr_sum -= 1
                
            # We need previous prefix sums < curr_sum
            # So we query for counts from total minimum up to (curr_sum - 1)
            ans += query(curr_sum - 1 + OFFSET)
            
            # Add the current prefix sum to the BIT
            update(curr_sum + OFFSET, 1)
            
        return ans