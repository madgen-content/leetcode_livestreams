# the actual good soln
from functools import reduce

def prod_getter(nums: list, ref, n):
    if n != 0 :
        return ref // n
    else:
        cp = nums[::]
        cp.remove(n)
    return reduce(lambda x,y: x * y, cp)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        refnum = reduce(lambda x,y: x * y, nums)
        return [ prod_getter(nums, refnum, n) for n in nums]

# soln that follows constraints
from collections import defaultdict
class Solution:

    mem = None

    def mem_mul(self, nums, left, right):
        # print(f'left:{left} right: {right}')
        mem = self.mem

        if mem[left][right] != None:
            # print(f'found: {mem[left][right]}')
            return mem[left][right]
        else:
            if right < 0 or left == len(nums):
                mem[left][right] = 1
                # print('edge, returning 1')
                return 1
            
            diff = right - left
            if diff == 0:
                res = nums[left]
                mem[left][right] = res
                # print('just identity')
                return res

            if diff == 1:
                res = nums[left] * nums[right]
                mem[left][right] = res
                # print(f'res: {res}')
                return res
            
            if diff > 1:
                mid = (left + right) // 2
                leftprod = self.mem_mul(nums, left, mid)
                rightprod = self.mem_mul(nums, mid + 1, right)
                fullprod = leftprod * rightprod
                mem[left][right] = fullprod
                # print(f'fullprod: {fullprod}')
                return fullprod
            # print('should not reach!')
        return

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        self.mem = defaultdict(lambda: defaultdict(lambda: None))

        for left in range(len(nums) - 1):
            right = left + 1
            self.mem[left][right] = nums[left] * nums[right]

            if left < len(nums) - 2:
                bigger_right = right + 1
                self.mem[left][bigger_right] = self.mem[left][right] * nums[bigger_right]

        result = []
        for i in range(len(nums)):
            # print(('!', i))
            prod = self.mem_mul(nums, 0, i-1) * self.mem_mul(nums, i+1, len(nums)-1)
            result.append(prod)
        # print(f'mem: {self.mem}')
        return result

# abandon ship
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [nums[0]]
        suffix = [nums[-1]]

        for i in range(1, len(nums)):
            prefix.append(prefix[-1] * nums[i])
            ri = len(nums) - 1 - i
            suffix.append(suffix[-1] * nums [ri])
    
        products = []
        for i in range(len(nums)):
            if i > 0:
                left = prefix[i-1]
            else:
                left = 1
            
            if i < len(nums) - 1:
                ri = len(nums) - 1 - (i + 1)
                right = suffix[ri]
            else:
                right = 1

            products.append(left * right)
        
        return products