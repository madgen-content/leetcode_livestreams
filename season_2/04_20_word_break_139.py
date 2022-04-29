# copy pasted the brute force because its worth knowing
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def wordBreakRecur(s: str, word_dict: Set[str], start: int):
            if start == len(s):
                return True
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_dict and wordBreakRecur(s, word_dict, end):
                    return True
            return False

        return wordBreakRecur(s, set(wordDict), 0)

# https://leetcode.com/problems/word-break/discuss/511991/Python-Trie
# ^ a good one

# my attempt?
from typing import *
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # degenerate case check
        s1 = set(s)
        s2 = set(''.join(wordDict))
        if len(s1.symmetric_difference(s2)) > 0:
            return False