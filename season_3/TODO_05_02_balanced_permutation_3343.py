import math
class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        digits = len(num)
        perms = (digits//2 + 1) * math.factorial(digits//2)**2
        return perms