from collections import defaultdict
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        idmap = defaultdict(lambda: list())
        stopping_pts = set()
        intervals.sort(key= lambda x: (x[0], -1 * x[1]))
        for i in range(len(intervals)):
            interval = intervals[i]
            idmap[interval[0]].append(i)
            idmap[interval[1]].append(i)
            stopping_pts.add(interval[0])
            stopping_pts.add(interval[1])

        stopping_pts = list(stopping_pts)
        stopping_pts.sort()

        tracker = []
        removal_count = 0
        i_list = []
        for stop in stopping_pts:
            delzero = False
            ranges = idmap[stop]
            for r in ranges:
                if r not in tracker:
                    tracker.append(r)
                else:
                    i = tracker.index(r)
                    if i > 0:
                        removal_count += 1
                        del tracker[i]
                    else:
                        delzero = True
            
            if delzero:
                del tracker[0]
                    
        return len(intervals) - removal_count