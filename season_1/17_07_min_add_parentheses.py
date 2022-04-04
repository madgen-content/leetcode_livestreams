class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        S = list(S)
        stack = [-1]
        count = 0

        for char in S:
            if char == '(':
                stack.append('(')
            else:
                if stack[-1] == -1:
                    count += 1
                else:
                    stack.pop()
        
        count += len(stack) - 1

        return count