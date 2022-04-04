class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        
        ans = []
        depth = 0

        for c in S:

            if c =='(':
                depth += 1
                if depth > 1:
                    ans.append(c)
            else:
                depth -= 1
                if depth > 0:
                    ans.append(c)

        return ''.join(ans)



# https://leetcode.com/problems/remove-outermost-parentheses/discuss/470223/Easy-to-understand-C%2B%2B-solution-using-stack