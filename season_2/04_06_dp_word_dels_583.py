from collections import Counter
def remove_chars(s, cs):
    return [c for c in s if c not in cs]

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        difference = 0

        # eliminate letters that aren't in the other (this could be skipped)
        s1 = set(word1)
        s2 = set(word2)
        lcounts = Counter(word1)
        lcounts.update(word2)

        exclusive_letters = s1.symmetric_difference(s2)
        difference = sum([lcounts[l] for l in exclusive_letters])
        word1 = remove_chars(word1, exclusive_letters)
        word2 = remove_chars(word2, exclusive_letters)

        # special case optimization, maybe get lucky and return?
        if word1 == word2:
            return difference
        
        # implement the DP soln
        solns = [list(range(i, i+len(word2)+1)) for i in range(len(word1)+1)]
        for a, c1 in enumerate(word1):
            for b,c2 in enumerate(word2):
                i = a+1
                j = b+1
                if c1 == c2:
                    solns[i][j] = solns[i-1][j-1]
                else:
                    base = min(solns[i-1][j], solns[i][j-1])
                    solns[i][j] = base + 1
        difference += solns[-1][-1]
        return difference