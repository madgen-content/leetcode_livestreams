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
    
# ----------------------------------------------
# ywanes soln

class Solution {
    public int removeCoveredIntervals(int[][] intervals) {
        int len=intervals.length;
        int retorno=len;
        boolean [] remove = new boolean[len];
        // analisando a remocao de i perante j
        for ( int i=0;i<len;i++ )
        {
            for ( int j=0;j<len;j++ )
            {
                if ( i == j ) continue;
                if ( intervals[i][0] >= intervals[j][0] && intervals[i][1] <= intervals[j][1] )
                {
                    remove[i]=true;
                    break;
                }
            }            
        }
        for ( int i=0;i<len;i++ )
            if ( remove[i] )
                retorno--;
        return retorno;
    }
}

# my python take on ywanes soln
from collections import defaultdict
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        ret  = [1] * len(intervals)
        for i in range(len(intervals)-1):
            for j in range(i+1, len(intervals)):
                a,b = intervals[i]
                c,d = intervals[j]
                
                if (a <= c and d <= b):
                    ret[j] = 0
                
                if (c <= a and b <= d):
                    ret[i] = 0
                    break
        return sum(ret)