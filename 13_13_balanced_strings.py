# gotta remember that depth zeros out at the end as well
# so start splits at 0 instead of 1

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        state = ""
        depth = 0
        splits = 0

        for c in s:
            if depth == 0:
                state = c
                depth +=1
                continue
            else:
                if c == state:
                    depth += 1
                else:
                    depth -= 1
                
                if depth == 0:
                    splits += 1
        
        return splits