class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        tracker = {}
        for c in s:
            v = tracker.get(c, None)
            if v == None:
                tracker[c] = 1
            else:
                tracker[c] = v + 1
        
        for i in range(len(s)):
            c = s[i]
            if tracker[c] == 1:
                return i
        
        return -1


# good soln using counter and relying on dict key insertion order
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        char_occ_dict = Counter(s)
        
        
        unique_char = [ c for c, occ in char_occ_dict.items() if occ == 1]
        
        if len(unique_char) == 0:
            return -1
        else:
            return s.index( unique_char[0] )