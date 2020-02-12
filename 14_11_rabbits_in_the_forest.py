from collections import Counter
from math import ceil
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        reftable = Counter(answers)

        min_num = 0
        for key in reftable:
            divisor = key + 1
            amt = reftable[key]
            uniq_rabbits = ceil(amt / divisor) * divisor
            
            min_num += uniq_rabbits
            
        return min_num