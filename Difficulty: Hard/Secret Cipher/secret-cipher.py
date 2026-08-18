class Solution:
    def compress(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
    
        # Step 1: Compute Z-array for prefix matching in O(N)
        z = [0] * n
        l, r = 0, 0
        for i in range(1, n):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] - 1 > r:
                l = i
                r = i + z[i] - 1
    
        # Step 2: Traverse backwards and greedily compress
        res = []
        i = n - 1
        while i >= 0:
            # If current prefix s[0...i] has even length (i + 1)
            # and first half s[0...k-1] == second half s[k...2k-1]
            if (i + 1) % 2 == 0:
                k = (i + 1) // 2
                if z[k] >= k:
                    res.append('*')
                    i = k - 1
                    continue
    
            res.append(s[i])
            i -= 1
    
        # Step 3: Return the reversed string
        return "".join(reversed(res)) 