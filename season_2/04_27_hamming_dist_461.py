class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        diff = x ^ y
        return bin(diff).count('1')

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        diff = x ^ y
        count = 0
        while diff:
            count += diff & 1
            diff >>= 1
        return count