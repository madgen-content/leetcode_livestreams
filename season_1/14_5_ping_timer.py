# here's the shitty list comprehension soln
class RecentCounter:

    times = []

    def __init__(self):
        self.times = []

    def ping(self, t: int) -> int:
        self.times.append(t)
        self.times = [x for x in self.times if t - x <= 3000]
        return len(self.times)


# here's the good one using dequeue courtesy of zombiekillerwhale
from collections import deque
class RecentCounter(object):
 
    def __init__(self):
        self.pings = deque()
 
    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        while self.pings and self.pings[0] < t - 3000:
            self.pings.popleft()
        self.pings.append(t)
        return len(self.pings)