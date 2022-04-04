def search(nums, target, i, j):

    # weird little optimization
    # in recursive divide and conquers, a linear scan is better beyond a certain 
    # smallness to save on the overhead of recursion
    # the exact number should be tuned, but I did well with 50
    if j - i <50:
        k = i
        while k <= j:
            if nums[k] == target:
                return k
            k += 1
        return -1
    
    mid = (i + j) // 2
    if nums[mid] == target:
        return mid
    elif i == j:
        return -1

    if nums[mid] < target:
        return search(nums, target, mid+1, j)
    else:
        return search(nums, target, i, mid)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return search(nums,target, 0, len(nums)-1)