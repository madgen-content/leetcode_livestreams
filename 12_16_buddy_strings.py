def has_repetition(A):
    s = list(sorted(A))
    for i in range(1, len(A)):
        if s[i] == s[i-1]:
            return True
    return False

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        
        if len(A) != len(B):
            return False
        
        if A == B:
            return has_repetition(A)

        diffs = []
        i = 0
        while i < len(A):
            if A[i] != B[i]:
                if len(diffs) >= 2:
                    return False
                diffs.append((A[i], B[i]))
            i += 1
        
        hasdiffs = len(diffs) == 2 and diffs[0][0] == diffs[1][1] and diffs[0][1] == diffs[1][0]
        
        return hasdiffs