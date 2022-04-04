from collections import defaultdict
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        event_ref = defaultdict(lambda: 0)

        for trip in trips:
            crowd, pickup, dropoff = trip
            event_ref[pickup] += crowd
            event_ref[dropoff] -= crowd
        
        events = sorted(list(event_ref.keys()))
        passengers = 0

        for event in events:
            passengers += event_ref[event]
            if passengers > capacity:
                return False
        return True