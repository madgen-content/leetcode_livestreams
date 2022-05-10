from typing import *
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        for i in range(-1,-len(num)-1,-1):
            num[i] += k 
            k  = num[i] // 10
            num[i] %= 10
        
        if k > 0:
            front = [int(d) for d in list(str(k))]
            front.extend(num)
            num = front
        
        return num