def get_eat_time(piles, k ):
    return sum([(h-1)//k + 1 for h in piles])

def binsearch_eat_speed(piles, H, lb, ub, ret):
    mid = (lb + ub) // 2
    hrs_to_eat = get_eat_time(piles, mid)

    if lb == ub:
        if hrs_to_eat <= H and lb < ret:
            return lb
        else:
            return ret

    if hrs_to_eat <= H:
        if mid < ret:
            ret = mid
        return binsearch_eat_speed(piles, H, lb, max(mid-1, lb), ret)
    else:
        return binsearch_eat_speed(piles, H, min(mid+1, ub), ub, ret)
    
    return

class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        lb = 1
        ub = max(piles)
        ret = float('inf')
        
        valid_speed = binsearch_eat_speed(piles, H, lb, ub, ret)
        return valid_speed