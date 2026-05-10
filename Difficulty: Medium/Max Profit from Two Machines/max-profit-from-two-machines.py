class Solution:
    def maxProfit(self, x, y, a, b):
        n = len(a)
        tasks = []
        
        # Store difference and profits
        for i in range(n):
            tasks.append((abs(a[i] - b[i]), a[i], b[i], i))
        
        # Sort by max difference so we assign high-impact tasks first
        tasks.sort(reverse=True)
        
        profit = 0
        countA, countB = 0, 0
        
        for diff, pa, pb, idx in tasks:
            if (pa >= pb and countA < x) or countB >= y:
                profit += pa
                countA += 1
            else:
                profit += pb
                countB += 1
        
        return profit