from collections import Counter
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        c = Counter( i for edge in edges for i in edge)
        return c.most_common()[0][0]

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        checker = set()
        for edge in edges:
            if edge[0] in checker:
                return edge[0]
            if edge[1] in checker:
                return edge[1]
            
            checker.add(edge[0])
            checker.add(edge[1])
        return