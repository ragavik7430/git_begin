class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        min_price=prices[0]
        for price in  prices[1:]:
                max_profit=max(max_profit,price-min_price)
                min_price=min(min_price,price)
        return max_profit
#Example 1:
#Input: prices = [7,1,5,3,6,4]

#Output: 5
#Explanation: Buy on day 2 (price = 1) and sell on day