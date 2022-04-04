# bottom up dynamic programming answer
# this will only yield what the max profit is
# NOT how to achieve it
# tracking logic would have to be added for that
import numpy
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # degeneracy checks
        num_prices = len(prices)

        if num_prices < 2:
            return 0
        elif num_prices == 2:
            return max(prices[1]-prices[0], 0)
        elif num_prices == 3:
            p1 = min(prices[0], prices[1])
            p2 = max(prices[1], prices[2])
            return max(p2 - p1, 0)

        # convert prices to a numpy array to prevent copy-on-slice
        prices = numpy.asarray(prices)

        # build matrices
        mins = numpy.zeros(shape=(num_prices + 1, num_prices+1))
        profits = numpy.zeros(shape=(num_prices + 1, num_prices+1))

        # initialize diagonals
        for i in range(num_prices - 1):
            j = i + 2
            mins[j][i] = prices[i:j].min()
            profits[j][i] = max(0, prices[i + 1] - prices[i])

        #build out nontrivial cells 
        for j in range(3, num_prices + 1):
            for i in reversed(range(j-2)):
                p1 = profits[j-1][i]
                p2 = prices[j-1] - mins[j-1][i]
                profits[j][i] = max(p1, p2, 0)
                mins[j][i] = min(mins[j-1][i], prices[j-1])
        
        # get max profit
        return int(max([profits[k][0] + profits[num_prices][k] for k in range(num_prices + 1)]))

# previous soln calculated far too many maxprofits
# going to use memoization to do better
# this still isn't great
# maybe defaultdict is slow?

import numpy
from collections import defaultdict

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # degeneracy checks
        num_prices = len(prices)

        if num_prices < 2:
            return 0
        elif num_prices == 2:
            return max(prices[1]-prices[0], 0)
        elif num_prices == 3:
            p1 = min(prices[0], prices[1])
            p2 = max(prices[1], prices[2])
            return max(p2 - p1, 0)
        
        # setup a place to store max trades for our ranges
        mem = defaultdict(lambda: 0)

        # Calculate forward maxes
        minprice = None
        maxprofit = 0
        potential_profit = 0

        for i in range(len(prices)):
            p = prices[i]

            if minprice == None or p < minprice:
                minprice = p
            else:
                potential_profit = p - minprice
                if potential_profit > maxprofit:
                    maxprofit = potential_profit
            mem[(0,i)] = maxprofit
        
        # calculate backward maxes
        maxprice = None
        maxprofit = 0
        potential_profit = 0
        n = num_prices - 1

        for i in reversed(range(1, len(prices))):
            p = prices[i]
            if maxprice == None or p > maxprice:
                maxprice = p
            else:
                potential_profit = maxprice - p
                if potential_profit > maxprofit:
                    maxprofit = potential_profit
            mem[(i, n)] = maxprofit
        
        return  max([mem[(0,i)] + mem[(i+1,n)] for i in range(num_prices)])

# copied from discussion board
# very smart approach
# ordering prevents stockdrop at end of life from giving an error
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        first_sell, second_sell = 0, 0
        first_buy, second_buy = -float('inf'), -float('inf')

        for price in prices:
            second_sell = max(second_sell, second_buy+price)
            second_buy = max(second_buy, first_sell-price)
            first_sell = max(first_sell, first_buy+price)
            first_buy = max(first_buy, -price)

        return second_sell
