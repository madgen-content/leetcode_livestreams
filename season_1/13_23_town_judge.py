from collections import Counter

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        if trust == []:
            return 1
        
        highcounts = {}
        potentials = set(list(range(1,N+1)))
        [(highcounts.update({x[1]: highcounts.get(x[1], 0) + 1}), potentials.discard(x[0])) for x in trust]
        highcounts = Counter(highcounts)
        perp, trustnum = highcounts.most_common()[0]
        
        if trustnum < N - 1:
            return -1
        
        hightrust = set([x for x in highcounts if highcounts[x] == trustnum])
        print(hightrust)

        lowtrust = potentials
        result = list(hightrust.intersection(lowtrust))

        if len(result) > 0 :
            return result[0]
        else:
            return -1


# slow but more concise
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        j, cnt = collections.Counter(b for a, b in trust).most_common(1)[0] if trust else (N, 0)
        return j if j not in {a for a, b in trust} and cnt == N - 1 else -1

# i made a point based soln
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if trust == []:
            return 1

        goal = N-1
        d = {}
        for truster, trustee in trust:
            d[truster] = d.get(truster, 0) - 1
            d[trustee] = d.get(trustee, 0) + 1

        potentials = [x for x in d if d[x] == goal]

        if len(potentials) == 1:
            return potentials[0]
        else:
            return -1


