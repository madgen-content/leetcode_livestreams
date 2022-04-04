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

# good twoliner from discussion
def numRabbits(self, answers):
    c = collections.Counter(answers)
    return sum((c[i] + i) / (i + 1) * (i + 1) for i in c)