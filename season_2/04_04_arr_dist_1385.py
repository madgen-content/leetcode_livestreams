class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        dist = 0
        for v1 in arr1:
            dist += all((abs(v1 - v2) > d for v2 in arr2))
        
        return dist