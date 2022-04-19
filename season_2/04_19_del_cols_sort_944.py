class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows, cols = len(strs), len(strs[0])
        bad_cols = []
        for c in range(cols):
            prev = None
            for r in range(rows):
                cur = strs[r][c]
                if prev is not None:
                    if cur < prev:
                        bad_cols.append(c)
                        break
                prev = cur
        
        for i, s in enumerate(strs):
            strs[i] = ''.join([c for i,c in enumerate(s) if i not in bad_cols])
        
        return strs

# real thing
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows, cols = len(strs), len(strs[0])
        bad_cols = 0
        for c in range(cols):
            prev = None
            for r in range(rows):
                cur = strs[r][c]
                if prev is not None and cur < prev:
                    bad_cols+=1
                    break
                prev = cur
        
        return bad_cols