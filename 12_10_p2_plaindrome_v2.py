def detect_palindromic(s, i, j, can_delete):
    
    l = j - i

    if l == 0:
        return True
    
    if l == 1:
        if can_delete == True:
            return True
        else:
            return s[i] == s[j]
    
    if l > 1:
        if can_delete == False:
            if s[i] == s[j]:
                return detect_palindromic(s, i+1, j-1, can_delete)
            else:
                return False
        else:
            if s[i] == s[j]:
                return detect_palindromic(s, i+1, j-1, can_delete)
            else:
                return detect_palindromic(s, i+1, j, False) or detect_palindromic(s, i, j-1, False)
    return

class Solution:
    def validPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        return detect_palindromic(s, start, end, True)
