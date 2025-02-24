class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        accum = ''.join([str(d) for d in digits])
        newnum = str(int(accum)+1)
        return [int(d) for d in newnum]

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        adder = 1
        accum  = []
        for d in reversed(digits):
            result = d + adder + carry
            adder = 0
            placement = result % 10
            carry = result // 10
            accum.append(placement)
        if carry > 0:
            accum.append(carry)
        return list(reversed(accum))