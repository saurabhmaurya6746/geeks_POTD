class Solution:
    def largestArea(self, n, m, arr):
        # Edge case: Agar koi bhi blocked cell nahi hai, to pura grid hi area hoga
        if not arr:
            return n * m
            
        # 0 aur n+1/m+1 ko boundaries ki tarah add kar rahe hain
        blocked_rows = [0, n + 1]
        blocked_cols = [0, m + 1]
        
        # Saare blocked cells ke rows aur columns ko alag karein
        for r, c in arr:
            blocked_rows.append(r)
            blocked_cols.append(c)
            
        # Sort karein taaki consecutive gaps nikal sakein
        blocked_rows.sort()
        blocked_cols.sort()
        
        # Max row gap dundhein
        max_row_gap = 0
        for i in range(1, len(blocked_rows)):
            # Beech ke unblocked cells ki ginti = current - previous - 1
            gap = blocked_rows[i] - blocked_rows[i-1] - 1
            max_row_gap = max(max_row_gap, gap)
            
        # Max column gap dundhein
        max_col_gap = 0
        for i in range(1, len(blocked_cols)):
            gap = blocked_cols[i] - blocked_cols[i-1] - 1
            max_col_gap = max(max_col_gap, gap)
            
        # Largest continuous area
        return max_row_gap * max_col_gap