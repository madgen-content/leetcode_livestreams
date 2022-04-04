def heapify(arr, i):
    m = len(arr)

    if i > (m - 1) // 2:
        return

    root_val = arr[i]

    lc = 2 * i
    rc = lc + 1

    lv = None
    rv = None

    if lc < m:
        lv = arr[lc]
    
    if rc < m:
        rv = arr[rc]
    
    if lv != None and lv > root_val and (rv == None or lv > rv):
        arr[i] = lv
        arr[lc] = root_val
        heapify(arr, lc)
    elif rv != None and rv > root_val:
        arr[i] = rv
        arr[rc] = root_val
        heapify(arr, rc)
    return

def build_max_heap(arr):
    arr = [None] + arr
    start = (len(arr) - 1) // 2
    for i in range(start, 0, -1):
        heapify(arr, i)
    return arr

def percolate(arr, i):
    if i == 1:
        return
    
    p = i // 2

    cv = arr[i]
    pv = arr[p]

    if cv > pv:
        arr[p] = cv
        arr[i] = pv
        percolate(arr, p)
    return

def insert(arr: list, val):
    arr.append(val)
    l = len(arr) - 1
    percolate(arr, l)
    return

def heapish_iter(arr: list):
    ret = arr[1]
    arr[1] = arr[-1]
    arr.pop()

    if(len(arr) > 2):
        heapify(arr, 1)
    return ret

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = build_max_heap(stones)
        while len(stones) > 2:
            s1 = heapish_iter(stones)
            s2 = heapish_iter(stones)

            if s2 < s1:
                new_s = s1 - s2
                insert(stones, new_s)
        
        if len(stones) == 2:
            return stones[1]
        else:
            return 0
        return


# MUCH BETTER SOLN
# i might've done something like this if i wasn't set on using a heap
class Solution(object):
    def lastStoneWeight(self, stones):
        def outputw(stones):
            if not stones:
                return 0
            elif len(stones) == 1:
                return stones.pop()        
            a = sorted(stones)
            y, x = a.pop(), a.pop()           
            if y-x:
                a.append(y-x)     
            return(outputw(a))       
        return outputw(stones)