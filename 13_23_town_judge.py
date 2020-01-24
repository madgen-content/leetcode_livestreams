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