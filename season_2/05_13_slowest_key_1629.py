from typing import *
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        releaseTimes.insert(0,0)
        result = list(enumerate(keysPressed))
        result.sort(key= lambda x: (releaseTimes[x[0]+1]-releaseTimes[x[0]], x[1]), reverse=True)
        return result[0][1]