# this problem is ez
class Solution:
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0

# here's a dp soln copied from leetcode
# didn't bother solving cuz it's dumb
# if N is even, you win. no need to 'solve'.
# it's a decent dp design tho
class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = [False for i in range(N+1)]
        for i in range(N+1):
             for j in range(1, i//2 + 1):
                    if i % j == 0 and (not dp[i - j]):
                        dp[i] = True
                        break
        return dp[N]