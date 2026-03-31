class Solution:
    def maxProfit(self, arr, k):
        n = len(arr)
        if n == 0:
            return 0
        
        # hold = max profit when holding a stock
        # cash = max profit when not holding a stock
        hold = -arr[0]
        cash = 0
        
        for price in arr[1:]:
            # Either keep holding or buy today
            hold = max(hold, cash - price)
            # Either keep cash or sell today (minus fee)
            cash = max(cash, hold + price - k)
        
        return cash