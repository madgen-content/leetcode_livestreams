class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        idxs = dict(reversed(t) for t in enumerate(nums2))
        return [idxs[n] for n in nums1]