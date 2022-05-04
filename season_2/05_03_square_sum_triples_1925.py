class Solution:
    def countTriples(self, n: int) -> int:
        squares = [i**2 for i in range(1, n+1)]
        checker = set(squares)
        roof = n ** 2
        triples = 0
        for i, a2 in enumerate(squares):
            for j in range(i+1, len(squares)):
                b2 = squares[j]
                c2 = a2 + b2
                if c2 > roof:
                    break
                if c2 in checker:
                    triples += 2
        return triples