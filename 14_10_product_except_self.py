# the actual good soln
from functools import reduce

def prod_getter(nums: list, ref, n):
    if n != 0 :
        return ref // n
    else:
        cp = nums[::]
        cp.remove(n)
    return reduce(lambda x,y: x * y, cp)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        refnum = reduce(lambda x,y: x * y, nums)
        return [ prod_getter(nums, refnum, n) for n in nums]

# soln that follows constraints
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        return 