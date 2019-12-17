# the main problem here is keeping track of original ID's
# after sorting the array
# so we work with an array of tups. (val, original_index)

# gotta remember, they can ask for 0. and one of the numbers can BE 0

# they're also giving negatives, shift the target and the arr by the min if min < 0 so we can maintain my optimization
def binsearch(arr, target, i, j):
    mid = (i + j) // 2

    if arr[mid][0] == target:
        return arr[mid][1]
    elif i == j:
        return -1

    if arr[mid][0] < target:
        return binsearch(arr, target, i, mid)
    else:
        return binsearch(arr, target, mid+1, j)
    return

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums = [(nums[i], i) for i in range(len(nums))]
        nums = sorted(nums,key=lambda x: x[0], reverse=True)
        negs_present = nums[-1][0] < 0

        i = 0
        while i < len(nums) - 1:
            val = nums[i][0]
            if (val <= target) or negs_present:
                i1 = nums[i][1]
                find = target - val
                i2 = binsearch(nums, find, i+1, len(nums)-1)
                if i2 > -1:
                    return sorted([i1, i2])
            i += 1
        return

# great solution from discussions
# maps/hashes are great for detecting presence of one thing (direct addresssing as well)
# you have to go through to the second number for this soln, but that's fine
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # can use a map of   value -> index
        # do one iteration of nums
        # at each nums[i], look if target-nums[i] is in the map
        # if so, return map[that value] and i
        
        seen = dict()
        for i in range(len(nums)):
            comp = seen.get(target-nums[i]) # complement that adds up to target
            if comp != None:
                return (comp, i)
            seen[nums[i]] = i