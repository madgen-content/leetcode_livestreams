from typing import *

def find_widest_pal_at(i, s):
    w = 1
    end = len(s)
    while i+w < end and i-w >= 0 and s[i+w] == s[i-w]: w+=1
    return w-1

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        s = list(s)
        count = 0
        while s != []:
            w,i = max((find_widest_pal_at(i,s), i) for i in range(len(s)))
            s = s[i-w]
            count += 1
        
        return count
            