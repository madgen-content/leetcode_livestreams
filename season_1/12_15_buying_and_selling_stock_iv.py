# adapt a previously seen linear scan solution for k transactions
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        if k < 1 or len(prices) < 2:
            return 0
        
        # if you can make unlimited transactions
        # just assume you make all gains possible
        if k > len(prices):
            profit = 0
            for i in range(len(prices) - 1):
                diff = prices[i + 1] - prices[i]
                if diff > 0:
                    profit += diff
            return profit
        
        n_trackers = k*2
        profit_trackers = [ (-float('inf'),0)[x % 2] for x in range(n_trackers)]

        for p in prices:
            for i in reversed(range(1, n_trackers)):
                if i % 2 == 0:
                    profit_trackers[i] = max(profit_trackers[i], profit_trackers[i-1] - p )
                else:
                    profit_trackers[i] = max(profit_trackers[i], profit_trackers[i-1] + p)
            
            profit_trackers[0] = max(profit_trackers[0], -p)
        
        print(profit_trackers)
        return max(profit_trackers[min(len(prices)//2*2-1,n_trackers-1)], 0)