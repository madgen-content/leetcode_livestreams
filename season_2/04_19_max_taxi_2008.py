from typing import *

# this is actually too slow!
class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        dp = [[0]*(n+1) for _ in range(len(rides)+1)]
        rides.sort()
        for row, (start, end, tip) in enumerate(rides):
            row = row+1                     #there's a buffer row at the top
            profit = end - start + tip
            dp[row][end] = dp[row-1][start] + profit
            for i in range(1,len(dp[row])): #places start at '1'
                dp[row][i] = max(dp[row][i-1], dp[row-1][i], dp[row][i])
        return dp[-1][-1]

# build a single arr? still bad!
class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        dp = [0]*(n+1)
        rides.sort()
        for start, end, tip in rides:
            profit = end - start + tip
            new_ride_tot = dp[start] + profit
            dp[end] = max(dp[end], new_ride_tot)
            for i in range(end,n+1): #places start at '1'
                dp[i] = max(dp[i-1], dp[i])
        return dp[-1]

#  can't iterate in the loop, do something else?
class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        dp = [0]*(n+1)
        rides.sort(key=lambda x: x[1])
        j = 0
        for i in range(1, n+1):
            dp[i] = dp[i-1]
            while j < len(rides) and i == rides[j][1]:
                start, end, tip = rides[j]
                profit = end - start + tip
                dp[i] = max(dp[i], profit + dp[start])
                j+=1
        return dp[-1]
