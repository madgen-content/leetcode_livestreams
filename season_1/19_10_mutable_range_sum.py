class NumArray:
        
    def __init__(self, nums: List[int]):
        self.nums = nums
        bit = [0] + nums

        for bidx in range(1, len(bit)):
            par = bidx + (bidx & -bidx) 
            if par < len(bit):
                bit[par] += bit[bidx]
        
        self.bit = bit
        return


    def add(self, bidx, delta):
        bit = self.bit
        while bidx < len(bit):
            bit[bidx] += delta
            bidx += (bidx & -bidx) 
        return

    def update(self, i: int, val: int) -> None:
        delta = val - self.nums[i]
        self.nums[i] = val
        bidx = i + 1 
        self.add(bidx, delta)
        return
    
    def sum_one_to(self, bidx):
        s = 0 
        while bidx > 0:
            s += self.bit[bidx]
            bidx -= (bidx & -bidx) 
        
        return s

    def sumRange(self, i: int, j: int) -> int:
        return self.sum_one_to(j+1) - self.sum_one_to(i)

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)