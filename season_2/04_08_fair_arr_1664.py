class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        flipper = -1
        for i in range(1,len(nums)):
            nums[i] = flipper*nums[i] + nums[i-1]
            flipper *= -1

        fair_deletes = 0
        for i in range(1,len(nums)):
            result =  nums[i-1] + -1*(nums[-1] - nums[i])
            if result == 0:
                fair_deletes += 1
        
        # account for the first element, which isn't in the loop
        if nums[0] == nums[-1]:
            fair_deletes += 1

        return fair_deletes

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        flipper = 1
        prefixes = [0]*(len(nums) + 1)
        for i in range(len(nums)):
            prefixes[i+1] = flipper*nums[i] + prefixes[i]
            flipper *= -1

        fair_deletes = 0
        for i in range(1,len(prefixes)):
            result =  prefixes[i-1] + -1*(prefixes[-1] - prefixes[i])
            if result == 0:
                fair_deletes += 1
        
        return fair_deletes
