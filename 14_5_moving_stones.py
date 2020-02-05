class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted([a, b, c])

        if c - b == 1 and b - a == 1:
            return [0,0]
        
        b = b - a
        c = c - a
        a = 0

        minmoves = 2
        if (b - a <= 2) or (c - b <= 2):
            minmoves = 1
        
        maxmoves = c - 2
        
        return [minmoves, maxmoves]