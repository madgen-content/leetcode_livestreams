import heapq
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(reverse = True)
        day = 0
        count = 0
        heap = []

        while events or heap:
            if not heap:
                day = events[-1][0]
            while events and events[-1][0] <= day:
                heapq.heappush(heap, events.pop()[1])
            if heap:
                count += 1
                heapq.heappop(heap)
                day += 1
            while heap and heap[0] < day:
                heapq.heappop(heap)
        
        return count
