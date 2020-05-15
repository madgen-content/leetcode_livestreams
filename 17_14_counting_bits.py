from math import log2, floor
class Solution:
    def countBits(self, num: int) -> List[int]:
        bitreference = {0: 0, 1:1, 2: 1, 3:2}

        if num < 4:
            return [bitreference[x] for x in sorted(bitreference) if x <= num]

        for i in range(3, floor(log2(num))+1 +1):
            allones = 2 ** i - 1
            bottom = 2 ** (i-1)
            
            bitreference[allones] = i
            new_entries = {n:i - bitreference[n ^ allones] for n in range(bottom, min(allones, num+1))}
            bitreference.update(new_entries)

        return [bitreference[x] for x in range(0,num+1)]