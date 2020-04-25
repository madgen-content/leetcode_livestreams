from collections import defaultdict
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        ids = defaultdict(lambda: float('inf'))
        for i in range(len(S)):
            c = S[i]
            if ids[c]== float('inf'):
                ids[c] = i
        ret = ''.join(sorted(list(T), key= lambda x: ids[x]))
        return ret

# really cool alternative soln by zombiekillerwhale
from collections import Counter
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        t_counter = Counter(T)
        return ''.join(c * t_counter[c] for c in S) + ''.join(c for c in T if c not in S)