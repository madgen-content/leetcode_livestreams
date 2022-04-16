# VERSION 1
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        self.memo = {1: 0, 2:1}
        buffer = list(range(lo, hi+1))
        buffer.sort(key=self.get_power)
        return buffer[k-1]
    
    def get_power(self, n):
        if n not in self.memo:
            m = n
            if m % 2 == 0:
                m /= 2
            else:
                m = 3*m + 1
            self.memo[n] = 1 + self.get_power(m)
        
        return self.memo[n]

# VERSION 2
# add in heap optimization to soln
# ... this isn't actually faster but probably would be for huge ranges
import heapq as h
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        self.memo = {1: 0, 2:1}
        buffer = []
        for i, n in enumerate(range(lo, hi+1)):
            h.heappush(buffer,(self.get_power(n), i, n))
        for _ in range(k):
            r = h.heappop(buffer)
        return r[-1]
    
    def get_power(self, n):
        if n not in self.memo:
            m = n
            if m % 2 == 0:
                m /= 2
            else:
                m = 3*m + 1
            self.memo[n] = 1 + self.get_power(m)
        
        return self.memo[n]