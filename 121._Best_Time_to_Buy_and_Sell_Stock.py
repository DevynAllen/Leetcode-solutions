# 121. Best Time to Buy and Sell Stock
# Runtime: 76 ms, faster than 23.95%

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = sys.maxsize
        maxProfit = 0

        for price in prices:
            currProfit = price - minPrice

            if maxProfit < currProfit:
                maxProfit = currProfit
                
            if price < minPrice:
                minPrice = price

        return maxProfit
