class Solution:
    def hammingWeight(self, n: int) -> int:
        
        ttl = 0
        while n > 0:
            ttl += n % 2
            n = n // 2
        return ttl