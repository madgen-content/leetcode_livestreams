from typing import *
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        l = len(nums)
        for i in range(l):
            if nums[min(start + i, l-1)] == target or nums[max(start - i, 0)] == target:
                return i
        return