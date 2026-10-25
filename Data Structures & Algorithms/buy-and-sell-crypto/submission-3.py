class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #have to consider price aka value + time aka index
        max_profit = 0
        for i in range(len(prices) - 1):
            future_prices = prices[i+1:]
            max_price = max(future_prices)
            #max_price stores the largest price after the current
            max_profit = max(max_profit, max_price - prices[i])
        if max_profit > 0: 
            return max_profit
        else:
            return 0