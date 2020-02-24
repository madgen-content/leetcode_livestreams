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