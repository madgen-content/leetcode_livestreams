# my original solution
# easily adjusted to allow deletion of more numbers
def detect_palindromic(s, i, j, can_delete):
    
    l = j - i

    if l == 0:
        return True
    
    if l == 1:
        if can_delete:
            return True
        else:
            return s[i] == s[j]
    else:
        if s[i] == s[j]:
                return detect_palindromic(s, i+1, j-1, can_delete)
        elif can_delete:
            return detect_palindromic(s, i+1, j, False) or detect_palindromic(s, i, j-1, False)
        else:
            return False
    return

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        start = 0
        end = len(s) - 1
        return detect_palindromic(s, start, end, True)

# leetcode provided solution
class Solution(object):
    def validPalindrome(self, s):
        def is_pali_range(i, j):
            return all(s[k] == s[j-k+i] for k in range(i, j))

        for i in range(len(s) / 2):
            if s[i] != s[~i]:
                j = len(s) - 1 - i
                return is_pali_range(i+1, j) or is_pali_range(i, j-1)
        return True

# better solution from comments
# holy shit
class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == s[::-1]:
            return True
        for i in range(len(s)-1):
            if s[i] != s[-i-1]:
                return s[i: -i-2] == s[i+1: -i-1][::-1] or s[i+1: -i-1] == s[i+2: len(s)-i][::-1]
        return False


#combination of previous two by me
# it's not better :(
# list slices must be faster than I thought
class Solution:
    def validPalindrome(self, s):
        def is_pali_range(i, j):
            return all(s[i+z] == s[j-z] for z in range((j-i + 1)//2))

        if s == s[::-1]:
            return True
        l = len(s) - 1
        for i in range(len(s)-1):
            if s[i] != s[-i-1]:
                return is_pali_range(i, l - i - 1) or is_pali_range(i + 1, l-i) 
        return False