class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
            
        divisors = [1]
        for f1 in range(2,num//2):
            if num % f1 == 0:
                f2 = num // f1
                if f1 > f2:
                    break
                divisors.append(f1)
                if f1 != f2:
                    divisors.append(f2)

        return sum(divisors) == num