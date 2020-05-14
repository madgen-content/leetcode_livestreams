def swap(l, i, j):
    temp = l[i]
    l[i] = l[j]
    l[j] = temp
    return

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        zeros = 0
        twos = len(nums) - 1
        cur = 0

        while cur <= twos:
            val = nums [cur]

            if val == 0:
                swap(nums, cur, zeros)
                zeros += 1
                cur += 1
            elif val == 2:
                swap(nums, cur, twos)
                twos -= 1
            else:
                cur += 1
        
        return