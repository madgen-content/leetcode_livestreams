from typing import *
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        candidates = set()
        for n in arr:
            if n in candidates:
                return True
            
            if n % 2 == 0:
                candidates.add( n // 2)
            candidates.add(n*2)
        
        return False