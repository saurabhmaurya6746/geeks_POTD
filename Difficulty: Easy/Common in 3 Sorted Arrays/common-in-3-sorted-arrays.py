class Solution:
    def commonElements(self, a, b, c):
        i = j = k = 0
        res = []
        
        while i < len(a) and j < len(b) and k < len(c):
            if a[i] == b[j] == c[k]:
                if not res or res[-1] != a[i]:  # avoid duplicates
                    res.append(a[i])
                i += 1
                j += 1
                k += 1
            else:
                min_val = min(a[i], b[j], c[k])
                if a[i] == min_val:
                    i += 1
                elif b[j] == min_val:
                    j += 1
                else:
                    k += 1
        return res