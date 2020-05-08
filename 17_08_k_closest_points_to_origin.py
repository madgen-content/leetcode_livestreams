# MAB soln. just sort and return
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda x: (x[0]**2 + x[1]**2)**.5)
        return points[0:K]

# quickselect soln
def swap(items, a, b):
    tmp = items[a]
    items[a] = items[b]
    items[b] = tmp
    return

def partition(items, i, j):
    mid = (i+j) // 2
    cur = i
    pb = i

    partition_val = items[mid][-1]
    swap(items, mid, j)
    while cur < j:
        val = items[cur][-1]
        if val <= partition_val:
            swap(items, cur, pb)
            pb += 1
        cur += 1
        
    swap(items, pb, j)
    return pb

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        items = [(x, x[0]**2 + x[1]**2) for x in points]

        pb = float('inf')
        i = 0
        j = len(items) - 1
        while pb > K or pb < K-1:
            pb = partition(items, i, j)
            if pb > K:
                j = pb - 1
            elif pb < K - 1:
                i = pb + 1
            else:
                continue
        print(items)
        return [x[0] for x in items[0:K]]

# work smarter use heap builtins
from heapq import nsmallest
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return nsmallest(K, points, lambda x: x[0]**2 + x[1]**2)
        
# smarter?
from heapq import nsmallest
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dists = {tuple(x): x[0]*x[0] + x[1]*x[1] for x in points}
        return nsmallest(K, dists, lambda p: dists[p])