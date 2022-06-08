from typing import *

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        n = len(nums)
        a = nums[0::2]
        b = nums[1::2]
        a.sort(reverse=True)
        b.sort()
        accum  = []
        while a or b:
            if a:
                accum.append(a.pop())
            
            if b:
                accum.append(b.pop())

        return accum