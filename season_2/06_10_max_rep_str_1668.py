class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        slen = len(sequence)
        wlen = len(word)
        best = 0
        starts = [i+wlen for i in range(slen) if sequence[i:i+wlen] == word and i+wlen < slen]
        for i in starts:
            cur = 1
            while i < slen:
                print(sequence[i:i+wlen])
                if word == sequence[i:i+wlen]:
                    cur += 1
                    i += wlen
                else:
                    cur = 0
                    i += 1
                best = max(best, cur)
        return best