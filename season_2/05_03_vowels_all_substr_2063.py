class Solution:
    def countVowels(self, word: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        bitmask = [c in vowels for c in word]        
        accum = 0
        tracker = 0
        for i, v in enumerate(bitmask):
            if v:
                tracker += (i+1)
            accum += tracker
        return accum
