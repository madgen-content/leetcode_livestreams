from random import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def pick(self, target: int) -> int:

        nums = self.nums
        idx = nums.index(target)
        i = idx + 1
        occurences = 1

        while i < len(nums):
            val = nums[i]
            if val == target:
                occurences += 1
                cutoff = 1 / occurences

                if random() < cutoff:
                    idx = i
            
            i += 1

        return idx


# better soln... problem lied
class Solution(object):
    def __init__(self, nums):
        self.pick = lambda target: random.choice([i for i, num in enumerate(nums) if num == target])