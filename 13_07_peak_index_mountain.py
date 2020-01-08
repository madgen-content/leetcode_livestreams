
def slope_sign(arr, i):
    candidate = arr[i]
    left = arr[i-1]
    right = arr[i+1]
    
    left_sign = candidate - left
    right_sign = right - candidate

    if left_sign > 0 and right_sign < 0:
        return 0
    elif left_sign > 0:
        return 1
    else:
        return -1
    return

def peak_search(arr, left, right):

    mid = (right + left) // 2
    sign = slope_sign(arr, mid)
    if sign == 0:
        return mid
    elif sign > 0:
        return peak_search(arr, mid+1, right)
    else:
        return peak_search(arr, left, mid -1)


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        left = 1
        right = len(A) - 2
        return peak_search(A, left, right)




# GAH
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        return A.index(max(A))
