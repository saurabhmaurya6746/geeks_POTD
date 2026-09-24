class Solution:
    def maxStackHeight(self, r, h):
        n = len(r)
        discs = list(zip(r, h))
        discs.sort(key=lambda x: (x[0], -x[1]))

        # Coordinate compress heights
        sorted_h = sorted(set(h))
        rank = {v: i + 1 for i, v in enumerate(sorted_h)}
        m = len(sorted_h)

        bit = [0] * (m + 1)

        def update(idx, val):
            while idx <= m:
                if bit[idx] < val:
                    bit[idx] = val
                idx += idx & (-idx)

        def query(idx):
            res = 0
            while idx > 0:
                if bit[idx] > res:
                    res = bit[idx]
                idx -= idx & (-idx)
            return res

        ans = 0
        for radius, height in discs:
            idx = rank[height]
            best = query(idx - 1)  # strictly smaller height
            new_val = best + height
            if new_val > ans:
                ans = new_val
            update(idx, new_val)

        return ans