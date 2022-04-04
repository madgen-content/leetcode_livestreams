class Solution:
    def isHappy(self, n: int) -> bool:
        tracker = []
        tracker.append(n)

        while True:
            n = sum([int(x)**2 for x in str(n)])
            if n == 1:
                return True
            elif n in tracker:
                return False
            tracker.append(n)
        return

class Solution:
    def isHappy(self, n: int) -> bool:
        tracker = {}
        tracker[n] = 1

        while True:
            n = sum([int(x)**2 for x in str(n)])
            
            if n == 1:
                return True
            elif tracker.get(n, 0) == 1:
                return False
            tracker[n] = 1
        return

class Solution:
    def isHappy(self, n: int) -> bool:
        tracker = set()
        tracker.add(n)

        while True:
            n = sum([int(x)**2 for x in str(n)])
            if n == 1:
                return True
            elif n in tracker:
                return False
            tracker.add(n)
        return

