def lookup_adder(tracker: dict, index, list):
    for p in list:
        twolist = tracker.get(p, None)
        if twolist == None:
            v = [0,0]
            v[index] = 1
            tracker[p] = v
        else:
            tracker[p][index] += 1
    return

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        tracker = {}
        lookup_adder(tracker, 0, nums1)
        lookup_adder(tracker, 1, nums2)

        nonflat = [ [k]*min(tracker[k]) for k in tracker ]
        return [item for sublist in nonflat for item in sublist]
