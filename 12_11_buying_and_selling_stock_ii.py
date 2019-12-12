
# stupid
# just because you can only buy or sell on a given day
# doesn't mean you need to properly assign buy and sells
# to know the max profit!
# this solution will likely be useful in advanced problems though
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) < 2:
            return 0
        
        stack = [None]
        buy = -1
        sell = 1

        for i in range(len(prices)):
            price = prices[i]
            if stack[-1] == None:
                stack.append((buy, price))
                continue
            
            differential = price - prices[i-1]
            if stack[-1][0] == buy:
                if differential > 0:
                    stack.append((sell, price))
                else:
                    stack[-1] = (buy, price)

            else:
                if differential < 0:
                    stack.append((buy, price))
                else:
                    stack[-1] = (sell, price)
        
        if stack[-1][0] == buy:
            del stack[-1]

        if len(stack) < 3:
            return 0

        return sum([x[0] * x[1] for x in stack[1:]])

# real soln
# just add up positive differentials
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        profit = 0
        for i in range(len(prices) - 1):
            diff = prices[i + 1] - prices[i]
            if diff > 0:
                profit += diff
        
        return profit

