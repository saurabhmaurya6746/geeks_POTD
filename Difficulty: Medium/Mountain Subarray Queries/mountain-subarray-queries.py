class Solution:
    def processQueries(self, arr, queries):
        n = len(arr)

        # furthest index reachable by non-decreasing sequence starting at i
        inc = [0] * n
        inc[-1] = n - 1
        for i in range(n - 2, -1, -1):
            if arr[i] <= arr[i + 1]:
                inc[i] = inc[i + 1]
            else:
                inc[i] = i

        # furthest index reachable by non-increasing sequence starting at i
        dec = [0] * n
        dec[-1] = n - 1
        for i in range(n - 2, -1, -1):
            if arr[i] >= arr[i + 1]:
                dec[i] = dec[i + 1]
            else:
                dec[i] = i

        ans = []
        for l, r in queries:
            peak = inc[l]
            if peak > r:
                ans.append(True)
            else:
                ans.append(dec[peak] >= r)

        return ans