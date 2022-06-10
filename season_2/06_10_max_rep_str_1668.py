class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        slen = len(sequence)
        wlen = len(word)
        i = 0
        best = 0
        starts = [i for i,c in enumerate(sequence) if c == word[0]]
        
        for i in starts:
            cur = 0
            while i < slen:
                if word == sequence[i:i+wlen]:
                    cur += 1
                    i += wlen
                else:
                    cur = 0
                    i += 1
                
                best = max(best, cur)
        
        return best