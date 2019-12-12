class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = None
        maxprofit = 0

        for i in range(len(prices)):
            p = prices[i]

            if minprice == None or p < minprice:
                minprice = p
                continue
            else:
                potential_profit = p - minprice
                if potential_profit > maxprofit:
                    maxprofit = potential_profit
        return  maxprofit
        