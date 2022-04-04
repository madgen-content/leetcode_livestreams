mul = lambda x, y: x * y
add = lambda x, y: x + y
sub = lambda x, y: x - y

from math import ceil
def div(x, y):
    if x >= 0 and y >= 0:
        return x // y
    else:
        return ceil(x / y)
    return
    
class Solution:
    def clumsy(self, N: int) -> int:

        farr = [mul, div, add, sub]
        accum = [N]
        nums = range(N-1, 0, -1)
        for i in range(len(nums)):
            n = nums[i]
            op = farr[i % 4]
            back = accum[-1]

            if op == mul or op == div:
                accum[-1] = op(back, n)
            if op == add:
                accum.append(n)
            if op == sub:
                accum.append(-1 * n)
        
        return sum(accum)

# other solns from discussion

# exploits some pattern I didn't see
class Solution:
    def clumsy(self, N):
            return [0, 1, 2, 6, 7][N] if N < 5 else N + [1, 2, 2, - 1][N % 4]

# python 2, as good as expr evaluation will be
from itertools import cycle
class Solution:
    def clumsy(self, N):
            op = itertools.cycle("*/+-")
            return eval("".join(str(x) + next(op) for x in range(N, 0, -1))[:-1])
