from typing import *
class Solution:
    def findDerangement(self, n: int) -> int:
        if n <= 1:
            return 0

        mod = 1000000007
        tot = 0
        mul = 1
        sub = 0
        sign = -1**(n)
        for i in range(n, -1, -1):
            print(tot, mul, sub)
            tot += mul * sign
            print(tot, mul, sub)
            print()
            mul *= (n - sub)
            sub += 1
            sign = -sign

        return tot % mod