
class RecentCounter:

    times = []

    def __init__(self):
        self.times = []

    def ping(self, t: int) -> int:
        self.times.append(t)
        self.times = [x for x in self.times if t - x <= 3000]

        return len(self.times)



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)