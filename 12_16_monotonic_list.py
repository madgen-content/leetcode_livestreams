class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        diffs = [A[i] - A[i-1] for i in range(1, len(A))]
        return all(map(lambda x: x <= 0, diffs)) or all(map(lambda x: x >= 0, diffs))