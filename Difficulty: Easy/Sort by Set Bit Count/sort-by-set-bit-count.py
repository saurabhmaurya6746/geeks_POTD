class Solution:
    def sortBySetBitCount(self, arr):
        # Stable sort based on set bits count (descending)
        arr.sort(key=lambda x: bin(x).count('1'), reverse=True)
        return arr