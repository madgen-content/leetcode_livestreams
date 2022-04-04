# could definitely optimize this more
# but this is a dumb problem and not gonna bother
# this'll do
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        diffs = [A[i] - A[i-1] for i in range(1, len(A))]
        return all(map(lambda x: x <= 0, diffs)) or all(map(lambda x: x >= 0, diffs))

# awesome oneliner from discussion
# realizing monotonicity implies either sorted form is amazing
# i don't think this relies on the fact that python's sort is stable
# but if you solved a similar problem on objects or dicts by a certain member
# this would still work because of that
# you'd have to have a key=lambda clause tho

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        return True if A == sorted(A) or A == sorted(A, reverse = True) else False