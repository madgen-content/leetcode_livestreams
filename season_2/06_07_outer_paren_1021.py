class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        s = list(s)
        depth = 0
        for i,c in enumerate(s):
            if c == "(":
                if depth == 0:
                    s[i] = ""
                depth += 1
            
            if c == ")":
                depth -= 1
                if depth == 0:
                    s[i] = ""
        
        return ''.join(s)